<div align="center">

<img src="assets/banner.svg" width="100%" alt="Yangxbao — Java 后端开发 × AI Agent 应用开发 · 信息管理与信息系统在读 · 正在寻找实习机会" />

</div>

## 🧭 关于我

我是 **Yangxbao**,信息管理与信息系统专业大三在读。比起罗列"学过什么",我更在意"**做出了什么**":把课堂上和自学中学到的东西,陆续做成了 **十几个能跑、能测、能交付的开源项目** —— 从 AI 研发协作平台、RAG 知识库,到 Android 应用与 Windows 桌面工具。

目前的主线:**Java 后端** 打地基,**AI Agent 应用** 往前冲;开发中大量使用 AI 辅助编码,但每一行进仓库的代码都以"本人实际运行验证"为标准。

<details>
<summary>⚠️ 诚实说明(建议展开看一眼)</summary>

- 本页所有项目均为**真实公开仓库**,开发方式为 **AI 辅助编码 + 本人设计、运行与验证**;
- 各项目的完成情况与未验证边界(如 DevPilot 的 Docker Compose 路径、真实 LLM Provider 效果)都在各自 README 中**如实披露**,不做任何夸大;
- 页面中的统计数据由第三方服务实时生成,仅作活跃度参考,**不代表技术水平**。

</details>

## ⚡ 技术方向

### ☕ Java 后端 &nbsp;<img src="https://img.shields.io/badge/方向-主力-3FB950?style=flat-square" alt="主力方向" />

<a href="https://github.com/Yangxbao?tab=repositories"><img src="https://skillicons.dev/icons?i=java,spring,mysql,redis,git,github&perline=12" alt="Java / Spring / MySQL / Redis" /></a>

- ✅ **已实践**(在开源项目中实际使用):Spring Boot 3 · MyBatis-Plus · Spring Security / JWT · MySQL 索引与 FULLTEXT · JUnit 集成测试 · GitHub Actions CI
- 🌱 **正在学习**:Redis 进阶 · 消息队列 · 分布式与微服务 · JVM 调优

### 🤖 AI Agent 应用 &nbsp;<img src="https://img.shields.io/badge/方向-主攻-7C3AED?style=flat-square" alt="主攻方向" />

<a href="https://github.com/Yangxbao?tab=repositories"><img src="https://skillicons.dev/icons?i=python,fastapi&perline=12" alt="Python / FastAPI" /></a>

- ✅ **已实践**(三个项目落地):RAG 全链路(解析 → 分块 → 索引 → 混合检索 → 证据引用)· Agent 工作流与工具白名单 · OpenAI 兼容 Provider 适配与降级
- 🌱 **正在学习**:向量数据库 · 多 Agent 协作 · 提示词工程

### 📱 移动端与前端 &nbsp;<img src="https://img.shields.io/badge/方向-实践中-58A6FF?style=flat-square" alt="实践中" />

<a href="https://github.com/Yangxbao?tab=repositories"><img src="https://skillicons.dev/icons?i=kotlin,android,vue,ts,html,css&perline=12" alt="Kotlin / Android / Vue / TypeScript" /></a>

- ✅ **已实践**:Kotlin + Jetpack Compose / Room / CameraX / ML Kit(**3 个 Android 应用,2 个发布 Release**)· Vue 3 + Element Plus + Pinia(4 个全栈项目前端)
- 🌱 **正在学习**:TypeScript 进阶 · 响应式布局

<div align="center">
<img src="assets/divider.svg" width="70%" alt="" />
</div>

## 🚀 精选项目

### 🥇 DevPilot — 自托管 AI 研发协作平台

<a href="https://github.com/Yangxbao/DevPilot">
  <img src="https://raw.githubusercontent.com/Yangxbao/DevPilot/main/docs/screenshots/04-qa-with-evidence.png" width="100%" alt="DevPilot AI 问答界面:回答附带可点击的代码证据引用" />
</a>

**让"读懂一个陌生代码库"变成可工程化的事**:代码库导入 → 关键词/语义混合检索 → **带证据引用的 AI 问答与 Bug 根因分析** → 缺陷任务闭环。

- 🔎 混合检索:MySQL FULLTEXT 关键词 + FTS5/向量语义,RRF 融合排序,结果带路径与行号
- 🤖 8 步 Agent 工作流:每条结论附**可点击核对的代码证据**,引用合法性自动核查
- 🐞 缺陷闭环:AI 分析一键转缺陷,状态机服务端校验,项目数据隔离
- 🧪 工程质量:20 JUnit + 31 pytest + 3 前端测试 + **18 步 E2E 全链路** + GitHub Actions CI

<img src="https://img.shields.io/badge/状态-三端可运行-3FB950?style=flat-square" alt="状态" />
<img src="https://img.shields.io/badge/测试-54项自动化_·_18步E2E-3FB950?style=flat-square" alt="测试" />
<img src="https://img.shields.io/badge/Java-21-blue?style=flat-square" alt="Java 21" />
<img src="https://img.shields.io/badge/Spring_Boot-3.5-6DB33F?style=flat-square" alt="Spring Boot" />
<img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square" alt="FastAPI" />
<img src="https://img.shields.io/badge/Vue-3.5-42B883?style=flat-square" alt="Vue 3" />
&nbsp; **→ [进入仓库](https://github.com/Yangxbao/DevPilot)**

<div align="center">

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Yangxbao/OfferDojo">
        <img src="https://raw.githubusercontent.com/Yangxbao/OfferDojo/main/screenshots/dashboard.png" width="100%" alt="OfferDojo 工作台截图" />
      </a>
      <h4><a href="https://github.com/Yangxbao/OfferDojo">🎓 OfferDojo</a></h4>
      面向大学生的岗位实战模拟平台:<b>220 个模拟任务 + 125 道八股</b>,AI 结构化评估报告,能力雷达。零配置即可一键启动(H2 内嵌库)。
      <br/>
      <img src="https://img.shields.io/badge/状态-一键启动_·_CI通过-3FB950?style=flat-square" alt="状态" />
      <img src="https://img.shields.io/badge/Spring_Boot_3-Vue_3-6DB33F?style=flat-square" alt="技术栈" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Yangxbao/repopilot-ai">
        <img src="https://raw.githubusercontent.com/Yangxbao/repopilot-ai/main/docs/screenshots/qa.png" width="100%" alt="repopilot-ai 代码问答界面:引用文件与行号证据" />
      </a>
      <h4><a href="https://github.com/Yangxbao/repopilot-ai">🤖 repopilot-ai</a></h4>
      代码库知识问答与 Bug 分析 Agent:<b>先检索证据,再让 AI 回答</b>,引用精确到文件 + 行号;检索不到依据时如实回答"无法确定"。DevPilot 的前身。
      <br/>
      <img src="https://img.shields.io/badge/状态-H2零依赖演示-3FB950?style=flat-square" alt="状态" />
      <img src="https://img.shields.io/badge/RAG-证据引用-7C3AED?style=flat-square" alt="RAG" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Yangxbao/docmind">
        <img src="https://raw.githubusercontent.com/Yangxbao/docmind/main/docs/screenshots/01-semantic-search.png" width="100%" alt="DocMind 语义检索界面:相关度百分比与命中片段高亮" />
      </a>
      <h4><a href="https://github.com/Yangxbao/docmind">📚 DocMind 智档</a></h4>
      完全本地的 RAG 文档知识库(检索层):MD / PDF / 截图穿透搜索,<b>相关度百分比 + 片段高亮</b>,自动打标签。数据不出本机,零 API 花费。
      <br/>
      <img src="https://img.shields.io/badge/状态-100%25本地_·_免费-3FB950?style=flat-square" alt="状态" />
      <img src="https://img.shields.io/badge/OCR-扫描件可搜-4285F4?style=flat-square" alt="OCR" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Yangxbao/QRCode-Aggregate">
        <img src="https://raw.githubusercontent.com/Yangxbao/QRCode-Aggregate/main/screenshots/home.jpg" width="100%" alt="ScanAggregator 首页截图" />
      </a>
      <h4><a href="https://github.com/Yangxbao/QRCode-Aggregate">📱 ScanAggregator 扫码聚合</a></h4>
      安卓本地扫码工具:<b>36 个应用快捷唤起</b>、平台识别规则引擎(改 JSON 不改代码)、二维码生成,全程<b>零网络权限</b>。
      <br/>
      <img src="https://img.shields.io/badge/状态-v1.1.0_已发布-3FB950?style=flat-square" alt="状态" />
      <img src="https://img.shields.io/badge/Kotlin-无网权限-7F52FF?style=flat-square" alt="Kotlin" />
    </td>
  </tr>
</table>

</div>

### 🧰 更多项目

| 项目 | 一句话介绍 | 状态 |
|---|---|---|
| [**QuizMaster**](https://github.com/Yangxbao/QuizMaster) | 拍照 OCR 录题 + 离线刷题 Android App,题库全本地不联网 | ![v1.0.0](https://img.shields.io/badge/APK-v1.0.0_已发布-3FB950?style=flat-square) |
| [**grandma-home 奶奶的家**](https://github.com/Yangxbao/grandma-home) | 适老化 Android 桌面:大字界面 · 一键通话 · 家属 PIN 管理 | ![真机](https://img.shields.io/badge/状态-真机验收通过-3FB950?style=flat-square) |
| [**windows-file-map**](https://github.com/Yangxbao/windows-file-map) | 本机文件只读地图 + 白名单安全一键清理,纯 Python 标准库 | ![v4](https://img.shields.io/badge/版本-清理模块_v4-58A6FF?style=flat-square) |
| [**CleanSweep**](https://github.com/Yangxbao/CleanSweep) | Windows 彻底卸载助手:官方卸载 + 注册表/文件残留清理 | ![可用](https://img.shields.io/badge/状态-可用-3FB950?style=flat-square) |
| [**wecat-demo**](https://github.com/Yangxbao/wecat-demo) | HTML 小游戏合集:雷霆1942 · 大鱼吃小鱼 · 摸金突围 等 | [▶ 在线可玩](https://yangxbao.github.io/wecat-demo/) |
| [**FMSR 幻想地图模拟器**](https://github.com/Yangxbao/FMSR-FantasyMapSimulator) | Godot 4.2 重建战争模拟游戏(粉丝项目):战争 · 军队 · 外交 | ![v0.5.3](https://img.shields.io/badge/EXE-v0.5.3_可下载-3FB950?style=flat-square) |
| [**DeadManSwitch 安全签到**](https://github.com/Yangxbao/DeadManSwitch-SafetyCheckin) | 微信小程序失联签到,超时自动邮件预警(学习 Demo) | ![demo](https://img.shields.io/badge/性质-学习演示-E3B341?style=flat-square) |

<div align="center">
<img src="assets/divider.svg" width="70%" alt="" />
</div>

## 📊 GitHub 数据

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Yangxbao&show_icons=true&hide_border=true&bg_color=0D1526&title_color=58A6FF&icon_color=3FB950&text_color=C9D1D9&include_all_commits=true&count_private=true" height="165" alt="GitHub 统计" />
<img src="https://streak-stats.demolab.com?user=Yangxbao&hide_border=true&background=0D1526&border=1B2A4A&stroke=0D1526&ring=58A6FF&fire=E3B341&currStreakNum=E6EDF3&sideNums=E6EDF3&currStreakLabel=58A6FF&sideLabels=8B949E&dates=8B949E" height="165" alt="连续提交" />

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Yangxbao&layout=compact&hide_border=true&bg_color=0D1526&title_color=58A6FF&text_color=C9D1D9&langs_count=8" width="42%" alt="语言分布" />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Yangxbao/Yangxbao/output/snake-dark.svg" />
  <img src="https://raw.githubusercontent.com/Yangxbao/Yangxbao/output/snake.svg" alt="贡献贪吃蛇动画" />
</picture>

</div>

## 🗺️ 学习路线

<div align="center">

<img src="assets/roadmap.svg" width="100%" alt="学习路线:2026.09 起步(HTML 游戏上线 Pages)→ 2026.10 全栈项目密集落地(OfferDojo / docmind 等六个项目开源)→ 2026.11 走向真实场景(DevPilot 平台化、真机验收、文件地图 v4)→ 进行中:补强与打磨(Redis/MQ、DevPilot P1、算法与八股)→ 下一步:探索(向量数据库、多 Agent、实习实践)" />

</div>

当前进行中的事:**Redis / 消息队列补强** · **DevPilot P1**(异步任务队列、Git 历史分析)· **算法与八股** 为实习做准备。

<div align="center">
<img src="assets/divider.svg" width="70%" alt="" />
</div>

## 📫 联系我

<div align="center">

<img src="assets/footer.svg" width="100%" alt="感谢你的到访 · 欢迎一起做点有趣的东西" />

[![GitHub](https://img.shields.io/badge/GitHub-@Yangxbao-181717?logo=github&style=for-the-badge)](https://github.com/Yangxbao)
[![项目仓库](https://img.shields.io/badge/项目仓库-全部-3FB950?style=for-the-badge&logo=git&logoColor=white)](https://github.com/Yangxbao?tab=repositories)
[![在线小游戏](https://img.shields.io/badge/🎮_在线小游戏-wecat_demo-58A6FF?style=for-the-badge)](https://yangxbao.github.io/wecat-demo/)
[![Issues 交流](https://img.shields.io/badge/Issues-欢迎交流-7C3AED?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Yangxbao)

<!-- 📮 邮箱(取消注释并替换为你的邮箱)
<a href="mailto:your-email@example.com"><img src="https://img.shields.io/badge/Email-your--email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
-->

</div>
