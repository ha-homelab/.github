<p align="center"><img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: rumah berwarna toska dengan simpul jaringan yang terhubung" width="144" /></p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Rumah yang dirancang matang. Otomasi yang dapat dipahami.</strong></p>
<p align="center"><a href="https://ha-homelab.github.io/home-studio/planner/">Coba Home Studio</a> · <a href="https://github.com/ha-homelab/home-assistant">Jelajahi konfigurasi</a> · <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.id.md">Alat komunitas</a></p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Kami membuat integrasi Home Assistant yang dapat digunakan kembali, klien suara, jembatan perangkat, alat perencanaan ruang, dan panduan penerapan. Proyek publik menggabungkan otomasi rumah praktis dengan build yang dapat direproduksi, kontrak yang jelas, dan pemulihan terdokumentasi. Mulailah dari satu proyek; setiap proyek memiliki cara pemasangan dan perangkat keras yang didukung sendiri.

![Peta peran proyek HA Homelab: perangkat, suara, konfigurasi, alat ruang, dan pengujian](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.id.svg)

Peta ini mengelompokkan pekerjaan yang berkaitan. Ini tidak berarti semua proyek dipasang bersama atau otomatis terintegrasi satu sama lain.

## Yang baru — Oktober 2026

- **Gambar dan jelajahi rumah di peramban.** [Home Studio](https://github.com/ha-homelab/home-studio) menggabungkan perencana 2D/3D, 195 desain objek, 24 bahasa editor, dan kompiler lokal untuk penampil yang dapat dipasang di Home Assistant. [Mode Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) memungkinkan Anda menjelajahi denah terpasang sambil memblokir perintah ke perangkat.
- **Lebih banyak cara memakai kembali perangkat.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) mendokumentasikan jalur suara, musik, dan BLE untuk Echo Dot 2; [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) mendokumentasikan jembatan Z-Wave. Proyek RF, Zigbee, dan Tuya di bawah mencakup keluarga perangkat lain. Kesiapan perangkat keras berbeda antarproyek: uji pengoperasian fisik ZAC93 masih menunggu.
- **Konfigurasi publik dan pemulihan.** [Home Assistant](https://github.com/ha-homelab/home-assistant) kini menyertakan pustaka otomasi/skrip yang dapat digunakan kembali serta kontrak integrasi; [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) menerbitkan alat penerapan, pencadangan, dan pemulihan. Satu instans dengan penyimpanan lokal tidak memberikan failover otomatis.
- **Bukti sebelum otomasi.** Proyek baru untuk pengamatan, arah kamera, dan akses melengkapi empat [alat komunitas](https://github.com/ha-homelab/.github/blob/main/community-tools/README.id.md) untuk migrasi entitas, asal-usul pengukuran, skenario otomasi, dan hasil suara. [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) kini memakai satu tombol tindakan adaptif sambil tetap mewajibkan konfirmasi pembukaan kunci.

Ini adalah potret editorial per **16 Oktober 2026**. Lihat README dan rilis masing-masing proyek untuk kompatibilitas dan status terkini.

## Jelajahi proyek

### Konfigurasi dan keandalan

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — konfigurasi publik, otomasi dan skrip bawaan, panduan penerapan, serta kontrak integrasi.

- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — Home Assistant portabel di k3s, pembaruan yang memerlukan persetujuan, cadangan terverifikasi, dan alat pemulihan.

### Suara dan media

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 dengan EchoMuse/emOS, Assist, musik, alat rumah lokal, dan proksi BLE yang didaftarkan terpisah. Jalur pengenalan ucapan yang dicatat memakai penyedia cloud; tidak sepenuhnya luring.

- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — jalur konversi EchoLocal untuk Echo Dot 2, dengan pelatihan kata pemicu dan alat evaluasi pada lingkungan eksekusi yang sama persis.

- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — konversi Echo Show 5 Gen2 ke Android, cadangan terverifikasi, dan pengaturan Home Assistant Companion.

- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — alat tangkapan layar LG webOS yang dapat digunakan kembali dan integrasi Home Assistant.

EchoLocal dan EchoMuse adalah jalur konversi berbeda. Baca persyaratan model dan pemulihan proyek pilihan sebelum memodifikasi perangkat.

### Integrasi perangkat, jembatan, dan pemulihan

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — integrasi cloud DESLOC tidak resmi untuk status kunci, kontrol, baterai, dan Wi-Fi; [kompatibilitas berbeda menurut model](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).

- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — kartu dasbor terpisah dengan editor visual, tindakan adaptif, dan konfirmasi pembukaan kunci.

- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — gerbang ESPHome CC1101 untuk pengamatan RF melalui MQTT, transmisi asli ESPHome, dan otomasi Home Assistant.

- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — firmware tombol Tuya untuk kontrol grup Zigbee langsung, tekan singkat untuk beralih dan tahan untuk mematikan; lihat [batas validasi fisik saat ini](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).

- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — konversi stopkontak ESP8266 lama, stasiun flashing Linux yang dapat direproduksi, dan panduan jembatan Matter.

- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — desain jembatan Zooz ZAC93 berilustrasi untuk ESP32-WROOM/S3, ESPHome, dan Z-Wave JS.

- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — pencadangan, peningkatan, dan pemulihan Ethernet lama untuk SLZB-06 asli; firmware inti dan radio merupakan sasaran terpisah.

### Alat ruang, pengamatan, dan akses

- **[home-studio](https://github.com/ha-homelab/home-studio)** — menggambar ruangan, menata furnitur, menjelajahi 3D, mengekspor proyek, dan mengompilasi penampil Home Assistant secara lokal.

- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — merekam, melabeli, dan membandingkan pengamatan dengan pemeriksaan kebaruan data dan jam yang eksplisit.

- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — pengamatan RuView melalui MQTT discovery, kebaruan per simpul, dan contoh pemutaran ulang sintetis.

- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — perkiraan area dari arah kamera yang hanya dibaca, sektor terkonfigurasi, dan pemeriksaan kebaruan data.

- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — sesi Cloudflare Access terverifikasi untuk dasbor eksternal dan token berumur pendek melalui gerbang terbatas. Memetakan satu administrator Home Assistant yang ditetapkan secara eksplisit dengan hak akses penuh.

Contoh pengamatan menjelaskan observasi dan batasnya. Pemutaran ulang sintetis dan arah kamera tidak membuktikan akurasi deteksi keberadaan di dunia nyata.

### Pengujian dan kontrak

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — rencana migrasi semantik luring yang membedakan peran perangkat dari perangkat kerasnya.

- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — pemeriksaan cakupan pengukuran, asal-usul, bukti kalibrasi, dan agregasi.

- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — skenario sintetis terbatas dalam mesin otomasi Home Assistant nyata yang terisolasi.

- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — bukti suara luring yang membedakan penyelesaian protokol, tindakan teramati, dan respons terdengar.

Ikuti [alur kerja dan hasil berilustrasi](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.id.md) atau [edisi Rusia](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md). Bukti perangkat lunak dan uji penerimaan fisik tetap merupakan langkah terpisah.

<details>
<summary>Alur peninjauan dan pemeriksaan perangkat lunak tercatat</summary>

![Empat alat komunitas dan batas uji penerimaan fisik yang terpisah](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.id.svg)

![Jumlah pengujian Linux bertanggal untuk empat alat, dengan catatan pengujian dilewati](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.id.svg)

Diagram mempertahankan [bukti panduan komunitas per 16 Oktober 2026 dan tautan eksekusi CI](https://github.com/ha-homelab/.github/blob/main/community-tools/README.id.md#validation-evidence--2026-10-16-utc). Panah adalah serah terima peninjauan. Jumlah tes merupakan bukti perangkat lunak dengan cakupan tertentu, bukan peringkat mutu, persentase cakupan, atau tolok ukur perangkat fisik.

</details>

## Lihat penggunaannya

<a href="https://ha-homelab.github.io/home-studio/planner/"><img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Editor peramban Home Studio menampilkan garasi, studio kreatif, dan teras fiktif dalam 3D" width="440" /></a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html"><img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Editor Home Studio menampilkan ruangan fiktif dengan furnitur, palet warna, dan pola permukaan" width="440" /></a>

**Home Studio:** tangkapan editor asli memakai denah fiktif — garasi/studio dan ruangan berperabot dengan pola. [Buka perencana](https://ha-homelab.github.io/home-studio/planner/) atau ikuti [panduan menggambar berilustrasi](https://ha-homelab.github.io/home-studio/planner/guide.html). Gambar: Home Studio contributors, MIT. [Sumber dan asal gambar](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Untuk tampilan proyek lain, jelajahi [arsitektur suara/musik/BLE EchoMuse](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md), [diagram pengawatan ZAC93](https://github.com/ha-homelab/zac93-esp32), dan [demonstrasi pemutaran ulang sintetis RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Potret proyek publik

![Grafik batang horizontal: perangkat dan jembatan 7; ruang, pengamatan, dan akses 5; suara dan media 4; tes dan kontrak 4; konfigurasi dan keandalan 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.id.svg)

**22 proyek + repositori profil ini = 23 repositori publik**, diperiksa pada 16 Oktober 2026. Setiap proyek masuk satu kategori editorial; jumlah tidak mengukur kematangan, pemakaian, atau kinerja. [Data sumber yang dapat direproduksi](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json). Untuk hasil pemeriksaan perangkat lunak sebenarnya, lihat [grafik tes alat komunitas bertanggal dan tautan eksekusi CI](https://github.com/ha-homelab/.github/blob/main/community-tools/README.id.md#validation-evidence--2026-10-16-utc) yang terpisah.

## Proyek publik terkait di luar organisasi ini

Proyek yang dipelihara secara terpisah ini melengkapi homelab. Semuanya komponen opsional, dengan pengaturan dan batas dukungan sendiri.

**Energi — [ekosistem Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) mengoordinasikan iklim melalui Home Assistant dan Venus OS, dengan mode pengamatan sebagai bawaan.

- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) menampilkan pembacaan sirkuit sebagai beban GX; [dbus-pump](https://github.com/victron-venus/dbus-pump) menjembatani entitas tangki, pompa, dan katup HA.

- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) menyediakan dasbor energi dengan antarmuka Vue dan perangkat Home Assistant opsional.

**Suara dan media — termasuk [ekosistem Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) adalah skill khusus Alexa hanya-baca; [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) mengirim video Cast dengan ucapan yang disintesis lokal. Keduanya bekerja tanpa konversi perangkat keras; Home Assistant opsional, dan skill Alexa tidak memerlukannya.

- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) mencari program XMLTV yang sedang tayang dan merutekan pemutaran melalui proksi HLS yang tersedia ke layar Alexa atau Google Cast.

- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) menyediakan perintah pemutar, kontrol terminal, dan penerapan k3s. Gerbang EPG tidak bergantung pada OttPlay.

**Infrastruktur yang dapat digunakan kembali**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) menawarkan konfigurasi acuan ESP32 untuk sensor baterai, suhu, dan tanaman.

- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) menghubungkan REST/WebSocket dan MQTT dengan autentikasi serta pembatasan topik.

- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) mengamati MQTT dan metrik Mosquitto melalui OpenTelemetry, Prometheus, dan Grafana; bukan proksi pesan.

- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) mengelola pengaturan GitHub dan repositori organisasi ini.

## Cara kami bekerja

Menjaga perilaku tetap dapat dipahami, perubahan dapat ditinjau, build dapat direproduksi, dan pemulihan terdokumentasi. Contoh serta tangkapan layar publik memakai data sintetis jika dinyatakan; kredensial rumah, rekaman, cadangan perangkat, dan ekspor operasional pribadi tetap di luar repositori ini. Setiap proyek mencatat apa yang diuji dan apa yang masih memerlukan verifikasi fisik.

Berkontribusilah melalui panduan repositori terkait; laporkan kerentanan melalui kebijakan keamanannya. Repositori ini juga menyimpan [logo asli dan catatan desain](https://github.com/ha-homelab/.github/blob/main/assets/README.md) kami.

---

Homelab independen yang dibangun dengan [Home Assistant](https://www.home-assistant.io/). Tidak berafiliasi dengan proyek Home Assistant atau produsen perangkat.

