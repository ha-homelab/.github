<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: бирюзовый дом с сетевыми узлами" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Продуманный дом. Понятная автоматизация.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Попробовать Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Конфигурация Home Assistant</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.ru.md">Инструменты сообщества</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md">English</a>
</p>

Мы создаём интеграции Home Assistant, голосовые клиенты, мосты для устройств,
инструменты планировки и руководства по развёртыванию. Практическую домашнюю
автоматизацию дополняют воспроизводимые сборки, явные контракты и инструкции
по восстановлению. Можно начать с одного проекта: у каждого свой способ
установки и перечень поддерживаемого оборудования.

![Карта ролей проектов HA Homelab: устройства, голос, конфигурация, пространство и тестирование](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.ru.svg)

Карта объединяет близкие темы. Она не означает, что все проекты устанавливаются
вместе или автоматически интегрируются друг с другом.

## Новое — октябрь 2026

- **Планировка дома в браузере.** [Home Studio](https://github.com/ha-homelab/home-studio)
  объединяет редактор 2D/3D, 195 дизайнов предметов, 24 языка интерфейса и локальный
  компилятор для установки плана в Home Assistant.
  [Режим Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md)
  позволяет изучать установленный план, блокируя команды устройствам.
- **Повторное использование оборудования.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse)
  добавляет путь для голоса, музыки и BLE на Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) описывает мост Z-Wave;
  проекты RF, Zigbee и Tuya охватывают другие семейства устройств. Готовность
  проверяется отдельно: физическая сборка ZAC93 ещё ожидает ввода в эксплуатацию.
- **Публичная конфигурация и восстановление.** [Home Assistant](https://github.com/ha-homelab/home-assistant)
  включает библиотеки автоматизаций и скриптов, а также контракты интеграций;
  [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) публикует инструменты
  развёртывания, резервного копирования и восстановления. Один экземпляр
  с локальным хранилищем не обеспечивает автоматический failover.
- **Доказательства перед автоматизацией.** Проекты наблюдений, определения направления
  камеры и доступа дополняют четыре [инструмента сообщества](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ru.md)
  для миграций сущностей, происхождения измерений, сценариев автоматизации и голосовых результатов.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) теперь использует одну
  адаптивную кнопку действия, сохраняя явное подтверждение отпирания.

Это редакционный срез на **16 октября 2026 года**. Актуальную совместимость
и состояние ищите в README и релизах соответствующего проекта.

## Каталог проектов

### Конфигурация и надёжность

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — публичная конфигурация,
  библиотеки автоматизаций и скриптов, развёртывание и контракты интеграций.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — Home Assistant
  на k3s, обновления с подтверждением, проверенные резервные копии и восстановление.

### Голос и медиа

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 с EchoMuse/emOS,
  Assist, музыка, локальные инструменты управления домом и отдельно подключаемый BLE-прокси.
  В зафиксированной конфигурации распознавание речи облачное: весь тракт не является офлайн.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — путь EchoLocal для Echo Dot 2,
  обучение ключевой фразы и проверка на целевой среде исполнения.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — установка Android
  на Echo Show 5 Gen2, проверка резервных копий и настройка Home Assistant Companion.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — захват экрана
  LG webOS и интеграция с Home Assistant.

EchoLocal и EchoMuse — разные пути переделки. Перед изменением устройства
прочитайте требования выбранного проекта к модели и восстановлению.

### Интеграции устройств, мосты и восстановление

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — неофициальная облачная интеграция
  DESLOC: состояние, управление, батарея и Wi-Fi; [возможности зависят от модели](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — отдельная карточка
  с визуальным редактором, адаптивным действием и подтверждением отпирания.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — шлюз ESPHome CC1101:
  наблюдения RF через MQTT, передача через нативный API ESPHome и автоматизация в Home Assistant.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — прошивка
  кнопки Tuya для прямого управления группой Zigbee: переключение коротким нажатием
  и выключение удержанием; см. [границы проверки на оборудовании](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — переделка старых розеток
  ESP8266, воспроизводимая станция прошивки Linux и руководства по мосту Matter.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — иллюстрированный проект
  моста Zooz ZAC93 для ESP32-WROOM/S3, ESPHome и Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — резервное копирование,
  обновление и восстановление исходного SLZB-06 через Ethernet;
  основная и радиопрошивка обновляются отдельно.

### Пространство, наблюдения и доступ

- **[home-studio](https://github.com/ha-homelab/home-studio)** — рисование комнат,
  расстановка мебели, просмотр 3D, экспорт проекта и локальная сборка плана для Home Assistant.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — запись,
  разметка и сравнение наблюдений с проверкой свежести данных и часов.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — наблюдения
  RuView через MQTT discovery, свежесть по узлам и синтетические примеры воспроизведения.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — оценка
  зоны по направлению камеры, заданным секторам и свежести данных; доступ только на чтение.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — проверенные сессии
  Cloudflare Access для внешних панелей, короткоживущие токены и ограниченный шлюз.
  Используется один явно настроенный администратор Home Assistant с полными правами.

Примеры описывают наблюдения и их ограничения. Синтетическое воспроизведение
и направление камеры не доказывают точность определения присутствия в реальном доме.

### Тестирование и контракты

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — офлайн-планы
  семантических миграций, отделяющие роль устройства от оборудования.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — область измерения,
  происхождение данных, доказательства калибровки и правила суммирования.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — ограниченные
  синтетические сценарии в изолированном настоящем движке автоматизации Home Assistant.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — офлайн-анализ
  голосовых свидетельств: завершение протокола, наблюдаемое действие и слышимый ответ.

Изучите [иллюстрированный процесс и результаты](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md)
или [английскую версию](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.md).
Программные проверки и приёмка физического оборудования остаются отдельными этапами.

<details>
<summary>Процесс проверки и результаты программных тестов</summary>

![Четыре инструмента сообщества и отдельная граница физической приёмки](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.ru.svg)

![Количество проверок Linux для четырёх инструментов, с отдельными пояснениями пропусков](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.ru.svg)

Иллюстрации сохраняют [результаты и ссылки на CI из руководства на 16 октября 2026 года](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ru.md).
Стрелки обозначают этапы рассмотрения. Числа тестов отражают конкретные программные
проверки, а не рейтинг качества, процент покрытия или испытания физических устройств.

</details>

## Как это выглядит

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Редактор Home Studio: вымышленный гараж, творческая студия и патио в 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Редактор Home Studio: вымышленная комната с мебелью, палитрами и узорами поверхностей" width="440" />
</a>

**Home Studio:** настоящие скриншоты редактора с вымышленными планами — гараж/студия
и комната с мебелью и узорами. [Открыть редактор](https://ha-homelab.github.io/home-studio/planner/)
или [руководство по рисованию](https://ha-homelab.github.io/home-studio/planner/guide.html).
Авторы изображений: Home Studio contributors, MIT. [Источники изображений](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Другие примеры: [архитектура голоса, музыки и BLE EchoMuse](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
[схемы подключения ZAC93](https://github.com/ha-homelab/zac93-esp32)
и [синтетическое демо RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Срез публичного каталога

![График: устройства и мосты — 7; пространство, наблюдения и доступ — 5; голос и медиа — 4; тесты и контракты — 4; конфигурация — 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.ru.svg)

**22 проекта + репозиторий профиля = 23 публичных репозитория**, проверено
16 октября 2026 года. Каждый проект отнесён к одному направлению;
числа не измеряют зрелость, популярность или производительность.
[Исходные данные](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Результаты программных проверок показаны отдельно:
[датированный график тестов и ссылки на запуски CI](https://github.com/ha-homelab/.github/blob/main/community-tools/README.ru.md).

## Связанные публичные проекты вне организации

Это отдельные проекты со своими настройками и границами поддержки.
Их можно использовать как дополнительные компоненты.

**Энергетика — [экосистема Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) координирует климат
  через Home Assistant и Venus OS; по умолчанию работает в режиме наблюдения.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) представляет показания
  цепей как нагрузки GX; [dbus-pump](https://github.com/victron-venus/dbus-pump)
  связывает сущности баков, насосов и клапанов HA с Venus OS.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) — энергетическая
  панель с интерфейсом Vue и необязательным подключением устройств Home Assistant.

**Голос и медиа — включая [экосистему Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) — Alexa custom skill
  только для чтения; [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats)
  отправляет Cast-видео с локально синтезированной речью. Переделка оборудования не нужна;
  Home Assistant необязателен, а Alexa skill не требует его установки.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) находит текущие программы XMLTV
  и направляет воспроизведение через существующий HLS-прокси на экраны Alexa или Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) — команды
  проигрывателям, управление из терминала и развёртывание на k3s. EPG gateway не зависит от OttPlay.

**Повторно используемая инфраструктура**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) — примеры
  ESP32 для батарей, температурных и растительных BLE-датчиков.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) связывает REST/WebSocket
  и MQTT с аутентификацией и ограничением тем.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) наблюдает MQTT
  и метрики Mosquitto через OpenTelemetry, Prometheus и Grafana; это не прокси сообщений.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) управляет
  настройками и репозиториями нашей GitHub-организации.

## Как мы работаем

Понятное поведение, обозримые изменения, воспроизводимые сборки и документированное
восстановление. Где указано, публичные примеры и скриншоты используют синтетические
данные; домашние учётные данные, записи, резервные копии устройств и приватные
экспорты остаются за пределами этих репозиториев. Каждый проект объясняет,
что проверено и чему ещё нужна физическая проверка.

Предлагайте изменения через руководство соответствующего репозитория;
об уязвимостях сообщайте по его политике безопасности. Здесь также хранятся
[наш логотип и описание дизайна](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Независимый homelab на основе [Home Assistant](https://www.home-assistant.io/).
Мы не связаны с проектом Home Assistant или производителями устройств.
