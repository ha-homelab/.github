<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: turkusowy dom z połączonymi węzłami sieci" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Przemyślany dom. Zrozumiała automatyzacja.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Wypróbuj Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Poznaj konfigurację</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.pl.md">Narzędzia społeczności</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Tworzymy integracje Home Assistant, klientów głosowych, mostki urządzeń,
narzędzia przestrzenne i poradniki wdrażania do ponownego wykorzystania.
Publiczne projekty łączą praktyczną automatykę domową z odtwarzalnymi kompilacjami,
jawnymi kontraktami i udokumentowanym odzyskiwaniem. Zacznij od jednego projektu:
każdy opisuje własną instalację i obsługiwany sprzęt.

![Role projektów HA Homelab: urządzenia, głos, konfiguracja, narzędzia przestrzenne i testy](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.pl.svg)

Mapa grupuje powiązane prace. Nie oznacza, że wszystkie projekty są instalowane
razem lub automatycznie integrują się ze sobą.

## Nowości — październik 2026

- **Narysuj i poznaj dom w przeglądarce.** [Home Studio](https://github.com/ha-homelab/home-studio) łączy planer 2D/3D,
  195 projektów przedmiotów, 24 języki edytora i lokalny kompilator tworzący
  przeglądarkę planu do instalacji w Home Assistant.
  [Tryb Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) pozwala poznawać zainstalowany plan, blokując polecenia do urządzeń.
- **Więcej sposobów na ponowne użycie sprzętu.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) dodaje
  udokumentowaną ścieżkę głosu, muzyki i BLE dla Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) opisuje mostek Z-Wave. Wymienione niżej projekty RF, Zigbee
  i Tuya obejmują inne rodziny urządzeń. Gotowość sprzętu zależy od projektu:
  fizyczne uruchomienie ZAC93 pozostaje do wykonania.
- **Publiczna konfiguracja i odzyskiwanie.** [Home Assistant](https://github.com/ha-homelab/home-assistant) zawiera teraz
  biblioteki automatyzacji i skryptów do ponownego użycia oraz kontrakty integracji;
  [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) publikuje narzędzia wdrażania, kopii zapasowych i odzyskiwania.
  Jedna instancja z lokalnym magazynem nie zapewnia automatycznego przejęcia po awarii.
- **Najpierw dowody, potem automatyzacja.** Nowe projekty obserwacji czujników,
  kierunku kamery i dostępu towarzyszą czterem [narzędziom społeczności](https://github.com/ha-homelab/.github/blob/main/community-tools/README.pl.md) do migracji
  encji, pochodzenia pomiarów, scenariuszy automatyzacji i wyników głosowych.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) używa teraz jednego adaptacyjnego przycisku, zachowując jawne potwierdzenie odblokowania.

To stan redakcyjny z **16 października 2026**. Aktualną zgodność i stan znajdziesz
w README i wydaniach poszczególnych projektów.

## Poznaj projekty

### Konfiguracja i niezawodność

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — publiczna konfiguracja, dołączone automatyzacje i skrypty,
  instrukcje wdrożenia i kontrakty integracji.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — przenośny Home Assistant na k3s, aktualizacje wymagające
  zgody, zweryfikowane kopie zapasowe i narzędzia odzyskiwania.

### Głos i multimedia

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 z EchoMuse/emOS, Assist, muzyką, lokalnymi
  narzędziami domowymi i osobno rejestrowanym proxy BLE. Udokumentowana ścieżka
  rozpoznawania mowy korzysta z chmury i nie jest całkowicie offline.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — konwersja Echo Dot 2 przez EchoLocal, z treningiem słowa
  aktywującego i narzędziami oceny w dokładnym środowisku wykonawczym.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — konwersja Echo Show 5 Gen2 do Androida, zweryfikowane
  kopie zapasowe i konfiguracja Home Assistant Companion.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — narzędzia przechwytywania ekranu LG webOS do ponownego
  użycia i integracja Home Assistant.

EchoLocal i EchoMuse to różne ścieżki konwersji. Przed modyfikacją urządzenia
przeczytaj wymagania wybranego projektu dotyczące modelu i odzyskiwania.

### Integracje, mostki i odzyskiwanie urządzeń

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — nieoficjalna integracja chmury DESLOC dla stanu zamka,
  sterowania, baterii i Wi-Fi; [zgodność zależy od modelu](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — osobna karta panelu z edytorem wizualnym, adaptacyjną
  akcją i odblokowaniem po potwierdzeniu.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — bramka ESPHome CC1101 dla obserwacji RF przez MQTT,
  natywnej transmisji ESPHome i automatyzacji Home Assistant.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — firmware przycisków Tuya z natywnym sterowaniem
  grupami Zigbee: krótkie naciśnięcie przełącza, przytrzymanie wyłącza;
  zobacz [obecne ograniczenia weryfikacji fizycznej](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — konwersja starszych gniazdek ESP8266, odtwarzalna
  stacja Linux do wgrywania firmware i poradniki mostka Matter.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — ilustrowany projekt mostka Zooz ZAC93 dla ESP32-WROOM/S3,
  ESPHome i Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — kopie zapasowe, aktualizacja i starsze odzyskiwanie
  przez Ethernet dla oryginalnego SLZB-06; firmware główny i radiowy to osobne cele.

### Przestrzeń, obserwacje czujników i dostęp

- **[home-studio](https://github.com/ha-homelab/home-studio)** — rysuj i wyposażaj pomieszczenia, oglądaj je w 3D,
  eksportuj projekt i lokalnie kompiluj przeglądarkę dla Home Assistant.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — zapisuj, oznaczaj i porównuj obserwacje
  z jawnymi kontrolami aktualności i zegara.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — obserwacje RuView przez MQTT discovery,
  aktualność na poziomie węzła i przykłady syntetycznego odtwarzania.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — oszacowanie obszaru na podstawie samego odczytu
  kierunku kamery, skonfigurowanych sektorów i kontroli aktualności.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — zweryfikowane sesje Cloudflare Access dla zewnętrznych
  paneli i krótkotrwałe tokeny przez ograniczoną bramkę. Mapuje jednego jawnie
  skonfigurowanego administratora Home Assistant z pełnymi uprawnieniami.

Przykłady czujników opisują obserwacje i ich ograniczenia. Syntetyczne odtwarzanie
oraz kierunek kamery nie dowodzą dokładności wykrywania obecności w rzeczywistym otoczeniu.

### Testy i kontrakty

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — semantyczne plany migracji offline odróżniające
  rolę urządzenia od jego sprzętu.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — kontrole zakresu pomiaru, pochodzenia,
  dowodów kalibracji i agregacji.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — ograniczone scenariusze syntetyczne w izolowanym,
  rzeczywistym silniku automatyzacji Home Assistant.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — dowody głosowe offline rozróżniające zakończenie
  protokołu, zaobserwowaną akcję i słyszalną odpowiedź.

Poznaj [ilustrowany proces i wyniki](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.pl.md) lub jego [wersję rosyjską](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md).
Dowody programowe i odbiór fizyczny pozostają oddzielnymi etapami.

<details>
<summary>Proces przeglądu i zapisane kontrole oprogramowania</summary>

![Cztery narzędzia społeczności i granica oddzielnego odbioru fizycznego](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.pl.svg)

![Datowane liczby testów Linux czterech narzędzi, z osobnymi uwagami o pominięciach](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.pl.svg)

Diagramy zachowują [dowody z 16 października 2026 i powiązane uruchomienia CI z poradnika społeczności](https://github.com/ha-homelab/.github/blob/main/community-tools/README.pl.md#validation-evidence--2026-10-16-utc).
Strzałki oznaczają przekazania do przeglądu. Liczby testów są dowodami programowymi
w określonym zakresie, a nie rankingiem jakości, procentem pokrycia lub benchmarkiem sprzętu.

</details>

## Zobacz w użyciu

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Edytor Home Studio w przeglądarce z fikcyjnym garażem, pracownią i patio w 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Edytor Home Studio z fikcyjnym pokojem, meblami, paletami kolorów i wzorami powierzchni" width="440" />
</a>

**Home Studio:** rzeczywiste zrzuty edytora z fikcyjnymi planami — garażem
z pracownią i umeblowanym pokojem ze wzorami. [Otwórz planer](https://ha-homelab.github.io/home-studio/planner/) lub skorzystaj
z [ilustrowanego poradnika rysowania](https://ha-homelab.github.io/home-studio/planner/guide.html). Obrazy: współtwórcy Home Studio, MIT.
[Źródła i pochodzenie obrazów](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Inne widoki projektów to [architektura głosu, muzyki i BLE w EchoMuse](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
[schematy połączeń ZAC93](https://github.com/ha-homelab/zac93-esp32) i [demonstracja syntetycznego odtwarzania RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Stan projektów publicznych

![Wykres słupkowy: urządzenia i mostki 7; przestrzeń, czujniki i dostęp 5; głos i multimedia 4; testy i kontrakty 4; konfiguracja i niezawodność 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.pl.svg)

**22 projekty + repozytorium tego profilu = 23 publiczne repozytoria**, sprawdzone
16 października 2026. Każdy projekt ma jedną kategorię redakcyjną; liczby nie mierzą
dojrzałości, użycia ani wydajności. [Odtwarzalne dane źródłowe](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Rzeczywiste wyniki kontroli oprogramowania znajdziesz na osobnym
[datowanym wykresie testów społeczności z odnośnikami do CI](https://github.com/ha-homelab/.github/blob/main/community-tools/README.pl.md#validation-evidence--2026-10-16-utc).

## Powiązane projekty publiczne spoza tej organizacji

Te oddzielnie utrzymywane projekty uzupełniają homelab. Są opcjonalnymi elementami
z własnymi procedurami konfiguracji i granicami wsparcia.

**Energia — [ekosystem Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) koordynuje klimatyzację przez Home Assistant i Venus OS,
  domyślnie tylko obserwując.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) udostępnia odczyty obwodów jako obciążenia GX;
  [dbus-pump](https://github.com/victron-venus/dbus-pump) łączy encje HA zbiornika, pompy i zaworu.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) zapewnia panel energii z interfejsem Vue
  i opcjonalnymi urządzeniami Home Assistant.

**Głos i multimedia — w tym [ekosystem Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) to własna umiejętność Alexa tylko do odczytu;
  [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) wysyła wideo Cast z lokalnie syntezowaną mową.
  Działają bez konwersji sprzętu; Home Assistant jest opcjonalny, a umiejętność Alexa go nie wymaga.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) znajduje bieżące programy XMLTV i kieruje odtwarzanie
  przez istniejące proxy HLS do ekranów Alexa lub Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) zapewnia polecenia odtwarzacza, sterowanie terminalem
  i wdrożenie na k3s. Bramka EPG nie zależy od OttPlay.

**Infrastruktura do ponownego wykorzystania**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) oferuje referencyjne konfiguracje ESP32
  dla czujników baterii, temperatury i roślin.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) łączy REST/WebSocket i MQTT z uwierzytelnianiem
  i ograniczeniami tematów.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) obserwuje metryki MQTT i Mosquitto przez OpenTelemetry,
  Prometheus i Grafana; nie jest proxy wiadomości.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) zarządza ustawieniami GitHub i repozytoriami tej organizacji.

## Jak pracujemy

Zachowanie ma być zrozumiałe, zmiany możliwe do przeglądu, kompilacje odtwarzalne,
a odzyskiwanie udokumentowane. Publiczne przykłady i zrzuty używają danych
syntetycznych tam, gdzie to wskazano; domowe dane uwierzytelniające, nagrania,
kopie urządzeń i prywatne eksporty operacyjne pozostają poza repozytoriami.
Każdy projekt opisuje, co sprawdzono i co nadal wymaga weryfikacji fizycznej.

Współtwórz zgodnie z poradnikiem odpowiedniego repozytorium; luki zgłaszaj według
jego polityki bezpieczeństwa. To repozytorium zawiera również nasze
[oryginalne logo i notatki projektowe](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Niezależny homelab zbudowany z [Home Assistant](https://www.home-assistant.io/).
Bez powiązania z projektem Home Assistant ani producentami urządzeń.
