<p align="center"><img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: 연결된 네트워크 노드를 담은 청록색 집" width="144" /></p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>세심하게 설계한 집. 이해할 수 있는 자동화.</strong></p>
<p align="center"><a href="https://ha-homelab.github.io/home-studio/planner/">Home Studio 체험</a> · <a href="https://github.com/ha-homelab/home-assistant">설정 살펴보기</a> · <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.ko.md">커뮤니티 도구</a></p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

재사용 가능한 Home Assistant 통합, 음성 클라이언트, 기기 브리지, 공간 도구와 배포 가이드를 만듭니다. 공개 프로젝트는 실용적인 홈 자동화에 재현 가능한 빌드, 명시적인 계약 명세, 문서화된 복구를 결합합니다. 하나의 프로젝트부터 시작하세요. 설치 방법과 지원 하드웨어는 프로젝트마다 다릅니다.

![HA Homelab 프로젝트 역할: 기기, 음성, 설정, 공간 도구, 테스트](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.ko.svg)

이 지도는 관련 작업을 묶어 보여 줍니다. 모든 프로젝트를 함께 설치하거나 서로 자동으로 통합한다는 뜻은 아닙니다.

## 새로운 소식 — 2026년 10월

- **브라우저에서 집을 그리고 살펴보세요.** [Home Studio](https://github.com/ha-homelab/home-studio)는 2D/3D 설계 도구, 가구와 정원용 디자인 206종, 편집기 24개 언어를 제공합니다. `home_floorplan.zip`을 포함한 릴리스에는 그리기, HA 영역 연결, 초안 저장, 3D 보기 게시를 위한 [Home Assistant 내부 편집기](https://github.com/ha-homelab/home-studio/blob/main/docs/home-assistant-editor.md)도 있습니다. 별도의 브라우저 편집기와 포터블 컴파일러/설치 도구도 계속 사용할 수 있습니다. [Dry run 모드](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md)에서는 기기 명령을 차단한 채 설치된 평면도를 살펴볼 수 있습니다. [첫 사용 가이드](https://github.com/ha-homelab/home-studio/blob/main/docs/first-session.md)는 예제로 시작하는 방법, 초안 복구, 3D를 사용할 수 없을 때 작업을 보존하는 방법을 설명합니다.
- **기존 하드웨어를 재사용하는 더 많은 방법.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse)는 Echo Dot 2의 음성, 음악, BLE 경로를 문서화하고, [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32)는 Z-Wave 브리지를 설명합니다. 아래의 RF, Zigbee, Tuya 프로젝트는 다른 기기군을 다룹니다. 하드웨어 준비 상태는 프로젝트별로 다르며 ZAC93 실물 시운전은 아직 남아 있습니다.
- **공개 설정과 복구.** [Home Assistant](https://github.com/ha-homelab/home-assistant)는 재사용 가능한 자동화·스크립트 라이브러리와 통합 계약 명세를 포함합니다. [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing)은 배포, 백업, 복구 도구를 공개합니다. 로컬 저장소를 사용하는 단일 인스턴스만으로는 자동 장애 조치가 이루어지지 않습니다.
- **자동화에 앞서 근거를 확인합니다.** 새 감지, 카메라 방향, 접근 프로젝트와 함께 엔터티 마이그레이션, 계측 출처, 자동화 시나리오, 음성 결과를 다루는 네 가지 [커뮤니티 도구](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ko.md)가 있습니다. [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card)는 명시적인 잠금 해제 확인을 유지하면서 상태에 맞게 바뀌는 하나의 동작 버튼을 사용합니다.

이 내용은 **2026년 10월 19일** 기준 편집 스냅샷입니다. 현재 호환성과 상태는 각 프로젝트의 README와 릴리스를 확인하세요.

## 프로젝트 둘러보기

### 설정과 신뢰성

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — 공개 설정, 포함된 자동화와 스크립트, 배포 가이드, 통합 계약 명세.

- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — k3s에서 이전 가능한 Home Assistant, 승인 후 업데이트, 검증된 백업, 복구 도구.

### 음성과 미디어

- **[asterisk-telephony](https://github.com/ha-homelab/asterisk-telephony)** — 검증된 업스트림 Asterisk 통합 설치 도구, SIP 전화 대시보드, Cisco 전화기 제어 기능을 제공하며, 별도의 Assist 오디오 경로와 문서화된 인수 시험 결과가 있습니다.
- **[ha-ottplay](https://github.com/ha-homelab/ha-ottplay)** — 기존 OTTPlay Control Server에 등록된 플레이어를 위한 Home Assistant 미디어 플레이어 및 리모컨 엔터티입니다. 사용 가능한 제어 기능은 플레이어에 따라 다릅니다.
- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — EchoMuse/emOS 기반 Echo Dot 2, Assist, 음악, 로컬 홈 도구, 별도로 등록하는 BLE 프록시. 기록된 음성 인식 경로는 클라우드 제공자를 사용하므로 완전한 오프라인 구성이 아닙니다. 러시아어 호출어와 Silero Baya 시험 구성은 비공개 모델 가중치를 배포하지 않습니다.

- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — Echo Dot 2의 EchoLocal 변환 경로와 호출어 학습 및 정확히 일치하는 실행 환경의 평가 도구.

- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — Echo Show 5 Gen2를 Android로 변환하고 백업을 검증하며 Home Assistant Companion을 설정하는 방법. 단일 문구 ONNX 호출어의 선택적 시험 구성에는 소프트웨어 검사가 있지만, 전체 음향 경로의 인수 시험은 아직 남아 있습니다.

- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — 재사용 가능한 LG webOS 화면 캡처 도구와 Home Assistant 통합.

EchoLocal과 EchoMuse는 서로 다른 변환 경로입니다. 기기를 수정하기 전에 선택한 프로젝트의 모델 및 복구 요구 사항을 읽으세요.

### 기기 통합, 브리지, 복구

- **[ha-radio-hub](https://github.com/ha-homelab/ha-radio-hub)** — 현재 MC2-C + FH1 모듈형 PoE 시제품으로, Zigbee, Thread, Bluetooth용 독립 외부 안테나 3개, 로컬 Thread 경계 라우터, Z-Wave, 433 MHz RF 및 감지 기능을 갖춥니다. CAD, 펌웨어, 배포 도구가 제공되며 실물 검증은 아직 남아 있습니다.

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — 잠금 상태, 제어, 배터리, Wi-Fi를 위한 비공식 DESLOC 클라우드 통합. [모델별 호환성은 다릅니다](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).

- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — 시각적 편집기, 상태에 맞는 동작, 잠금 해제 확인을 제공하는 별도 대시보드 카드.

- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — MQTT RF 관측, 기본 ESPHome 송신, Home Assistant 자동화를 위한 ESPHome CC1101 게이트웨이.

- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — 기본 Zigbee 그룹 제어, 짧게 눌러 전환, 길게 눌러 끄기를 제공하는 Tuya 버튼 펌웨어. [현재 실물 검증 범위](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md)를 확인하세요.

- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — 구형 ESP8266 플러그 변환, 재현 가능한 Linux 플래싱 환경, Matter 브리지 가이드.

- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — ESP32-WROOM/S3, ESPHome, Z-Wave JS를 사용하는 Zooz ZAC93 브리지의 그림 설명 설계.

- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — 원래 SLZB-06의 백업, 업그레이드, 구형 Ethernet 복구. 코어와 무선 펌웨어는 별도 대상입니다.

### 공간 도구, 감지, 접근

- **[home-studio](https://github.com/ha-homelab/home-studio)** — 별도의 브라우저 편집기 또는 Home Assistant 내부에서 방을 그리고 가구를 배치하며, JSON을 내보내거나 HA 보기를 게시합니다.
- **[ruview-home-sensing](https://github.com/ha-homelab/ruview-home-sensing)** — 실험적인 CSI 수집, 수신기 펌웨어, 활동 가설 및 추론 근거 도구를 제공합니다. ruview-home-assistant를 통해 게시하며 실제 환경의 감지 정확도를 입증하지는 않습니다.

- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — 데이터 최신성과 시계를 명시적으로 확인하며 관측을 기록, 분류, 비교합니다.

- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — MQTT discovery를 통한 RuView 관측, 노드별 최신성 확인, 합성 재생 예제.

- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — 읽기 전용 카메라 방향, 설정된 구역, 최신성 확인에 따른 영역 추정.

- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — 외부 대시보드용 검증된 Cloudflare Access 세션과 제한된 게이트웨이를 통한 단기 토큰. 명시적으로 설정한 한 명의 Home Assistant 관리자를 모든 권한으로 연결합니다. 인증을 거쳐 미디어 플레이어 아트워크를 제공하는 선택적 기능은 기본적으로 꺼져 있습니다.

감지 예제는 관측과 그 한계를 설명합니다. 합성 재생과 카메라 방향만으로 실제 환경의 재실 감지 정확도를 입증할 수 없습니다.

### 테스트와 계약 명세

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — 기기의 역할과 하드웨어를 구분하는 오프라인 의미 기반 마이그레이션 계획.

- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — 측정 범위, 출처, 교정 근거, 집계 검사.

- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — 격리된 실제 Home Assistant 자동화 엔진에서 실행하는 범위가 제한된 합성 시나리오.

- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — 프로토콜 완료, 관측된 동작, 들을 수 있는 응답을 구분하는 오프라인 음성 근거.

[그림으로 보는 작업 흐름과 결과](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ko.md)를 따라 진행하세요. 가이드의 언어 선택기에서 24개 언어를 모두 고를 수 있습니다. 소프트웨어 근거 확인과 실물 인수 시험은 별도 단계입니다.

<details>
<summary>검토 흐름과 기록된 소프트웨어 검사</summary>

![네 가지 커뮤니티 도구와 별도의 실물 인수 검증 경계](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.ko.svg)

![네 도구의 날짜별 Linux 테스트 수와 별도 건너뛰기 설명](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.ko.svg)

이 그림은 [커뮤니티 가이드의 2026년 10월 16일 근거와 연결된 CI 실행](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ko.md#validation-evidence--2026-10-16-utc)을 보존합니다. 화살표는 검토 과정의 인계를 뜻합니다. 테스트 수는 특정 범위의 소프트웨어 근거이지 품질 순위, 커버리지 비율, 실물 기기 벤치마크가 아닙니다.

</details>

## 사용 화면 보기

<a href="https://ha-homelab.github.io/home-studio/planner/"><img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="가상 차고, 창작 스튜디오, 파티오를 3D로 보여 주는 Home Studio 브라우저 편집기" width="440" /></a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html"><img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="가구, 색상 팔레트, 표면 패턴을 배치한 가상 방을 보여 주는 Home Studio 편집기" width="440" /></a>

**Home Studio:** 가상 평면도를 사용한 실제 편집기 화면입니다. 차고와 스튜디오, 패턴이 있는 가구를 배치한 방을 보여 줍니다. [편집기를 열거나](https://ha-homelab.github.io/home-studio/planner/) [그림 설계 가이드](https://ha-homelab.github.io/home-studio/planner/guide.html)를 따라 해 보세요. 이미지: Home Studio contributors, MIT. [이미지 출처와 유래](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

다른 프로젝트는 [EchoMuse 음성·음악·BLE 구조](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md), [ZAC93 배선도](https://github.com/ha-homelab/zac93-esp32), [RuView 합성 재생 시연](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware)을 살펴보세요.

## 공개 프로젝트 스냅샷

![가로 막대그래프: 기기와 브리지 8, 공간·감지·접근 6, 음성과 미디어 6, 테스트와 계약 4, 설정과 신뢰성 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.ko.svg)

**26개 프로젝트 + 이 프로필 저장소 = 공개 저장소 27개**이며, 2026년 10월 19일 확인했습니다. 각 프로젝트를 하나의 편집 분류에만 배정합니다. 수치는 성숙도, 사용량, 성능을 측정하지 않습니다. [재현 가능한 원본 데이터](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json). 실제 소프트웨어 검사 결과는 별도의 [날짜가 명시된 커뮤니티 도구 테스트 그래프와 CI 실행 링크](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ko.md#validation-evidence--2026-10-16-utc)를 보세요.

## 이 조직 밖의 관련 공개 프로젝트

별도로 유지 관리되는 다음 프로젝트가 홈랩을 보완합니다. 선택적 구성 요소이며 각자 설정 방법과 지원 범위가 있습니다.

**에너지 — [Victron / Venus OS 생태계](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate)는 Home Assistant와 Venus OS를 통해 냉난방을 조정하며 기본값은 관측 모드입니다.

- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue)는 회로 측정값을 GX 부하로 노출합니다. [dbus-pump](https://github.com/victron-venus/dbus-pump)는 HA 탱크, 펌프, 밸브 엔터티를 연결합니다.

- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go)는 Vue UI와 선택적 Home Assistant 기기를 지원하는 에너지 대시보드를 제공합니다.

**음성과 미디어 — [Open OTT Play 생태계](https://github.com/open-ott-play) 포함**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice)는 읽기 전용 Alexa 사용자 정의 스킬입니다. [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats)는 로컬 합성 음성과 함께 Cast 동영상을 전송합니다. 하드웨어 개조가 필요 없으며 Home Assistant는 선택 사항입니다. Alexa 스킬은 Home Assistant를 요구하지 않습니다.

- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway)는 현재 XMLTV 프로그램을 찾아 기존 HLS 프록시를 통해 Alexa 화면이나 Google Cast로 재생을 보냅니다.

- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server)는 플레이어 명령, 터미널 제어, k3s 배포를 제공합니다. EPG 게이트웨이는 OttPlay에 의존하지 않습니다.
- [Cisco Home Telephony](https://github.com/4alvit/cisco-home-telephony) — Cisco 7945G SIP 프로비저닝, k3s의 Asterisk, 전화 CLI 및 선택적 Home Assistant 음성·제어 작업 흐름을 제공합니다.

**재사용 가능한 인프라**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns)는 배터리, 온도, 식물 센서용 ESP32 참조 설정을 제공합니다.

- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway)는 인증과 토픽 제한을 적용해 REST/WebSocket과 MQTT를 연결합니다.

- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry)는 OpenTelemetry, Prometheus, Grafana로 MQTT와 Mosquitto 지표를 관측합니다. 메시지 프록시가 아닙니다.

- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab)은 이 조직의 GitHub 설정과 저장소를 관리합니다.
- [Venus OS CI Toolkit](https://github.com/victron-venus/venus-os-ci-toolkit) — 검증, 릴리스, 보안 검사를 위한 공통 GitHub Actions 워크플로와 CI 도구를 제공합니다. 사용하는 프로젝트는 검토된 커밋을 고정합니다.

## 작업 방식

동작은 이해할 수 있게, 변경은 검토할 수 있게, 빌드는 재현할 수 있게 하고 복구는 문서화합니다. 명시된 공개 예제와 화면은 합성 데이터를 사용합니다. 가정의 자격 증명, 녹음, 기기 백업, 비공개 운영 내보내기는 이 저장소들에 넣지 않습니다. 각 프로젝트는 무엇을 테스트했고 어떤 실물 검증이 남았는지 문서화합니다.

기여는 해당 저장소 가이드를 따르고, 취약점은 보안 정책에 따라 신고하세요. 이 저장소에는 [독자적인 로고와 디자인 기록](https://github.com/ha-homelab/.github/blob/main/assets/README.md)도 있습니다.

---

[Home Assistant](https://www.home-assistant.io/)로 구축한 독립 홈랩입니다. Home Assistant 프로젝트나 기기 제조사와 제휴하지 않습니다.

