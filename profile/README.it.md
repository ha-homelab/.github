<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: una casa turchese con nodi di rete collegati" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Una casa progettata con cura. Automazioni comprensibili.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Prova Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Esplora la configurazione</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.it.md">Strumenti della community</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Sviluppiamo integrazioni Home Assistant, client vocali, bridge per dispositivi,
strumenti spaziali e guide alla distribuzione riutilizzabili. I progetti pubblici
uniscono la domotica pratica a build riproducibili, contratti espliciti e procedure
di ripristino documentate. Inizia da un progetto: ciascuno descrive il proprio
percorso di installazione e l'hardware supportato.

![Ruoli dei progetti HA Homelab: dispositivi, voce, configurazione, strumenti spaziali e test](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.it.svg)

La mappa raggruppa attività correlate. Non implica che tutti i progetti siano
installati insieme o si integrino automaticamente tra loro.

## Novità — ottobre 2026

- **Disegna ed esplora una casa nel browser.** [Home Studio](https://github.com/ha-homelab/home-studio) combina un progettista
  2D/3D, 195 modelli di oggetti, 24 lingue dell'editor e un compilatore locale per
  un visualizzatore installabile in Home Assistant. La
  [modalità Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) permette di esplorare la planimetria installata bloccando i comandi ai dispositivi.
  La [guida alla prima sessione](https://github.com/ha-homelab/home-studio/blob/main/docs/first-session.md) spiega come partire dagli esempi, recuperare le bozze e conservare il lavoro quando il 3D non è disponibile.
- **Altri modi per riutilizzare l'hardware esistente.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) aggiunge un
  percorso documentato per voce, musica e BLE su Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) documenta un bridge Z-Wave. I progetti RF, Zigbee e Tuya elencati
  sotto coprono altre famiglie di dispositivi. La preparazione dell'hardware varia
  per progetto: la messa in servizio fisica di ZAC93 è ancora da completare.
- **Configurazione e ripristino pubblici.** [Home Assistant](https://github.com/ha-homelab/home-assistant) include ora librerie
  riutilizzabili di automazioni e script e contratti d'integrazione;
  [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) pubblica strumenti di distribuzione, backup e ripristino.
  Un'istanza singola con archiviazione locale non offre failover automatico.
- **Verifiche prima dell'automazione.** Nuovi progetti per osservazioni dei sensori,
  direzione della telecamera e accesso affiancano quattro [strumenti della community](https://github.com/ha-homelab/.github/blob/main/community-tools/README.it.md)
  per migrazioni di entità, provenienza delle misure, scenari di automazione e risultati vocali.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) usa ora un solo pulsante adattivo, mantenendo la conferma esplicita dello sblocco.

Questa è un'istantanea editoriale del **16 ottobre 2026**. Consulta README e release
di ciascun progetto per compatibilità e stato aggiornati.

## Esplora i progetti

### Configurazione e affidabilità

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — configurazione pubblica, automazioni e script inclusi,
  guide alla distribuzione e contratti d'integrazione.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — Home Assistant portabile su k3s, aggiornamenti soggetti
  ad approvazione, backup verificati e strumenti di ripristino.

### Voce e media

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 con EchoMuse/emOS, Assist, musica, strumenti
  locali per la casa e proxy BLE registrato separatamente. Il percorso di
  riconoscimento vocale documentato usa un provider cloud: non è completamente offline.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — conversione EchoLocal per Echo Dot 2, con strumenti di
  addestramento della parola di attivazione e valutazione nell'esatto ambiente di esecuzione.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — conversione di Echo Show 5 Gen2 ad Android, backup
  verificati e configurazione di Home Assistant Companion.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — strumenti riutilizzabili di acquisizione dello schermo
  LG webOS e integrazione Home Assistant.

EchoLocal ed EchoMuse sono percorsi di conversione distinti. Prima di modificare
un dispositivo, leggi i requisiti di modello e ripristino del progetto scelto.

### Integrazioni, bridge e ripristino dei dispositivi

- **[ha-radio-hub](https://github.com/ha-homelab/ha-radio-hub)** — prototipo PoE modulare per Zigbee, Thread, Bluetooth, Z-Wave, 433 MHz e rilevamento; include CAD, firmware e strumenti di distribuzione; la validazione fisica è ancora da eseguire.
- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — integrazione cloud DESLOC non ufficiale per stato della
  serratura, comandi, batteria e Wi-Fi; [la compatibilità varia per modello](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — scheda dashboard separata con editor visuale, azione
  adattiva e comandi di sblocco con conferma.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — gateway ESPHome CC1101 per osservazioni RF via MQTT,
  trasmissione nativa ESPHome e automazione Home Assistant.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — firmware per pulsanti Tuya con controllo nativo
  di gruppi Zigbee: pressione breve per commutare e prolungata per spegnere;
  consulta gli [attuali limiti della validazione fisica](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — conversione di prese ESP8266 meno recenti, postazione
  Linux riproducibile per il flashing e guide al bridge Matter.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — progetto illustrato di bridge Zooz ZAC93 per ESP32-WROOM/S3,
  ESPHome e Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — backup, aggiornamento e ripristino Ethernet legacy
  dell'SLZB-06 originale; firmware core e radio sono obiettivi separati.

### Spazi, osservazioni dei sensori e accesso

- **[home-studio](https://github.com/ha-homelab/home-studio)** — disegna stanze, arredale, esplorale in 3D, esporta il
  progetto e compila localmente un visualizzatore Home Assistant.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — registra, annota e confronta osservazioni con
  controlli espliciti di attualità e sincronizzazione temporale.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — osservazioni RuView tramite MQTT discovery,
  verifica di attualità per nodo ed esempi di riproduzione sintetici.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — stime dell'area basate sulla sola lettura della
  direzione della telecamera, settori configurati e controlli di attualità.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — sessioni Cloudflare Access verificate per dashboard
  esterne e token di breve durata tramite un gateway limitato. Associa un solo
  amministratore Home Assistant configurato esplicitamente e dotato di tutti i privilegi.

Gli esempi dei sensori descrivono osservazioni e relativi limiti. La riproduzione
sintetica e la direzione della telecamera non attestano l'accuratezza del rilevamento
reale di occupazione.

### Test e contratti

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — piani offline di migrazione semantica che
  distinguono il ruolo di un dispositivo dal suo hardware.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — controlli di ambito della misura, provenienza,
  prove di calibrazione e aggregazione.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — scenari sintetici delimitati, eseguiti in un vero
  motore di automazione Home Assistant isolato.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — evidenze vocali offline che distinguono completamento
  del protocollo, azione osservata e risposta udibile.

Segui il [flusso illustrato con i risultati](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.it.md) o la sua [edizione russa](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md).
Le evidenze software e l'accettazione fisica rimangono passaggi separati.

<details>
<summary>Flusso di revisione e verifiche software documentate</summary>

![Quattro strumenti della community e il confine con l'accettazione fisica separata](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.it.svg)

![Conteggi datati dei test Linux dei quattro strumenti, con note separate sui test saltati](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.it.svg)

Questi diagrammi conservano le [evidenze del 16 ottobre 2026 e i run CI collegati della guida della community](https://github.com/ha-homelab/.github/blob/main/community-tools/README.it.md#validation-evidence--2026-10-16-utc).
Le frecce indicano passaggi di revisione. I conteggi dei test sono evidenze software
con ambito definito, non classifiche qualitative, percentuali di copertura o benchmark di dispositivi fisici.

</details>

## Guarda gli strumenti in uso

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Editor Home Studio nel browser con garage, studio creativo e patio fittizi in 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Editor Home Studio con una stanza fittizia, mobili, tavolozze e motivi delle superfici" width="440" />
</a>

**Home Studio:** schermate reali dell'editor con planimetrie fittizie — un garage
con studio e una stanza arredata con motivi. [Apri il progettista](https://ha-homelab.github.io/home-studio/planner/) o segui la
[guida illustrata al disegno](https://ha-homelab.github.io/home-studio/planner/guide.html). Immagini: collaboratori di Home Studio, MIT.
[Fonti e provenienza delle immagini](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Per altre viste dei progetti, esplora l'[architettura EchoMuse per voce, musica e BLE](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
gli [schemi di cablaggio ZAC93](https://github.com/ha-homelab/zac93-esp32) e la [dimostrazione di riproduzione sintetica RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Istantanea dei progetti pubblici

![Grafico a barre: dispositivi e bridge 8; spazi, sensori e accesso 5; voce e media 4; test e contratti 4; configurazione e affidabilità 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.it.svg)

**23 progetti + questo repository del profilo = 24 repository pubblici**, verificati
il 16 ottobre 2026. Ogni progetto ha una sola categoria editoriale; i conteggi non
misurano maturità, utilizzo o prestazioni. [Dati sorgente riproducibili](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Per risultati effettivi delle verifiche software, consulta il
[grafico datato dei test della community e i run CI collegati](https://github.com/ha-homelab/.github/blob/main/community-tools/README.it.md#validation-evidence--2026-10-16-utc).

## Progetti pubblici correlati esterni a questa organizzazione

Questi progetti gestiti separatamente completano l'homelab. Sono componenti
opzionali con procedure di configurazione e limiti di supporto propri.

**Energia — [ecosistema Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) coordina la climatizzazione tramite Home Assistant e Venus OS,
  limitandosi per impostazione predefinita all'osservazione.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) espone le letture dei circuiti come carichi GX;
  [dbus-pump](https://github.com/victron-venus/dbus-pump) collega le entità HA di serbatoi, pompe e valvole.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) offre una dashboard energetica con interfaccia Vue
  e dispositivi Home Assistant opzionali.

**Voce e media — incluso l'[ecosistema Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) è una skill Alexa personalizzata di sola lettura;
  [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) invia video Cast con voce sintetizzata localmente.
  Funzionano senza conversione hardware; Home Assistant è opzionale e la skill Alexa non lo richiede.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) trova i programmi XMLTV correnti e instrada la riproduzione
  tramite un proxy HLS esistente verso schermi Alexa o Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) offre comandi del player, controllo da terminale e
  distribuzione su k3s. Il gateway EPG non dipende da OttPlay.

**Infrastruttura riutilizzabile**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) offre configurazioni ESP32 di riferimento per
  sensori di batteria, temperatura e piante.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) collega REST/WebSocket e MQTT con autenticazione e
  restrizioni sui topic.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) osserva le metriche MQTT e Mosquitto tramite OpenTelemetry,
  Prometheus e Grafana; non è un proxy di messaggi.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) gestisce impostazioni GitHub e repository di questa organizzazione.

## Come lavoriamo

Comportamenti comprensibili, modifiche revisionabili, build riproducibili e
ripristino documentato. Gli esempi pubblici e le schermate usano dati sintetici
quando indicato; credenziali domestiche, registrazioni, backup dei dispositivi ed
esportazioni operative private restano fuori da questi repository. Ogni progetto
documenta ciò che è stato testato e ciò che richiede ancora una verifica fisica.

Contribuisci seguendo la guida del repository interessato; segnala vulnerabilità
tramite la sua policy di sicurezza. Questo repository ospita anche il nostro
[logo originale e le note di progettazione](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Un homelab indipendente basato su [Home Assistant](https://www.home-assistant.io/).
Non affiliato al progetto Home Assistant o ai produttori di dispositivi.
