---
title: "SO-101"
description: "SO-101 开源 6 轴机械臂 + LeRobot 学习记录 · 已下单采购等待到货 · 进度与花费如实标注"
hideMeta: true
---

<style>
/* ===== 鸭子分区 · 专属视觉 ===== */
.so101-wrap { --so101-accent: #00BFA5; --so101-accent-deep: #00897B; }

/* Hero */
.so101-hero {
  position: relative;
  overflow: hidden;
  border-radius: 16px;
  padding: 3.2rem 2rem 2.6rem;
  margin-bottom: 2.5rem;
  background:
    radial-gradient(ellipse 60% 70% at 15% 10%, rgba(0,191,165,0.16) 0%, transparent 60%),
    radial-gradient(ellipse 50% 60% at 85% 90%, rgba(64,158,255,0.12) 0%, transparent 55%),
    linear-gradient(150deg, var(--bg-dark) 0%, var(--bg-medium) 100%);
  border: 1px solid var(--border-color);
  border-bottom: 2px solid var(--so101-accent);
  text-align: center;
}
.so101-hero::after {
  content: "🦆";
  position: absolute;
  right: 1.2rem;
  bottom: -1.4rem;
  font-size: 7rem;
  opacity: 0.07;
  transform: rotate(-12deg);
  pointer-events: none;
}
.so101-badge {
  display: inline-block;
  font-size: 0.68rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--so101-accent);
  border: 1px solid rgba(0,191,165,0.35);
  padding: 5px 14px;
  border-radius: 3px;
  margin-bottom: 1.4rem;
  font-weight: 500;
}
.so101-hero h1 {
  font-size: clamp(2rem, 5.5vw, 3rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: var(--text-primary);
  margin: 0 0 0.7rem;
  border: none;
}
.so101-hero h1 .hl {
  background: linear-gradient(135deg, #4DD0C4 0%, var(--so101-accent) 55%, var(--so101-accent-deep) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.so101-hero p.lead {
  font-size: clamp(0.9rem, 2vw, 1.05rem);
  color: var(--text-secondary);
  max-width: 620px;
  margin: 0 auto 1.6rem;
  line-height: 1.7;
  font-weight: 300;
}
.so101-hero-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
}
.so101-chip {
  font-size: 0.75rem;
  padding: 5px 14px;
  border-radius: 20px;
  background: var(--bg-hover);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  transition: all 0.25s ease;
}
.so101-chip:hover {
  border-color: var(--so101-accent);
  color: var(--so101-accent);
  transform: translateY(-1px);
}

/* Section title */
.so101-sec { margin: 3rem 0; }
.so101-sec-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.3rem;
  border: none;
}
.so101-sec-title::before {
  content: "";
  width: 4px;
  height: 20px;
  border-radius: 2px;
  background: linear-gradient(180deg, var(--so101-accent), var(--so101-accent-deep));
}
.so101-sec-sub {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin: 0 0 1.6rem 14px;
}

/* Goal cards */
.so101-goals {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.1rem;
}
.so101-goal {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.6rem 1.4rem;
  transition: all 0.3s ease;
}
.so101-goal:hover {
  transform: translateY(-3px);
  border-color: var(--so101-accent);
  box-shadow: 0 8px 24px var(--shadow-color);
}
.so101-goal .num {
  font-family: "SF Mono", Consolas, monospace;
  font-size: 0.8rem;
  color: var(--so101-accent);
  font-weight: 600;
  letter-spacing: 1px;
}
.so101-goal h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0.5rem 0 0.5rem;
  border: none;
}
.so101-goal p {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.65;
  margin: 0;
}

/* Progress */
.so101-progress {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 1.8rem;
}
.so101-progress-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 1.2rem;
}
.so101-progress-head .now {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
}
.so101-progress-head .now em {
  font-style: normal;
  color: var(--so101-accent);
}
.so101-progress-head .pct {
  font-family: "SF Mono", Consolas, monospace;
  font-size: 0.8rem;
  color: var(--text-muted);
}
.so101-track {
  display: flex;
  gap: 6px;
  margin-bottom: 1.4rem;
}
.so101-track span {
  flex: 1;
  height: 8px;
  border-radius: 4px;
  background: var(--bg-hover);
  border: 1px solid var(--border-color);
}
.so101-track span.done { background: linear-gradient(90deg, var(--so101-accent), var(--so101-accent-deep)); border-color: transparent; }
.so101-track span.active { background: rgba(0,191,165,0.25); border-color: var(--so101-accent); animation: so101pulse 2s infinite; }
@keyframes so101pulse { 0%,100%{opacity:1} 50%{opacity:0.45} }
.so101-steps {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 8px;
  margin: 0; padding: 0; list-style: none;
}
.so101-steps li {
  font-size: 0.78rem;
  color: var(--text-muted);
  padding: 8px 12px;
  border-radius: 8px;
  background: var(--bg-medium);
  border: 1px solid var(--border-color);
  display: flex; align-items: center; gap: 7px;
}
.so101-steps li.done { color: var(--text-secondary); }
.so101-steps li.done::before { content: "✔"; color: var(--accent-green); font-size: 0.7rem; }
.so101-steps li.active { color: var(--so101-accent); border-color: var(--so101-accent); }
.so101-steps li.active::before { content: "▸"; }
.so101-steps li.todo::before { content: "○"; font-size: 0.7rem; }

/* Stats */
.so101-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1px;
  background: var(--border-color);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  overflow: hidden;
}
.so101-stat {
  background: var(--bg-card);
  text-align: center;
  padding: 1.5rem 1rem;
}
.so101-stat .v {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--so101-accent);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
.so101-stat .k {
  font-size: 0.72rem;
  color: var(--text-muted);
  margin-top: 0.35rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Tables */
.so101-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
  border: 1px solid var(--border-color);
  border-radius: 10px;
  overflow: hidden;
}
.so101-table th, .so101-table td {
  padding: 10px 14px;
  text-align: left;
  border-bottom: 1px solid var(--border-color);
}
.so101-table th {
  background: var(--bg-medium);
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.so101-table td { color: var(--text-muted); }
.so101-table tr:last-child td { border-bottom: none; }
.so101-table tr:hover td { background: var(--bg-hover); }
.so101-pill {
  display: inline-block;
  font-size: 0.7rem;
  padding: 2px 10px;
  border-radius: 3px;
  font-weight: 500;
}
.so101-pill.done { background: rgba(0,230,118,0.15); color: var(--accent-green); }
.so101-pill.doing { background: rgba(0,191,165,0.15); color: var(--so101-accent); }
.so101-pill.todo { background: rgba(123,143,168,0.15); color: var(--text-muted); }

/* Disclaimer */
.so101-note {
  border-left: 3px solid var(--so101-accent);
  background: var(--bg-card);
  border-radius: 0 10px 10px 0;
  padding: 1.1rem 1.4rem;
  font-size: 0.82rem;
  color: var(--text-muted);
  line-height: 1.7;
}
.so101-note strong { color: var(--text-secondary); }
</style>

<div class="so101-wrap">

<div class="so101-hero">
  <div class="so101-badge">SO-101 · 开源 6 轴机械臂</div>
  <h1>让机械臂<span class="hl">自己学会抓</span></h1>
  <p class="lead">
    一台 3D 打印的 6 自由度开源机械臂，跑在 Hugging Face LeRobot 生态里。<br>
    从装机、标定、遥操作采数据，到训练 ACT 策略、真机评估——全过程公开，每个结论都带数字。
  </p>
  <div class="so101-hero-tags">
    <span class="so101-chip">🦾 SO-101 双臂</span>
    <span class="so101-chip">🤗 LeRobot 生态</span>
    <span class="so101-chip">🎯 ACT 模仿学习</span>
    <span class="so101-chip">🖨️ 3D 打印结构件</span>
    <span class="so101-chip">📊 成功率可量化</span>
  </div>
</div>

<!-- 目标 -->
<div class="so101-sec">
  <h2 class="so101-sec-title">这个项目要做成什么样</h2>
  <p class="so101-sec-sub">PROJECT GOALS</p>
  <div class="so101-goals">
    <div class="so101-goal">
      <div class="num">01</div>
      <h3>跑通全链路</h3>
      <p>装机 → 标定 → 遥操作 → 采数据 → 训策略 → 真机评估。每一步都留下可复现的记录，而不是只截一张成功的图。</p>
    </div>
    <div class="so101-goal">
      <div class="num">02</div>
      <h3>结论必须带数字</h3>
      <p>成本、数据条数、抓取成功率、推理延迟、单次任务耗时——五个数字都要实测。不写「效果不错」这种话。</p>
    </div>
    <div class="so101-goal">
      <div class="num">03</div>
      <h3>做出别人没做的那一步</h3>
      <p>不做官方教程的搬运工。机械改进件或数据效率消融，选一到两个做深，用 A/B 对比说话。</p>
    </div>
  </div>
</div>

<!-- 进度 -->
<div class="so101-sec">
  <h2 class="so101-sec-title">现在做到哪了</h2>
  <p class="so101-sec-sub">BUILD PROGRESS · 采购中</p>
  <div class="so101-progress">
    <div class="so101-progress-head">
      <div class="now">当前 · 采购阶段 <em>9 类已下单，等待到货</em></div>
      <div class="pct">2 / 7</div>
    </div>
    <div class="so101-track">
      <span class="done"></span><span class="active"></span><span></span><span></span><span></span><span></span><span></span>
    </div>
    <ul class="so101-steps">
      <li class="done">准备 · 路线与打样清单</li>
      <li class="active">采购 · 下单与到货</li>
      <li class="todo">阶段 0 · 把机器动起来</li>
      <li class="todo">阶段 1 · 采数据</li>
      <li class="todo">阶段 2 · 训练与评估</li>
      <li class="todo">阶段 3 · 机械改进 / 数据消融</li>
      <li class="todo">阶段 4 · 包装与发布</li>
    </ul>
  </div>
</div>

<!-- 硬件与预算 -->
<div class="so101-sec">
  <h2 class="so101-sec-title">硬件与预算</h2>
  <p class="so101-sec-sub">PARTS &amp; SPEND · 约 ¥1373–1385（G 型夹按估算浮动）</p>
  <div class="so101-stats">
    <div class="so101-stat"><div class="v">¥1373+</div><div class="k">已发生支出</div></div>
    <div class="so101-stat"><div class="v">9 类</div><div class="k">已下单</div></div>
    <div class="so101-stat"><div class="v">12 个</div><div class="k">舵机（双臂）</div></div>
    <div class="so101-stat"><div class="v">10 天</div><div class="k">最慢一件 · 代打</div></div>
  </div>
</div>

<!-- 采购清单 -->
<div class="so101-sec">
  <h2 class="so101-sec-title">采购清单（实付）</h2>
  <p class="so101-sec-sub">PURCHASE LOG · 2026-09-20 下单，按实付金额排序</p>
  <table class="so101-table">
    <thead>
      <tr><th>平台</th><th>物品</th><th>实付</th><th>状态</th></tr>
    </thead>
    <tbody>
      <tr><td>淘宝</td><td>飞特 ST3215 舵机 ×12</td><td>¥1080.00</td><td><span class="so101-pill doing">待发货</span></td></tr>
      <tr><td>拼多多</td><td>3D 打印结构件代打</td><td>¥136.20</td><td><span class="so101-pill doing">待发货 · 最慢</span></td></tr>
      <tr><td>淘宝</td><td>微雪总线舵机驱动板 (A) ×2</td><td>¥59.46</td><td><span class="so101-pill doing">待发货</span></td></tr>
      <tr><td>淘宝</td><td>5V6A 电源适配器 ×2</td><td>¥32.38</td><td><span class="so101-pill doing">待发货</span></td></tr>
      <tr><td>京东</td><td>京东京造 Type-C 线 ×2</td><td>¥19.74</td><td><span class="so101-pill doing">正在出库</span></td></tr>
      <tr><td>拼多多</td><td>得力数显卡尺 0–150mm</td><td>¥17.91</td><td><span class="so101-pill doing">打包中</span></td></tr>
      <tr><td>拼多多</td><td>盛利德 9205A 万用表</td><td>¥17.43</td><td><span class="so101-pill doing">打包中</span></td></tr>
      <tr><td>拼多多</td><td>G 型夹 2 寸 ×2~3</td><td>约 ¥6–18</td><td><span class="so101-pill doing">刚下单</span></td></tr>
      <tr><td>拼多多</td><td>24 合一精密螺丝刀</td><td>¥3.80</td><td><span class="so101-pill doing">打包中</span></td></tr>
      <tr><td colspan="2"><strong>合计</strong></td><td><strong>约 ¥1373–1385</strong></td><td></td></tr>
    </tbody>
  </table>
  <div class="so101-note" style="margin-top:1rem">
    <strong>两笔账值得记：</strong>舵机实际单价 <strong>¥90.0/个</strong>（12 个 ¥1080），比官方 BOM 表里的 ¥97.72 便宜约 8%；
    结构件代打 <strong>¥136.20</strong>，比海外代打（双臂约 $95 ≈ ¥680）低得多。
    卡尺、万用表、精密螺丝刀、G 型夹属<strong>装配与测量工具</strong>，不进 BOM 但必须买——
    后面验收打印件配合精度靠的就是卡尺。
    <strong>关键路径是结构件代打（10 天）</strong>，其余件到齐了也得等它。
  </div>
</div>

<!-- 打样清单 -->
<div class="so101-sec">
  <h2 class="so101-sec-title">打样验证清单</h2>
  <p class="so101-sec-sub">PROTOTYPE PLAN · 基于 SO-ARM100 main（commit eecbe3e）</p>
  <table class="so101-table">
    <thead>
      <tr><th>批次</th><th>内容</th><th>状态</th></tr>
    </thead>
    <tbody>
      <tr><td>第 0 批 · 精度量具</td><td>4 个 Gauge（名义尺寸 / 紧配合 / 乐高尺寸 ×2）——先验打印方精度，成本几块钱</td><td><span class="so101-pill todo">待打样</span></td></tr>
      <tr><td>第 1 批 · 舵机槽件</td><td>8 件（Base_motor_holder / Rotation_Pitch / Motor_holder_Wrist / Wrist_Roll_Pitch 等）——风险最高</td><td><span class="so101-pill todo">待打样</span></td></tr>
      <tr><td>第 1 批 · 花键件</td><td>Moving_Jaw（夹爪）/ Trigger（扳机）——必须装上舵机输出实测转动</td><td><span class="so101-pill todo">待打样</span></td></tr>
      <tr><td>第 1 批 · 驱动板与结构件</td><td>WaveShare_Mounting_Plate + Base / Under_arm / Upper_arm</td><td><span class="so101-pill todo">待打样</span></td></tr>
      <tr><td>量具（随打样一起买）</td><td>STS3215 舵机、Waveshare 驱动板、Type-C 线 —— 均已下单，见下方采购清单（螺丝混装包待补）</td><td><span class="so101-pill doing">已下单</span></td></tr>
      <tr><td>第 2 批 · 量产</td><td>验收通过后按整盘文件打双份（Ender_Follower + Ender_Leader）</td><td><span class="so101-pill todo">待定义</span></td></tr>
    </tbody>
  </table>
</div>

<!-- 贡献方向 -->
<div class="so101-sec">
  <h2 class="so101-sec-title">我打算做深的方向</h2>
  <p class="so101-sec-sub">MY CONTRIBUTION · 选 1~2 个，不贪多</p>
  <div class="so101-goals">
    <div class="so101-goal">
      <div class="num">A</div>
      <h3>机械改进件</h3>
      <p>软指夹爪、相机支架、线缆管理、快换末端。纯做算法的人碰不了这一段——每版都做 A/B 成功率对比。</p>
    </div>
    <div class="so101-goal">
      <div class="num">B</div>
      <h3>边缘部署</h3>
      <p>ACT 导出 ONNX，在笔记本或树莓派上做 CPU 推理，测延迟与帧率，画精度-延迟权衡曲线。</p>
    </div>
    <div class="so101-goal">
      <div class="num">C</div>
      <h3>数据效率消融</h3>
      <p>10 / 25 / 50 / 100 条各训一次，画成功率-数据量曲线，用一张图回答「到底多少数据够用」。</p>
    </div>
    <div class="so101-goal">
      <div class="num">D</div>
      <h3>语音 / 语言条件</h3>
      <p>Whisper 中文指令 → 任务选择 → SmolVLA 执行，出效果最快的一条路。</p>
    </div>
  </div>
</div>

<!-- 声明 -->
<div class="so101-sec">
  <div class="so101-note">
    <strong>说明：</strong>本分区记录个人学习过程，基于开源项目
    <a href="https://github.com/TheRobotStudio/SO-ARM100" target="_blank" rel="noopener">SO-ARM100 / SO-101</a>
    与 Hugging Face <a href="https://github.com/huggingface/lerobot" target="_blank" rel="noopener">LeRobot</a>。
    <strong>进度如实标注，未完成的不写成已完成</strong>；踩坑与失败案例同样保留。
  </div>
</div>

</div>
