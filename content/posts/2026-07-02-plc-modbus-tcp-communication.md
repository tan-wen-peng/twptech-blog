---
title: "PLC 与视觉通信：Modbus TCP 报文解析与超时处理"
description: "视觉系统判完结果要发给 PLC。Modbus TCP 是最通用的桥梁，但『发过去了PLC没收到』『收到了但超时了』才是产线上每天在发生的真实问题。"
slug: plc-vision-modbus-tcp-guide
date: 2026-07-02
image: /images/cover-plc-modbus.svg
tags:
  - 机器视觉
  - PLC
  - Modbus TCP
  - C#
  - 工业通信
categories:
  - 机器视觉
series:
  - 视觉入门到交付
weight: 5
---

## 前言

视觉系统判完结果，最终是要发给 PLC 去执行的。Modbus TCP 作为工业以太网里最通用的协议，是视觉上位机和 PLC 之间的默认桥梁。

但现实是：**Modbus 的坑不在协议本身，而在超时、重连、字节序这些边角料上**。

本文不讲 Modbus 协议规范（那玩意满网都是），只讲 C# 里发 Modbus TCP 时的 4 个实坑和完整的通信封装。

---

## 环境

- PLC：汇川 H5U（实测）、西门子 S7-1200（Modbus TCP Server 模式）
- 上位机：C# .NET Framework 4.7.2 / .NET 6
- 通信库：`NModbus4`（NuGet 包，开源）
- 配置：PLC IP 192.168.1.100，端口 502

---

## 坑 1：发送后 PLC 没反应 — 字节序错了

### 现象

C# 发了一段 Modbus 报文，PLC 那边收到的数据和预期不符。

### 原因

Modbus TCP 是多字节数据时用的是 **Big-Endian（大端）**，而 C# 的 `BitConverter` 默认是 **Little-Endian（小端）**。

### 解决

对多字节数据做端序转换：

```csharp
// 写入保持寄存器的值
short value = 1234;

// ❌ 错误
byte[] data = BitConverter.GetBytes(value);
// 结果：D2 04（小端）→ PLC 读到的是 0xD204 = 53764

// ✅ 正确
byte[] data = BitConverter.GetBytes(value);
if (BitConverter.IsLittleEndian)
    Array.Reverse(data);
// 结果：04 D2（大端）→ PLC 读到 1234
```

用 NModbus4 库时不需要手动处理，库会自动转换。但如果你自己构造报文或者用其他库，这是最常见的翻车点。

**对照表：**

| 数据类型 | .NET 默认 | Modbus | 要不要调 |
|----------|-----------|--------|---------|
| short / ushort | Little | Big | ✅ 调 |
| int / uint | Little | Big | ✅ 调 |
| float | Little | Big | ✅ 调 |
| byte | — | — | ❌ 不用 |
| bool | — | — | ❌ 不用 |

---

## 坑 2：PLC 断开后再连不上 — 端口未释放

### 现象

第一次连接正常，通信正常。但断开后重连，`TcpClient` 抛异常或卡死。

### 原因

TCP 的 TIME_WAIT 状态。Modbus TCP 端口 502 被占用，2-4 分钟内无法复用。

### 解决

关闭 TCP 连接时设置 `LingerState`：

```csharp
private TcpClient _tcpClient;

public void Disconnect()
{
    if (_tcpClient != null && _tcpClient.Connected)
    {
        try
        {
            // 设置 LingerState：关闭后立即释放端口
            _tcpClient.LingerState = new LingerOption(true, 0);
            _tcpClient.Close();
        }
        catch { }
    }
}
```

另外，重连时加一个不可达检测：

```csharp
public bool IsConnected()
{
    if (_tcpClient == null || !_tcpClient.Connected)
        return false;

    // 真正检测连接状态：发一个空包看是否异常
    try
    {
        return !_tcpClient.Client.Poll(10, SelectMode.SelectRead)
            || _tcpClient.Client.Available != 0;
    }
    catch
    {
        return false;
    }
}
```

---

## 坑 3：通信超时不处理，整个 UI 线程卡死

### 现象

PLC 突然断电，上位机界面卡死了。等了 30 秒才弹超时，用户早就 Alt+F4 了。

### 原因

默认 `TcpClient.Connect` 的超时时间是 **∞**。

### 解决

异步连接 + 自定义超时：

```csharp
private static readonly TimeSpan DefaultTimeout = TimeSpan.FromSeconds(3);

public bool Connect(string ipAddress, int port = 502)
{
    _tcpClient = new TcpClient();

    // 手动实现超时
    var connectTask = _tcpClient.ConnectAsync(ipAddress, port);
    if (Task.WaitAny(new[] { connectTask }, (int)DefaultTimeout.TotalMilliseconds) != 0)
    {
        throw new TimeoutException($"连接 {ipAddress}:{port} 超时 ({DefaultTimeout.TotalSeconds}s)");
    }

    if (connectTask.IsFaulted)
        throw connectTask.Exception.InnerException;

    Console.WriteLine($"PLC {ipAddress}:{port} 连接成功");
    return true;
}
```

读写操作也要设超时：

```csharp
public void WriteRegister(ushort address, short value)
{
    if (!IsConnected())
        throw new InvalidOperationException("未连接到 PLC");

    using (var master = new ModbusIpMaster(_tcpClient))
    {
        // ✅ 关键：设 ReceiveTimeout 和 SendTimeout
        _tcpClient.ReceiveTimeout = 2000;
        _tcpClient.SendTimeout = 2000;

        master.WriteSingleRegister(address, (ushort)value);
    }
}
```

---

## 完整封装：ModbusTcpClient.cs

```csharp
using System;
using System.Net.Sockets;
using System.Threading.Tasks;
using Modbus.Device;

namespace PlcCommunication
{
    public class ModbusTcpClient : IDisposable
    {
        private TcpClient _tcpClient;
        private ModbusIpMaster _master;
        private readonly string _ipAddress;
        private readonly int _port;
        private readonly TimeSpan _timeout;

        public bool Connected => IsConnected();

        public ModbusTcpClient(string ipAddress, int port = 502, int timeoutSeconds = 3)
        {
            _ipAddress = ipAddress;
            _port = port;
            _timeout = TimeSpan.FromSeconds(timeoutSeconds);
        }

        public bool Connect()
        {
            try
            {
                _tcpClient = new TcpClient();
                _tcpClient.LingerState = new LingerOption(true, 0);

                var connectTask = _tcpClient.ConnectAsync(_ipAddress, _port);
                if (Task.WaitAny(new[] { connectTask }, (int)_timeout.TotalMilliseconds) != 0)
                {
                    _tcpClient.Close();
                    throw new TimeoutException($"连接 PLC 超时 ({_ipAddress}:{_port})");
                }

                if (connectTask.IsFaulted)
                    throw connectTask.Exception.InnerException;

                _tcpClient.ReceiveTimeout = 2000;
                _tcpClient.SendTimeout = 2000;
                _master = ModbusIpMaster.CreateIp(_tcpClient);

                Console.WriteLine($"[OK] PLC {_ipAddress}:{_port} 已连接");
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[ERR] PLC 连接失败: {ex.Message}");
                return false;
            }
        }

        public bool WriteRegister(ushort address, short value)
        {
            try
            {
                _master?.WriteSingleRegister(address, (ushort)value);
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[ERR] 写入寄存器 {address} 失败: {ex.Message}");
                return false;
            }
        }

        public bool WriteRegisters(ushort startAddress, short[] values)
        {
            try
            {
                ushort[] data = new ushort[values.Length];
                for (int i = 0; i < values.Length; i++)
                    data[i] = (ushort)values[i];

                _master?.WriteMultipleRegisters(startAddress, data);
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[ERR] 批量写入失败: {ex.Message}");
                return false;
            }
        }

        public short[] ReadRegisters(ushort startAddress, ushort count)
        {
            try
            {
                ushort[] data = _master?.ReadHoldingRegisters(startAddress, count);
                if (data == null) return null;

                short[] result = new short[data.Length];
                for (int i = 0; i < data.Length; i++)
                    result[i] = (short)data[i];
                return result;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[ERR] 读取寄存器失败: {ex.Message}");
                return null;
            }
        }

        public bool WriteCoil(ushort address, bool value)
        {
            try
            {
                _master?.WriteSingleCoil(address, value);
                return true;
            }
            catch
            {
                return false;
            }
        }

        public bool[] ReadCoils(ushort startAddress, ushort count)
        {
            try
            {
                return _master?.ReadCoils(startAddress, count);
            }
            catch
            {
                return null;
            }
        }

        public void Disconnect()
        {
            try
            {
                _master?.Dispose();
                _master = null;

                if (_tcpClient != null)
                {
                    _tcpClient.LingerState = new LingerOption(true, 0);
                    _tcpClient.Close();
                    _tcpClient = null;
                }

                Console.WriteLine("[OK] PLC 已断开");
            }
            catch { }
        }

        private bool IsConnected()
        {
            if (_tcpClient == null || !_tcpClient.Connected)
                return false;

            try
            {
                return !_tcpClient.Client.Poll(10, SelectMode.SelectRead)
                    || _tcpClient.Client.Available != 0;
            }
            catch
            {
                return false;
            }
        }

        public void Dispose()
        {
            Disconnect();
        }
    }
}
```

### 使用示例

```csharp
var plc = new ModbusTcpClient("192.168.1.100", 502, timeoutSeconds: 3);

if (plc.Connect())
{
    // 写入检测结果：OK=1, NG=0
    plc.WriteRegister(0, (short)(isOK ? 1 : 0));

    // 写入 X/Y 坐标
    plc.WriteRegisters(10, new short[] {
        (short)(coordX * 100),  // 保留两位小数
        (short)(coordY * 100)
    });

    // 触发拍照信号
    plc.WriteCoil(0, true);

    // 读取 PLC 状态
    bool startSignal = plc.ReadCoils(0, 1)?[0] ?? false;

    plc.Disconnect();
}
```

---

## 通信协议设计建议

视觉发给 PLC 的数据，推荐用一组映射寄存器：

| 地址 | 长度（word） | 方向 | 内容 |
|------|-------------|------|------|
| 0 | 1 | 视觉→PLC | 状态字：0=待机, 1=检测中, 2=OK, 3=NG, 4=错误 |
| 1 | 1 | 视觉→PLC | 错误码（状态=4 时有效） |
| 10-11 | 2 | 视觉→PLC | X 坐标（mm × 100，即 cm） |
| 12-13 | 2 | 视觉→PLC | Y 坐标（mm × 100） |
| 14-15 | 2 | 视觉→PLC | 角度（度 × 100） |
| 20 | 1 | PLC→视觉 | 触发信号：1=拍照请求 |
| 21 | 1 | PLC→视觉 | 复位信号：1=复位错误 |

> 这个映射表不是标准，是我自己在项目里验证过好使的。重点是留够余量（不要贴着脸用地址）、状态字要覆盖异常情况。

---

## 总结

| 坑 | 现象 | 解决 |
|----|------|------|
| 字节序错了 | PLC 收到乱码 | 确认大端序，用库不用手写 |
| 端口未释放 | 重连失败 | LingerState + 真实连接检测 |
| 无限超时 | UI 卡死 | 手动 Task.WaitAny 3s 超时 |
| 断线无人知 | 发数据永远等不到 ACK | 心跳检测 + 自动重连 |

Modbus TCP 本身很简单，**但通信永远不是『发出去就行了』**。断线重连、超时处理、状态监控，这些防呆代码写的越多，上线后半夜被电话叫醒的概率就越低。

*发布日期：2026-07-02*  
*标签：#机器视觉 #PLC #Modbus TCP #C# #工业通信*
