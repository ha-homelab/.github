<p align="center"><img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab：ネットワークノードを結ぶターコイズ色の家" width="144" /></p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>よく考えられた家。理解できる自動化。</strong></p>
<p align="center"><a href="https://ha-homelab.github.io/home-studio/planner/">Home Studio を試す</a> · <a href="https://github.com/ha-homelab/home-assistant">設定を見る</a> · <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.ja.md">コミュニティツール</a></p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

再利用できる Home Assistant 統合、音声クライアント、機器用ブリッジ、空間設計ツール、導入ガイドを開発しています。公開プロジェクトは、実用的なホームオートメーションに、再現可能なビルド、明確な契約仕様、文書化された復旧手順を組み合わせます。まずは一つのプロジェクトから始めてください。導入方法と対応機器は各プロジェクトで異なります。

![HA Homelab の役割マップ：機器、音声、設定、空間ツール、テスト](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.ja.svg)

このマップは関連する取り組みをまとめたものです。すべてのプロジェクトを一緒に導入することや、相互に自動連携することを意味しません。

## 新着情報 — 2026年10月

- **ブラウザーで家を描き、探索する。** [Home Studio](https://github.com/ha-homelab/home-studio) は、2D/3D プランナー、195種類のアイテム、24言語のエディター、Home Assistant に導入できるビューアーを生成するローカルコンパイラーを備えています。[Dry run モード](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) では、機器へのコマンドを遮断しながら導入済みの間取りを探索できます。
- **既存機器を再利用する選択肢。** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) は Echo Dot 2 の音声、音楽、BLE の構成を文書化し、[ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) は Z-Wave ブリッジを解説しています。下記の RF、Zigbee、Tuya プロジェクトは他の機器群を扱います。機器の準備状況はプロジェクトごとに異なり、ZAC93 の実機での稼働確認は未実施です。
- **公開設定と復旧。** [Home Assistant](https://github.com/ha-homelab/home-assistant) に再利用可能な自動化・スクリプトライブラリーと統合の契約仕様が加わりました。[k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) は導入、バックアップ、復旧ツールを公開しています。ローカルストレージを使う単一インスタンスでは、自動フェイルオーバーは実現しません。
- **自動化の前に根拠を。** 新しいセンシング、カメラ方向、アクセス用のプロジェクトに加え、エンティティ移行、計測値の出所、自動化シナリオ、音声結果を扱う四つの[コミュニティツール](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ja.md)があります。[DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) は、明示的な解錠確認を維持しつつ、状態に応じて変化する一つの操作ボタンを使うようになりました。

これは **2026年10月16日** 時点の編集スナップショットです。最新の互換性と状態は、各プロジェクトの README とリリースを参照してください。

## プロジェクトを探す

### 設定と信頼性

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — 公開設定、同梱の自動化とスクリプト、導入ガイド、統合の契約仕様。

- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — k3s 上で移設可能な Home Assistant、承認を要する更新、検証済みバックアップ、復旧ツール。

### 音声とメディア

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — EchoMuse/emOS を搭載した Echo Dot 2、Assist、音楽、ローカルのホームツール、別途登録する BLE プロキシ。記録された音声認識経路はクラウド事業者を使うため、完全なオフライン構成ではありません。

- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — Echo Dot 2 を EchoLocal に変換する手順と、ウェイクワードの学習、本番と同じ実行環境での評価ツール。

- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — Echo Show 5 Gen2 の Android 化、検証済みバックアップ、Home Assistant Companion の設定。

- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — 再利用可能な LG webOS の画面キャプチャーツールと Home Assistant 統合。

EchoLocal と EchoMuse は異なる変換方式です。機器を変更する前に、選んだプロジェクトの対応モデルと復旧要件を確認してください。

### 機器統合、ブリッジ、復旧

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — 錠の状態、操作、電池、Wi-Fi を扱う非公式 DESLOC クラウド統合。[モデルごとに互換性が異なります](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md)。

- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — ビジュアルエディター、状態に応じた操作、解錠確認を備える独立したダッシュボードカード。

- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — MQTT による RF 観測、ESPHome ネイティブ送信、Home Assistant 自動化のための ESPHome CC1101 ゲートウェイ。

- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — ネイティブな Zigbee グループ制御、短押しの切り替え、長押しの消灯を実現する Tuya ボタン用ファームウェア。[現在の実機検証の範囲](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md)を参照してください。

- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — 旧型 ESP8266 プラグの変換、再現可能な Linux 書き込み環境、Matter ブリッジのガイド。

- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — ESP32-WROOM/S3、ESPHome、Z-Wave JS を使う Zooz ZAC93 ブリッジの図解設計。

- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — 初代 SLZB-06 のバックアップ、更新、旧式 Ethernet 復旧。コアと無線のファームウェアは別々の対象です。

### 空間ツール、センシング、アクセス

- **[home-studio](https://github.com/ha-homelab/home-studio)** — 部屋を描き、家具を置き、3D で探索し、プロジェクトを書き出して Home Assistant ビューアーをローカルでコンパイル。

- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — データの鮮度と時計を明示的に確認しながら、観測を記録、ラベル付け、比較。

- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — MQTT discovery 経由の RuView 観測、ノード単位の鮮度確認、合成データのリプレイ例。

- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — 読み取り専用のカメラ方向、設定した区画、鮮度確認に基づくエリア推定。

- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — 外部ダッシュボード用の検証済み Cloudflare Access セッションと、制限付きゲートウェイ経由の短命トークン。明示的に設定した一人の Home Assistant 管理者に、完全な権限で対応付けます。

センシング例は観測内容とその限界を示します。合成リプレイやカメラの方向から、実環境での在室判定精度が確立されるわけではありません。

### テストと契約仕様

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — 機器の役割とハードウェアを区別する、オフラインの意味的移行計画。

- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — 計測範囲、出所、校正の根拠、集約に関する検査。

- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — 分離された本物の Home Assistant 自動化エンジンで実行する、範囲を限定した合成シナリオ。

- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — プロトコル完了、観測された動作、耳で聞ける応答を区別するオフライン音声証拠。

[図解したワークフローと結果](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ja.md)、または[ロシア語版](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md)を参照してください。ソフトウェアの証拠と実機受け入れ確認は別の工程です。

<details>
<summary>レビューフローと記録済みのソフトウェア検査</summary>

![四つのコミュニティツールと、別工程である実機受け入れ確認](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.ja.svg)

![四つのツールの Linux テスト件数。日付とスキップの説明付き](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.ja.svg)

図は[コミュニティガイドの2026年10月16日時点の証拠と CI 実行リンク](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ja.md#validation-evidence--2026-10-16-utc)を保持しています。矢印はレビュー上の引き継ぎです。テスト件数は範囲を限定したソフトウェア上の証拠であり、品質順位、カバレッジ率、実機ベンチマークではありません。

</details>

## 使用画面を見る

<a href="https://ha-homelab.github.io/home-studio/planner/"><img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="架空のガレージ、創作スタジオ、中庭を3D表示する Home Studio ブラウザーエディター" width="440" /></a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html"><img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="家具、カラーパレット、表面模様を配置した架空の部屋を表示する Home Studio エディター" width="440" /></a>

**Home Studio：** 架空のプランを使った実際のエディター画面です。ガレージとスタジオ、および模様付き家具のある部屋を示します。[プランナーを開く](https://ha-homelab.github.io/home-studio/planner/)か、[図解描画ガイド](https://ha-homelab.github.io/home-studio/planner/guide.html)を参照してください。画像：Home Studio contributors、MIT。[画像の出典と由来](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md)。

その他の例として、[EchoMuse の音声・音楽・BLE 構成](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md)、[ZAC93 の配線図](https://github.com/ha-homelab/zac93-esp32)、[RuView の合成リプレイデモ](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware)もご覧ください。

## 公開プロジェクトのスナップショット

![横棒グラフ：機器とブリッジ7、空間・センシング・アクセス5、音声とメディア4、テストと契約4、設定と信頼性2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.ja.svg)

**22プロジェクト + このプロフィール用リポジトリ = 23公開リポジトリ**。2026年10月16日に確認しました。各プロジェクトを一つの編集上の分類に割り当てています。件数は成熟度、利用量、性能を測るものではありません。[再現可能な元データ](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json)。実際のソフトウェア検査結果は、別の[日付付きコミュニティツールのテストグラフと CI 実行リンク](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ja.md#validation-evidence--2026-10-16-utc)を参照してください。

## この組織外の関連公開プロジェクト

別々に保守されている以下のプロジェクトが homelab を補完します。任意で利用できる構成要素であり、設定方法とサポート範囲はそれぞれ異なります。

**エネルギー — [Victron / Venus OS エコシステム](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) は Home Assistant と Venus OS を通じて空調を調整し、既定では観測のみを行います。

- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) は回路の計測値を GX 負荷として公開します。[dbus-pump](https://github.com/victron-venus/dbus-pump) は HA のタンク、ポンプ、バルブのエンティティを橋渡しします。

- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) は Vue UI と任意の Home Assistant 機器連携を備えたエネルギーダッシュボードです。

**音声とメディア — [Open OTT Play エコシステム](https://github.com/open-ott-play)を含む**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) は読み取り専用の Alexa カスタムスキルです。[Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) はローカル合成音声付きの Cast 動画を送信します。機器の改造は不要で、Home Assistant は任意です。Alexa スキルは Home Assistant を必要としません。

- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) は放送中の XMLTV 番組を検索し、既存の HLS プロキシ経由で Alexa 画面または Google Cast へ再生を送ります。

- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) はプレーヤーへのコマンド、端末からの制御、k3s への導入を提供します。EPG ゲートウェイは OttPlay に依存しません。

**再利用可能なインフラ**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) は電池、温度、植物センサー向けの ESP32 参照設定を提供します。

- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) は認証とトピック制限を備え、REST/WebSocket と MQTT を接続します。

- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) は OpenTelemetry、Prometheus、Grafana で MQTT と Mosquitto の指標を観測します。メッセージプロキシではありません。

- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) はこの組織の GitHub 設定とリポジトリを管理します。

## 取り組み方

挙動を理解可能に、変更をレビュー可能に、ビルドを再現可能にし、復旧を文書化します。明記した公開例とスクリーンショットには合成データを使用します。家庭内の認証情報、録音、機器バックアップ、非公開の運用エクスポートはこれらのリポジトリに含めません。各プロジェクトは、検証済みの内容と、まだ実機確認が必要な内容を文書化しています。

貢献は該当リポジトリのガイドに従い、脆弱性はそのセキュリティ方針に沿って報告してください。このリポジトリには[オリジナルロゴとデザインノート](https://github.com/ha-homelab/.github/blob/main/assets/README.md)もあります。

---

[Home Assistant](https://www.home-assistant.io/) を基盤とする独立した homelab です。Home Assistant プロジェクトや機器メーカーとの提携関係はありません。

