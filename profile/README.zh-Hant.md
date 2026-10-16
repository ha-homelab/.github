<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab：帶有網絡節點的青綠色房屋" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>用心建置家，讓自動化清晰易懂。</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">體驗 Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">探索設定</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.zh-Hant.md">社區工具</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

我們開發可重複使用的 Home Assistant 整合、語音客戶端、設備橋接、空間工具和部署指南。這些公開專案將實用的家庭自動化與可復現建置、明確的契約和有文件記錄的復原流程相結合。從一個專案開始即可；每個專案都有自己的安裝方式和支援的硬體。

![HA Homelab 專案分工：設備、語音、設定、空間工具與測試](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.zh-Hant.svg)

圖中按相關工作分組，並不表示所有專案都已一同安裝，或能彼此自動整合。

## 最新進展 — 2026 年 10 月

- **在瀏覽器中繪製和探索房屋。** [Home Studio](https://github.com/ha-homelab/home-studio) 結合了 2D/3D 規劃器、195 種物品設計、24 種編輯器語言，以及用於生成可安裝的 Home Assistant 查看器的本地編譯器。[Dry run 模式](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) 可以在阻止設備命令的同時探索已安裝的平面圖。
- **以更多方式複用現有硬體。** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) 提供有文件說明的 Echo Dot 2 語音、音樂和 BLE 方案；[ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) 介紹 Z-Wave 橋接；下方的 RF、Zigbee 和 Tuya 專案覆蓋其他設備系列。硬體就緒程度因專案而異：ZAC93 的實機建置與驗證仍未完成。
- **公開設定與復原流程。** [Home Assistant](https://github.com/ha-homelab/home-assistant) 現在包含可重複使用的自動化與指令碼庫，以及整合契約；[k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) 提供部署、備份和復原工具。使用本地儲存的單實例並不具備自動故障轉移能力。
- **先有證據，再做自動化。** 新增的感知、房間方向和存取專案，與用於實體遷移、計量來源、自動化場景和語音結果的四個[社區工具](https://github.com/ha-homelab/.github/blob/main/community-tools/README.zh-Hant.md) 相互補充。[DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) 現採用單個自適應操作按鈕，並保留明確的解鎖確認。

這是截至 **2026 年 10 月 16 日**的編輯快照。最新兼容性與狀態請參閱各專案的 README 和發佈記錄。

## 探索專案

### 設定與可靠性

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — 公開設定、配套自動化與指令碼、部署指南和整合契約。
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — 可移植的 k3s 上 Home Assistant 部署、需經批准的更新、經過驗證的備份和復原工具。

### 語音與媒體

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 上的 EchoMuse/emOS、Assist、音樂、本地家庭工具和單獨註冊的 BLE 代理。有記錄的語音識別方案使用雲服務提供商，並非完全離線。
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — Echo Dot 2 的 EchoLocal 改裝方案，包含喚醒詞訓練和針對確切執行環境的評估工具。
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — 將 Echo Show 5 Gen2 改為 Android、經過驗證的備份和 Home Assistant Companion 設置。
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — 可重複使用的 LG webOS 螢幕捕獲工具和 Home Assistant 整合。

EchoLocal 和 EchoMuse 是不同的改裝路線。改動設備前，請閱讀所選專案的型號要求與復原要求。

### 設備整合、橋接與復原

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — 非官方 DESLOC 雲整合，提供鎖狀態、控制、電池和 Wi-Fi 資訊；[兼容性因型號而異](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md)。
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — 獨立的儀表板卡片，帶有可視化編輯器、自適應操作和解鎖確認。
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — ESPHome CC1101 閘道，支援 MQTT RF 觀測、原生 ESPHome 發送和 Home Assistant 自動化。
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — Tuya 按鈕韌體，支援原生 Zigbee 組控制、短按切換和長按關閉；請參閱[當前實物驗證限制](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md)。
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — 舊款 ESP8266 插座改裝、可復現的 Linux 刷寫工作站和 Matter 橋接指南。
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — 配有插圖的 Zooz ZAC93 橋接設計，適用於 ESP32-WROOM/S3、ESPHome 和 Z-Wave JS。
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — 初代 SLZB-06 的備份、升級和舊版以太網復原；主控韌體與無線韌體是兩個獨立目標。

### 空間工具、感知與存取

- **[home-studio](https://github.com/ha-homelab/home-studio)** — 繪製房間、佈置傢俱、以 3D 探索、匯出專案，並在本地編譯 Home Assistant 查看器。
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — 記錄、標註和比較觀測，並明確檢查資料時效與時鐘。
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — 通過 MQTT discovery 提供 RuView 觀測、逐節點時效檢查和合成回放示例。
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — 根據唯讀的攝影機方向、設定的扇區和時效檢查，估算所在區域。
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — 為外部儀表板驗證 Cloudflare Access 會話，並經受限閘道提供短期權杖。它映射到一個顯式設定、擁有完整權限的 Home Assistant 管理員。

感知示例說明觀測及其限制。合成回放和攝影機方向不能證明實際佔用檢測的準確率。

### 測試與契約

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — 離線語義遷移計畫，區分設備的角色與硬體。
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — 檢查測量範圍、來源、校準證據和聚合。
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — 在隔離的真實 Home Assistant 自動化引擎中執行有明確邊界的合成場景。
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — 離線語音證據分析，區分協議完成、觀察到的動作和可聽見的回應。

請參閱[流程與結果圖解](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.zh-Hant.md)或[俄語版本](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md)。軟體證據與實物驗收仍是兩個獨立步驟。

<details>
<summary>審查流程與已記錄的軟體檢查</summary>

![四個社區工具與獨立的實物驗收邊界](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.zh-Hant.svg)

![四個社區工具的 Linux 測試計數快照，單獨註明跳過項](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.zh-Hant.svg)

這些圖保留了[社區指南中 2026 年 10 月 16 日的證據及 CI 執行連結](https://github.com/ha-homelab/.github/blob/main/community-tools/README.zh-Hant.md#validation-evidence--2026-10-16-utc)。箭頭表示審查交接。測試計數是有範圍限制的軟體證據，並非品質排名、覆蓋率或實物設備基準測試。

</details>

## 使用效果

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Home Studio 瀏覽器編輯器，以 3D 展示虛構的車庫、創作工作室和露臺" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Home Studio 編輯器，展示帶有傢俱、配色和表面紋理的虛構房間" width="440" />
</a>

**Home Studio：** 使用虛構平面圖拍攝的真實編輯器截圖，展示車庫/工作室和帶紋理的傢俱房間。[打開規劃器](https://ha-homelab.github.io/home-studio/planner/)，或參閱[繪圖圖解指南](https://ha-homelab.github.io/home-studio/planner/guide.html)。圖片：Home Studio 貢獻者，MIT 許可。[圖片來源與溯源](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md)。

其他專案視圖請參閱 [EchoMuse 語音/音樂/BLE 架構](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md)、[ZAC93 接線圖](https://github.com/ha-homelab/zac93-esp32)和 [RuView 合成回放演示](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware)。

## 公開專案快照

![水平條形圖：設備與橋接 7；空間、感知與存取 5；語音與媒體 4；測試與契約 4；設定與可靠性 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.zh-Hant.svg)

**22 個專案 + 本簡介儲存庫 = 23 個公開儲存庫**，核查於 2026 年 10 月 16 日。每個專案只歸入一個編輯分類；計數不衡量成熟度、使用量或性能。[可復現的源資料](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json)。實際軟體檢查結果見獨立的[社區工具測試計數快照及 CI 執行連結](https://github.com/ha-homelab/.github/blob/main/community-tools/README.zh-Hant.md#validation-evidence--2026-10-16-utc)。

## 本組織之外的相關公開專案

這些獨立維護的專案可補充家庭實驗室。它們都是可選組件，各自有安裝要求和支援範圍。

**能源 — [Victron / Venus OS 生態](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) 通過 Home Assistant 和 Venus OS 協調溫控，預設僅觀測。
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) 將電路讀數呈現為 GX 負載；[dbus-pump](https://github.com/victron-venus/dbus-pump) 橋接 HA 水箱、水泵和閥門實體。
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) 提供帶 Vue 界面的能源儀表板，可選接入 Home Assistant 設備。

**語音與媒體 — 包括 [Open OTT Play 生態](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) 是唯讀的 Alexa 自定義技能；[Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) 發送帶有本地合成語音的 Cast 影片。兩者無需改裝硬體；Home Assistant 是可選項，Alexa 技能不依賴它。
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) 查找當前 XMLTV 節目，並通過現有的 HLS 代理將播放路由到 Alexa 螢幕或 Google Cast。
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) 提供播放器命令、終端控制和 k3s 部署。EPG 閘道不依賴 OttPlay。

**可重複使用基礎設施**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) 提供面向電池、溫度和植物感測器的 ESP32 參考設定。
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) 連接 REST/WebSocket 與 MQTT，並提供身份驗證和主題限制。
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) 通過 OpenTelemetry、Prometheus 和 Grafana 觀測 MQTT 與 Mosquitto 指標；它不是訊息代理。
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) 管理本組織的 GitHub 設置與儲存庫。

## 我們的工作方式

讓行為清晰易懂、變更可審查、建置可復現、復原有文件。公開示例和截圖在註明時使用合成資料；家庭憑據、錄音、設備備份與私有執行資料匯出不放入這些儲存庫。每個專案都說明已測試的內容和仍需實物驗證的部分。

請遵循相關儲存庫的指南參與貢獻，並按其安全政策報告漏洞。本儲存庫還保存我們的[原創標誌與設計說明](https://github.com/ha-homelab/.github/blob/main/assets/README.md)。

---

使用 [Home Assistant](https://www.home-assistant.io/) 建置的獨立家庭實驗室。與 Home Assistant 專案及設備製造商沒有隸屬關係。
