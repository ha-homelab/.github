<p align="center">
  <img src="https://raw.githubusercontent.com/ha-homelab/.github/main/assets/ha-homelab-logo.png" alt="HA Homelab : une maison turquoise avec des nœuds réseau reliés" width="144" />
</p>

<h1 align="center">HA Homelab</h1>
<p align="center"><strong>Une maison bien pensée. Une automatisation compréhensible.</strong></p>
<p align="center">
  <a href="https://ha-homelab.github.io/home-studio/planner/">Essayer Home Studio</a> ·
  <a href="https://github.com/ha-homelab/home-assistant">Explorer la configuration</a> ·
  <a href="https://github.com/ha-homelab/.github/blob/main/community-tools/README.fr.md">Outils communautaires</a>
</p>
<!-- language-navigation:start -->
<p dir="ltr" align="center">
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.md" lang="en" dir="ltr">English</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.es.md" lang="es" dir="ltr">Español</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.he.md" lang="he" dir="rtl">עברית</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="https://github.com/ha-homelab/.github/blob/main/profile/README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="https://github.com/ha-homelab/.github/blob/main/profile/README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Nous créons des intégrations Home Assistant réutilisables, des clients vocaux,
des passerelles pour appareils, des outils de planification spatiale et des guides
de déploiement. Les projets publics associent la domotique pratique à des builds
reproductibles, des contrats explicites et une restauration documentée.
Commencez par un projet : chacun précise son installation et le matériel pris en charge.

![Rôles des projets HA Homelab : appareils, voix, configuration, outils spatiaux et tests](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/ecosystem.fr.svg)

Cette carte regroupe les travaux apparentés. Elle ne signifie pas que tous les
projets s'installent ensemble ou s'intègrent automatiquement les uns aux autres.

## Nouveautés — octobre 2026

- **Dessiner et explorer une maison dans le navigateur.** [Home Studio](https://github.com/ha-homelab/home-studio)
  associe un éditeur 2D/3D, 195 modèles d'objets, 24 langues d'interface et un
  compilateur local produisant une visionneuse installable dans Home Assistant.
  Son [mode Dry run](https://github.com/ha-homelab/home-studio/blob/main/docs/dry-run.md)
  permet d'explorer le plan installé tout en bloquant les commandes aux appareils.
  Le [guide de première utilisation](https://github.com/ha-homelab/home-studio/blob/main/docs/first-session.md) explique comment partir des exemples, récupérer un brouillon et préserver son travail lorsque la 3D n'est pas disponible.
- **D'autres façons de réutiliser le matériel existant.** [EchoMuse](https://github.com/ha-homelab/ha-echomuse)
  documente la voix, la musique et le BLE sur Echo Dot 2 ;
  [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) décrit une passerelle Z-Wave.
  Les projets RF, Zigbee et Tuya ci-dessous couvrent d'autres familles d'appareils.
  La maturité matérielle varie selon le projet : la mise en service physique du ZAC93 reste à faire.
- **Configuration publique et restauration.** [Home Assistant](https://github.com/ha-homelab/home-assistant)
  inclut désormais des bibliothèques réutilisables d'automatisations et de scripts,
  ainsi que des contrats d'intégration ;
  [k3s self-healing](https://github.com/ha-homelab/k3s-self-healing) publie des outils
  de déploiement, de sauvegarde et de restauration. Une seule instance avec un
  stockage local n'assure pas un basculement automatique.
- **Des preuves avant l'automatisation.** Les nouveaux projets d'observation, de
  direction de caméra et d'accès accompagnent quatre
  [outils communautaires](https://github.com/ha-homelab/.github/blob/main/community-tools/README.fr.md)
  consacrés aux migrations d'entités, à la provenance des mesures, aux scénarios
  d'automatisation et aux résultats vocaux.
  [DESLOC Lock Card](https://github.com/ha-homelab/ha-desloc-card) utilise désormais
  un seul bouton d'action adaptatif et conserve une confirmation explicite du déverrouillage.

Cet aperçu éditorial est daté du **16 octobre 2026**. Consultez le README et les
versions de chaque projet pour connaître sa compatibilité et son état actuels.

## Explorer les projets

### Configuration et fiabilité

- **[home-assistant](https://github.com/ha-homelab/home-assistant)** — configuration publique,
  automatisations et scripts inclus, conseils de déploiement et contrats d'intégration.
- **[k3s-self-healing](https://github.com/ha-homelab/k3s-self-healing)** — Home Assistant portable
  sur k3s, mises à jour soumises à approbation, sauvegardes vérifiées et outils de restauration.

### Voix et médias

- **[ha-echomuse](https://github.com/ha-homelab/ha-echomuse)** — Echo Dot 2 avec EchoMuse/emOS,
  Assist, musique, outils domotiques locaux et proxy BLE enregistré séparément.
  La reconnaissance vocale documentée utilise un fournisseur cloud ; le trajet n'est pas entièrement hors ligne.
- **[ha-echo-dot](https://github.com/ha-homelab/ha-echo-dot)** — conversion EchoLocal
  pour Echo Dot 2, avec entraînement du mot d'activation et évaluation dans l'environnement d'exécution exact.
- **[ha-echo-show-5](https://github.com/ha-homelab/ha-echo-show-5)** — conversion de l'Echo Show 5 Gen2
  vers Android, sauvegardes vérifiées et configuration de Home Assistant Companion.
- **[ha-lg-tv-capture](https://github.com/ha-homelab/ha-lg-tv-capture)** — outils réutilisables
  de capture d'écran LG webOS et intégration à Home Assistant.

EchoLocal et EchoMuse sont deux voies de conversion distinctes. Avant de modifier
un appareil, lisez les exigences du projet choisi concernant le modèle et la restauration.

### Intégrations d'appareils, passerelles et restauration

- **[ha-radio-hub](https://github.com/ha-homelab/ha-radio-hub)** — prototype PoE modulaire pour Zigbee, Thread, Bluetooth, Z-Wave, 433 MHz et la détection ; comprend les fichiers de CAO, le firmware et les outils de déploiement ; validation physique en attente.

- **[ha-desloc](https://github.com/ha-homelab/ha-desloc)** — intégration cloud DESLOC non officielle
  pour l'état des serrures, les commandes, la batterie et le Wi-Fi ;
  [la compatibilité varie selon le modèle](https://github.com/ha-homelab/ha-desloc/blob/main/docs/compatibility.md).
- **[ha-desloc-card](https://github.com/ha-homelab/ha-desloc-card)** — carte de tableau de bord
  distincte avec éditeur visuel, action adaptative et confirmation du déverrouillage.
- **[rf-airbridge](https://github.com/ha-homelab/rf-airbridge)** — passerelle ESPHome CC1101
  pour les observations RF via MQTT, l'émission native ESPHome et l'automatisation Home Assistant.
- **[zigbee-direct-button](https://github.com/ha-homelab/zigbee-direct-button)** — micrologiciel
  de bouton Tuya pour commander directement un groupe Zigbee : basculement par appui bref,
  extinction par appui long ; voir les
  [limites actuelles de validation physique](https://github.com/ha-homelab/zigbee-direct-button/blob/main/docs/validation.md).
- **[ha-tuya-esphome](https://github.com/ha-homelab/ha-tuya-esphome)** — conversion d'anciennes
  prises ESP8266, station de flash Linux reproductible et guides de passerelle Matter.
- **[zac93-esp32](https://github.com/ha-homelab/zac93-esp32)** — conception illustrée d'une
  passerelle Zooz ZAC93 avec ESP32-WROOM/S3, ESPHome et Z-Wave JS.
- **[slzb-06-recovery](https://github.com/ha-homelab/slzb-06-recovery)** — sauvegarde, mise à jour
  et restauration Ethernet historique du SLZB-06 original ; les micrologiciels du cœur
  et de la radio sont des cibles distinctes.

### Outils spatiaux, observations et accès

- **[home-studio](https://github.com/ha-homelab/home-studio)** — dessiner et meubler des pièces,
  explorer en 3D, exporter son projet et compiler localement une visionneuse Home Assistant.
- **[sensing-evidence-kit](https://github.com/ha-homelab/sensing-evidence-kit)** — enregistrer,
  annoter et comparer des observations avec vérification explicite de leur fraîcheur et des horloges.
- **[ruview-home-assistant](https://github.com/ha-homelab/ruview-home-assistant)** — observations
  RuView via MQTT discovery, fraîcheur par nœud et exemples de rejeu synthétique.
- **[ha-onvif-room-direction](https://github.com/ha-homelab/ha-onvif-room-direction)** — estimation
  de zone à partir de la direction de caméra lue sans modification, de secteurs configurés
  et de vérifications de fraîcheur.
- **[ha-access-session](https://github.com/ha-homelab/ha-access-session)** — sessions Cloudflare Access
  vérifiées pour des tableaux de bord externes et jetons de courte durée via une passerelle
  restreinte. Un seul administrateur Home Assistant, explicitement configuré, est associé avec tous ses privilèges.

Les exemples décrivent les observations et leurs limites. Un rejeu synthétique et
la direction d'une caméra ne prouvent pas la précision de détection d'occupation en conditions réelles.

### Tests et contrats

- **[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations)** — plans hors ligne
  de migration sémantique distinguant le rôle d'un appareil de son matériel.
- **[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts)** — vérification du
  périmètre de mesure, de la provenance, des preuves d'étalonnage et de l'agrégation.
- **[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests)** — scénarios synthétiques
  bornés exécutés dans un véritable moteur d'automatisation Home Assistant isolé.
- **[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab)** — preuves vocales
  hors ligne distinguant la fin du protocole, l'action observée et la réponse audible.

Suivez le [processus illustré et ses résultats](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.fr.md)
ou sa [version russe](https://github.com/ha-homelab/.github/blob/main/community-tools/process-and-results.ru.md).
Les preuves logicielles et la réception physique restent des étapes distinctes.

<details>
<summary>Processus de revue et vérifications logicielles enregistrées</summary>

![Quatre outils communautaires et la limite distincte de réception physique](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/architecture.fr.svg)

![Nombre daté de tests Linux pour les quatre outils, avec explication séparée des tests ignorés](https://raw.githubusercontent.com/ha-homelab/.github/main/community-tools/validation.fr.svg)

Ces schémas conservent les [preuves du 16 octobre 2026 et les liens CI du guide communautaire](https://github.com/ha-homelab/.github/blob/main/community-tools/README.fr.md#validation-evidence--2026-10-16-utc).
Les flèches représentent des transmissions lors de la revue. Le nombre de tests
constitue une preuve logicielle limitée à son périmètre, pas un classement de qualité,
un pourcentage de couverture ni une mesure comparative d'appareils physiques.

</details>

## Voir les outils en action

<a href="https://ha-homelab.github.io/home-studio/planner/">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/09-garage-studio.jpg" alt="Éditeur Home Studio dans le navigateur : garage, atelier créatif et patio fictifs en 3D" width="440" />
</a>
<a href="https://github.com/ha-homelab/home-studio/blob/1da65687bb5471628799873b32789813457c7085/planner/guide.html">
  <img src="https://raw.githubusercontent.com/ha-homelab/home-studio/1da65687bb5471628799873b32789813457c7085/planner/guide-assets/11-pattern-studio.jpg" alt="Éditeur Home Studio : pièce fictive avec meubles, palettes de couleurs et motifs de surface" width="440" />
</a>

**Home Studio :** véritables captures de l'éditeur utilisant des plans fictifs —
un garage/atelier et une pièce meublée avec des motifs.
[Ouvrir l'éditeur](https://ha-homelab.github.io/home-studio/planner/)
ou suivre le [guide de dessin illustré](https://ha-homelab.github.io/home-studio/planner/guide.html).
Images : Home Studio contributors, MIT.
[Sources et provenance des images](https://github.com/ha-homelab/.github/blob/main/assets/profile/README.md).

Pour d'autres vues, découvrez l'[architecture voix/musique/BLE d'EchoMuse](https://github.com/ha-homelab/ha-echomuse/blob/main/docs/architecture.md),
les [schémas de câblage ZAC93](https://github.com/ha-homelab/zac93-esp32)
et la [démonstration de rejeu synthétique RuView](https://github.com/ha-homelab/ruview-home-assistant#try-it-without-hardware).

## Aperçu du catalogue public

![Diagramme en barres : appareils et passerelles 8 ; outils spatiaux, observations et accès 5 ; voix et médias 4 ; tests et contrats 4 ; configuration et fiabilité 2](https://raw.githubusercontent.com/ha-homelab/.github/main/assets/profile/portfolio.fr.svg)

**23 projets + ce dépôt de profil = 24 dépôts publics**, vérifiés le 16 octobre 2026.
Chaque projet appartient à une seule catégorie éditoriale ; les nombres ne mesurent
ni la maturité, ni l'utilisation, ni les performances.
[Données sources reproductibles](https://github.com/ha-homelab/.github/blob/main/assets/profile/catalog.json).
Les résultats des vérifications logicielles figurent séparément dans le
[graphique daté des tests communautaires et ses liens CI](https://github.com/ha-homelab/.github/blob/main/community-tools/README.fr.md#validation-evidence--2026-10-16-utc).

## Projets publics associés hors de cette organisation

Ces projets maintenus séparément complètent le homelab. Ce sont des composants
facultatifs, avec leur propre configuration et leur propre périmètre de support.

**Énergie — [écosystème Victron / Venus OS](https://github.com/victron-venus)**

- [inverter-climate](https://github.com/victron-venus/inverter-climate) coordonne le climat
  via Home Assistant et Venus OS, en mode observation par défaut.
- [dbus-emporia-vue](https://github.com/victron-venus/dbus-emporia-vue) expose les mesures
  des circuits comme charges GX ; [dbus-pump](https://github.com/victron-venus/dbus-pump)
  relie les entités HA des réservoirs, pompes et vannes.
- [inverter-dashboard-go](https://github.com/victron-venus/inverter-dashboard-go) fournit
  un tableau de bord énergétique avec interface Vue et appareils Home Assistant facultatifs.

**Voix et médias — dont l'[écosystème Open OTT Play](https://github.com/open-ott-play)**

- [Amazon Echo Home Energy](https://github.com/4alvit/amazon-echo-home-voice) est une skill
  Alexa personnalisée en lecture seule ; [Google Home / Nest reports](https://github.com/4alvit/google-home-voice-stats)
  envoie une vidéo Cast avec synthèse vocale locale. Ces projets fonctionnent sans
  conversion matérielle ; Home Assistant est facultatif, et la skill Alexa ne l'exige pas.
- [EPG Voice Gateway](https://github.com/4alvit/epg-voice-gateway) trouve les programmes
  XMLTV en cours et achemine leur lecture via un proxy HLS existant vers les écrans Alexa ou Google Cast.
- [OTT-play Control Server](https://github.com/open-ott-play/ottplay-control-server) fournit
  des commandes de lecteurs, un contrôle par terminal et un déploiement k3s.
  La passerelle EPG ne dépend pas d'OttPlay.

**Infrastructure réutilisable**

- [ESPHome BLE Sensor Patterns](https://github.com/4alvit/esphome-ble-sensor-patterns) propose
  des configurations ESP32 de référence pour capteurs de batterie, de température et de plantes.
- [FastAPI MQTT Gateway](https://github.com/4alvit/fastapi-mqtt-gateway) relie REST/WebSocket
  et MQTT avec authentification et restrictions de sujets.
- [MQTT Observability](https://github.com/4alvit/mqtt-observability-opentelemetry) observe MQTT
  et les métriques Mosquitto via OpenTelemetry, Prometheus et Grafana ; ce n'est pas un proxy de messages.
- [HA Homelab Terraform](https://github.com/4alvit/terraform-github-ha-homelab) gère les
  paramètres GitHub et les dépôts de cette organisation.

## Notre façon de travailler

Un comportement compréhensible, des changements faciles à examiner, des builds
reproductibles et une restauration documentée. Les exemples publics et les captures
d'écran utilisent des données synthétiques là où c'est indiqué ; les identifiants
du foyer, enregistrements, sauvegardes d'appareils et exports opérationnels privés
restent hors de ces dépôts. Chaque projet précise ce qui a été testé et ce qui
nécessite encore une vérification physique.

Pour contribuer, suivez le guide du dépôt concerné ; signalez les vulnérabilités
selon sa politique de sécurité. Ce dépôt contient aussi notre
[logo original et ses notes de conception](https://github.com/ha-homelab/.github/blob/main/assets/README.md).

---

Un homelab indépendant construit avec [Home Assistant](https://www.home-assistant.io/).
Sans affiliation au projet Home Assistant ni aux fabricants d'appareils.
