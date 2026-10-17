<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: a turquoise house with connected network nodes" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>A thoughtful home. Understandable automation.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Try Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Explore the configuration</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.md">Community tools</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

We build reusable Home Assistant integrations, voice clients, device bridges,
spatial tools and deployment guides. The public projects connect practical home
automation with reproducible builds, explicit contracts and documented recovery.
Start with one project; each has its own installation path and supported hardware.

![Map of HA Homelab project roles: devices, voice, configuration, spatial tools and testing](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.svg)

The map groups related work. It does not imply that every project is installed
together or automatically integrates with every other project.

## What's new — October 2026

- **Draw and explore a home in the browser.** [Home Studio](https://github.com/ha-homelab/home-studio)
  combines a 2D/3D planner, 195 item designs, 24 editor languages and a local
  compiler for an installable Home Assistant viewer. Its
  [Dry run mode](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md)
  lets you explore the installed plan while blocking device commands.
  The [first-session guide](https://github.com/ha-homelab/home-studio/blob/main/docs/first-session.md)
  explains starting from examples, recovering drafts and preserving work when 3D is unavailable.
- **More ways to reuse existing hardware.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse)
  adds a documented Echo Dot 2 voice, music and BLE path;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) documents a Z-Wave bridge;
  RF, Zigbee and Tuya projects cover other device families below. Hardware
  readiness is project-specific: ZAC93 physical commissioning is still pending.
- **Public configuration and recovery.** [Home Assistant](https://github.com/ha-homelab/home-assistant)
  now includes reusable automation/script libraries and integration contracts;
  [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) publishes deployment,
  backup and recovery tools. A single instance with local storage is not automatic failover.
- **Evidence before automation.** New sensing, room-direction and access projects
  accompany four [community tools](https://github.com/ha-homelab/.github/blob/main/community-tools/README.md)
  for entity migrations, meter provenance, automation scenarios and voice outcomes.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) now uses one adaptive
  action button while retaining explicit unlock confirmation.

This is a **16 October 2026** editorial snapshot. See each project's README and
releases for current compatibility and status.

## Explore the projects

### Configuration and reliability

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — public configuration,
  bundled automations and scripts, deployment guidance and integration contracts.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — portable Home Assistant
  on k3s, approval-gated updates, verified backups and recovery tooling.

### Voice and media

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 with EchoMuse/emOS,
  Assist, music, local home tools and a separately enrolled BLE proxy.
  The recorded speech-recognition path uses a cloud provider; it is not fully offline.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — the EchoLocal conversion path
  for Echo Dot 2, with wake-word training and exact-runtime evaluation tools.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — Echo Show 5 Gen2
  conversion to Android, verified backups and Home Assistant Companion setup.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — reusable LG webOS
  screen-capture tooling and Home Assistant integration.

EchoLocal and EchoMuse are distinct conversion paths. Read the selected project's
model and recovery requirements before modifying a device.

### Device integrations, bridges and recovery

- **[ha-radio-hub](https://github.com/ha-homelab/ha-radio-hub)** — modular PoE prototype for
  Zigbee, Thread, Bluetooth, Z-Wave, 433 MHz RF and sensing, with CAD, firmware
  and deployment tooling. Physical validation is pending.
- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — unofficial DESLOC cloud integration
  for lock state, controls, battery and Wi-Fi; [model compatibility varies](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — a separate dashboard
  card with a visual editor, adaptive action and confirmed unlock controls.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — ESPHome CC1101 gateway
  for MQTT RF observations, native ESPHome transmission and Home Assistant automation.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — Tuya button
  firmware for native Zigbee group control, short-press toggle and hold-to-off;
  see its [current physical-validation limits](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — legacy ESP8266 plug
  conversion, a reproducible Linux flashing station and Matter bridge guides.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — illustrated Zooz ZAC93 bridge
  design for ESP32-WROOM/S3, ESPHome and Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — backup, upgrade and
  legacy Ethernet recovery for the original SLZB-06; core and radio firmware are separate targets.

### Spatial tools, sensing and access

- **[home-studio](https://github.com/ha-homelab/home-studio)** — draw rooms, furnish them,
  explore in 3D, export your project and compile a Home Assistant viewer locally.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — record,
  label and compare observations with explicit freshness and clock checks.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — RuView
  observations through MQTT discovery, per-node freshness and synthetic replay examples.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — area
  estimates from read-only camera direction, configured sectors and freshness checks.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — verified
  Cloudflare Access sessions for external dashboards and short-lived tokens through a restricted
  gateway. It maps one explicitly configured, full-privilege Home Assistant administrator.

Sensing examples describe observations and their limits. Synthetic replay and
camera direction do not establish real-world occupancy accuracy.

### Testing and contracts

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — offline
  semantic migration plans that distinguish a device's role from its hardware.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — checks for
  measurement scope, provenance, calibration evidence and aggregation.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — bounded synthetic
  scenarios running in an isolated, real Home Assistant automation engine.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — offline voice
  evidence that distinguishes protocol completion, observed action and audible response.

Follow the [illustrated workflow and results](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.md)
or its [Russian edition](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md).
Software evidence and physical acceptance remain separate steps.

<details>
<summary>Review workflow and recorded software checks</summary>

![Four community tools and the separate physical acceptance boundary](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.svg)

![Dated Linux test counts for the four community tools, with separate skip notes](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.svg)

These diagrams preserve the [community guide's 16 October 2026 evidence and linked CI runs](https://github.com/ha-homelab/.github/blob/main/community-tools/README.md#validation-evidence--2026-10-16-utc).
The arrows are review handoffs. Test counts are scoped software evidence, not a
quality ranking, coverage percentage or physical-device benchmark.

</details>

## See it in use

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Home Studio browser editor showing a fictional garage, creative studio and patio in 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Home Studio editor showing a fictional room with furniture, color palettes and surface patterns" width="440" />
</a>

**Home Studio:** real editor screenshots using fictional plans — a garage/studio
and a furnished room with patterns. [Open the planner](https://ha-homelab.github.io/home-studio/planner/)
or follow the [illustrated drawing guide](https://ha-homelab.github.io/home-studio/planner/guide.html).
Images: Home Studio contributors, MIT. [Image sources and provenance](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

For other project views, explore the [EchoMuse voice/music/BLE architecture](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
[ZAC93 wiring diagrams](https://github.com/ha-homelab/zac93-esp32),
and [RuView's synthetic replay demonstration](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Public project snapshot

![Horizontal bar chart: devices and bridges 8; spatial tools, sensing and access 5; voice and media 4; tests and contracts 4; configuration and reliability 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.svg)

**23 projects + this profile repository = 24 public repositories**, checked on
16 October 2026. Each project has one editorial category; counts do not measure
maturity, usage or performance. [Reproducible source data](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
For actual software-check results, see the separate
[dated community-tool test chart and linked CI runs](https://github.com/ha-homelab/.github/blob/main/community-tools/README.md#validation-evidence--2026-10-16-utc).

## Related public projects beyond this organization

These separately maintained projects complement the homelab. They are optional
building blocks, with their own setup and support boundaries.

**Energy — [Victron / Venus OS ecosystem](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) coordinates climate
  through Home Assistant and Venus OS, observing by default.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) exposes circuit readings
  as GX loads; [dbus-pump](https://github.com/victron-venus/dbus-pump) bridges HA tank, pump and valve entities.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) provides
  an energy dashboard with a Vue UI and optional Home Assistant devices.

**Voice and media — including the [Open OTT Play ecosystem](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) is a read-only
  Alexa custom skill; [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats)
  sends Cast video with locally synthesized speech. These work without hardware conversion;
  Home Assistant is optional, and the Alexa skill does not require it.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) finds current XMLTV programmes
  and routes playback through an existing HLS proxy to Alexa screens or Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) provides
  player commands, terminal control and k3s deployment. The EPG gateway does not depend on OttPlay.

**Reusable infrastructure**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) offers
  ESP32 reference configurations for battery, temperature and plant sensors.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) connects REST/WebSocket
  and MQTT with authentication and topic restrictions.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) observes MQTT
  and Mosquitto metrics through OpenTelemetry, Prometheus and Grafana; it is not a message proxy.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) manages
  this organization's GitHub settings and repositories.

## How we work

Keep behavior understandable, changes reviewable, builds reproducible and recovery
documented. Public examples and screenshots use synthetic data where stated;
household credentials, recordings, device backups and private operational exports
stay outside these repositories. Each project documents what was tested and what
still needs physical verification.

Contribute through the relevant repository's guide; report vulnerabilities through
its security policy. This repository also holds our
[original logo and design notes](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

An independent homelab built with [Home Assistant](https://www.home-assistant.io/).
Not affiliated with the Home Assistant project or device manufacturers.
