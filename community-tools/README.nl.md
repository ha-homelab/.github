# Eerst bewijs, dan automatisering

<!-- language-navigation:start -->
<p dir="ltr">
<a href="README.md" lang="en" dir="ltr">English</a> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="README.es.md" lang="es" dir="ltr">Español</a> · <a href="README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="README.he.md" lang="he" dir="rtl">עברית</a> · <a href="README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

<!-- community-beta-releases:start -->
<p dir="ltr">
<a href="https://github.com/ha-homelab/ha-entity-migrations/releases/tag/v0.1.1b1">Entity Migrations · 0.1.1b1</a> ·
<a href="https://github.com/ha-homelab/ha-meter-contracts/releases/tag/v0.1.1b1">Meter Contracts · 0.1.1b1</a> ·
<a href="https://github.com/ha-homelab/ha-scenario-tests/releases/tag/v0.1.1b1">Scenario Tests · 0.1.1b1</a> ·
<a href="https://github.com/ha-homelab/assist-scenario-lab/releases/tag/v0.1.1b1">Assist Scenario Lab · 0.1.1b1</a>
</p>
<!-- community-beta-releases:end -->

Deze documentatievertalingen breiden de taalondersteuning van de CLI of spraakfuncties niet uit; controleer de ondersteunde talen van elk project.

Vier kleine tools helpen een Home Assistant-communityproject vier verschillende vragen te beantwoorden: **wat moet een apparaatrol worden, wat omvat een meting, wat doet de automatiseringsengine werkelijk en welk bewijs ondersteunt een spraakresultaat?** De eerste releases werken met lokale bestanden en synthetische testgegevens. Ze implementeren geen huishoudelijke configuratie en certificeren geen fysieke apparaten.

![Vier reviewfasen en de grens met afzonderlijke fysieke acceptatie](architecture.nl.svg)

[Visuele rondleiding: proces, uitvoer en resultaten](process-and-results.nl.md) · [Diagram van toestandsveranderingen](role-transfer.nl.svg) · [Diagram met testbewijs](validation.nl.svg)

## De vier projecten

- [HA Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations) maakt een offline migratieplan. Expliciet rol-/hardwarebeleid, mogelijkheden en bestandsvingerafdrukken voorkomen dat een gewone hernoeming ongemerkt een lichtautomatisering koppelt aan een stekker die een ander doel heeft gekregen. Een gereed plan geldt alleen voor het aangeleverde, ondersteunde configuratiebereik.
- [HA Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts) controleert fysieke meetomvang, bronherkomst, eenheden, actualiteit van monsters en optelregels. Een meter van een stekkerdoos wordt geen afzonderlijke pompmeter door hem te hernoemen. Dubbele representaties van één stroomtransformator mogen niet worden opgeteld als afzonderlijke belastingen.
- [HA Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests) voert een beperkt synthetisch scenario uit in de echte Home Assistant-automatiserings- en scriptengine. Het controleert geordende aanroepen, verboden aanroepen en synthetische eindtoestanden. De huidige runtime is vastgezet op HA 2026.10.1 en Python 3.14.2–3.14.x; gebruik een omgeving apart van de andere tools.
- [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab) beoordeelt lokaal spraakbewijs. Het scheidt juistheid van commando's, API-voltooiing en hoorbare uitvoer. Alle meegeleverde tijden zijn synthetisch en aangeleverde waarnemingen worden niet onafhankelijk geverifieerd.

De projecten hebben eigen installatiehandleidingen, Engelse/Russische documentatie en CLI-meldingen in Engels, Russisch, Duits en Spaans. Volg hun versiegebonden contracten en neem niet aan dat alle exitcodes hetzelfde betekenen. De diagrammen tonen **reviewoverdrachten**, geen geïmplementeerde automatische integraties. Er is geen centrale daemon of universeel implementatiecommando.

Gehoste wiki's: [Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations/wiki) · [Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts/wiki) · [Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests/wiki) · [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab/wiki) · [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32/wiki)

<a id="validation-evidence--2026-10-16-utc"></a>

## Validatiebewijs — 2026-10-16 UTC

Dit zijn versiegebonden softwarecontroles met synthetische gegevens, geen hardwarecertificering of huishoudelijke benchmark.

![Vastgelegde Linux-testaantallen, met opmerkingen over bereik en overgeslagen tests](validation.nl.svg)

De balken tonen aantallen, geen dekking of kwaliteitsranglijst. De gedateerde brongegevens staan in [validation-evidence.json](validation-evidence.json).

- **Entity Migrations:** 37 tests plus 9 subtests slaagden lokaal, inclusief regressies voor bronaliassen. De [Linux-run op main](https://github.com/ha-homelab/ha-entity-migrations/actions/runs/38843701264) slaagde voor 36 tests en sloeg de test voor een hoofdletterongevoelig bestandssysteem over; die is lokaal uitgevoerd.
- **Meter Contracts:** [75 tests geslaagd in Linux-CI](https://github.com/ha-homelab/ha-meter-contracts/actions/runs/38843671896), inclusief herkomstconflicten, toelating van bronbestanden en meetsemantiek.
- **Assist Scenario Lab:** [24 tests geslaagd in Linux-CI](https://github.com/ha-homelab/assist-scenario-lab/actions/runs/38843304306). Deze valideren aangeleverd bewijs en synthetische voorbeelden; er wordt geen fysieke spraakvergelijking geclaimd.
- **Scenario Tests:** [54 tests geslaagd zonder overslagen in Linux-CI](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199) op CPython 3.14.8 met echte Home Assistant 2026.10.0, waaronder zeven runtimegevallen waarvan één het bijbehorende roloverdrachtscenario test. De volledige suite duurde 21.42 seconden.

Linux is de geteste runneromgeving. De [gedocumenteerde fout bij native afsluiten op macOS](https://github.com/ha-homelab/ha-scenario-tests/blob/main/docs/validation.md) blijft een beperking; een verwacht JSON-resultaat vóór een procescrash is nog steeds een mislukte run. Het verslag van 16 oktober claimt geen Docker-uitvoering of fysieke apparaatacceptatie.

Update van 19 oktober 2026: de [Linux-CI](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/39264346721) heeft ook een Docker-smoketest van de verpakte runtime doorstaan. Dit toont geen fysieke apparaatacceptatie aan.

## Proces en geïllustreerde resultaten

![Invoer, controles en resultaten van de vier tools](results.nl.svg)

Volg de [visuele rondleiding](process-and-results.nl.md) om elke uitvoer te interpreteren, de toestanden van vervangend en oud apparaat te volgen en softwarebewijs te onderscheiden van fysieke acceptatie. De illustraties vatten meegeleverde synthetische voorbeelden samen; het zijn geen screenshots van ruwe rapporten.

<a id="a-concrete-migration-to-test-workflow"></a>

## Een concreet proces van migratie tot test

1. Voer in `ha-entity-migrations` na installatie van die repository het meegeleverde voorbeeld voor domeinwijziging uit:

   ```sh
   ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
   ```

   Beoordeel de voorgestelde wijzigingen `light.table` → `switch.table` en `light.turn_off` → `switch.turn_off`. Zie vingerafdrukken en ondersteunde verwijzingen als een grens van het bereik. Een geblokkeerd plan vereist onderzoek; vervang ontbrekend bewijs van mogelijkheden niet door onvoorwaardelijk zoeken en vervangen.

2. Vertaal het beoordeelde gedrag naar een synthetische test. [role-transfer.scenario.json](role-transfer.scenario.json) is een handgeschreven begeleidend voorbeeld, **geen automatische export** van het migratieplan. Het verstuurt een synthetisch “tafel uit”-event, verwacht één aanroep naar de vervangende rol en verbiedt het uitschakelen van de oude hardware. Het controleert ook dat die hardware aan blijft. Voer vanuit de map van deze handleiding, met de scenariorunner in zijn eigen omgeving, het volgende uit:

   ```sh
   ha-scenario validate role-transfer.scenario.json
   ha-scenario run role-transfer.scenario.json
   ```

   Dit voorbeeld is bytegelijk aan de [roloverdrachtfixture](https://github.com/ha-homelab/ha-scenario-tests/blob/0ea7e5a5d24dc89ebe896b1a2387396b3fce18f4/tests/fixtures/role_transfer.json) die is getest in de [geslaagde Linux-run](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199). De SHA-256 is `bb8544517eeb4895b80b049cf9e242d04635e7785bd198c1d57a7cf3f5fc8ab4`. De eerdere fout bij afsluiten op macOS blijft gedocumenteerd en telt niet als geslaagde run.

   Het scenario gebruikt de echte HA-engine met actuatorcallbacks in het geheugen. Een geslaagd resultaat bewijst het enginegedrag voor de aangeleverde synthetische reeks, niet radio-overdracht, het sluiten van contacten of stroom bij een apparaat. Het ene event dekt geen volledige huishoudelijke configuratie.

3. Voeg vóór implementatie relevante foutreeksen toe: afwezigheid onderbroken door sensoronbeschikbaarheid, handmatig vasthouden, opnieuw laden van automatisering, dubbele triggers en herstelde toestand. De voorbeelden van de runner dekken aanwezigheid, handmatig vasthouden, verouderde invoer en reconciliatie na opnieuw laden. De klok volgt echt verstreken tijd: een korte fixture valideert geen productie-interval van twintig minuten. HA documenteert dat `for`-wachttijden niet blijven bestaan na herstart/opnieuw laden; kies en test zo nodig expliciete reconciliatie of opgeslagen deadlines. [HA-triggerdocumentatie](https://www.home-assistant.io/docs/automation/trigger/)

4. Beoordeel meetbewijs onafhankelijk. Vanuit de meterrepository:

   ```sh
   ha-meter-contracts check examples/valid-three-meters.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/kmc-shared-meter.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/duplicate-emporia.json --at 2026-01-01T12:00:05Z --json
   ```

   Het geldige voorbeeld slaagt. De laatste twee eindigen bewust met code 1: respectievelijk een poging om een meting van een hele stekkerdoos aan één aansluiting toe te wijzen en dubbele representaties van één bron. Behandel dit als verwachte fouten in voorbeeldscripts. Gebruik geen totaalvermogen van een stekkerdoos voor een beschermingsdrempel die alleen voor een pomp is gekalibreerd. Spanningskalibratie is geen stroom- of vermogenskalibratie. Ontbrekend of verouderd bewijs blijft niet beschikbaar en wordt geen nul. [HA-semantiek voor sensoren en statistieken](https://developers.home-assistant.io/docs/core/entity/sensor/#long-term-statistics)

5. Als spraak een trigger of feedbackpad is, beoordeel het bewijs apart in de spraakrepository:

   ```sh
   assist-lab evaluate examples/synthetic-pass.json
   assist-lab evaluate examples/synthetic-incomplete.json
   ```

   Het onvolledige voorbeeld eindigt bewust met code 3 omdat API-voltooiing onvoldoende bewijs voor hoorbaarheid is. Een echte benchmark vereist toestemming voor opname, een vastgelegde klok/methode, vergelijkbare omstandigheden en onafhankelijke waarneming van de actie en het hoorbare antwoord. Publiceer geen huishoudelijke opnamen, transcripties of geëxporteerde tokens. Het eerste audioblok van een server is niet het eerste geluid bij de luisteraar. [HA Assist-pipelines](https://developers.home-assistant.io/docs/voice/pipelines/)

6. Bewaar elk rapport bij de beoordeelde wijziging. Pas die toe via de bestaande review-/implementatieprocedure van de installatie en voer daarna apparaatspecifieke acceptatie uit. Fysiek aan/uit, indicatorpolariteit, herstartgedrag, brontijd en kalibratie per grootheid vereisen echte waarnemingen. Deze vier tools voeren die stap niet uit en vervangen hem niet.

## Wat de controles niet aantonen

Een ingestelde toestand, geaccepteerde serviceaanroep, waargenomen stroomverbruik en waterstroming zijn afzonderlijk bewijs. Een totaalmeter voor drie belastingen kan niet vaststellen welke het vermogen opnam. Een synthetische toestand “uit” bewijst niet dat relaiscontacten geopend zijn. Noch de metertool noch een scenariotest is een veiligheidscontroller voor water, verwarming, toegang of andere belastingen met grote gevolgen.

De tools dwingen elkaars resultaten niet af. Een toekomstige integratie kan hun stabiele JSON gebruiken, maar moet expliciet aanvaarde waarschuwingsniveaus, versiecompatibiliteit en de betekenis van “volledig bewijs” definiëren. Maak van `ready`, `available`, `passed` en `audible` niet één uitwisselbare booleaanse waarde.

## Roadmap: veertien ideeën met een eerlijke gereedheidsstatus

De eerste vier onderstaande codeproducten zijn beschikbaar als eerste offline tools. Alle genoemde vervolgstappen blijven voorstellen; een repositorynaam of diagram betekent niet dat hardware in gebruik is genomen.

1. **Rolmigraties — eerste tool geïmplementeerd.** Breid ondersteunde verwijzingsformaten alleen uit met rondreis- en conflicttests; behoud de expliciete grens voor niet-ondersteunde invoer.
2. **Metercontracten — eerste tool geïmplementeerd.** Beproef private echte waarnemingen met tijdstempels; meet stroom en vermogen onafhankelijk voordat je kalibratie claimt. Toewijzing per aansluiting vereist nog steeds bewijs per aansluiting.
3. **Automatiseringsscenariotests — eerste tool geïmplementeerd.** Voeg beoordeeld beleid en herstart-/deadlinegevallen toe; test waar nodig timing over de productieduur apart.
4. **Spraakbewijs — eerste tool geïmplementeerd; fysieke benchmark nog open.** Kies satellieten, observatiemethode en opnametoestemming vóór het verzamelen van vergelijkbare sessies. Nog geen hardwareranglijst.
5. **Luchtkwaliteitscoördinatie — verificatie van sensoren/actuatoren nog open.** Controleer of een apparaat CO₂ of deeltjes meet, de leeftijd/nauwkeurigheid en wat ventilatie of filtering kan beïnvloeden. Bevestig buitenomstandigheden voordat je ventilatiebeleid vastlegt.
6. **Radar-/aanwezigheidsbewijs — ingebruikname hardware nog open.** Verifieer LD2450-printplaat, voeding, behuizing, protocol en dekking. Doelen zijn geen menselijke identiteiten en ontvangstouderdom is geen gemeten sensorlatentie. CSI blijft experimenteel.
7. **Water-/pompobservatie — onafhankelijk bewijs nog open.** Onderscheid toestemming om een pomp te voeden, elektrisch verbruik, waterstroming en waterniveau. Een totaalmeter van een stekkerdoos kan geen ontbrekend pompspecifiek beschermingssignaal leveren. Vermijd automatisch opnieuw proberen van kritieke commando's zonder waargenomen toestand en installatiespecifieke review.
8. **BLE-telemetrie — compatibele proxy's en dekkingstests nog open.** Valideer daadwerkelijke sensoren, temperatuurbereik, batterijen en plaatsing. ESP8266-apparaten zijn geen BLE-proxy's; RSSI is geen identiteit of ontgrendelingsbewijs. [ESPHome Bluetooth-proxy](https://esphome.io/components/bluetooth_proxy/)
9. **Aanwezigheidsverklaringen en huishoudelijke apparaten — verificatie van mogelijkheden nog open.** Leg uit welke waarneming een lamp aanhield; gebruik echte wasmachine-/drogerevents indien ondersteund. Leid een apparaatcyclus niet alleen af uit een gedeelde meter en verzin geen statistische zekerheid uit ongerelateerde sensorvlaggen.
10. **Z-Wave-bridge — levering/montage en radioacceptatie nog open.** De [ZAC93 + ESP32-handleiding](https://github.com/ha-homelab/zac93-esp32) is een afzonderlijk hardwaretraject. Verifieer bedrading, regionale frequentie, serieel transport en Z-Wave JS-inclusie op de echte printplaat. Long Range-ondersteuning van een controller maakt een oudere sensor geen Long Range-apparaat. [Z-Wave JS-handleiding](https://zwave-js.github.io/zwave-js/#/getting-started/index)
11. **ESPHome-stekkeracceptatie — individuele hardwaretests nog open.** Leg per revisie bewijs vast voor knop, relais, indicator en herstart, plus afzonderlijke spannings-/stroom-/vermogenskalibratie. Geslaagd flashen is geen voltooide acceptatie. Geen onbeheerd massaal uit- en inschakelen van aangesloten apparaten.
12. **Voorspellingsbenchmark — verzamelde gegevens nog nodig.** Archiveer uitgegeven voorspellingen en latere werkelijkheid, bewaar het uitgiftetijdstip en beoordeel horizons zonder informatie uit de toekomst te lekken. Dit vereist verstreken observatietijd, geen energiebesparingsclaim op basis van een synthetisch voorbeeld.
13. **Begrensde gastbediening — review van backendmachtigingen nog open.** Verifieer identiteit en serverautorisatie. Verborgen dashboardknoppen alleen beperken toegang niet. Verzwak authenticatie niet om een paneel eenvoudiger te maken.
14. **Planning van uitstelbare belastingen — gemeten beperkingen en mogelijkheden nog nodig.** Integreer bestaande planningstools na validatie van meters, toestandsterugkoppeling en voorspellingen. Bevestig welke belastingen echt kunnen uitstellen of moduleren, hun deadlines en handmatige overrides. Begin met beoordeelde aanbevelingen, zonder speculatieve besparingen of veiligheidsgaranties. [EMHASS](https://emhass.readthedocs.io/en/latest/emhass.html) · [evcc](https://docs.evcc.io/en/)

## Bijdragen en deze handleiding reproduceren

Dit overzicht, het synthetische scenario en het diagram zijn oorspronkelijk materiaal onder de MIT-licentie; zie [LICENSE](LICENSE). Genereer alle vertaalde SVG's opnieuw met `python3 render_architecture.py`. Ze bevatten geen externe afbeeldingen, scripts, huishoudelijke identificatoren of gemeten huishoudelijke gegevens. De [visuele rondleiding](process-and-results.nl.md#reproduce-or-translate-the-illustrations) verklaart brongegevens en controles voor hergeneratie. Houd openbare fixtures synthetisch en private exports buiten Git. Gebruik de beveiligings- en bijdragerichtlijnen van elke repository voor wijzigingen.
