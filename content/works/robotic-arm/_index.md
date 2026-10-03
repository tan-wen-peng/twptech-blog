---
title: "机械臂"
description: "作品 · 机械臂：成图大赛机械类赛题复现——气动楔块杠杆式回转夹爪整机建模"
hideMeta: true
---

<style>
/* ===== 鸭子分区 · 专属视觉 ===== */
.works-wrap { --works-accent: #7C4DFF; --works-accent-deep: #5E35B1; }

/* Hero */
.works-hero {
  position: relative;
  overflow: hidden;
  border-radius: 16px;
  padding: 3.2rem 2rem 2.6rem;
  margin-bottom: 2.5rem;
  background:
    radial-gradient(ellipse 60% 70% at 15% 10%, rgba(124,77,255,0.16) 0%, transparent 60%),
    radial-gradient(ellipse 50% 60% at 85% 90%, rgba(64,158,255,0.12) 0%, transparent 55%),
    linear-gradient(150deg, var(--bg-dark) 0%, var(--bg-medium) 100%);
  border: 1px solid var(--border-color);
  border-bottom: 2px solid var(--works-accent);
  text-align: center;
}
.works-hero::after {
  content: "🦆";
  position: absolute;
  right: 1.2rem;
  bottom: -1.4rem;
  font-size: 7rem;
  opacity: 0.07;
  transform: rotate(-12deg);
  pointer-events: none;
}
.works-badge {
  display: inline-block;
  font-size: 0.68rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--works-accent);
  border: 1px solid rgba(124,77,255,0.35);
  padding: 5px 14px;
  border-radius: 3px;
  margin-bottom: 1.4rem;
  font-weight: 500;
}
.works-hero h1 {
  font-size: clamp(2rem, 5.5vw, 3rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: var(--text-primary);
  margin: 0 0 0.7rem;
  border: none;
}
.works-hero h1 .hl {
  background: linear-gradient(135deg, #B39DFF 0%, var(--works-accent) 55%, var(--works-accent-deep) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.works-hero p.lead {
  font-size: clamp(0.9rem, 2vw, 1.05rem);
  color: var(--text-secondary);
  max-width: 620px;
  margin: 0 auto 1.6rem;
  line-height: 1.7;
  font-weight: 300;
}
.works-hero-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
}
.works-chip {
  font-size: 0.75rem;
  padding: 5px 14px;
  border-radius: 20px;
  background: var(--bg-hover);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  transition: all 0.25s ease;
}
.works-chip:hover {
  border-color: var(--works-accent);
  color: var(--works-accent);
  transform: translateY(-1px);
}

/* Section title */
.works-sec { margin: 3rem 0; }
.works-sec-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.3rem;
  border: none;
}
.works-sec-title::before {
  content: "";
  width: 4px;
  height: 20px;
  border-radius: 2px;
  background: linear-gradient(180deg, var(--works-accent), var(--works-accent-deep));
}
.works-sec-sub {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin: 0 0 1.6rem 14px;
}

/* Goal cards */
.works-goals {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.1rem;
}
.works-goal {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.6rem 1.4rem;
  transition: all 0.3s ease;
}
.works-goal:hover {
  transform: translateY(-3px);
  border-color: var(--works-accent);
  box-shadow: 0 8px 24px var(--shadow-color);
}
.works-goal .num {
  font-family: "SF Mono", Consolas, monospace;
  font-size: 0.8rem;
  color: var(--works-accent);
  font-weight: 600;
  letter-spacing: 1px;
}
.works-goal h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0.5rem 0 0.5rem;
  border: none;
}
.works-goal p {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.65;
  margin: 0;
}

/* Progress */
.works-progress {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 1.8rem;
}
.works-progress-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 1.2rem;
}
.works-progress-head .now {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
}
.works-progress-head .now em {
  font-style: normal;
  color: var(--works-accent);
}
.works-progress-head .pct {
  font-family: "SF Mono", Consolas, monospace;
  font-size: 0.8rem;
  color: var(--text-muted);
}
.works-track {
  display: flex;
  gap: 6px;
  margin-bottom: 1.4rem;
}
.works-track span {
  flex: 1;
  height: 8px;
  border-radius: 4px;
  background: var(--bg-hover);
  border: 1px solid var(--border-color);
}
.works-track span.done { background: linear-gradient(90deg, var(--works-accent), var(--works-accent-deep)); border-color: transparent; }
.works-track span.active { background: rgba(124,77,255,0.25); border-color: var(--works-accent); animation: workspulse 2s infinite; }
@keyframes workspulse { 0%,100%{opacity:1} 50%{opacity:0.45} }
.works-steps {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 8px;
  margin: 0; padding: 0; list-style: none;
}
.works-steps li {
  font-size: 0.78rem;
  color: var(--text-muted);
  padding: 8px 12px;
  border-radius: 8px;
  background: var(--bg-medium);
  border: 1px solid var(--border-color);
  display: flex; align-items: center; gap: 7px;
}
.works-steps li.done { color: var(--text-secondary); }
.works-steps li.done::before { content: "✔"; color: var(--accent-green); font-size: 0.7rem; }
.works-steps li.active { color: var(--works-accent); border-color: var(--works-accent); }
.works-steps li.active::before { content: "▸"; }
.works-steps li.todo::before { content: "○"; font-size: 0.7rem; }

/* Stats */
.works-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1px;
  background: var(--border-color);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  overflow: hidden;
}
.works-stat {
  background: var(--bg-card);
  text-align: center;
  padding: 1.5rem 1rem;
}
.works-stat .v {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--works-accent);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
.works-stat .k {
  font-size: 0.72rem;
  color: var(--text-muted);
  margin-top: 0.35rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Tables */
.works-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
  border: 1px solid var(--border-color);
  border-radius: 10px;
  overflow: hidden;
}
.works-table th, .works-table td {
  padding: 10px 14px;
  text-align: left;
  border-bottom: 1px solid var(--border-color);
}
.works-table th {
  background: var(--bg-medium);
  color: var(--text-secondary);
  font-weight: 600;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.works-table td { color: var(--text-muted); }
.works-table tr:last-child td { border-bottom: none; }
.works-table tr:hover td { background: var(--bg-hover); }
.works-pill {
  display: inline-block;
  font-size: 0.7rem;
  padding: 2px 10px;
  border-radius: 3px;
  font-weight: 500;
}
.works-pill.done { background: rgba(0,230,118,0.15); color: var(--accent-green); }
.works-pill.doing { background: rgba(124,77,255,0.15); color: var(--works-accent); }
.works-pill.todo { background: rgba(123,143,168,0.15); color: var(--text-muted); }

/* Disclaimer */
.works-note {
  border-left: 3px solid var(--works-accent);
  background: var(--bg-card);
  border-radius: 0 10px 10px 0;
  padding: 1.1rem 1.4rem;
  font-size: 0.82rem;
  color: var(--text-muted);
  line-height: 1.7;
}
.works-note strong { color: var(--text-secondary); }

.works-gallery { display:grid; grid-template-columns: repeat(auto-fit, minmax(300px,1fr)); gap:1.2rem; }
.works-gallery figure { margin:0; background:var(--bg-card); border:1px solid var(--border-color); border-radius:12px; overflow:hidden; padding:0.8rem; }
.works-gallery img { width:100%; height:auto; border-radius:8px; display:block; background:#0d1a2f; }
.works-gallery figcaption { font-size:0.8rem; color:var(--text-muted); text-align:center; padding:0.6rem 0 0.2rem; }
</style>
<div class="works-wrap">

<div class="works-hero">
  <div class="works-badge">练习作品 · 赛题复现 · 未参赛</div>
  <h1>把一张二维图纸<br>变成<span class="hl">整台机械手</span></h1>
  <p class="lead">
    以第十六届「高教杯」全国大学生先进成图技术与产品信息建模创新大赛
    <strong>机械类产品信息建模试卷</strong>为对象，独立完成的气动楔块杠杆式回转夹爪整机建模。<br>
    从读图、建零件、装配到参数化——全程一人完成，作为能力展示公开。
  </p>
  <div class="works-hero-tags">
    <span class="works-chip">🦾 气动回转夹爪</span>
    <span class="works-chip">🧊 布尔运算建模</span>
    <span class="works-chip">📐 全参数化</span>
    <span class="works-chip">⚙️ 机构连接</span>
    <span class="works-chip">📏 二维反建三维</span>
  </div>
</div>

<!-- 背景 -->
<div class="works-sec">
  <h2 class="works-sec-title">作品背景</h2>
  <p class="works-sec-sub">BACKGROUND · 如实说明</p>
  <div class="works-goals">
    <div class="works-goal">
      <div class="num">01</div>
      <h3>对象</h3>
      <p>成图大赛国赛机械类产品信息建模赛题：一台<strong>气动楔块杠杆式回转夹爪</strong>。
      回转缸体（轴承 6015 / 16007）、夹紧缸体、活塞、楔块、杠杆、手指、电位器座、压缩 / 拉伸弹簧，40+ 种零件。</p>
    </div>
    <div class="works-goal">
      <div class="num">02</div>
      <h3>定性</h3>
      <p>这是官方公开赛题的<strong>个人练习复现</strong>——<strong>没有参赛</strong>，也不代表任何成绩。
      赛题图纸来自公开资料，所有零件均按图纸独立重建。</p>
    </div>
    <div class="works-goal">
      <div class="num">03</div>
      <h3>目的</h3>
      <p>用一个有难度的完整产品，检验三件事：二维图纸读图反建、高级特征建模（布尔 / 相交 / 螺旋扫描）、参数化与装配。</p>
    </div>
  </div>
</div>

<!-- 做了什么 -->
<div class="works-sec">
  <h2 class="works-sec-title">我做了什么</h2>
  <p class="works-sec-sub">WHAT I DID</p>
  <table class="works-table">
    <thead>
      <tr><th>环节</th><th>内容</th></tr>
    </thead>
    <tbody>
      <tr><td>读图反建</td><td>按试卷二维工程图建立 <strong>29 个零件</strong>，含后盖、回转缸体、夹紧缸体、楔块、杠杆、手指等全部自制件</td></tr>
      <tr><td>装配</td><td>5 层装配结构：<strong>000_机械手整体 → 夹爪 / 联轴 / base / 6015</strong> 四个子装配</td></tr>
      <tr><td>高级特征</td><td>布尔运算、相交、实体化、镜像、阵列、倒角/圆角、<strong>12 处参数化螺纹特征</strong>（M4~M10）</td></tr>
      <tr><td>弹簧</td><td>压缩 / 拉伸弹簧按 <strong>7 参数方程曲线方案</strong>建立，并封装成 UDF（<code>弹簧.gph</code>）</td></tr>
      <tr><td>环形切除</td><td>沉孔 / 环形槽封装为 UDF（<code>环形切除.gph</code>），多处复用</td></tr>
      <tr><td>机构</td><td>按运动关系建立机构连接，并做运动约束检查</td></tr>
    </tbody>
  </table>
</div>

<!-- 作品展示 -->
<div class="works-sec">
  <h2 class="works-sec-title">作品展示</h2>
  <p class="works-sec-sub">GALLERY</p>
  <div class="works-gallery">
    <figure>
      <img src="/images/works/cover.webp" alt="机械手整体渲染图" loading="lazy" />
      <figcaption>机械手整体渲染图</figcaption>
    </figure>
    <figure>
      <img src="/images/works/section-view.webp" alt="剖面分析图" loading="lazy" />
      <figcaption>剖面分析图</figcaption>
    </figure>
  </div>
  <div class="works-note" style="margin-top:1rem">
    更多视图（爆炸图、手指开合状态、各子装配拆解）会陆续补充。
  </div>
</div>

<!-- 技术账 -->
<div class="works-sec">
  <h2 class="works-sec-title">建模技术账</h2>
  <p class="works-sec-sub">NUMBERS</p>
  <div class="works-stats">
    <div class="works-stat"><div class="v">29</div><div class="k">自制零件</div></div>
    <div class="works-stat"><div class="v">5</div><div class="k">装配层级</div></div>
    <div class="works-stat"><div class="v">12</div><div class="k">螺纹特征</div></div>
    <div class="works-stat"><div class="v">6</div><div class="k">螺旋扫描</div></div>
    <div class="works-stat"><div class="v">2</div><div class="k">UDF 复用</div></div>
  </div>
</div>

<!-- 亮点 -->
<div class="works-sec">
  <h2 class="works-sec-title">一个亮点：弹簧是从方程里长出来的</h2>
  <p class="works-sec-sub">HIGHLIGHT</p>
  <p style="font-size:0.92rem;line-height:1.8;color:var(--text-muted)">
    这台机械手里的压缩弹簧和拉伸弹簧，用的是和本站教程
    <a href="/posts/spring-parametric/" style="color:var(--works-accent);text-decoration:none;border-bottom:1px solid var(--works-accent)">
    《弹簧不是画出来的，是算出来的——Creo 参数化变径弹簧实操》</a>
    完全相同的方案：<strong>7 个参数（高度 / 圈数 / 线径 / 大端直径 / 小端直径 / 两端支撑圈数）+ 三段柱坐标方程曲线 + 修剪 + 扫描</strong>，
    并且封装成了 UDF。教程里的做法，在这台整机里被当成标准件直接复用——改一个数字，弹簧自动重建。
  </p>
</div>


<!-- 赛题图纸 -->
<div class="works-sec">
  <h2 class="works-sec-title">赛题图纸（已去水印）</h2>
  <p class="works-sec-sub">CONTEST DRAWINGS · 7 页 · 仅作学习参考</p>
  <div class="works-gallery">
    <figure><img src="/images/works/drawings/page-01.webp" alt="赛题图纸第1页" loading="lazy"><figcaption>第 1 页 · 明细表与装配图</figcaption></figure>
    <figure><img src="/images/works/drawings/page-02.webp" alt="赛题图纸第2页" loading="lazy"><figcaption>第 2 页</figcaption></figure>
    <figure><img src="/images/works/drawings/page-03.webp" alt="赛题图纸第3页" loading="lazy"><figcaption>第 3 页 · 试卷封面</figcaption></figure>
    <figure><img src="/images/works/drawings/page-04.webp" alt="赛题图纸第4页" loading="lazy"><figcaption>第 4 页</figcaption></figure>
    <figure><img src="/images/works/drawings/page-05.webp" alt="赛题图纸第5页" loading="lazy"><figcaption>第 5 页</figcaption></figure>
    <figure><img src="/images/works/drawings/page-06.webp" alt="赛题图纸第6页" loading="lazy"><figcaption>第 6 页</figcaption></figure>
    <figure><img src="/images/works/drawings/page-07.webp" alt="赛题图纸第7页" loading="lazy"><figcaption>第 7 页</figcaption></figure>
  </div>
  <div class="works-note" style="margin-top:1rem">
    <strong>说明：</strong>图纸版权归大赛组委会及相关出题方所有。原分享版中的第三方推广水印已去除，
    官方图纸内容未做任何修改；本页仅用于个人学习记录与能力展示。
  </div>
</div>

<!-- 说明 -->
<div class="works-sec">
  <div class="works-note">
    <strong>说明：</strong>本作品为第十六届「高教杯」成图大赛机械类产品信息建模试卷的<strong>个人练习复现，未参赛</strong>。
    赛题与图纸版权归大赛组委会及相关出题方所有；本页仅展示个人建模能力与过程记录，不用于任何商业用途。
  </div>
</div>

</div>
