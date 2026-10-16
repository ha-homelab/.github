<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab: una casa turquesa con nodos de red conectados" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Un hogar bien pensado. Una automatización comprensible.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Probar Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Explorar la configuración</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.es.md">Herramientas de la comunidad</a>
</p>
<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Creamos integraciones reutilizables de Home Assistant, clientes de voz, puentes
para dispositivos, herramientas espaciales y guías de despliegue. Los proyectos
públicos combinan la domótica práctica con compilaciones reproducibles, contratos
explícitos y procedimientos de recuperación documentados. Empieza por un proyecto;
cada uno tiene su propio proceso de instalación y su hardware compatible.

![Mapa de funciones de los proyectos de HA Homelab: dispositivos, voz, configuración, herramientas espaciales y pruebas](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.es.svg)

El mapa agrupa trabajos relacionados. No implica que todos los proyectos se
instalen juntos ni que se integren automáticamente entre sí.

## Novedades — octubre de 2026

- **Dibuja y explora un hogar en el navegador.** [Home Studio](https://github.com/ha-homelab/home-studio)
  combina un planificador 2D/3D, 195 diseños de objetos, 24 idiomas del editor y un
  compilador local para un visor instalable en Home Assistant. Su
  [modo Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md)
  permite explorar el plano instalado mientras bloquea los comandos a dispositivos.
- **Más formas de reutilizar el hardware existente.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse)
  añade una opción documentada de voz, música y BLE para Echo Dot 2;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) documenta un puente Z-Wave;
  los proyectos de RF, Zigbee y Tuya que aparecen más abajo cubren otras familias
  de dispositivos. El estado de preparación depende del proyecto: la puesta en
  servicio física del ZAC93 sigue pendiente.
- **Configuración pública y recuperación.** [Home Assistant](https://github.com/ha-homelab/home-assistant)
  incluye ahora bibliotecas reutilizables de automatizaciones y scripts, además de
  contratos de integración; [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing)
  publica herramientas de despliegue, copia de seguridad y recuperación. Una sola
  instancia con almacenamiento local no proporciona conmutación automática ante fallos.
- **Evidencias antes de automatizar.** Los nuevos proyectos de observación, dirección
  de cámara por estancia y acceso acompañan a cuatro
  [herramientas de la comunidad](https://github.com/ha-homelab/.github/blob/main/community-tools/README.es.md)
  para migraciones de entidades, procedencia de mediciones, escenarios de
  automatización y resultados de voz.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) utiliza ahora un único
  botón de acción adaptable y mantiene la confirmación explícita de desbloqueo.

Esta es una instantánea editorial del **16 de octubre de 2026**. Consulta el README
y las versiones de cada proyecto para conocer su compatibilidad y estado actuales.

## Explora los proyectos

### Configuración y fiabilidad

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — configuración pública,
  automatizaciones y scripts incluidos, guías de despliegue y contratos de integración.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — Home Assistant
  portátil sobre k3s, actualizaciones sujetas a aprobación, copias de seguridad
  verificadas y herramientas de recuperación.

### Voz y multimedia

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 con EchoMuse/emOS,
  Assist, música, herramientas locales del hogar y un proxy BLE registrado por separado.
  La ruta de reconocimiento de voz documentada utiliza un proveedor en la nube;
  no funciona completamente sin conexión.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — conversión de Echo Dot 2
  con EchoLocal, herramientas de entrenamiento de la palabra de activación y
  evaluación en el entorno de ejecución exacto.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — conversión de Echo
  Show 5 Gen2 a Android, copias de seguridad verificadas y configuración de
  Home Assistant Companion.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — herramientas
  reutilizables de captura de pantalla de LG webOS e integración con Home Assistant.

EchoLocal y EchoMuse son vías de conversión distintas. Antes de modificar un
dispositivo, lee los requisitos de modelo y recuperación del proyecto elegido.

### Integraciones de dispositivos, puentes y recuperación

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — integración no oficial con
  la nube de DESLOC para estado de cerraduras, controles, batería y Wi-Fi;
  [la compatibilidad varía según el modelo](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — tarjeta de panel
  independiente con editor visual, acción adaptable y controles de desbloqueo con confirmación.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — pasarela ESPHome CC1101
  para observaciones RF por MQTT, transmisión nativa de ESPHome y automatización en Home Assistant.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — firmware
  para botones Tuya con control nativo de grupos Zigbee, conmutación por pulsación
  corta y apagado por pulsación prolongada; consulta sus
  [límites actuales de validación física](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — conversión de
  enchufes ESP8266 antiguos, una estación Linux reproducible para grabar firmware
  y guías de puentes Matter.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — diseño ilustrado de un
  puente Zooz ZAC93 para ESP32-WROOM/S3, ESPHome y Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — copias de
  seguridad, actualización y recuperación de Ethernet antiguo para el SLZB-06
  original; el firmware principal y el de radio son destinos independientes.

### Herramientas espaciales, observación y acceso

- **[home-studio](https://github.com/ha-homelab/home-studio)** — dibuja estancias,
  amuéblalas, explóralas en 3D, exporta tu proyecto y compila localmente un visor
  para Home Assistant.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — registra,
  etiqueta y compara observaciones con comprobaciones explícitas de vigencia y reloj.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** —
  observaciones RuView mediante descubrimiento MQTT, vigencia por nodo y ejemplos
  de reproducción sintética.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** —
  estimaciones de área a partir de la dirección de cámara en modo de solo lectura,
  sectores configurados y comprobaciones de vigencia.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — sesiones
  verificadas de Cloudflare Access para paneles externos y tokens de corta duración
  mediante una pasarela restringida. Asocia un único administrador de Home Assistant
  configurado explícitamente y con todos los privilegios.

Los ejemplos de observación describen las observaciones y sus límites. La
reproducción sintética y la dirección de cámara no demuestran la precisión real
de la detección de ocupación.

### Pruebas y contratos

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — planes
  de migración semántica sin conexión que distinguen el rol de un dispositivo de su hardware.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — comprobaciones
  del alcance de las mediciones, su procedencia, las evidencias de calibración y la agregación.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — escenarios
  sintéticos acotados que se ejecutan en un motor real y aislado de automatización
  de Home Assistant.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — evidencias
  de voz evaluadas sin conexión que distinguen la finalización del protocolo,
  la acción observada y la respuesta audible.

Sigue el [proceso ilustrado y sus resultados](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.es.md)
o su [edición rusa](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md).
Las evidencias de software y la aceptación física siguen siendo pasos separados.

<details>
<summary>Proceso de revisión y comprobaciones de software registradas</summary>

![Cuatro herramientas de la comunidad y el límite separado de aceptación física](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.es.svg)

![Recuentos de pruebas Linux de las cuatro herramientas en una fecha concreta, con notas separadas de omisión](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.es.svg)

Estos diagramas conservan las [evidencias del 16 de octubre de 2026 y las ejecuciones de CI enlazadas de la guía comunitaria](https://github.com/ha-homelab/.github/blob/main/community-tools/README.es.md#validation-evidence--2026-10-16-utc).
Las flechas representan pasos de revisión. Los recuentos son evidencias de software
con un alcance definido, no una clasificación de calidad, un porcentaje de cobertura
ni una comparativa de dispositivos físicos.

</details>

## Mira cómo se utiliza

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Editor de Home Studio en el navegador con un garaje, un estudio creativo y un patio ficticios en 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Editor de Home Studio con una estancia ficticia, muebles, paletas de colores y patrones de superficies" width="440" />
</a>

**Home Studio:** capturas reales del editor con planos ficticios: un garaje/estudio
y una estancia amueblada con patrones. [Abre el planificador](https://ha-homelab.github.io/home-studio/planner/)
o sigue la [guía ilustrada de dibujo](https://ha-homelab.github.io/home-studio/planner/guide.html).
Imágenes: colaboradores de Home Studio, MIT.
[Fuentes y procedencia de las imágenes](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Para ver otros proyectos, explora la [arquitectura de voz/música/BLE de EchoMuse](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
los [diagramas de cableado del ZAC93](https://github.com/ha-homelab/zac93-esp32)
y la [demostración de reproducción sintética de RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Instantánea de los proyectos públicos

![Gráfico de barras horizontales: dispositivos y puentes 7; herramientas espaciales, observación y acceso 5; voz y multimedia 4; pruebas y contratos 4; configuración y fiabilidad 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.es.svg)

**22 proyectos + este repositorio de perfil = 23 repositorios públicos**, comprobados
el 16 de octubre de 2026. Cada proyecto tiene una categoría editorial; los recuentos
no miden madurez, uso ni rendimiento.
[Datos de origen reproducibles](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Para consultar los resultados reales de las comprobaciones de software, ve al
[gráfico de pruebas de las herramientas comunitarias, fechado y con enlaces a CI](https://github.com/ha-homelab/.github/blob/main/community-tools/README.es.md#validation-evidence--2026-10-16-utc).

## Proyectos públicos relacionados fuera de esta organización

Estos proyectos, mantenidos por separado, complementan el laboratorio doméstico.
Son componentes opcionales, con sus propios procesos de configuración y límites de soporte.

**Energía — [ecosistema Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) coordina el clima
  mediante Home Assistant y Venus OS, con observación por defecto.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) expone las lecturas
  de circuitos como cargas GX; [dbus-pump](https://github.com/victron-venus/dbus-pump)
  conecta las entidades de HA de depósitos, bombas y válvulas.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) ofrece
  un panel de energía con interfaz Vue y dispositivos opcionales de Home Assistant.

**Voz y multimedia — incluido el [ecosistema Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) es una skill
  personalizada de Alexa de solo lectura;
  [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats) envía
  vídeo por Cast con voz sintetizada localmente. Funcionan sin modificar el hardware;
  Home Assistant es opcional y la skill de Alexa no lo requiere.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) busca programas XMLTV
  en emisión y dirige su reproducción mediante un proxy HLS existente a pantallas
  Alexa o Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server)
  ofrece comandos para el reproductor, control desde terminal y despliegue en k3s.
  La pasarela EPG no depende de OttPlay.

**Infraestructura reutilizable**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns)
  ofrece configuraciones de referencia ESP32 para sensores de batería, temperatura y plantas.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) conecta
  REST/WebSocket y MQTT con autenticación y restricciones de temas.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry)
  observa MQTT y las métricas de Mosquitto mediante OpenTelemetry, Prometheus y
  Grafana; no es un proxy de mensajes.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) gestiona
  la configuración de GitHub y los repositorios de esta organización.

## Cómo trabajamos

Mantenemos un comportamiento comprensible, cambios revisables, compilaciones
reproducibles y recuperación documentada. Los ejemplos públicos y las capturas
utilizan datos sintéticos cuando así se indica; las credenciales del hogar,
grabaciones, copias de seguridad de dispositivos y exportaciones operativas
privadas quedan fuera de estos repositorios. Cada proyecto documenta qué se ha
probado y qué sigue necesitando verificación física.

Contribuye siguiendo la guía del repositorio correspondiente; informa de
vulnerabilidades mediante su política de seguridad. Este repositorio también
contiene nuestro [logotipo original y notas de diseño](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Un laboratorio doméstico independiente construido con [Home Assistant](https://www.home-assistant.io/).
Sin afiliación con el proyecto Home Assistant ni con los fabricantes de dispositivos.
