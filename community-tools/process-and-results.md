# Process and results: a visual walkthrough

<!-- language-navigation:start -->
<p dir="ltr">
<a href="process-and-results.md" lang="en" dir="ltr">English</a> · <a href="process-and-results.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="process-and-results.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="process-and-results.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="process-and-results.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="process-and-results.es.md" lang="es" dir="ltr">Español</a> · <a href="process-and-results.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="process-and-results.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="process-and-results.he.md" lang="he" dir="rtl">עברית</a> · <a href="process-and-results.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="process-and-results.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="process-and-results.it.md" lang="it" dir="ltr">Italiano</a> · <a href="process-and-results.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="process-and-results.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="process-and-results.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="process-and-results.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="process-and-results.pt.md" lang="pt" dir="ltr">Português</a> · <a href="process-and-results.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="process-and-results.th.md" lang="th" dir="ltr">ไทย</a> · <a href="process-and-results.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="process-and-results.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="process-and-results.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="process-and-results.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="process-and-results.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Project overview](README.md)

A useful result answers a specific question and preserves the evidence behind the answer. The four tools work independently: a reviewer chooses the relevant checks and carries their results into a change. The arrows below describe that review process, not an implemented automatic pipeline.

![Process: prepare local inputs, choose independent checks, review evidence and perform separate physical acceptance](architecture.svg)

## 1. Define the change and collect the inputs

For a device replacement, distinguish the **role** from the **physical hardware**. A lamp role may move to a different outlet while the old outlet starts powering something else. Record which references follow the role, which follow the hardware, and which should be retired. Supply the migration manifest, entity snapshot and supported source files to Entity Migrations.

For metering, supply each meter's physical scope, source identity, units and timestamp. For automation, describe a synthetic initial state, event sequence and explicit expectations. For voice, provide observations of the intent, action and audible response. The tools accept different inputs; no shared live-household export is required by this workflow.

## 2. Read the output and its limits

![Inputs, checks and illustrated outcomes for the four tools](results.svg)

These are explanatory summaries of bundled examples, **not screenshots of raw reports**:

- **Migration:** the domain-change example proposes `light.table` → `switch.table` and the corresponding service change. Review every proposed edit, its fingerprint and any blocking conflict. The plan does not apply itself.
- **Metering:** the valid three-meter example has distinct, fresh sources with values `700 W`, `0.02 kW` and `0 W`. Normalizing the second value gives `700 + 20 + 0 = 720 W`. That result is supported by three meters; a single strip meter does not provide these three per-outlet observations. Shared-scope and duplicate-source examples deliberately expose invalid assumptions.
- **Automation:** the role-transfer fixture expects one call to the replacement entity and no call to the retired hardware. Both the call list and final states matter: a matching end state alone could conceal an unintended extra command.
- **Voice:** the incomplete example lacks sufficient audible evidence. It exits with code `3`, even if an API stage has finished. This means more evidence is needed, not that the listener definitely heard silence.

Sources: [migration example](https://github.com/ha-homelab/ha-entity-migrations/tree/main/examples/domain-change), [three-meter input](https://github.com/ha-homelab/ha-meter-contracts/blob/main/examples/valid-three-meters.json), [voice input](https://github.com/ha-homelab/assist-scenario-lab/blob/main/examples/synthetic-incomplete.json). Exact installation and execution commands are in the [overview walkthrough](README.md#a-concrete-migration-to-test-workflow).

## 3. Inspect the change over time

![Logical state sequence: the replacement turns off and the retired device stays on](role-transfer.svg)

In [role-transfer.scenario.json](role-transfer.scenario.json), both synthetic switches start `on`. The `scenario_table_off` event causes `switch.turn_off` for `switch.scenario_table`. The expected result is `off` for the replacement and `on` for `switch.scenario_retired_plug`. Turning off the retired switch is explicitly forbidden.

The chart uses **logical stages**, not a measured time scale. The fixture requests a 40 ms wait before the event and 100 ms to settle. These are test inputs, not observed relay latency or a guarantee of event completion within 40 ms. The actual HA runtime test of this fixture passed in the [recorded Linux run](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199). Device callbacks still run in memory.

## 4. Understand what was tested

![Recorded Linux passed-test counts: 36, 75, 54 and 24; one filesystem case skipped](validation.svg)

The chart reads [validation-evidence.json](validation-evidence.json). Each record links to its original GitHub Actions run. It is a dated snapshot, not a live CI badge. The bar length is a count of passed tests; it is **not coverage percentage, reliability, speed or a ranking of the projects**. Suite scopes differ.

Entity Migrations has one Linux skip for case-insensitive filesystem behavior, checked locally on macOS. Scenario Tests includes seven actual-HA runtime cases in its total of 54. The documented native teardown failure on macOS remains a separate limitation; passing Linux tests do not remove it.

## 5. Decide whether to proceed

Keep the reviewed inputs, tool versions, reports and outstanding findings with the change. Resolve unsupported references, conflicting meter sources, failed assertions and missing observations before interpreting the result as sufficient for its intended use. Use each tool's documented status and exit-code contract.

Deployment and physical acceptance remain separate. Verify the actual device, radio delivery, relay behavior, connected load, source timestamp and audible output as applicable. A synthetic pass confirms the tested software behavior, not successful power delivery or a complete household configuration.

## Reproduce or translate the illustrations

Run from this directory:

```sh
python3 render_architecture.py
python3 -m unittest discover -s . -p 'test_*.py'
```

The generator produces four SVGs per language listed in the shared [language registry](../languages.json). It needs only Python's standard library, embeds no remote assets and includes an accessible title and description in every image. The same color identifies a tool across illustrations; labels also identify every series. For a new evidence snapshot, update the source records and accompanying explanations together, retaining links to the recorded runs. All illustrations are original and covered by [MIT](LICENSE).
