<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: бірюзовий будинок зі з’єднаними мережевими вузлами" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Продуманий дім. Зрозуміла автоматизація.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Спробувати Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Переглянути конфігурацію</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.uk.md">Інструменти спільноти</a>
</p>

<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Ми створюємо придатні до повторного використання інтеграції Home Assistant,
голосові клієнти, мости для пристроїв, просторові інструменти та посібники
з розгортання. Публічні проєкти поєднують практичну домашню автоматизацію
з відтворюваними збірками, явними контрактами й документованим відновленням.
Почніть з одного проєкту: кожен має власний спосіб встановлення та підтримуване обладнання.

![Ролі проєктів HA Homelab: пристрої, голос, конфігурація, просторові інструменти й тести](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.uk.svg)

Карта групує пов’язані роботи. Вона не означає, що всі проєкти встановлюються
разом або автоматично інтегруються один з одним.

## Нове — жовтень 2026

- **Намалюйте та дослідіть дім у браузері.** [Home Studio](https://github.com/ha-homelab/home-studio) поєднує планувальник
  2D/3D, 195 моделей предметів, 24 мови редактора та локальний компілятор для
  переглядача, який можна встановити в Home Assistant.
  [Режим Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md) дає змогу досліджувати встановлений план, блокуючи команди пристроям.
- **Більше способів повторно використати обладнання.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse) додає
  документований шлях для голосу, музики та BLE на Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) описує міст Z-Wave. Наведені нижче проєкти RF, Zigbee і Tuya
  охоплюють інші сімейства пристроїв. Готовність обладнання залежить від проєкту:
  фізичне введення ZAC93 в експлуатацію ще попереду.
- **Публічна конфігурація та відновлення.** [Home Assistant](https://github.com/ha-homelab/home-assistant) тепер містить
  бібліотеки автоматизацій і скриптів для повторного використання та контракти
  інтеграцій; [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) публікує інструменти розгортання, резервного
  копіювання й відновлення. Один екземпляр із локальним сховищем не забезпечує автоматичного перемикання після відмови.
- **Спочатку докази, потім автоматизація.** Нові проєкти спостережень датчиків,
  напрямку камери та доступу доповнюють чотири [інструменти спільноти](https://github.com/ha-homelab/.github/blob/main/community-tools/README.uk.md) для
  міграцій сутностей, походження вимірювань, сценаріїв автоматизації та голосових результатів.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) тепер використовує одну адаптивну кнопку, зберігаючи явне підтвердження відмикання.

Це редакційний зріз станом на **16 жовтня 2026 року**. Актуальні сумісність і стан
шукайте в README та випусках кожного проєкту.

## Перегляньте проєкти

### Конфігурація та надійність

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — публічна конфігурація, включені автоматизації та
  скрипти, посібники з розгортання й контракти інтеграцій.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — переносний Home Assistant на k3s, оновлення після
  схвалення, перевірені резервні копії та інструменти відновлення.

### Голос і медіа

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 з EchoMuse/emOS, Assist, музикою, локальними
  домашніми інструментами й окремо зареєстрованим BLE-проксі. Задокументований
  шлях розпізнавання мовлення використовує хмарного постачальника й не є повністю автономним.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — перетворення Echo Dot 2 через EchoLocal з інструментами
  навчання слова активації та оцінювання в точному середовищі виконання.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — перетворення Echo Show 5 Gen2 на Android, перевірені
  резервні копії та налаштування Home Assistant Companion.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — повторно використовувані інструменти захоплення
  екрана LG webOS та інтеграція Home Assistant.

EchoLocal і EchoMuse — різні шляхи перетворення. Перш ніж змінювати пристрій,
прочитайте вимоги обраного проєкту до моделі та відновлення.

### Інтеграції, мости й відновлення пристроїв

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — неофіційна інтеграція хмари DESLOC для стану замка,
  керування, батареї та Wi-Fi; [сумісність залежить від моделі](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — окрема картка панелі з візуальним редактором,
  адаптивною дією та відмиканням із підтвердженням.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — шлюз ESPHome CC1101 для RF-спостережень через MQTT,
  нативного передавання ESPHome й автоматизації Home Assistant.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — прошивка кнопок Tuya для нативного керування
  групами Zigbee: коротке натискання перемикає, утримання вимикає;
  дивіться [поточні межі фізичної перевірки](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — перетворення старих розеток ESP8266, відтворювана
  станція Linux для прошивання та посібники з мосту Matter.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — ілюстрований проєкт мосту Zooz ZAC93 для ESP32-WROOM/S3,
  ESPHome і Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — резервне копіювання, оновлення та старі способи
  відновлення через Ethernet для оригінального SLZB-06; основна й радіопрошивка — окремі цілі.

### Простір, спостереження датчиків і доступ

- **[home-studio](https://github.com/ha-homelab/home-studio)** — малюйте кімнати, розставляйте меблі, досліджуйте в 3D,
  експортуйте проєкт і локально компілюйте переглядач Home Assistant.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — записуйте, позначайте й порівнюйте спостереження
  з явними перевірками актуальності та годинника.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — спостереження RuView через MQTT discovery,
  актуальність для кожного вузла та приклади синтетичного відтворення.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — оцінювання області за напрямком камери,
  який лише зчитується, налаштованими секторами й перевірками актуальності.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — перевірені сеанси Cloudflare Access для зовнішніх
  панелей і короткочасні токени через обмежений шлюз. Він зіставляє одного явно
  налаштованого адміністратора Home Assistant з повними привілеями.

Приклади датчиків описують спостереження та їхні межі. Синтетичне відтворення
й напрямок камери не доводять точності визначення присутності в реальному світі.

### Тести й контракти

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — автономні семантичні плани міграції, що
  відокремлюють роль пристрою від його обладнання.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — перевірки охоплення вимірювань, походження,
  доказів калібрування й агрегації.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — обмежені синтетичні сценарії в ізольованому
  справжньому рушії автоматизації Home Assistant.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — автономні голосові докази, що розрізняють
  завершення протоколу, спостережувану дію та чутну відповідь.

Ознайомтеся з [ілюстрованим процесом і результатами](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.uk.md) або його [російською версією](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md).
Програмні докази та фізичне приймання залишаються окремими етапами.

<details>
<summary>Процес перевірки й зафіксовані програмні тести</summary>

![Чотири інструменти спільноти та межа окремого фізичного приймання](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.uk.svg)

![Датовані кількості тестів Linux чотирьох інструментів з окремими примітками про пропуски](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.uk.svg)

Діаграми зберігають [докази від 16 жовтня 2026 року й пов’язані запуски CI з посібника спільноти](https://github.com/ha-homelab/.github/blob/main/community-tools/README.uk.md#validation-evidence--2026-10-16-utc).
Стрілки означають передавання на перевірку. Кількість тестів — це програмні докази
з визначеним охопленням, а не рейтинг якості, відсоток покриття чи порівняння фізичних пристроїв.

</details>

## Подивіться у використанні

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Браузерний редактор Home Studio з вигаданими гаражем, творчою студією та патіо в 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Редактор Home Studio з вигаданою кімнатою, меблями, палітрами й візерунками поверхонь" width="440" />
</a>

**Home Studio:** справжні знімки редактора з вигаданими планами — гаражем зі
студією та мебльованою кімнатою з візерунками. [Відкрийте планувальник](https://ha-homelab.github.io/home-studio/planner/) або
скористайтеся [ілюстрованим посібником із малювання](https://ha-homelab.github.io/home-studio/planner/guide.html). Зображення: учасники Home Studio, MIT.
[Джерела й походження зображень](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Інші види проєктів: [архітектура голосу, музики та BLE в EchoMuse](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
[схеми з’єднання ZAC93](https://github.com/ha-homelab/zac93-esp32) і [демонстрація синтетичного відтворення RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Зріз публічних проєктів

![Смугова діаграма: пристрої й мости 7; простір, датчики та доступ 5; голос і медіа 4; тести й контракти 4; конфігурація та надійність 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.uk.svg)

**22 проєкти + репозиторій цього профілю = 23 публічні репозиторії**, перевірено
16 жовтня 2026 року. Кожен проєкт має одну редакційну категорію; кількості не
вимірюють зрілість, використання чи продуктивність. [Відтворювані вихідні дані](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Фактичні результати програмних перевірок наведені в окремій
[датованій діаграмі тестів спільноти з посиланнями на CI](https://github.com/ha-homelab/.github/blob/main/community-tools/README.uk.md#validation-evidence--2026-10-16-utc).

## Пов’язані публічні проєкти поза цією організацією

Ці проєкти з окремим супроводом доповнюють homelab. Вони є необов’язковими
компонентами з власним налаштуванням і межами підтримки.

**Енергія — [екосистема Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) координує клімат через Home Assistant і Venus OS,
  типово лише спостерігаючи.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) представляє показники контурів як навантаження GX;
  [dbus-pump](https://github.com/victron-venus/dbus-pump) з’єднує сутності HA резервуара, насоса й клапана.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) надає енергетичну панель з інтерфейсом Vue
  та необов’язковими пристроями Home Assistant.

**Голос і медіа — включно з [екосистемою Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) — власна навичка Alexa лише для читання;
  [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) надсилає Cast-відео з локально синтезованим мовленням.
  Вони працюють без перетворення обладнання; Home Assistant необов’язковий, а навичка Alexa його не потребує.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) знаходить поточні програми XMLTV та спрямовує відтворення
  через наявний HLS-проксі на екрани Alexa або Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) надає команди програвача, термінальне керування
  та розгортання на k3s. Шлюз EPG не залежить від OttPlay.

**Інфраструктура для повторного використання**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) пропонує еталонні конфігурації ESP32
  для датчиків батареї, температури й рослин.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) поєднує REST/WebSocket і MQTT з автентифікацією
  та обмеженнями тем.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) спостерігає за метриками MQTT і Mosquitto через
  OpenTelemetry, Prometheus і Grafana; це не проксі повідомлень.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) керує налаштуваннями GitHub і репозиторіями цієї організації.

## Як ми працюємо

Поведінка має бути зрозумілою, зміни — придатними до перевірки, збірки —
відтворюваними, відновлення — документованим. Публічні приклади й знімки
використовують синтетичні дані там, де це зазначено; домашні облікові дані,
записи, резервні копії пристроїв і приватні операційні експорти залишаються
поза репозиторіями. Кожен проєкт описує, що перевірено та що ще потребує фізичної перевірки.

Робіть внески за посібником відповідного репозиторію; повідомляйте про вразливості
через його політику безпеки. Цей репозиторій також містить наші
[оригінальний логотип і нотатки щодо дизайну](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Незалежний homelab на основі [Home Assistant](https://www.home-assistant.io/).
Не пов’язаний із проєктом Home Assistant або виробниками пристроїв.
