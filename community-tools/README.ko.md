# 자동화에 앞서 근거 확인

<!-- language-navigation:start -->
<p dir="ltr">
<a href="README.md" lang="en" dir="ltr">English</a> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="README.es.md" lang="es" dir="ltr">Español</a> · <a href="README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="README.he.md" lang="he" dir="rtl">עברית</a> · <a href="README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

이 문서 번역이 CLI나 음성 지원 언어를 늘리지는 않습니다. 각 프로젝트가 지원하는 언어를 확인하세요.

네 가지 작은 도구는 Home Assistant 커뮤니티 프로젝트가 서로 다른 네 질문에 답하도록 돕습니다. **기기의 역할은 어떻게 바뀌어야 하는가, 측정은 무엇을 포함하는가, 자동화 엔진은 실제로 무엇을 하는가, 음성 결과를 뒷받침하는 근거는 무엇인가?** 초기 릴리스는 로컬 파일과 합성 테스트 데이터를 사용합니다. 가정 설정을 배포하거나 실물 기기를 인증하지 않습니다.

![네 단계 검토와 별도의 실물 인수 검증 경계](architecture.ko.svg)

[그림 안내: 과정, 출력, 결과](process-and-results.ko.md) · [상태 변화도](role-transfer.ko.svg) · [테스트 근거 그래프](validation.ko.svg)

## 네 가지 프로젝트

- [HA Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations)는 오프라인 마이그레이션 계획을 만듭니다. 명시적 역할·하드웨어 정책, 기능 정보, 파일 지문은 단순 이름 변경이 조명 자동화를 다른 용도로 전환된 전원 콘센트에 조용히 배정하는 일을 방지합니다. 준비된 계획도 제공된 지원 설정 범위에만 적용됩니다.

- [HA Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts)는 물리적 측정 범위, 출처, 단위, 샘플 최신성, 합산 규칙을 검사합니다. 멀티탭 계측기의 이름을 바꿔도 개별 펌프 계측기가 되지 않습니다. 하나의 변류기를 중복 표현한 값을 별도 부하처럼 더할 수 없습니다.

- [HA Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests)는 실제 Home Assistant 자동화·스크립트 엔진에서 제한된 합성 시나리오를 실행합니다. 순서가 있는 호출, 금지된 호출, 최종 합성 상태를 검사합니다. 최초 실행 환경은 HA 2026.10.0과 Python 3.14.2–3.14.x로 고정되어 있으므로 다른 도구와 분리된 환경을 쓰세요.

- [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab)은 로컬 음성 근거를 평가합니다. 명령의 정확성, API 완료, 들을 수 있는 출력을 구분합니다. 포함된 모든 시간값은 합성 값이며 제공된 관측은 독립적으로 검증되지 않았습니다.

프로젝트마다 설치 가이드가 있으며 CLI 메시지는 영어·러시아어·독일어·스페인어를 지원합니다. 모든 종료 코드가 같은 의미라고 가정하지 말고 버전별 계약 명세를 따르세요. 그림의 화살표는 **검토 과정의 인계**이지 구현된 자동 통합이 아닙니다. 중앙 데몬이나 범용 배포 명령은 없습니다.

공개 위키: [Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations/wiki) · [Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts/wiki) · [Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests/wiki) · [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab/wiki) · [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32/wiki)

<a id="validation-evidence--2026-10-16-utc"></a>

## 검증 근거 — 2026-10-16 UTC

이는 합성 데이터를 사용하는 특정 버전의 소프트웨어 검사이며, 하드웨어 인증이나 가정 환경 벤치마크가 아닙니다.

![기록된 Linux 테스트 수와 범위 및 건너뛰기 주석](validation.ko.svg)

막대는 테스트 수를 나타내며 커버리지나 품질 순위가 아닙니다. 날짜가 명시된 원본 기록은 [validation-evidence.json](validation-evidence.json)에 있습니다.

- **Entity Migrations:** 소스 별칭 회귀 검사를 포함해 로컬에서 테스트 37개와 하위 테스트 9개가 통과했습니다. [main의 Linux 실행](https://github.com/ha-homelab/ha-entity-migrations/actions/runs/38843701264)에서는 36개가 통과했고 대소문자를 구분하지 않는 파일 시스템 사례는 건너뛰었습니다. 이 사례는 로컬에서 실행했습니다.
- **Meter Contracts:** [Linux CI에서 테스트 75개가 통과](https://github.com/ha-homelab/ha-meter-contracts/actions/runs/38843671896)했으며 출처 충돌, 소스 파일 허용, 측정 의미 검사를 포함합니다.
- **Assist Scenario Lab:** [Linux CI에서 테스트 24개가 통과](https://github.com/ha-homelab/assist-scenario-lab/actions/runs/38843304306)했습니다. 제공된 근거와 합성 예제를 검증한 것이며 실제 음성 기기 비교를 주장하지 않습니다.
- **Scenario Tests:** CPython 3.14.8과 실제 Home Assistant 2026.10.0으로 [Linux CI에서 건너뛰기 없이 테스트 54개가 통과](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199)했습니다. 실행 사례 일곱 개 중 하나가 역할 이전 보조 시나리오를 검사합니다. 전체 테스트는 21.42초에 완료되었습니다.

검증된 실행 환경은 Linux입니다. [문서화된 네이티브 macOS 종료 정리 실패](https://github.com/ha-homelab/ha-scenario-tests/blob/main/docs/validation.md)는 여전히 제한 사항입니다. 프로세스 충돌 전에 기대한 JSON 결과가 나와도 실행은 실패입니다. Docker 실행이나 실물 기기 인수 검증 완료를 주장하지 않습니다.

## 과정과 그림으로 보는 결과

![네 도구의 입력, 검사, 결과](results.ko.svg)

[그림 안내](process-and-results.ko.md)를 통해 각 출력을 해석하고 교체 기기와 이전 기기의 상태를 추적하며 소프트웨어 근거와 실물 검증을 구분하세요. 그림은 포함된 합성 예제를 요약한 것으로 원본 보고서 화면이 아닙니다.

<a id="a-concrete-migration-to-test-workflow"></a>

## 마이그레이션에서 테스트까지의 구체적인 절차

1. `ha-entity-migrations` 저장소를 설치한 뒤 포함된 도메인 변경 예제를 실행합니다.

   ```sh
   ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
   ```

   제안된 `light.table` → `switch.table` 및 `light.turn_off` → `switch.turn_off` 변경을 검토하세요. 지문과 지원 참조를 범위 경계로 취급합니다. 차단된 계획은 조사가 필요합니다. 빠진 기능 근거를 무조건적인 찾기·바꾸기로 대체하지 마세요.

2. 검토한 동작을 합성 테스트로 옮깁니다. [role-transfer.scenario.json](role-transfer.scenario.json)은 직접 작성한 보조 자료로, 마이그레이션 계획의 **자동 내보내기가 아닙니다**. 합성 “table off” 이벤트를 보내 교체 역할에 한 번의 호출을 기대하고 이전 하드웨어를 끄지 못하게 합니다. 이전 하드웨어가 계속 켜져 있는지도 확인합니다. 전용 환경에 시나리오 실행기를 설치한 후 이 가이드 디렉터리에서 실행하세요.

   ```sh
   ha-scenario validate role-transfer.scenario.json
   ha-scenario run role-transfer.scenario.json
   ```

   이 보조 자료는 [성공한 Linux 실행](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199)에서 검사한 [역할 이전 테스트 데이터](https://github.com/ha-homelab/ha-scenario-tests/blob/0ea7e5a5d24dc89ebe896b1a2387396b3fce18f4/tests/fixtures/role_transfer.json)와 바이트 단위로 동일합니다. SHA-256은 `bb8544517eeb4895b80b049cf9e242d04635e7785bd198c1d57a7cf3f5fc8ab4`입니다. 앞서 발생한 macOS 종료 정리 실패는 계속 문서에 남으며 통과 실행으로 세지 않습니다.

   시나리오는 실제 HA 엔진과 메모리 내 액추에이터 콜백을 사용합니다. 통과 결과는 제공된 합성 순서에 대한 엔진 동작을 증명할 뿐, 무선 전달, 접점 닫힘, 가전기기에 공급된 전력을 증명하지 않습니다. 이벤트 하나로 전체 가정 설정을 검증할 수 없습니다.

3. 배포 전 관련 실패 순서를 추가하세요. 센서 사용 불가로 중단된 부재 대기, 수동 유지, 자동화 다시 로드, 중복 트리거, 복원된 상태 등이 있습니다. 포함된 예제는 재실, 수동 유지, 오래된 입력, 다시 로드 시 조정을 다룹니다. 실제 경과 시간을 사용하므로 짧은 테스트 데이터로 운영 환경의 20분 구간을 검증할 수는 없습니다. HA 문서에 따르면 `for` 대기는 재시작·다시 로드 후 유지되지 않습니다. 필요에 따라 명시적인 조정이나 영속화한 마감 시각을 선택하고 테스트하세요. [HA 트리거 문서](https://www.home-assistant.io/docs/automation/trigger/)

4. 계측 근거는 독립적으로 검토합니다. 계측기 저장소에서 실행하세요.

   ```sh
   ha-meter-contracts check examples/valid-three-meters.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/kmc-shared-meter.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/duplicate-emporia.json --at 2026-01-01T12:00:05Z --json
   ```

   유효한 예제는 성공합니다. 뒤의 두 예제는 의도적으로 종료 코드 1을 반환합니다. 각각 멀티탭 전체 계측값을 개별 콘센트에 귀속하려는 시도와 한 소스의 중복 표현입니다. 예제를 스크립트화할 때는 예상된 실패로 처리하세요. 펌프 단독으로 교정한 보호 임계값에 멀티탭 전체 와트 값을 입력하지 마세요. 전압 교정은 전류나 전력 교정과 다릅니다. 없거나 오래된 근거는 0이 아니라 사용 불가로 유지합니다. [HA 센서·통계 의미](https://developers.home-assistant.io/docs/core/entity/sensor/#long-term-statistics)

5. 음성이 트리거나 피드백 경로라면 음성 저장소에서 근거를 별도로 평가합니다.

   ```sh
   assist-lab evaluate examples/synthetic-pass.json
   assist-lab evaluate examples/synthetic-incomplete.json
   ```

   불완전한 예제는 의도적으로 종료 코드 3을 반환합니다. API 완료만으로 들렸다는 근거가 충분하지 않기 때문입니다. 실제 벤치마크에는 녹음 동의, 명시한 시계·방법, 비교 가능한 조건, 동작과 들을 수 있는 응답에 대한 독립적인 관측이 필요합니다. 가정 녹음, 대화 기록, 내보낸 토큰을 공개하지 마세요. 서버의 첫 오디오 조각은 청취자가 듣는 첫 소리와 다릅니다. [HA Assist 파이프라인](https://developers.home-assistant.io/docs/voice/pipelines/)

6. 각 보고서를 검토한 변경과 함께 보관합니다. 현장에서 정한 검토·배포 절차로 적용한 뒤 기기별 인수 검증을 수행하세요. 실제 켜짐·꺼짐, 표시등 극성, 재시작 동작, 소스 시각, 측정량별 교정에는 실제 관측이 필요합니다. 네 도구는 이 단계를 수행하거나 대체하지 않습니다.

## 검사가 입증하지 않는 것

설정된 상태, 수락된 서비스 호출, 관측된 소비 전력, 물의 흐름은 서로 다른 근거입니다. 부하 세 개의 합계 계측기만으로 어느 부하가 전력을 사용했는지 알 수 없습니다. 합성 “off” 상태는 릴레이 접점이 열렸다는 증거가 아닙니다. 계측 도구나 시나리오 테스트는 물, 난방기, 출입 또는 영향이 큰 다른 부하를 위한 안전 제어기가 아닙니다.

이 도구들은 서로의 결과를 강제하지 않습니다. 향후 통합이 안정적인 JSON을 사용할 수 있지만 허용 경고 수준, 버전 호환성, “완전한 근거”의 뜻을 명시해야 합니다. `ready`, `available`, `passed`, `audible`를 하나의 대체 가능한 불리언 값으로 축약하지 마세요.

## 로드맵: 14가지 아이디어와 정확한 준비 상태

아래 첫 네 코드 결과물은 초기 오프라인 도구로 사용할 수 있습니다. 명시된 모든 후속 작업은 아직 제안 상태입니다. 저장소 이름이나 그림이 존재한다고 하드웨어 시운전이 끝난 것은 아닙니다.

1. **역할 마이그레이션 — 초기 도구 구현 완료.** 왕복 변환 및 충돌 테스트를 갖춘 경우에만 지원 참조 형식을 늘리고 미지원 입력 경계를 명확하게 유지합니다.

2. **계측 계약 — 초기 도구 구현 완료.** 시각이 기록된 비공개 실제 관측으로 시험하고 전류·전력을 독립적으로 측정한 뒤에야 교정을 주장합니다. 콘센트별 귀속에는 여전히 콘센트별 근거가 필요합니다.

3. **자동화 시나리오 테스트 — 초기 도구 구현 완료.** 검토된 정책과 재시작·마감 사례를 추가하고 필요한 경우 운영 환경과 같은 지속 시간을 별도로 테스트합니다.

4. **음성 근거 — 초기 도구 구현 완료, 실물 벤치마크 대기.** 비교 가능한 세션을 수집하기 전에 위성 기기, 관측 방법, 녹음 동의를 정합니다. 아직 하드웨어 순위는 없습니다.

5. **공기질 조정 — 센서·액추에이터 검증 대기.** 기기가 CO₂와 입자 중 무엇을 측정하는지, 사용 연수와 정확도, 환기나 여과가 무엇에 영향을 미치는지 확인합니다. 환기 정책 전 외부 조건을 확인하세요.

6. **레이더·재실 근거 — 하드웨어 시운전 대기.** LD2450 보드, 전원, 케이스, 프로토콜, 범위를 검증합니다. 감지 대상은 개인 신원이 아니며 수신 후 경과 시간은 측정된 센서 지연이 아닙니다. CSI는 실험 단계입니다.

7. **물·펌프 관측 — 독립적 근거 대기.** 펌프 전원 허용, 전력 소비, 물 흐름, 수위를 구분합니다. 멀티탭 합계 계측값은 빠진 펌프 전용 보호 신호를 대신할 수 없습니다. 관측된 상태와 현장별 검토 없이 중요한 명령을 자동 재시도하지 마세요.

8. **BLE 텔레메트리 — 호환 프록시와 범위 테스트 대기.** 실제 센서, 온도 범위, 배터리, 배치를 검증합니다. ESP8266 기기는 BLE 프록시가 아니며 RSSI는 신원도 잠금 해제 자격도 아닙니다. [ESPHome Bluetooth 프록시](https://esphome.io/components/bluetooth_proxy/)

9. **재실 기반 설명과 가전기기 — 기능 검증 대기.** 어떤 관측 때문에 조명이 켜진 상태를 유지했는지 설명하고 지원된다면 실제 세탁기·건조기 이벤트를 사용합니다. 공유 계측기만으로 가전 작동 주기를 추론하거나 무관한 센서 플래그에서 통계적 신뢰도를 만들어 내지 마세요.

10. **Z-Wave 브리지 — 배송·조립 및 무선 인수 검증 대기.** [ZAC93 + ESP32 가이드](https://github.com/ha-homelab/zac93-esp32)는 별도 하드웨어 작업입니다. 실제 보드에서 배선, 지역 주파수, 직렬 전송, Z-Wave JS 포함을 검증하세요. 컨트롤러가 Long Range를 지원해도 기존 센서가 Long Range 기기로 바뀌지는 않습니다. [Z-Wave JS 가이드](https://zwave-js.github.io/zwave-js/#/getting-started/index)

11. **ESPHome 플러그 인수 검증 — 개별 하드웨어 테스트 대기.** 각 리비전의 버튼, 릴레이, 표시등, 재시작 근거와 별도의 전압·전류·전력 교정을 기록합니다. 플래싱 성공이 인수 검증 완료는 아닙니다. 연결된 가전기기 전원을 무인으로 대량 반복 차단·복구하지 마세요.

12. **예측 벤치마크 — 데이터 축적 대기.** 발행한 예측과 후속 실측을 보관하고 발행 시각을 유지하며 미래 정보 유출 없이 예측 구간을 평가합니다. 합성 예제로 절감 효과를 주장할 일이 아니라 실제 관측 시간이 필요한 작업입니다.

13. **범위가 제한된 게스트 제어 — 백엔드 권한 검토 대기.** 신원과 서버 측 권한을 검증합니다. 대시보드 버튼을 숨기는 것만으로는 접근이 제한되지 않습니다. 패널을 단순하게 만들려고 인증을 약화하지 마세요.

14. **지연 가능한 부하 예약 — 측정된 제약과 기능 대기.** 계측기, 상태 피드백, 예측을 검증한 뒤 기존 예약 도구를 통합합니다. 실제로 지연·조절할 수 있는 부하, 마감 시각, 수동 재정의를 확인하세요. 추측성 절감이나 안전 보장 없이 검토된 권고부터 시작합니다. [EMHASS](https://emhass.readthedocs.io/en/latest/emhass.html) · [evcc](https://docs.evcc.io/en/)

## 기여와 가이드 재현

이 개요, 합성 시나리오, 그림은 독자 제작한 MIT 라이선스 자료입니다. [LICENSE](LICENSE)를 보세요. `python3 render_architecture.py`로 모든 번역 SVG를 다시 생성합니다. 외부 이미지, 스크립트, 가정 식별 정보, 실측 가정 데이터는 없습니다. [그림 안내](process-and-results.ko.md#reproduce-or-translate-the-illustrations)는 원본 기록과 재생성 검사를 설명합니다. 공개 테스트 데이터는 합성으로 유지하고 비공개 내보내기는 Git 밖에 보관하세요. 변경 시 각 저장소의 보안 및 기여 지침을 따르세요.

