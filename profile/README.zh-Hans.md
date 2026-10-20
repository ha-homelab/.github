<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab：带有网络节点的青绿色房屋" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>用心构建家，让自动化清晰易懂。</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">体验 Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">探索配置</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.zh-Hans.md">社区工具</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

我们开发可复用的 Home Assistant 集成、语音客户端、设备桥接、空间工具和部署指南。这些公开项目将实用的家庭自动化与可复现构建、明确的契约和有文档记录的恢复流程相结合。从一个项目开始即可；每个项目都有自己的安装方式和支持的硬件。

![HA Homelab 项目分工：设备、语音、配置、空间工具与测试](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.zh-Hans.svg)

图中按相关工作分组，并不表示所有项目都已一同安装，或能彼此自动集成。

## 最新进展 — 2026 年 10 月

- **在浏览器中绘制和探索房屋。** [Home Studio](https://github.com/ha-homelab/home-studio) 结合了 2D/3D 规划器、206 种家具和园艺物品设计，以及 24 种编辑器语言。包含 `home_floorplan.zip` 的版本还提供 [Home Assistant 内置编辑器](https://github.com/ha-homelab/home-studio/blob/main/docs/home-assistant-editor.md)，用于绘图、关联 HA 区域、保存草稿和发布 3D 视图。独立浏览器编辑器及便携式编译器和安装工具仍然可用。[Dry run 模式](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) 可以在阻止设备命令的同时探索已安装的平面图。
  [首次使用指南](https://github.com/ha-homelab/home-studio/blob/main/docs/first-session.md)介绍如何从示例开始、恢复草稿，以及在 3D 不可用时保存工作。
- **以更多方式复用现有硬件。** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) 提供有文档说明的 Echo Dot 2 语音、音乐和 BLE 方案；[ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) 介绍 Z-Wave 桥接；下方的 RF、Zigbee 和 Tuya 项目覆盖其他设备系列。硬件就绪程度因项目而异：ZAC93 的实物调试仍未完成。
- **公开配置与恢复流程。** [Home Assistant](https://github.com/ha-homelab/home-assistant) 现在包含可复用的自动化与脚本库，以及集成契约；[k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) 提供部署、备份和恢复工具。使用本地存储的单实例并不具备自动故障转移能力。
- **先有证据，再做自动化。** 新增的感知、房间方向和访问项目，与用于实体迁移、计量来源、自动化场景和语音结果的四个[社区工具](https://github.com/ha-homelab/.github/blob/main/community-tools/README.zh-Hans.md) 相互补充。[DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) 现采用单个自适应操作按钮，并保留明确的解锁确认。

这是截至 **2026 年 10 月 19 日**的编辑快照。最新兼容性与状态请参阅各项目的 README 和发布记录。

## 探索项目

### 配置与可靠性

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — 公开配置、配套自动化与脚本、部署指南和集成契约。
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — 可移植的 k3s 上 Home Assistant 部署、需经批准的更新、经过验证的备份和恢复工具。

### 语音与媒体

- **[asterisk-telephony](https://github.com/ha-homelab/asterisk-telephony)** — 经过校验的上游 Asterisk 集成安装工具、SIP 电话仪表盘和 Cisco 话机控制，配有独立的 Assist 音频路径及记录在案的验收结果。
- **[ha-ottplay](https://github.com/ha-homelab/ha-ottplay)** — 通过现有 OTTPlay Control Server 为已注册播放器提供 Home Assistant 媒体播放器和遥控器实体；可用控制取决于播放器。
- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 上的 EchoMuse/emOS、Assist、音乐、本地家庭工具和单独注册的 BLE 代理。有记录的语音识别方案使用云服务提供商，并非完全离线。
  俄语唤醒词与 Silero Baya 试点不分发私有模型权重。
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — Echo Dot 2 的 EchoLocal 改装方案，包含唤醒词训练和针对确切运行环境的评估工具。
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — 将 Echo Show 5 Gen2 改为 Android、经过验证的备份和 Home Assistant Companion 设置。
  可选的单短语 ONNX 唤醒词试验已进行软件检查；端到端声学验收仍待完成。
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — 可复用的 LG webOS 屏幕捕获工具和 Home Assistant 集成。

EchoLocal 和 EchoMuse 是不同的改装路线。改动设备前，请阅读所选项目的型号要求与恢复要求。

### 设备集成、桥接与恢复

- **[ha-radio-hub](https://github.com/ha-homelab/ha-radio-hub)** — 当前的 MC2-C + FH1 模块化 PoE 原型，具有 Zigbee、Thread 和 Bluetooth 三条独立外置天线路径、本地 Thread 边界路由器、Z-Wave、433 MHz 射频和传感功能。提供 CAD 设计、固件和部署工具；实物验证尚待完成。
- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — 非官方 DESLOC 云集成，提供锁状态、控制、电池和 Wi-Fi 信息；[兼容性因型号而异](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md)。
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — 独立的仪表盘卡片，带有可视化编辑器、自适应操作和解锁确认。
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — ESPHome CC1101 网关，支持 MQTT RF 观测、原生 ESPHome 发送和 Home Assistant 自动化。
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — Tuya 按钮固件，支持原生 Zigbee 组控制、短按切换和长按关闭；请参阅[当前实物验证限制](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md)。
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — 旧款 ESP8266 插座改装、可复现的 Linux 刷写工作站和 Matter 桥接指南。
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — 配有插图的 Zooz ZAC93 桥接设计，适用于 ESP32-WROOM/S3、ESPHome 和 Z-Wave JS。
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — 初代 SLZB-06 的备份、升级和旧版以太网恢复；主控固件与无线固件是两个独立目标。

### 空间工具、感知与访问

- **[home-studio](https://github.com/ha-homelab/home-studio)** — 在独立浏览器编辑器或 Home Assistant 内绘制房间和布置家具；导出 JSON 或发布 HA 视图。
- **[ruview-home-sensing](https://github.com/ha-homelab/ruview-home-sensing)** — 实验性 CSI 采集、接收器固件、活动假设和推断证据工具；通过 ruview-home-assistant 发布数据，尚不能证明实际环境中的检测准确率。
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — 记录、标注和比较观测，并明确检查数据时效与时钟。
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — 通过 MQTT discovery 提供 RuView 观测、逐节点时效检查和合成回放示例。
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — 根据只读的摄像机方向、配置的扇区和时效检查，估算所在区域。
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — 为外部仪表盘验证 Cloudflare Access 会话，并经受限网关提供短期令牌。它映射到一个显式配置、拥有完整权限的 Home Assistant 管理员。
  可选的媒体播放器封面访问需要身份验证，且默认关闭。

感知示例说明观测及其限制。合成回放和摄像机方向不能证明实际占用检测的准确率。

### 测试与契约

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — 离线语义迁移计划，区分设备的角色与硬件。
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — 检查测量范围、来源、校准证据和聚合。
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — 在隔离的真实 Home Assistant 自动化引擎中运行有明确边界的合成场景。
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — 离线语音证据分析，区分协议完成、观察到的动作和可听见的响应。

请参阅[流程与结果图解](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.zh-Hans.md)。指南的语言切换器提供全部 24 种语言。软件证据与实物验收仍是两个独立步骤。

<details>
<summary>审查流程与已记录的软件检查</summary>

![四个社区工具与独立的实物验收边界](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.zh-Hans.svg)

![四个社区工具的 Linux 测试计数快照，单独注明跳过项](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.zh-Hans.svg)

这些图保留了[社区指南中 2026 年 10 月 16 日的证据及 CI 运行链接](https://github.com/ha-homelab/.github/blob/main/community-tools/README.zh-Hans.md#validation-evidence--2026-10-16-utc)。箭头表示审查交接。测试计数是有范围限制的软件证据，并非质量排名、覆盖率或实物设备基准测试。

</details>

## 使用效果

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Home Studio 浏览器编辑器，以 3D 展示虚构的车库、创作工作室和露台" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Home Studio 编辑器，展示带有家具、配色和表面纹理的虚构房间" width="440" />
</a>

**Home Studio：** 使用虚构平面图拍摄的真实编辑器截图，展示车库/工作室和带纹理的家具房间。[打开规划器](https://ha-homelab.github.io/home-studio/planner/)，或参阅[绘图图解指南](https://ha-homelab.github.io/home-studio/planner/guide.html)。图片：Home Studio 贡献者，MIT 许可。[图片来源与溯源](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md)。

其他项目视图请参阅 [EchoMuse 语音/音乐/BLE 架构](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md)、[ZAC93 接线图](https://github.com/ha-homelab/zac93-esp32)和 [RuView 合成回放演示](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware)。

## 公开项目快照

![水平条形图：设备与桥接 8；空间、感知与访问 6；语音与媒体 6；测试与契约 4；配置与可靠性 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.zh-Hans.svg)

**26 个项目 + 本简介仓库 = 27 个公开仓库**，核查于 2026 年 10 月 19 日。每个项目只归入一个编辑分类；计数不衡量成熟度、使用量或性能。[可复现的源数据](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json)。实际软件检查结果见独立的[社区工具测试计数快照及 CI 运行链接](https://github.com/ha-homelab/.github/blob/main/community-tools/README.zh-Hans.md#validation-evidence--2026-10-16-utc)。

## 本组织之外的相关公开项目

这些独立维护的项目可补充家庭实验室。它们都是可选组件，各自有安装要求和支持范围。

**能源 — [Victron / Venus OS 生态](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) 通过 Home Assistant 和 Venus OS 协调温控，默认只观测。
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) 将电路读数呈现为 GX 负载；[dbus-pump](https://github.com/victron-venus/dbus-pump) 桥接 HA 水箱、水泵和阀门实体。
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) 提供带 Vue 界面的能源仪表盘，可选接入 Home Assistant 设备。

**语音与媒体 — 包括 [Open OTT Play 生态](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) 是只读的 Alexa 自定义技能；[Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) 发送带有本地合成语音的 Cast 视频。两者无需改装硬件；Home Assistant 是可选项，Alexa 技能不依赖它。
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) 查找当前 XMLTV 节目，并通过现有的 HLS 代理将播放路由到 Alexa 屏幕或 Google Cast。
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) 提供播放器命令、终端控制和 k3s 部署。EPG 网关不依赖 OttPlay。
- [Cisco Home Telephony](https://github.com/4alvit/cisco-home-telephony) — Cisco 7945G SIP 配置、k3s 上的 Asterisk、电话命令行工具及可选的 Home Assistant 语音和控制流程。

**可复用基础设施**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) 提供面向电池、温度和植物传感器的 ESP32 参考配置。
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) 连接 REST/WebSocket 与 MQTT，并提供身份验证和主题限制。
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) 通过 OpenTelemetry、Prometheus 和 Grafana 观测 MQTT 与 Mosquitto 指标；它不是消息代理。
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) 管理本组织的 GitHub 设置与仓库。
- [Venus OS CI Toolkit](https://github.com/victron-venus/venus-os-ci-toolkit) — 用于验证、发布和安全检查的共享 GitHub Actions 工作流与 CI 工具；使用方固定经过审查的提交。

## 我们的工作方式

让行为清晰易懂、变更可审查、构建可复现、恢复有文档。公开示例和截图在注明时使用合成数据；家庭凭据、录音、设备备份与私有运行数据导出不放入这些仓库。每个项目都说明已测试的内容和仍需实物验证的部分。

请遵循相关仓库的指南参与贡献，并按其安全政策报告漏洞。本仓库还保存我们的[原创标志与设计说明](https://github.com/ha-homelab/.github/blob/main/assets/README.md)。

---

使用 [Home Assistant](https://www.home-assistant.io/) 构建的独立家庭实验室。与 Home Assistant 项目及设备制造商没有隶属关系。
