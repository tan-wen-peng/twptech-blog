---
title: "C# 调用 Halcon 的内存泄漏排查记录"
description: "一个视觉程序跑了 8 小时内存涨了 2GB，从任务管理器一路查到 Halcon 内部对象的完整排查实录。"
slug: halcon-csharp-memory-leak-debug
date: 2026-07-02
image: /images/cover-memory-leak.svg
tags:
  - 机器视觉
  - Halcon
  - C#
  - 内存泄漏
  - .NET
categories:
  - 机器视觉
series:
  - 视觉入门到交付
weight: 6
---

## 前言

事情是这样的：

产线上线第三天，现场打来电话——"上位机跑了一上午，操作越来越卡，最后崩了，报 OutOfMemoryException。"

远程连上去一看，任务管理器里进程内存 1.8GB，还在涨。刚启动时只有 80MB。

这不是 Halcon 的 Bug，是**我代码的 Bug**。并且很惭愧，这个 bug 我在之前的文章里自己就写过。

排查过程走了不少弯路，记录成文，希望其他人不要重复踩。

---

## 现象

| 时间 | 内存占用 | 备注 |
|------|---------|------|
| 启动 | 80 MB | 正常 |
| 1 小时 | 350 MB | 察觉不到 |
| 2 小时 | 620 MB | 轻微卡顿 |
| 4 小时 | 1.1 GB | 操作明显变慢 |
| 8 小时 | 1.8 GB | 崩溃 |

在 .NET 里，这种**持续增长但从不下降**的模式，基本是：
- 有对象被持有了永远不会释放（引用泄漏）
- 或者非托管资源没释放（内存泄漏）

---

## 排查工具

| 工具 | 用途 | 链接 |
|------|------|------|
| **dotMemory** | .NET 内存快照对比 | JetBrains 付费 |
| **Windbg + SOS** | 生产环境离线分析 | 免费 |
| **Visual Studio Diagnostic Tools** | 实时内存分析 | VS 自带 |
| **PerfView** | 托管/非托管全面分析 | 微软免费 |

现场没有 VS，只能用 Windbg 抓 dump。这里用 Visual Studio 的 Diagnostic Tools 来复现分析步骤。

---

## 排查过程

### Step 1：确认是托管泄漏还是非托管泄漏

```
内存持续上涨 → 怀疑泄漏
        ↓
   抓第一个内存快照（启动后不久）
   抓第二个内存快照（2小时后）
        ↓
   对比快照 → 发现 HObject 实例数量暴涨
   其他托管对象无明显异常
```

关键证据：差量快照显示多出了 **数千个 `HObject` 实例**，但代码里明明调了 `Dispose()`。

### Step 2：定位到持有引用的地方

```
HObject × 4800（2小时差量）
    ↓
谁持有这些对象？
    ↓
ConcurrentQueue<HObject> 内部数组引用了它们
    ↓
队列深度 4800，处理线程消费太慢！
```

问题暴露了：取图线程往队列里扔 `HObject`，但处理线程来不及消费，队列越堆越深，已经处理完的对象也被队列引用着无法释放。

### Step 3：跟踪到根因

```csharp
// ❌ 错误代码（这就是我第一篇 Halcon 文章里写的）
ConcurrentQueue<HObject> queue = new ConcurrentQueue<HObject>();

// 取图线程（快：30fps）
while (running)
{
    GrabImage(out img, handle);
    queue.Enqueue(img.Clone());  // ← 这里！
    img.Dispose();
}

// 处理线程（慢：5fps）
while (running)
{
    if (queue.TryDequeue(out HObject frame))
    {
        ProcessImage(frame);
        frame.Dispose();
    }
}
```

取图 30fps 入队，处理 5fps 出队，差值 25fps。队列越堆越多，里面排队的 `HObject` 全部持有 Halcon 的非托管图像内存。

---

## 3 种解决方案

### 方案 1：限制队列最大长度（最简单）

```csharp
// 取图时检查队列长度，满了就丢弃旧帧
ConcurrentQueue<HObject> queue = new ConcurrentQueue<HObject>();

while (running)
{
    GrabImage(out img, handle);

    if (queue.Count < queueSizeLimit)  // 如：30
    {
        queue.Enqueue(img.Clone());
    }
    // 队列满了就直接丢弃，不排队
    // 视觉程序**不需要**每一帧都处理
    // 处理最新的帧比处理"还没排到的旧帧"更有意义

    img.Dispose();
}
```

### 方案 2：环形缓冲（推荐）

```csharp
public class RingBuffer<T> where T : class
{
    private readonly T[] _buffer;
    private int _head;
    private int _tail;
    private readonly object _lock = new object();

    public RingBuffer(int capacity)
    {
        _buffer = new T[capacity];
        _head = 0;
        _tail = 0;
    }

    public void Write(T item)
    {
        lock (_lock)
        {
            // 如果满了，覆盖最旧的数据并释放旧对象
            var old = _buffer[_head];
            if (old is IDisposable d) d.Dispose();

            _buffer[_head] = item;
            _head = (_head + 1) % _buffer.Length;
        }
    }

    public bool Read(out T item)
    {
        lock (_lock)
        {
            if (_tail == _head)
            {
                item = null;
                return false;
            }
            item = _buffer[_tail];
            _buffer[_tail] = null;
            _tail = (_tail + 1) % _buffer.Length;
            return true;
        }
    }
}
```

用这个环形缓冲代替 `ConcurrentQueue`，满了自动覆盖最旧帧，不会无限堆积。

### 方案 3：事件驱动（最省内存）

```csharp
// 直接用事件回调，不要队列
// 效果：如果处理太慢，下一帧来了直接覆盖当前帧
// 永远只保留 1 帧在处理

private HObject _currentFrame;
private readonly object _frameLock = new object();
private bool _isProcessing;

camera.FrameCaptured += (img) =>
{
    lock (_frameLock)
    {
        _currentFrame?.Dispose();
        _currentFrame = img.Clone();

        if (!_isProcessing)
        {
            _isProcessing = true;
            // signal worker to process
        }
    }
};
```

**注意：** 这个方案的前提是你的视觉程序允许丢帧。OK/NG 检测式的视觉应用完全允许丢帧——**最新的帧比旧帧重要**。

---

## 额外发现：HOperatorSet 线程安全问题

排查过程中还发现了一个非泄漏但会导致内存异常增长的问题：

```csharp
// ❌ 多个线程同时调用 HOperatorSet
// Halcon 的 HOperatorSet 不是线程安全的！

// 线程 1：取图
new Thread(() => HOperatorSet.GrabImage(out img, handle)).Start();

// 线程 2：匹配
new Thread(() => HOperatorSet.FindShapeModel(...)).Start();

// 结果：内部的 Halcon 引擎可能死锁或异常
// 表现为内存异常 + 卡死
```

**正确做法：**

```csharp
// ✅ 取图和匹配串行化
// 或者把匹配操作放到取图线程里（取完直接匹配）
// 或者每个线程用独立的 HOperatorSet 上下文（不推荐，太费资源）
```

最简单的做法就是：**取图和图像处理都在同一个线程里串行执行**，取图 → 处理 → 取下一帧。30fps 的相机，单帧处理在 20ms 内完成的话，完全跟得上。

---

## 排查清单速查表

| 现象 | 可能原因 | 怎么查 |
|------|---------|--------|
| 内存持续涨，GC 不回收 | 队列/列表持有引用 | 查 `ConcurrentQueue.Count` |
| 内存涨到某个值不动了 | 队列满了，但正常往下走 | 问题不大，但说明处理跟不上 |
| 内存涨到 OOM 崩溃 | 队列无限增长 | 加最大长度限制 |
| 释放了还涨 | 非托管泄漏（HObject没Dispose） | 搜代码里 `out HObject` 的地方 |
| 偶尔暴涨一次 | 某次采集或处理异常，临时对象没释放 | try/catch/finally 确保 Dispose |
| GC 后内存不回缩 | 对象被 Pinned 或进入 LOH | dotMemory 查大对象堆 |

---

## 最终修复效果

```
修复前：
  启动 → 8小时 → 1.8GB → OOM崩溃

修复后（环形缓冲 + 串行处理）：
  启动 → 24小时 → 82-95MB（稳定）
```

内存从 1.8GB 降到 95MB，跑了 24 小时纹丝不动。

回头想想，这个 Bug 本质上就是**生产者比消费者快，且没有背压机制**。视觉程序里这个模式太常见了，不止是 Halcon，任何有图像队列的场景都要注意。

*发布日期：2026-07-02*  
*标签：#机器视觉 #Halcon #C# #内存泄漏 #.NET*
