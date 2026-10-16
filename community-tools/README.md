# Evidence before automation

[Русский](README.ru.md)

Four small tools help a Home Assistant community project answer four different questions: **what should a device role become, what does a measurement cover, what does the automation engine actually do, and what evidence supports a voice outcome?** Their first releases work with local files and synthetic fixtures. They do not deploy household configuration or certify physical devices.

![Four review stages and the separate physical acceptance boundary](architecture.svg)

## The four projects

- [HA Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations) produces an offline migration plan. Explicit role/hardware policies, capabilities and file fingerprints prevent a routine rename from silently assigning a lighting automation to a repurposed power outlet. A ready plan applies only to the supplied, supported configuration scope.
- [HA Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts) checks physical measurement scope, source provenance, units, sample freshness and additive rules. A strip meter cannot become an individual pump meter by renaming it. Duplicate representations of one current transformer cannot be added as separate loads.
- [HA Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests) executes a restricted synthetic scenario in the real Home Assistant automation/script engine. It checks ordered calls, forbidden calls and final synthetic states. Its first runtime is pinned to HA 2026.10.0 and Python 3.14.2–3.14.x; use a separate environment from the other tools.
- [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab) evaluates local voice evidence. It separates command correctness, API completion and audible output. All included timings are synthetic, and supplied observations are not independently verified.

The projects have their own installation guides, English/Russian documentation and English/Russian/German/Spanish CLI messages. Follow their versioned contracts rather than assuming all exit codes have the same meaning. The diagram arrows are **review handoffs**, not implemented automatic integrations. There is no central daemon or universal deploy command.

Hosted wikis: [Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations/wiki) · [Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts/wiki) · [Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests/wiki) · [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab/wiki) · [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32/wiki)

## Validation evidence — 2026-10-16 UTC

These are version-specific software checks using synthetic data, not hardware certification or a household benchmark.

- **Entity Migrations:** 37 tests plus 9 subtests passed locally, including the source-alias regressions. The [Linux run on main](https://github.com/ha-homelab/ha-entity-migrations/actions/runs/38843701264) passed 36 tests and skipped the case-insensitive-filesystem case, which was exercised locally.
- **Meter Contracts:** [75 tests passed in Linux CI](https://github.com/ha-homelab/ha-meter-contracts/actions/runs/38843671896), including provenance conflicts, source-file admission and measurement semantics.
- **Assist Scenario Lab:** [24 tests passed in Linux CI](https://github.com/ha-homelab/assist-scenario-lab/actions/runs/38843304306). These validate supplied evidence and synthetic examples; no physical voice comparison is claimed.
- **Scenario Tests:** [54 tests passed with no skips in Linux CI](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199) on CPython 3.14.8 with actual Home Assistant 2026.10.0, including seven runtime cases, one of which tests the role-transfer companion. The full suite completed in 21.42 seconds.

Linux is the tested runner environment. The [documented native macOS teardown failure](https://github.com/ha-homelab/ha-scenario-tests/blob/main/docs/validation.md) remains a limitation; an expected JSON result before a process crash is still a failed run. No Docker execution or physical device acceptance is claimed.

## A concrete migration-to-test workflow

1. In `ha-entity-migrations`, run the bundled domain-change example after installing that repository:

   ```sh
   ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
   ```

   Review the proposed `light.table` → `switch.table` and `light.turn_off` → `switch.turn_off` changes. Treat fingerprints and supported references as a scope boundary. A blocked plan needs investigation; do not replace missing capability evidence with an unconditional find-and-replace.

2. Translate the reviewed behavior into a synthetic test. [role-transfer.scenario.json](role-transfer.scenario.json) is a hand-authored companion, **not an automatic export** of the migration plan. It sends a synthetic “table off” event, expects one call to the replacement role and forbids turning off the retired hardware. It also asserts that retired hardware stays on. From this guide's directory, with the scenario runner installed in its own environment:

   ```sh
   ha-scenario validate role-transfer.scenario.json
   ha-scenario run role-transfer.scenario.json
   ```

   This companion is byte-identical to the [role-transfer fixture](https://github.com/ha-homelab/ha-scenario-tests/blob/0ea7e5a5d24dc89ebe896b1a2387396b3fce18f4/tests/fixtures/role_transfer.json) tested in the [successful Linux run](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199). Its SHA-256 is `bb8544517eeb4895b80b049cf9e242d04635e7785bd198c1d57a7cf3f5fc8ab4`. The earlier macOS teardown failure remains documented and is not counted as a passing run.

   The scenario uses the actual HA engine with in-memory actuator callbacks. A passing result proves that supplied synthetic sequence's engine behavior, not radio delivery, contact closure or power at an appliance. Its one event does not cover an entire household configuration.

3. Add relevant failure sequences before deployment: absence interrupted by sensor unavailability, a manual hold, automation reload, duplicate triggers and restored state. The runner's bundled examples cover presence, manual hold, stale input and reload reconciliation. Its real elapsed clock means a short fixture does not validate a production twenty-minute interval. HA documents that `for` waits do not survive restart/reload; choose and test explicit reconciliation or persisted deadlines where needed. [HA trigger documentation](https://www.home-assistant.io/docs/automation/trigger/)

4. Review meter evidence independently. From the meter repository:

   ```sh
   ha-meter-contracts check examples/valid-three-meters.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/kmc-shared-meter.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/duplicate-emporia.json --at 2026-01-01T12:00:05Z --json
   ```

   The valid example succeeds. The latter two intentionally exit 1: respectively an attempted outlet attribution from a whole-strip meter and duplicate representations of one source. Treat these as expected failures when scripting examples. Do not feed whole-strip watts into a protection threshold originally calibrated for a pump alone. A voltage calibration is not a current or power calibration. Missing or stale evidence stays unavailable, not zero. [HA sensor/statistics semantics](https://developers.home-assistant.io/docs/core/entity/sensor/#long-term-statistics)

5. If voice is a trigger or feedback path, evaluate evidence separately in the voice repository:

   ```sh
   assist-lab evaluate examples/synthetic-pass.json
   assist-lab evaluate examples/synthetic-incomplete.json
   ```

   The incomplete example intentionally exits 3 because an API completion is insufficient evidence of audibility. A real benchmark needs consent to record, a declared clock/method, comparable conditions, and independent observation of the action and audible response. Do not publish household recordings, transcripts or exported tokens. A server's first audio chunk is not the first sound at the listener. [HA Assist pipelines](https://developers.home-assistant.io/docs/voice/pipelines/)

6. Keep each report with the reviewed change. Apply through the site's established review/deployment procedure, then perform device-specific acceptance. Physical on/off, indicator polarity, restart behavior, source time and per-quantity calibration require real observations. These four tools neither perform nor replace that step.

## What the checks do not establish

A configured state, accepted service call, observed power draw and water flow are separate evidence. A total meter for three loads cannot identify which load drew the power. A synthetic “off” state does not prove relay contacts opened. Neither the meter tool nor a scenario test is a safety controller for water, heaters, access or other consequential loads.

These tools do not enforce one another's results. A future integration can consume their stable JSON, but must explicitly define accepted warning levels, version compatibility and what “complete evidence” means. Do not reduce `ready`, `available`, `passed` and `audible` to one interchangeable boolean.

## Roadmap: fourteen ideas, with honest readiness

The first four code deliverables below are available as initial offline tooling. All named follow-on work remains proposed; a repository name or diagram does not mean that hardware has been commissioned.

1. **Role migrations — implemented initial tool.** Extend supported reference formats only with round-trip and conflict tests; retain the explicit unsupported-input boundary.
2. **Meter contracts — implemented initial tool.** Pilot private real timestamped observations; measure current/power independently before claiming their calibration. Per-outlet attribution still requires per-outlet evidence.
3. **Automation scenario testing — implemented initial tool.** Add reviewed policies and restart/deadline cases; test production-duration timing separately when required.
4. **Voice evidence — implemented initial tool; physical benchmark pending.** Select satellites, observation method and recording consent before collecting comparable sessions. No hardware ranking yet.
5. **Air-quality coordination — pending sensor/actuator verification.** Check whether a device measures CO₂ or particles, its age/accuracy, and what ventilation or filtration can affect. Confirm outdoor conditions before a ventilation policy.
6. **Radar/presence evidence — pending hardware commissioning.** Verify the LD2450 board, power supply, enclosure, protocol and coverage. Targets are not human identities, and reception age is not measured sensor latency. CSI remains experimental.
7. **Water/pump observability — pending independent evidence.** Distinguish permission to power a pump, electrical draw, water flow and water level. An aggregate strip meter cannot supply a missing pump-only protection signal. Avoid automatic retry policies for critical commands without observed state and a site-specific review.
8. **BLE telemetry — pending compatible proxies and coverage tests.** Validate the actual sensors, temperature range, batteries and placement. ESP8266 devices are not BLE proxies; RSSI is neither identity nor an unlock credential. [ESPHome Bluetooth proxy](https://esphome.io/components/bluetooth_proxy/)
9. **Presence-based explanations and appliances — pending capability verification.** Explain which observation kept a light on; use actual washer/dryer events if supported. Do not infer an appliance cycle solely from a shared meter or invent statistical confidence from unrelated sensor flags.
10. **Z-Wave bridge — pending delivery/assembly and radio acceptance.** The [ZAC93 + ESP32 guide](https://github.com/ha-homelab/zac93-esp32) is a separate hardware track. Verify wiring, regional frequency, serial transport and Z-Wave JS inclusion against the actual board. Long Range controller support does not turn a legacy sensor into a Long Range device. [Z-Wave JS guide](https://zwave-js.github.io/zwave-js/#/getting-started/index)
11. **ESPHome plug acceptance — pending individual hardware tests.** Record button, relay, indicator and restart evidence for each revision, plus distinct voltage/current/power calibration. A successful flash is not completed acceptance. No unattended mass power cycling of connected appliances.
12. **Forecast benchmarking — pending accumulated data.** Archive issued forecasts and later actuals, retain the issue time, and score horizons without look-ahead leakage. This needs elapsed observation time, not a claim of energy savings from a synthetic example.
13. **Scoped guest controls — pending backend permission review.** Verify identity and server-side authorization. Hidden dashboard controls alone do not limit access. Do not weaken authentication to simplify a panel.
14. **Deferrable-load scheduling — pending measured constraints and capabilities.** Integrate established scheduling tools after validating meters, state feedback and forecasts. Confirm which loads can actually defer or modulate, their deadlines and manual overrides. Start with reviewed recommendations, without speculative savings or safety guarantees. [EMHASS](https://emhass.readthedocs.io/en/latest/emhass.html) · [evcc](https://docs.evcc.io/en/)

## Contributing and reproducing this guide

This overview, the synthetic scenario and diagram are original MIT-licensed material; see [LICENSE](LICENSE). Recreate the SVG with `python3 render_architecture.py`. It contains no external images, scripts, household identifiers or measured household data. Keep public fixtures synthetic and private exports outside Git. Use each repository's security and contribution guidance for changes.
