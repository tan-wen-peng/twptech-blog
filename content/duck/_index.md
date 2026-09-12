---
title: "超能花钱鸭"
description: "Microduck 1:1 复刻记录 · 非官方 · 仅用于个人学习与研究"
hideMeta: true
---

<style>
/* ===== 鸭子分区 · 专属视觉 ===== */
.duck-wrap { --duck-accent: #FFB300; --duck-accent-deep: #FF8F00; }

/* Hero */
.duck-hero {
  position: relative;
  overflow: hidden;
  border-radius: 16px;
  padding: 3.2rem 2rem 2.6rem;
  margin-bottom: 2.5rem;
  background:
    radial-gradient(ellipse 60% 70% at 15% 10%, rgba(255,179,0,0.16) 0%, transparent 60%),
    radial-gradient(ellipse 50% 60% at 85% 90%, rgba(64,158,255,0.12) 0%, transparent 55%),
    linear-gradient(150deg, var(--bg-dark) 0%, var(--bg-medium) 100%);
  border: 1px solid var(--border-color);
  border-bottom: 2px solid var(--duck-accent);
  text-align: center;
}
.duck-hero::after {
  content: "🦆";
  position: absolute;
  right: 1.2rem;
  bottom: -1.4rem;
  font-size: 7rem;
  opacity: 0.07;
  transform: rotate(-12deg);
  pointer-events: none;
}
.duck-badge {
  display: inline-block;
  font-size: 0.68rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--duck-accent);
  border: 1px solid rgba(255,179,0,0.35);
  padding: 5px 14px;
  border-radius: 3px;
  margin-bottom: 1.4rem;
  font-weight: 500;
}
.duck-hero h1 {
  font-size: clamp(2rem, 5.5vw, 3rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: var(--text-primary);
  margin: 0 0 0.7rem;
  border: none;
}
.duck-hero h1 .hl {
  background: linear-gradient(135deg, #FFD54F 0%, var(--duck-accent) 55%, var(--duck-accent-deep) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.duck-hero p.lead {
  font-size: clamp(0.9rem, 2vw, 1.05rem);
  color: var(--text-secondary);
  max-width: 620px;
  margin: 0 auto 1.6rem;
  line-height: 1.7;
  font-weight: 300;
}
.duck-hero-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
}
.duck-chip {
  font-size: 0.75rem;
  padding: 5px 14px;
  border-radius: 20px;
  background: var(--bg-hover);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  transition: all 0.25s ease;
}
.duck-chip:hover {
  border-color: var(--duck-accent);
  color: var(--duck-accent);
  transform: translateY(-1px);
}

/* Section title */
.duck-sec { margin: 3rem 0; }
.duck-sec-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.3rem;
  border: none;
}
.duck-sec-title::before {
  content: "";
  width: 4px;
  height: 20px;
  border-radius: 2px;
  background: linear-gradient(180deg, var(--duck-accent), var(--duck-accent-deep));
}
.duck-sec-sub {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin: 0 0 1.6rem 14px;
}

/* Goal cards */
.duck-goals {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.1rem;
}
.duck-goal {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.6rem 1.4rem;
  transition: all 0.3s ease;
}
.duck-goal:hover {
  transform: translateY(-3px);
  border-color: var(--duck-accent);
  box-shadow: 0 8px 24px var(--shadow-color);
}
.duck-goal .num {
  font-family: "SF Mono", Consolas, monospace;
  font-size: 0.8rem;
  color: var(--duck-accent);
  font-weight: 600;
  letter-spacing: 1px;
}
.duck-goal h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0.5rem 0 0.5rem;
  border: none;
}
.duck-goal p {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.65;
  margin: 0;
}

/* Progress */
.duck-progress {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 1.8rem;
}
.duck-progress-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 1.2rem;
}
.duck-progress-head .now {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
}
.duck-progress-head .now em {
  font-style: normal;
  color: var(--duck-accent);
}
.duck-progress-head .pct {
  font-family: "SF Mono", Consolas, monospace;
  font-size: 0.8rem;
  color: var(--text-muted);
}
.duck-track {
  display: flex;
  gap: 6px;
  margin-bottom: 1.4rem;
}
.duck-track span {
  flex: 1;
  height: 8px;
  border-radius: 4px;
  background: var(--bg-hover);
  border: 1px solid var(--border-color);
}
.duck-track span.done { background: linear-gradient(90deg, var(--duck-accent), var(--duck-accent-deep)); border-color: transparent; }
.duck-track span.active { background: rgba(255,179,0,0.25); border-color: var(--duck-accent); animation: duckpulse 2s infinite; }
@keyframes duckpulse { 0%,100%{opacity:1} 50%{opacity:0.45} }
.duck-steps {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 8px;
  margin: 0; padding: 0; list-style: none;
}
.duck-steps li {
  font-size: 0.78rem;
  color: var(--text-muted);
  padding: 8px 12px;
  border-radius: 8px;
  background: var(--bg-medium);
  border: 1px solid var(--border-color);
  display: flex; align-items: center; gap: 7px;
}
.duck-steps li.done { color: var(--text-secondary); }
.duck-steps li.done::before { content: "✔"; color: var(--accent-green); font-size: 0.7rem; }
.duck-steps li.active { color: var(--duck-accent); border-color: var(--duck-accent); }
.duck-steps li.active::before { content: "▸"; }
.duck-steps li.todo::before { content: "○"; font-size: 0.7rem; }

/* Stats */
.duck-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1px;
  background: var(--border-color);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  overflow: hidden;
}
.duck-stat {
  background: var(--bg-card);
  text-align: center;
  padding: 1.5rem 1rem;
}
.duck-stat .v {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--duck-accent);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
.duck-stat .k {
  font-size: 0.72rem;
  color: var(--text-muted);
  margin-top: 0.35rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Tables */
.duck-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
  border: 1px solid var(--border-color);
  border-radius: 10px;
  overflow: hidden;
}
.duck-table th, .duck-table td {
  padding: 10px 14px;
  text-align: left;
  border-bottom: 1px solid var(--border-color);
}
.duck-table th {
  background: var(--bg-medium);
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.duck-table td { color: var(--text-muted); }
.duck-table tr:last-child td { border-bottom: none; }
.duck-table tr:hover td { background: var(--bg-hover); }
.duck-pill {
  display: inline-block;
  font-size: 0.7rem;
  padding: 2px 10px;
  border-radius: 3px;
  font-weight: 500;
}
.duck-pill.done { background: rgba(0,230,118,0.15); color: var(--accent-green); }
.duck-pill.doing { background: rgba(255,179,0,0.15); color: var(--duck-accent); }
.duck-pill.todo { background: rgba(123,143,168,0.15); color: var(--text-muted); }

/* Disclaimer */
.duck-note {
  border-left: 3px solid var(--duck-accent);
  background: var(--bg-card);
  border-radius: 0 10px 10px 0;
  padding: 1.1rem 1.4rem;
  font-size: 0.82rem;
  color: var(--text-muted);
  line-height: 1.7;
}
.duck-note strong { color: var(--text-secondary); }
</style>

<div class="duck-wrap">

<div class="duck-hero">
  <div class="duck-badge">FANDUCK · 非官方复刻记录</div>
  <h1>超能<span class="hl">花钱鸭</span></h1>
  <p class="lead">
    一台开源桌面机器鸭 Microduck 的个人复刻记录。<br>
    在公开证据允许的范围内尽可能 1:1 还原，全程公开采购、装配、调试与踩坑。
  </p>
  <div class="duck-hero-tags">
    <span class="duck-chip">🦆 Microduck 复刻</span>
    <span class="duck-chip">🦿 16 自由度</span>
    <span class="duck-chip">🧠 强化学习策略</span>
    <span class="duck-chip">🔌 Robot HAT + Radxa</span>
    <span class="duck-chip">🇨🇳 国产替代探索</span>
  </div>
</div>

<!-- 目标 -->
<div class="duck-sec">
  <h2 class="duck-sec-title">这个项目要做三件事</h2>
  <p class="duck-sec-sub">PROJECT GOALS</p>
  <div class="duck-goals">
    <div class="duck-goal">
      <div class="num">01</div>
      <h3>尽可能还原原版</h3>
      <p>优先采用官方证据确认的原版组件，让机械、电子与软件设计尽可能贴近 Microduck。</p>
    </div>
    <div class="duck-goal">
      <div class="num">02</div>
      <h3>全过程持续公开</h3>
      <p>在许可允许的范围内，持续公开采购、制造、装配、测试与踩坑记录，让过程可追踪、可复现。</p>
    </div>
    <div class="duck-goal">
      <div class="num">03</div>
      <h3>探索国产替代路线</h3>
      <p>独立验证国产零件、控制链路与制造方案；不混入原版一致 BOM，也不冒充官方配置。</p>
    </div>
  </div>
</div>

<!-- 进度 -->
<div class="duck-sec">
  <h2 class="duck-sec-title">现在做到哪了</h2>
  <p class="duck-sec-sub">BUILD PROGRESS</p>
  <div class="duck-progress">
    <div class="duck-progress-head">
      <div class="now">当前 · 第 1 阶段 <em>立项与资料收集</em></div>
      <div class="pct">1 / 7</div>
    </div>
    <div class="duck-track">
      <span class="active"></span><span></span><span></span><span></span><span></span><span></span><span></span>
    </div>
    <ul class="duck-steps">
      <li class="active">立项与资料收集</li>
      <li class="todo">原版 BOM 梳理</li>
      <li class="todo">采购与到货</li>
      <li class="todo">机械装配</li>
      <li class="todo">上电与传感器</li>
      <li class="todo">策略部署</li>
      <li class="todo">整机站立</li>
    </ul>
  </div>
</div>

<!-- 花费 -->
<div class="duck-sec">
  <h2 class="duck-sec-title">配件和花费</h2>
  <p class="duck-sec-sub">PARTS &amp; SPEND · 随采购持续更新</p>
  <div class="duck-stats">
    <div class="duck-stat"><div class="v">¥0</div><div class="k">已发生支出</div></div>
    <div class="duck-stat"><div class="v">0 / 24</div><div class="k">硬件到货</div></div>
    <div class="duck-stat"><div class="v">0 / 9</div><div class="k">软件模块</div></div>
    <div class="duck-stat"><div class="v">第 1 周</div><div class="k">项目周期</div></div>
  </div>
</div>

<!-- 硬件清单 -->
<div class="duck-sec">
  <h2 class="duck-sec-title">硬件清单框架</h2>
  <p class="duck-sec-sub">HARDWARE BOM · 待逐项确认到货后打勾</p>
  <table class="duck-table">
    <thead>
      <tr><th>分组</th><th>关键件</th><th>状态</th></tr>
    </thead>
    <tbody>
      <tr><td>执行器与测试台架</td><td>XL330 系列舵机 ×16、U2D2 调试器、电机线</td><td><span class="duck-pill todo">待采购</span></td></tr>
      <tr><td>主控与 Robot HAT</td><td>Radxa ZERO 3W / microSD / Robot HAT</td><td><span class="duck-pill todo">待采购</span></td></tr>
      <tr><td>机械与轮滑附件</td><td>整机机械件、M2 紧固件、滚轮轴承、支架</td><td><span class="duck-pill todo">待采购</span></td></tr>
      <tr><td>视觉与姿态感知</td><td>MIPI 相机、ToF 阵列、头部 IMU</td><td><span class="duck-pill todo">待采购</span></td></tr>
      <tr><td>供电、音频与交互</td><td>电池、充电器、扬声器、麦克风、NFC 标签</td><td><span class="duck-pill todo">待采购</span></td></tr>
      <tr><td>板件与线束</td><td>头部/鸭嘴 PCB、电源板、整机线束</td><td><span class="duck-pill todo">待定义</span></td></tr>
    </tbody>
  </table>
</div>

<!-- 国产替代 -->
<div class="duck-sec">
  <h2 class="duck-sec-title">国产替代设想</h2>
  <p class="duck-sec-sub">DOMESTIC ALTERNATIVE · 仅概念，未采购、未打样、未装机</p>
  <div class="duck-goals">
    <div class="duck-goal">
      <div class="num">A</div>
      <h3>执行器与通信</h3>
      <p>国产舵机候选 + 单总线 USB 模块 + 半双工总线驱动；舵机动力学需重新标定扭矩、摩擦与延迟。</p>
    </div>
    <div class="duck-goal">
      <div class="num">B</div>
      <h3>感知与交互</h3>
      <p>国产双 IMU、MIPI-CSI 相机、ToF 阵列与 NFC 前端，头部/鸭嘴各一套候选。</p>
    </div>
    <div class="duck-goal">
      <div class="num">C</div>
      <h3>机械与软件</h3>
      <p>孔位与花键逐位测量、打印公差重新标定；总线驱动、多舵机闭环与策略重训安全门槛。</p>
    </div>
  </div>
</div>

<!-- 声明 -->
<div class="duck-sec">
  <div class="duck-note">
    <strong>声明：</strong>本分区为个人学习与研究性质的非官方复刻记录，
    不代表任何官方机构或原作者的授权、认证或商业背书。
    原版软件遵循 Apache 2.0，3D 模型采用非商业许可；本站不涉及任何商业销售行为。
    涉及他人图纸与资料的内容一律脱敏后再发布，如有异议请联系
    <a href="mailto:2129336372@qq.com">2129336372@qq.com</a>。
  </div>
</div>

</div>
