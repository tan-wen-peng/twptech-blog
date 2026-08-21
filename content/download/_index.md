---
title: "📥 免费资源下载"
description: "机械设计自动化自研工具与模板：NX 出图示例、爆炸参数样例、钣金折弯速查表"
layout: "archives"
placeholder: ""
---

<style>
.download-hero {
  background: linear-gradient(135deg, #0f172a, #1e293b);
  border-radius: 12px;
  padding: 3rem 2rem;
  margin-bottom: 2rem;
  color: #fff;
}
.download-hero h1 {
  font-size: 1.8rem;
  margin: 0 0 0.5rem;
}
.download-hero p {
  color: rgba(255,255,255,0.6);
  margin: 0;
  line-height: 1.6;
}
.resource-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.2rem;
  margin: 2rem 0;
}
.resource-card {
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 1.5rem;
  transition: box-shadow 0.2s;
}
.resource-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.resource-card h3 {
  font-size: 1rem;
  margin: 0 0 0.4rem;
  display: flex;
  align-items: center;
  gap: 8px;
}
.resource-card h3 a {
  box-shadow: none;
  text-decoration: none;
}
.resource-card p {
  font-size: 0.85rem;
  color: #666;
  margin: 0 0 0.8rem;
  line-height: 1.5;
}
.resource-meta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.resource-tag {
  font-size: 0.7rem;
  padding: 2px 10px;
  border-radius: 3px;
  background: #e8edf5;
  color: #2563eb;
  font-weight: 500;
}
.resource-badge {
  font-size: 0.7rem;
  padding: 2px 10px;
  border-radius: 3px;
  background: #fef3c7;
  color: #92400e;
  font-weight: 500;
}
.resource-badge.live {
  background: #dcfce7;
  color: #166534;
}
</style>

<div class="download-hero">
  <h1>📥 自研工具与模板</h1>
  <p>每篇文章配套的源码、样例与速查表——不是演示玩具，都是产线上真实趟过雷之后沉淀下来的东西。</p>
</div>

## 已上架

<div class="resource-grid">

<div class="resource-card">
<h3>📐 NX 中心线示例源码（C++）</h3>
<p>NX12 NXOpen 制图环境创建中心线的完整模块源码，含"任意视图拾取投影边"的关联修正写法，配套《我给 NX 写出图插件》一文。</p>
<div class="resource-meta">
  <span class="resource-tag">NXOpen</span>
  <span class="resource-tag">C++</span>
  <span class="resource-badge live">可下载</span>
</div>
<h3><a href="/downloads/nx-centerline-example.cpp">⬇ 下载 nx-centerline-example.cpp</a></h3>
</div>

<div class="resource-card">
<h3>💥 爆炸参数提取样例</h3>
<p>NX 装配爆炸图组件显示名与 dx/dy/dz 偏移参数的提取结果样例，直观展示"爆炸参数"模块的输出格式。</p>
<div class="resource-meta">
  <span class="resource-tag">NX</span>
  <span class="resource-tag">爆炸图</span>
  <span class="resource-badge live">可下载</span>
</div>
<h3><a href="/downloads/explosion-params-example.txt">⬇ 下载 explosion-params-example.txt</a></h3>
</div>

<div class="resource-card">
<h3>📊 钣金折弯扣除速查表</h3>
<p>SPCC / SUS304 / AL5052 常用板厚的折弯扣除值与 K 因子速查（xlsx），直接进 Excel 或 ERP 用。</p>
<div class="resource-meta">
  <span class="resource-tag">钣金</span>
  <span class="resource-tag">DFM</span>
  <span class="resource-badge live">可下载</span>
</div>
<h3><a href="/downloads/bend-allowance-table.xlsx">⬇ 下载 bend-allowance-table.xlsx</a></h3>
</div>

<div class="resource-card">
<h3>🔧 NX 制图自动化工具集（全部源码）</h3>
<p>7 步出图向导 + 打标图、爆炸参数、爆炸图、球标模块，9333 行 C++，GitHub 开源，持续更新。</p>
<div class="resource-meta">
  <span class="resource-tag">GitHub</span>
  <span class="resource-tag">开源</span>
  <span class="resource-badge live">可下载</span>
</div>
<h3><a href="https://github.com/tan-wen-peng/UG_Draw_NXopen_Dill" target="_blank">⬇ 前往仓库 UG_Draw_NXopen_Dill</a></h3>
</div>

</div>

## 整理中

- **Creo 工程图模板** — 从公司项目沉淀的通用图框/标题栏模板，脱敏后上架。
- **M10 螺纹 UDF** — 配合《螺纹不是乱线，是三角形》一文的参数化 UDF 文件。

> 上架进度会在文章末尾同步。有问题发邮件到 **2129336372@qq.com**。

---

*资源均为个人整理，标注来源与版本日期；涉及公司图纸信息的内容一律脱敏后再发布。*
