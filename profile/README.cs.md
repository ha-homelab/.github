<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: tyrkysový dům s propojenými síťovými uzly" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Promyšlená domácnost. Srozumitelná automatizace.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Vyzkoušejte Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Prozkoumejte konfiguraci</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.cs.md">Komunitní nástroje</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Vytváříme opakovaně použitelné integrace Home Assistant, hlasové klienty,
mosty pro zařízení, prostorové nástroje a návody k nasazení. Veřejné projekty
spojují praktickou domácí automatizaci s reprodukovatelným sestavením, výslovnými
kontrakty a zdokumentovanou obnovou. Začněte jedním projektem; každý má vlastní
postup instalace a podporovaný hardware.

![Role projektů HA Homelab: zařízení, hlas, konfigurace, prostorové nástroje a testování](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.cs.svg)

Mapa seskupuje související práci. Neznamená, že se všechny projekty instalují
společně nebo že se automaticky navzájem integrují.

## Novinky — říjen 2026

- **Nakreslete a prozkoumejte domácnost v prohlížeči.** [Home Studio](https://github.com/ha-homelab/home-studio) spojuje plánovač 2D/3D, 206 návrhů nábytku a zahradních prvků a 24 jazyků editoru.
  Vydání obsahující `home_floorplan.zip` nabízejí také [editor uvnitř Home Assistant](https://github.com/ha-homelab/home-studio/blob/main/docs/home-assistant-editor.md)
  pro kreslení, propojení oblastí HA, ukládání konceptů a publikování 3D pohledu.
  Samostatný editor v prohlížeči i přenositelný kompilátor a instalátor zůstávají dostupné. Jeho
  [režim Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) umožňuje procházet nainstalovaný plán a přitom blokuje příkazy zařízením.
  [Průvodce první relací](https://github.com/ha-homelab/home-studio/blob/main/docs/first-session.md) vysvětluje začátek s příklady, obnovu rozpracovaných návrhů a zachování práce, když 3D není dostupné.
- **Další způsoby využití stávajícího hardwaru.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) přidává
  zdokumentovanou cestu pro hlas, hudbu a BLE na Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) popisuje most Z-Wave. Níže uvedené projekty RF, Zigbee a Tuya
  pokrývají další rodiny zařízení. Připravenost hardwaru se liší podle projektu:
  fyzické uvedení ZAC93 do provozu stále čeká na dokončení.
- **Veřejná konfigurace a obnova.** [Home Assistant](https://github.com/ha-homelab/home-assistant) nyní obsahuje opakovaně
  použitelné knihovny automatizací a skriptů i integrační kontrakty;
  [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) zveřejňuje nástroje pro nasazení, zálohování a obnovu.
  Jedna instance s místním úložištěm neposkytuje automatické převzetí při selhání.
- **Nejdříve důkazy, potom automatizace.** Nové projekty pro pozorování senzorů,
  směr kamery a přístup doplňují čtyři [komunitní nástroje](https://github.com/ha-homelab/.github/blob/main/community-tools/README.cs.md) pro migrace entit,
  původ měření, scénáře automatizace a hlasové výsledky.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) nyní používá jediné adaptivní tlačítko a stále vyžaduje výslovné potvrzení odemknutí.

Jde o redakční snímek k **19. říjnu 2026**. Aktuální kompatibilitu a stav najdete
v README a vydáních jednotlivých projektů.

## Prozkoumejte projekty

### Konfigurace a spolehlivost

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — veřejná konfigurace, přibalené automatizace a skripty,
  návody k nasazení a integrační kontrakty.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — přenositelný Home Assistant na k3s, aktualizace po
  schválení, ověřené zálohy a nástroje obnovy.

### Hlas a média

- **[asterisk-telephony](https://github.com/ha-homelab/asterisk-telephony)** — ověřený instalátor integrace Asterisk z upstream projektu, přehledové panely SIP telefonů a ovládání telefonů Cisco se samostatnou zvukovou cestou Assist a zdokumentovanými výsledky přejímky.
- **[ha-ottplay](https://github.com/ha-homelab/ha-ottplay)** — entity přehrávače médií a dálkového ovládání v Home Assistant pro registrované přehrávače přes existující OTTPlay Control Server; dostupné ovládání závisí na přehrávači.
- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 s EchoMuse/emOS, Assist, hudbou, místními
  nástroji pro domácnost a samostatně registrovaným BLE proxy. Zdokumentovaná
  cesta rozpoznávání řeči používá cloudového poskytovatele, není tedy zcela offline.
  Pilotní provoz s ruským aktivačním slovem a Silero Baya nezveřejňuje soukromé váhy modelu.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — přestavba Echo Dot 2 pomocí EchoLocal, s nástroji pro
  trénování aktivačního slova a vyhodnocení v přesném běhovém prostředí.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — přestavba Echo Show 5 Gen2 na Android, ověřené zálohy
  a nastavení Home Assistant Companion.
  Volitelný pokus s ONNX a jedinou aktivační frází má softwarové kontroly; úplná akustická přejímka dosud chybí.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — opakovaně použitelné nástroje snímání obrazovky LG
  webOS a integrace Home Assistant.

EchoLocal a EchoMuse jsou různé cesty přestavby. Před úpravou zařízení si přečtěte
požadavky vybraného projektu na model a obnovu.

### Integrace zařízení, mosty a obnova

- **[ha-radio-hub](https://github.com/ha-homelab/ha-radio-hub)** — aktuální modulární PoE prototyp MC2-C + FH1 se třemi nezávislými externími anténami pro Zigbee, Thread a Bluetooth, místním Thread Border Routerem, Z-Wave, RF na 433 MHz a senzory. Obsahuje CAD, firmware a nástroje pro nasazení; fyzické ověření dosud chybí.
- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — neoficiální cloudová integrace DESLOC pro stav zámku,
  ovládání, baterii a Wi-Fi; [kompatibilita se liší podle modelu](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — samostatná karta ovládacího panelu s vizuálním editorem,
  adaptivní akcí a odemknutím s potvrzením.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — brána ESPHome CC1101 pro RF pozorování přes MQTT,
  nativní vysílání ESPHome a automatizaci Home Assistant.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — firmware tlačítek Tuya pro nativní řízení skupin
  Zigbee, krátký stisk pro přepnutí a podržení pro vypnutí;
  viz [současná omezení fyzického ověření](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — přestavba starších zásuvek ESP8266, reprodukovatelná
  linuxová stanice pro nahrávání firmwaru a návody k mostu Matter.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — ilustrovaný návrh mostu Zooz ZAC93 pro ESP32-WROOM/S3,
  ESPHome a Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — zálohování, aktualizace a starší obnova přes Ethernet
  pro původní SLZB-06; firmware jádra a rádia jsou samostatné cíle.

### Prostor, pozorování senzorů a přístup

- **[home-studio](https://github.com/ha-homelab/home-studio)** — kreslete a zařizujte místnosti v samostatném editoru v prohlížeči nebo uvnitř Home Assistant; exportujte JSON nebo publikujte pohled HA.
- **[ruview-home-sensing](https://github.com/ha-homelab/ruview-home-sensing)** — experimentální sběr CSI, firmware přijímačů, hypotézy o aktivitě a nástroje pro důkazy o inferenci; publikuje přes ruview-home-assistant a neprokazuje přesnost detekce v reálném prostředí.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — záznam, označování a porovnávání pozorování
  s výslovnou kontrolou aktuálnosti a času.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — pozorování RuView přes MQTT discovery,
  aktuálnost podle uzlu a příklady syntetického přehrávání.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — odhady oblasti z pouze čteného směru kamery,
  nastavených sektorů a kontrol aktuálnosti.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — ověřené relace Cloudflare Access pro externí
  panely a krátkodobé tokeny přes omezenou bránu. Mapuje jediného výslovně
  nastaveného správce Home Assistant s plnými oprávněními.
  Volitelný autentizovaný přístup k obalům médií přehrávače je ve výchozím stavu vypnutý.

Příklady senzorů popisují pozorování a jejich omezení. Syntetické přehrávání a směr
kamery neprokazují přesnost detekce přítomnosti v reálném světě.

### Testy a kontrakty

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — offline sémantické migrační plány, které
  rozlišují roli zařízení od jeho hardwaru.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — kontroly rozsahu měření, původu, dokladů
  o kalibraci a agregace.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — omezené syntetické scénáře v izolovaném skutečném
  automatizačním enginu Home Assistant.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — offline hlasové důkazy rozlišující dokončení
  protokolu, pozorovanou akci a slyšitelnou odpověď.

Projděte [ilustrovaný postup a výsledky](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.cs.md). Přepínač jazyků příručky nabízí všech 24 jazyků.
Softwarové důkazy a fyzická přejímka zůstávají samostatnými kroky.

<details>
<summary>Postup revize a zaznamenané softwarové kontroly</summary>

![Čtyři komunitní nástroje a hranice samostatné fyzické přejímky](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.cs.svg)

![Datované počty linuxových testů čtyř nástrojů se samostatnými poznámkami o přeskočení](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.cs.svg)

Diagramy zachovávají [důkazy z 16. října 2026 a odkazované běhy CI z komunitní příručky](https://github.com/ha-homelab/.github/blob/main/community-tools/README.cs.md#validation-evidence--2026-10-16-utc).
Šipky označují předání při revizi. Počty testů jsou softwarové důkazy s vymezeným
rozsahem, nikoli žebříček kvality, procento pokrytí ani benchmark fyzických zařízení.

</details>

## Ukázky použití

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Editor Home Studio v prohlížeči s fiktivní garáží, tvůrčím studiem a terasou ve 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Editor Home Studio s fiktivní místností, nábytkem, barevnými paletami a vzory povrchů" width="440" />
</a>

**Home Studio:** skutečné snímky editoru s fiktivními plány — garáží se studiem
 a vybavenou místností se vzory. [Otevřete plánovač](https://ha-homelab.github.io/home-studio/planner/) nebo postupujte podle
[ilustrovaného návodu ke kreslení](https://ha-homelab.github.io/home-studio/planner/guide.html). Obrázky: přispěvatelé Home Studio, MIT.
[Zdroje a původ obrázků](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Další ukázky nabízí [architektura hlasu, hudby a BLE v EchoMuse](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
[schémata zapojení ZAC93](https://github.com/ha-homelab/zac93-esp32) a [ukázka syntetického přehrávání RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Přehled veřejných projektů

![Pruhový graf: zařízení a mosty 8; prostor, senzory a přístup 6; hlas a média 6; testy a kontrakty 4; konfigurace a spolehlivost 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.cs.svg)

**26 projektů + tento profilový repozitář = 27 veřejných repozitářů**, ověřeno dne 19. října 2026. Každý projekt patří do jedné redakční kategorie; počty neměří
vyspělost, využití ani výkon. [Reprodukovatelná zdrojová data](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Skutečné výsledky softwarových kontrol najdete v samostatném
[datovaném grafu komunitních testů a odkazovaných bězích CI](https://github.com/ha-homelab/.github/blob/main/community-tools/README.cs.md#validation-evidence--2026-10-16-utc).

## Související veřejné projekty mimo tuto organizaci

Tyto samostatně spravované projekty doplňují homelab. Jsou to volitelné stavební
bloky s vlastními postupy nastavení a hranicemi podpory.

**Energie — [ekosystém Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) koordinuje klimatizaci přes Home Assistant a Venus OS;
  ve výchozím stavu pouze pozoruje.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) zpřístupňuje měření okruhů jako zátěže GX;
  [dbus-pump](https://github.com/victron-venus/dbus-pump) propojuje entity HA pro nádrž, čerpadlo a ventil.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) nabízí energetický panel s rozhraním Vue
  a volitelnými zařízeními Home Assistant.

**Hlas a média — včetně [ekosystému Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) je vlastní dovednost Alexa pouze pro čtení;
  [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) posílá video Cast s místně syntetizovanou řečí.
  Fungují bez přestavby hardwaru; Home Assistant je volitelný a dovednost Alexa jej nevyžaduje.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) vyhledává aktuální pořady XMLTV a směruje přehrávání přes
  existující proxy HLS na obrazovky Alexa nebo Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) nabízí příkazy přehrávače, ovládání terminálu
  a nasazení na k3s. Brána EPG nezávisí na OttPlay.
- [Cisco Home Telephony](https://github.com/4alvit/cisco-home-telephony) — SIP provisioning pro Cisco 7945G, Asterisk na k3s, telefonní CLI a volitelné hlasové a ovládací postupy s Home Assistant.

**Opakovaně použitelná infrastruktura**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) nabízí referenční konfigurace ESP32 pro
  bateriové, teplotní a rostlinné senzory.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) propojuje REST/WebSocket a MQTT s autentizací
  a omezením témat.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) sleduje metriky MQTT a Mosquitto přes OpenTelemetry,
  Prometheus a Grafanu; nejde o proxy zpráv.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) spravuje nastavení GitHubu a repozitáře této organizace.
- [Venus OS CI Toolkit](https://github.com/victron-venus/venus-os-ci-toolkit) — sdílené workflow GitHub Actions a nástroje CI pro validaci, vydávání a bezpečnostní kontroly; uživatelské projekty připínají zkontrolovaný commit.

## Jak pracujeme

Chování má být srozumitelné, změny kontrolovatelné, sestavení reprodukovatelné
 a obnova zdokumentovaná. Veřejné příklady a snímky používají syntetická data tam,
kde je to uvedeno; domácí přihlašovací údaje, nahrávky, zálohy zařízení a soukromé
provozní exporty zůstávají mimo tyto repozitáře. Každý projekt dokumentuje,
co bylo testováno a co ještě vyžaduje fyzické ověření.

Přispívejte podle příručky příslušného repozitáře; zranitelnosti hlaste podle
jeho bezpečnostních zásad. Tento repozitář také obsahuje naše
[původní logo a poznámky k návrhu](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Nezávislý homelab postavený na [Home Assistant](https://www.home-assistant.io/).
Bez spojení s projektem Home Assistant nebo výrobci zařízení.
