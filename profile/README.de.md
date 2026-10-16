<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: ein türkisfarbenes Haus mit verbundenen Netzwerkknoten" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Ein durchdachtes Zuhause. Verständliche Automation.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Home Studio ausprobieren</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Konfiguration erkunden</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.de.md">Community-Werkzeuge</a>
</p>
<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Wir entwickeln wiederverwendbare Home-Assistant-Integrationen, Sprachclients,
Geräte-Bridges, Raumplanungswerkzeuge und Anleitungen für den Betrieb. Die
öffentlichen Projekte verbinden praktische Hausautomation mit reproduzierbaren
Builds, klaren Schnittstellenverträgen und dokumentierter Wiederherstellung.
Beginne mit einem Projekt: Jedes beschreibt seinen Installationsweg und die unterstützte Hardware.

![Projektrollen bei HA Homelab: Geräte, Sprache, Konfiguration, Raumplanung und Tests](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.de.svg)

Die Übersicht gruppiert verwandte Arbeiten. Sie bedeutet nicht, dass alle Projekte
gemeinsam installiert werden oder sich automatisch miteinander integrieren.

## Neuigkeiten — Oktober 2026

- **Ein Zuhause im Browser zeichnen und erkunden.** [Home Studio](https://github.com/ha-homelab/home-studio)
  verbindet einen 2D/3D-Planer, 195 Objektdesigns, 24 Editor-Sprachen und einen lokalen
  Compiler für einen installierbaren Home-Assistant-Viewer. Der
  [Dry-run-Modus](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md)
  lässt dich den installierten Plan erkunden und blockiert dabei Gerätebefehle.
- **Weitere Möglichkeiten, vorhandene Hardware weiterzuverwenden.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse)
  ergänzt einen dokumentierten Weg für Sprache, Musik und BLE auf dem Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) beschreibt eine Z-Wave-Bridge.
  Die unten aufgeführten RF-, Zigbee- und Tuya-Projekte decken weitere Gerätefamilien
  ab. Der Hardwarestand unterscheidet sich je nach Projekt: Die physische
  Inbetriebnahme des ZAC93 steht noch aus.
- **Öffentliche Konfiguration und Wiederherstellung.** [Home Assistant](https://github.com/ha-homelab/home-assistant)
  enthält jetzt wiederverwendbare Automations- und Skriptbibliotheken sowie
  Integrationsverträge; [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing)
  veröffentlicht Werkzeuge für Bereitstellung, Sicherung und Wiederherstellung.
  Eine einzelne Instanz mit lokalem Speicher bietet kein automatisches Failover.
- **Erst Nachweise, dann Automation.** Neue Projekte für Sensorbeobachtungen,
  Kamerarichtung und Zugriff ergänzen vier [Community-Werkzeuge](https://github.com/ha-homelab/.github/blob/main/community-tools/README.de.md)
  für Entitätsmigrationen, Messwertherkunft, Automationsszenarien und Sprachergebnisse.
  Die [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) verwendet jetzt
  eine adaptive Aktionstaste und verlangt weiterhin eine ausdrückliche Entriegelungsbestätigung.

Dies ist ein redaktioneller Stand vom **16. Oktober 2026**. Aktuelle Angaben zu
Kompatibilität und Status findest du im README und in den Releases des jeweiligen Projekts.

## Projekte erkunden

### Konfiguration und Zuverlässigkeit

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — öffentliche Konfiguration,
  mitgelieferte Automationen und Skripte, Betriebsanleitungen und Integrationsverträge.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — portables Home Assistant
  auf k3s, Updates nach ausdrücklicher Freigabe, verifizierte Sicherungen und Wiederherstellungswerkzeuge.

### Sprache und Medien

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 mit EchoMuse/emOS,
  Assist, Musik, lokalen Werkzeugen zur Haussteuerung und einem separat eingebundenen BLE-Proxy.
  Der dokumentierte Spracherkennungsweg nutzt einen Cloudanbieter und ist nicht vollständig offline.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — Umbau des Echo Dot 2 mit
  EchoLocal, einschließlich Aktivierungswort-Training und Auswertung in der tatsächlichen Laufzeitumgebung.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — Umbau des Echo Show 5 Gen2
  auf Android, verifizierte Sicherungen und Einrichtung von Home Assistant Companion.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — wiederverwendbare
  Werkzeuge zur Bildschirmaufnahme auf LG webOS und Home-Assistant-Integration.

EchoLocal und EchoMuse sind unterschiedliche Umbauwege. Lies vor einem Eingriff
in das Gerät die Modell- und Wiederherstellungsanforderungen des ausgewählten Projekts.

### Geräteintegrationen, Bridges und Wiederherstellung

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — inoffizielle DESLOC-Cloudintegration
  für Schlosszustand, Steuerung, Batterie und WLAN; die [Kompatibilität hängt vom Modell ab](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — separate Dashboard-Karte
  mit visuellem Editor, adaptiver Aktion und Entriegelung nach Bestätigung.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — ESPHome-CC1101-Gateway
  für RF-Beobachtungen über MQTT, natives Senden über ESPHome und Home-Assistant-Automation.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — Firmware
  für Tuya-Tasten mit nativer Zigbee-Gruppensteuerung: kurz drücken zum Umschalten,
  gedrückt halten zum Ausschalten; beachte die [aktuellen Grenzen der Hardwareprüfung](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — Umbau älterer
  ESP8266-Steckdosen, reproduzierbare Linux-Flashstation und Anleitungen zur Matter-Bridge.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — illustrierter Entwurf einer
  Zooz-ZAC93-Bridge für ESP32-WROOM/S3, ESPHome und Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — Sicherung, Upgrade
  und ältere Ethernet-Wiederherstellungsverfahren für den ursprünglichen SLZB-06;
  Core- und Funkfirmware sind getrennte Ziele.

### Raumplanung, Sensorbeobachtungen und Zugriff

- **[home-studio](https://github.com/ha-homelab/home-studio)** — Räume zeichnen, einrichten,
  in 3D erkunden, das Projekt exportieren und lokal einen Home-Assistant-Viewer erzeugen.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — Beobachtungen
  aufzeichnen, annotieren und vergleichen, mit ausdrücklichen Aktualitäts- und Zeitprüfungen.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — RuView-
  Beobachtungen über MQTT Discovery, Aktualitätsprüfung je Knoten und synthetische Wiedergabebeispiele.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** —
  Bereichsschätzungen aus ausschließlich gelesener Kamerarichtung, konfigurierten Sektoren und Aktualitätsprüfungen.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — verifizierte
  Cloudflare-Access-Sitzungen für externe Dashboards und kurzlebige Tokens über ein
  eingeschränktes Gateway. Es ordnet genau einen ausdrücklich konfigurierten
  Home-Assistant-Administrator mit vollen Rechten zu.

Sensorbeispiele beschreiben Beobachtungen und deren Grenzen. Synthetische Wiedergaben
und Kamerarichtung belegen keine Genauigkeit der Anwesenheitserkennung im realen Einsatz.

### Tests und Verträge

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — semantische
  Offline-Migrationspläne, die die Rolle eines Geräts von seiner Hardware unterscheiden.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — Prüfungen von
  Messumfang, Herkunft, Kalibrierungsnachweisen und Aggregation.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — begrenzte synthetische
  Szenarien in einer isolierten, echten Home-Assistant-Automationsengine.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — Offline-
  Sprachnachweise, die Protokollabschluss, beobachtete Aktion und hörbare Antwort unterscheiden.

Sieh dir den [illustrierten Ablauf und die Ergebnisse](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.de.md)
oder die [russische Fassung](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md) an.
Softwarenachweise und physische Abnahme bleiben getrennte Schritte.

<details>
<summary>Review-Ablauf und dokumentierte Softwareprüfungen</summary>

![Vier Community-Werkzeuge und die Grenze zur separaten physischen Abnahme](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.de.svg)

![Datierte Linux-Testanzahlen der vier Community-Werkzeuge mit gesonderten Hinweisen zu übersprungenen Tests](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.de.svg)

Diese Diagramme geben die [Nachweise vom 16. Oktober 2026 mit verlinkten CI-Läufen aus dem Community-Leitfaden](https://github.com/ha-homelab/.github/blob/main/community-tools/README.de.md#prüfnachweise--2026-10-16-utc) wieder.
Die Pfeile zeigen Übergaben im Review. Testanzahlen sind Softwarenachweise mit
begrenztem Geltungsbereich, keine Qualitätsrangliste, kein Abdeckungsprozentsatz
und kein Benchmark physischer Geräte.

</details>

## Einblicke in die Nutzung

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Home-Studio-Browsereditor mit einer fiktiven Garage, einem Kreativstudio und einer Terrasse in 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Home-Studio-Editor mit einem fiktiven Raum, Möbeln, Farbpaletten und Oberflächenmustern" width="440" />
</a>

**Home Studio:** echte Editor-Screenshots mit fiktiven Plänen — einer Garage mit
Studio und einem eingerichteten Raum mit Mustern. [Öffne den Planer](https://ha-homelab.github.io/home-studio/planner/)
oder folge der [illustrierten Zeichenanleitung](https://ha-homelab.github.io/home-studio/planner/guide.html).
Bilder: Mitwirkende von Home Studio, MIT. [Bildquellen und Herkunft](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Weitere Projekteinblicke bieten die [EchoMuse-Architektur für Sprache, Musik und BLE](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
die [ZAC93-Verdrahtungsdiagramme](https://github.com/ha-homelab/zac93-esp32)
und die [synthetische RuView-Wiedergabedemo](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Stand der öffentlichen Projekte

![Balkendiagramm: Geräte und Bridges 7; Raumplanung, Sensorik und Zugriff 5; Sprache und Medien 4; Tests und Verträge 4; Konfiguration und Zuverlässigkeit 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.de.svg)

**22 Projekte + dieses Profil-Repository = 23 öffentliche Repositories**, geprüft
am 16. Oktober 2026. Jedes Projekt gehört zu genau einer redaktionellen Kategorie;
die Anzahlen messen weder Reifegrad noch Nutzung oder Leistung.
[Reproduzierbare Quelldaten](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Tatsächliche Ergebnisse der Softwareprüfungen zeigt das separate
[datierte Testdiagramm der Community-Werkzeuge mit verlinkten CI-Läufen](https://github.com/ha-homelab/.github/blob/main/community-tools/README.de.md#prüfnachweise--2026-10-16-utc).

## Verwandte öffentliche Projekte außerhalb dieser Organisation

Diese unabhängig gepflegten Projekte ergänzen das Homelab. Sie sind optionale
Bausteine mit eigenen Einrichtungswegen und Unterstützungsgrenzen.

**Energie — [Victron-/Venus-OS-Ökosystem](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) koordiniert die
  Klimasteuerung über Home Assistant und Venus OS und beobachtet standardmäßig nur.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) stellt Stromkreiswerte
  als GX-Lasten bereit; [dbus-pump](https://github.com/victron-venus/dbus-pump) bindet HA-Entitäten für Tank, Pumpe und Ventil an.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) bietet
  ein Energiedashboard mit Vue-Oberfläche und optionalen Home-Assistant-Geräten.

**Sprache und Medien — einschließlich des [Open-OTT-Play-Ökosystems](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) ist ein
  ausschließlich lesender Alexa Custom Skill; [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats)
  sendet Cast-Video mit lokal synthetisierter Sprache. Beide funktionieren ohne
  Hardwareumbau; Home Assistant ist optional, der Alexa Skill benötigt es nicht.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) findet aktuelle
  XMLTV-Sendungen und leitet die Wiedergabe über einen vorhandenen HLS-Proxy an Alexa-Bildschirme oder Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) bietet
  Playerbefehle, Terminalsteuerung und k3s-Bereitstellung. Das EPG-Gateway ist nicht von OttPlay abhängig.

**Wiederverwendbare Infrastruktur**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) bietet
  ESP32-Referenzkonfigurationen für Batterie-, Temperatur- und Pflanzensensoren.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) verbindet
  REST/WebSocket und MQTT mit Authentifizierung und Topic-Beschränkungen.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) beobachtet
  MQTT- und Mosquitto-Metriken über OpenTelemetry, Prometheus und Grafana; es ist kein Nachrichtenproxy.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) verwaltet
  die GitHub-Einstellungen und Repositories dieser Organisation.

## Unsere Arbeitsweise

Verhalten verständlich halten, Änderungen prüfbar machen, Builds reproduzierbar
und Wiederherstellung dokumentiert. Öffentliche Beispiele und Screenshots verwenden
synthetische Daten, wo dies angegeben ist. Zugangsdaten, Aufnahmen, Gerätesicherungen
und private Betriebsexporte eines Haushalts bleiben außerhalb dieser Repositories.
Jedes Projekt dokumentiert, was getestet wurde und was noch physisch geprüft werden muss.

Für Beiträge gilt die Anleitung des jeweiligen Repositorys, für Schwachstellen dessen
Sicherheitsrichtlinie. Dieses Repository enthält außerdem unser
[Original-Logo und die Gestaltungsnotizen](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Ein unabhängiges Homelab auf Basis von [Home Assistant](https://www.home-assistant.io/).
Keine Verbindung zum Home-Assistant-Projekt oder zu Geräteherstellern.
