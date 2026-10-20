<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: een turquoise huis met verbonden netwerkknooppunten" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Een doordacht huis. Begrijpelijke automatisering.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/install.html#native-studio">Home Studio in Home Assistant installeren</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Verken de configuratie</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.nl.md">Communitytools</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

We bouwen herbruikbare Home Assistant-integraties, spraakclients, apparaatbridges,
ruimtelijke tools en implementatiehandleidingen. De openbare projecten verbinden
praktische huisautomatisering met reproduceerbare builds, expliciete contracten
en gedocumenteerd herstel. Begin met één project: elk beschrijft zijn eigen
installatieroute en ondersteunde hardware.

![Projectrollen van HA Homelab: apparaten, spraak, configuratie, ruimtelijke tools en tests](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.nl.svg)

Het overzicht groepeert verwant werk. Het betekent niet dat alle projecten samen
worden geïnstalleerd of automatisch met elkaar integreren.

## Nieuw — oktober 2026

- **Teken en publiceer je huis rechtstreeks in Home Assistant.** [Home Studio](https://ha-homelab.github.io/home-studio/install.html#native-studio) brengt de 2D/3D-editor, 206 meubel- en tuinontwerpen en 24 editortalen naar HA. Teken kamers, koppel HA-gebieden en apparaten en kies **Save draft**, gevolgd door **Publish family view**, om **3D Home** bij te werken.
  [Dry run-modus](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) kun je de geïnstalleerde plattegrond verkennen terwijl apparaatcommando's worden geblokkeerd.
  De [gids voor de eerste sessie](https://github.com/ha-homelab/home-studio/blob/main/docs/first-session.md) legt uit hoe je met voorbeelden begint, concepten herstelt en je werk behoudt wanneer 3D niet beschikbaar is.
- **Meer manieren om bestaande hardware te hergebruiken.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) voegt een
  gedocumenteerde route toe voor spraak, muziek en BLE op de Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) beschrijft een Z-Wave-bridge. De onderstaande RF-, Zigbee- en
  Tuya-projecten omvatten andere apparaatfamilies. De gereedheid verschilt per
  project: de fysieke ingebruikname van ZAC93 moet nog plaatsvinden.
- **Openbare configuratie en herstel.** [Home Assistant](https://github.com/ha-homelab/home-assistant) bevat nu herbruikbare
  automatiserings- en scriptbibliotheken en integratiecontracten;
  [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) publiceert implementatie-, back-up- en hersteltools.
  Eén instantie met lokale opslag biedt geen automatische failover.
- **Eerst bewijs, dan automatisering.** Nieuwe projecten voor sensorwaarnemingen,
  camerarichting en toegang vullen vier [communitytools](https://github.com/ha-homelab/.github/blob/main/community-tools/README.nl.md) aan voor entiteitsmigraties,
  herkomst van metingen, automatiseringsscenario's en spraakresultaten.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) gebruikt nu één adaptieve actieknop en vereist nog steeds expliciete bevestiging van ontgrendeling.

Dit is een redactionele momentopname van **19 oktober 2026**. Raadpleeg de README
en releases van elk project voor actuele compatibiliteit en status.

## Home Studio in Home Assistant installeren

Gebruik **Home Assistant 2026.10 of nieuwer** en een beheerdersaccount.
Maak eerst een back-up van HA. Als er al een gegenereerde of aangepaste **home_floorplan** is geïnstalleerd, lees dan de [migratiehandleiding](https://github.com/ha-homelab/home-studio/blob/main/docs/home-assistant-editor.md#existing-generated-homes) voordat je deze vervangt.

1. Voeg in HACS [`ha-homelab/home-studio`](https://github.com/ha-homelab/home-studio) toe als aangepaste repository in de categorie **Integration**. Installeer de nieuwste stabiele versie met **`home_floorplan.zip`**.
2. Herstart Home Assistant, open **Settings → Devices & services → Add integration** en selecteer **Home Studio**.
3. Open **Home Studio** in de zijbalk. Teken en richt een kamer in, koppel het HA-gebied en de apparaten en kies **Save draft**.
4. Kies **Publish family view** en open **3D Home**. Controleer de plattegrond en koppelingen met **Dry run** voordat je apparaatbediening inschakelt.

Een nieuwe native installatie vereist geen Python-opdrachten, YAML-invoer of API-token. De [native installatiehandleiding](https://ha-homelab.github.io/home-studio/install.html#native-studio) beschrijft de volledige installatie, handmatige ZIP-installatie en bestaande installaties.

## Verken de projecten

### Configuratie en betrouwbaarheid

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — openbare configuratie, meegeleverde automatiseringen
  en scripts, implementatiehandleidingen en integratiecontracten.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — overdraagbare Home Assistant op k3s, updates na
  goedkeuring, geverifieerde back-ups en hersteltools.

### Spraak en media

- **[asterisk-telephony](https://github.com/ha-homelab/asterisk-telephony)** — geverifieerde installer voor de Asterisk-integratie van het upstreamproject, SIP-telefoondashboards en Cisco-telefoonbediening, met een apart Assist-audiopad en gedocumenteerde acceptatieresultaten.
- **[ha-ottplay](https://github.com/ha-homelab/ha-ottplay)** — Home Assistant-entiteiten voor mediaspelers en afstandsbediening van geregistreerde spelers via een bestaande OTTPlay Control Server; de beschikbare bediening hangt van de speler af.
- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 met EchoMuse/emOS, Assist, muziek, lokale tools
  voor huisbesturing en een afzonderlijk geregistreerde BLE-proxy. Het gedocumenteerde
  spraakherkenningspad gebruikt een cloudprovider en is niet volledig offline.
  De pilot met een Russisch activeringswoord en Silero Baya verspreidt geen particuliere modelgewichten.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — de EchoLocal-ombouwroute voor Echo Dot 2, met training van
  activeringswoorden en evaluatietools voor de exacte uitvoeromgeving.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — ombouw van Echo Show 5 Gen2 naar Android, geverifieerde
  back-ups en configuratie van Home Assistant Companion.
  Een optionele ONNX-proef met één activeringszin heeft softwarecontroles; volledige akoestische acceptatie moet nog plaatsvinden.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — herbruikbare schermopnametools voor LG webOS en
  Home Assistant-integratie.

EchoLocal en EchoMuse zijn verschillende ombouwroutes. Lees de model- en
hersteleisen van het gekozen project voordat je een apparaat aanpast.

### Apparaatintegraties, bridges en herstel

- **[ha-radio-hub](https://github.com/ha-homelab/ha-radio-hub)** — huidig modulair PoE-prototype MC2-C + FH1 met drie onafhankelijke externe antennes voor Zigbee, Thread en Bluetooth, een lokale Thread Border Router, Z-Wave, 433MHz-RF en sensoren. CAD, firmware en uitrolhulpmiddelen zijn inbegrepen; fysieke validatie moet nog plaatsvinden.
- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — onofficiële DESLOC-cloudintegratie voor slotstatus, bediening,
  batterij en wifi; [de compatibiliteit verschilt per model](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — afzonderlijke dashboardkaart met visuele editor,
  adaptieve actie en ontgrendeling na bevestiging.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — ESPHome CC1101-gateway voor RF-waarnemingen via MQTT,
  native ESPHome-transmissie en Home Assistant-automatisering.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — firmware voor Tuya-knoppen met native Zigbee-
  groepsbesturing, kort indrukken om te schakelen en vasthouden om uit te schakelen;
  zie de [huidige grenzen van fysieke validatie](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — ombouw van oudere ESP8266-stekkers, een reproduceerbaar
  Linux-flashstation en handleidingen voor Matter-bridges.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — geïllustreerd ontwerp van een Zooz ZAC93-bridge voor
  ESP32-WROOM/S3, ESPHome en Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — back-up, upgrade en legacy Ethernet-herstel voor de
  oorspronkelijke SLZB-06; core- en radiofirmware zijn afzonderlijke doelen.

### Ruimte, sensorwaarnemingen en toegang

- **[home-studio](https://github.com/ha-homelab/home-studio)** — kamers rechtstreeks in Home Assistant tekenen en inrichten, bewerkbare concepten opslaan en de weergave 3D Home publiceren.
- **[ruview-home-sensing](https://github.com/ha-homelab/ruview-home-sensing)** — experimentele CSI-verzameling, ontvangerfirmware, activiteitshypothesen en hulpmiddelen voor inferentiebewijs; publiceert via ruview-home-assistant en bewijst geen detectienauwkeurigheid in de praktijk.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — registreer, label en vergelijk waarnemingen met
  expliciete actualiteits- en klokcontroles.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — RuView-waarnemingen via MQTT discovery,
  actualiteitscontrole per knooppunt en voorbeelden van synthetische replay.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — gebiedsschattingen uit alleen-lezen
  camerarichting, ingestelde sectoren en actualiteitscontroles.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — geverifieerde Cloudflare Access-sessies voor externe
  dashboards en kortlevende tokens via een beperkte gateway. Het koppelt één
  expliciet ingestelde Home Assistant-beheerder met volledige rechten.
  Optionele geauthenticeerde toegang tot albumhoezen van mediaspelers staat standaard uit.

Sensorvoorbeelden beschrijven waarnemingen en hun beperkingen. Synthetische replay
en camerarichting bewijzen geen nauwkeurigheid van aanwezigheidsdetectie in de praktijk.

### Tests en contracten

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — offline semantische migratieplannen die de rol
  van een apparaat onderscheiden van de hardware.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — controles van meetbereik, herkomst,
  kalibratiebewijs en aggregatie.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — begrensde synthetische scenario's in een
  geïsoleerde, echte Home Assistant-automatiseringsengine.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — offline spraakbewijs dat protocolvoltooiing,
  waargenomen actie en hoorbaar antwoord onderscheidt.

Volg de [geïllustreerde werkwijze en resultaten](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.nl.md). Via de taalkeuze van de handleiding zijn alle 24 talen beschikbaar.
Softwarebewijs en fysieke acceptatie blijven afzonderlijke stappen.

<details>
<summary>Reviewproces en vastgelegde softwarecontroles</summary>

![Vier communitytools en de grens met afzonderlijke fysieke acceptatie](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.nl.svg)

![Gedateerde Linux-testaantallen voor de vier tools, met afzonderlijke opmerkingen over overgeslagen tests](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.nl.svg)

Deze diagrammen behouden het [bewijs van 16 oktober 2026 en de gekoppelde CI-runs uit de communityhandleiding](https://github.com/ha-homelab/.github/blob/main/community-tools/README.nl.md#validation-evidence--2026-10-16-utc).
De pijlen zijn overdrachten tijdens review. Testaantallen zijn softwarebewijs
binnen een afgebakend bereik, geen kwaliteitsranglijst, dekkingspercentage of benchmark van fysieke apparaten.

</details>

## Bekijk het gebruik

<a href="https://ha-homelab.github.io/home-studio/install.html#native-studio">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Home Studio-browsereditor met een fictieve garage, creatieve studio en patio in 3D" width="440" />
</a>
<a href="https://ha-homelab.github.io/home-studio/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Home Studio-editor met een fictieve ingerichte kamer, kleurenpaletten en oppervlaktepatronen" width="440" />
</a>

**Home Studio:** Deze bestaande schermafbeeldingen van de afzonderlijke editor tonen fictieve plannen: een garage met studio en een ingerichte kamer met patronen. Dezelfde tekengereedschappen zijn beschikbaar binnen HA.
[Home Studio in Home Assistant installeren](https://ha-homelab.github.io/home-studio/install.html#native-studio) · [Geïllustreerde tekenhandleiding](https://ha-homelab.github.io/home-studio/planner/guide.html).
Home Studio contributors · MIT · [Afbeeldingsbronnen en herkomst](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

### Optioneel: buiten Home Assistant tekenen

De [gehoste planner](https://ha-homelab.github.io/home-studio/planner/) blijft handig tijdens het instellen of oplossen van problemen met HA. Gebruik voor offline tekenen een gedownloade lokale kopie volgens de [handleiding van de afzonderlijke editor](https://github.com/ha-homelab/home-studio/blob/main/docs/home-assistant-editor.md). Deze editor maakt geen verbinding met HA en bewaart een eigen concept in de browser. Zet een plan handmatig over met **Export JSON** en daarna **Open JSON** in Home Studio binnen HA; kies **Save draft** en **Publish family view** wanneer het klaar is.

Bekijk voor andere projectbeelden de [EchoMuse-architectuur voor spraak, muziek en BLE](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
[ZAC93-bedradingsdiagrammen](https://github.com/ha-homelab/zac93-esp32) en [RuView-demonstratie met synthetische replay](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Momentopname van openbare projecten

![Staafdiagram: apparaten en bridges 8; ruimte, sensoren en toegang 6; spraak en media 6; tests en contracten 4; configuratie en betrouwbaarheid 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.nl.svg)

**26 projecten + deze profielrepository = 27 openbare repositories**, gecontroleerd
op 19 oktober 2026. Elk project heeft één redactionele categorie; aantallen meten
geen volwassenheid, gebruik of prestaties. [Reproduceerbare brongegevens](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Bekijk voor daadwerkelijke softwarecontroleresultaten het afzonderlijke
[gedateerde testdiagram van communitytools en de gekoppelde CI-runs](https://github.com/ha-homelab/.github/blob/main/community-tools/README.nl.md#validation-evidence--2026-10-16-utc).

## Verwante openbare projecten buiten deze organisatie

Deze afzonderlijk onderhouden projecten vullen het homelab aan. Het zijn optionele
bouwstenen met hun eigen installatie- en ondersteuningsgrenzen.

**Energie — [Victron / Venus OS-ecosysteem](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) coördineert klimaatregeling via Home Assistant en Venus OS
  en observeert standaard alleen.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) maakt circuitmetingen beschikbaar als GX-belastingen;
  [dbus-pump](https://github.com/victron-venus/dbus-pump) koppelt HA-entiteiten voor tanks, pompen en kleppen.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) biedt een energiedashboard met Vue-interface en
  optionele Home Assistant-apparaten.

**Spraak en media — inclusief het [Open OTT Play-ecosysteem](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) is een alleen-lezen Alexa custom skill;
  [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) verstuurt Cast-video met lokaal gesynthetiseerde
  spraak. Ze werken zonder hardwareombouw; Home Assistant is optioneel en de Alexa-skill vereist het niet.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) vindt actuele XMLTV-programma's en stuurt weergave via
  een bestaande HLS-proxy naar Alexa-schermen of Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) biedt spelercommando's, terminalbesturing en
  k3s-implementatie. De EPG-gateway is niet afhankelijk van OttPlay.
- [Cisco Home Telephony](https://github.com/4alvit/cisco-home-telephony) — SIP-provisioning voor Cisco 7945G, Asterisk op k3s, een telefoon-CLI en optionele Home Assistant-workflows voor spraak en bediening.

**Herbruikbare infrastructuur**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) biedt ESP32-referentieconfiguraties voor
  batterij-, temperatuur- en plantensensoren.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) verbindt REST/WebSocket en MQTT met authenticatie
  en topicbeperkingen.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) observeert MQTT- en Mosquitto-metrieken via OpenTelemetry,
  Prometheus en Grafana; het is geen berichtenproxy.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) beheert de GitHub-instellingen en repositories van deze organisatie.
- [Venus OS CI Toolkit](https://github.com/victron-venus/venus-os-ci-toolkit) — gedeelde GitHub Actions-workflows en CI-hulpmiddelen voor validatie, releases en beveiligingscontroles; afnemers zetten de versie vast op een beoordeelde commit.

## Onze werkwijze

Houd gedrag begrijpelijk, wijzigingen controleerbaar, builds reproduceerbaar en
herstel gedocumenteerd. Openbare voorbeelden en screenshots gebruiken synthetische
gegevens waar dit vermeld staat. Huishoudelijke inloggegevens, opnamen,
apparaatback-ups en private operationele exports blijven buiten deze repositories.
Elk project documenteert wat getest is en wat nog fysieke verificatie vereist.

Volg voor bijdragen de handleiding van de betreffende repository; meld
kwetsbaarheden via het beveiligingsbeleid. Deze repository bevat ook ons
[oorspronkelijke logo en de ontwerpnotities](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Een onafhankelijk homelab gebouwd met [Home Assistant](https://www.home-assistant.io/).
Niet verbonden aan het Home Assistant-project of apparaatfabrikanten.
