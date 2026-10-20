# Des preuves avant l'automatisation

<!-- language-navigation:start -->
<p dir="ltr">
<a href="README.md" lang="en" dir="ltr">English</a> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="README.es.md" lang="es" dir="ltr">Español</a> · <a href="README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="README.he.md" lang="he" dir="rtl">עברית</a> · <a href="README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Quatre petits outils aident un projet communautaire Home Assistant à répondre à quatre questions différentes : **que doit devenir le rôle d'un appareil, que couvre une mesure, que fait réellement le moteur d'automatisation et quelles preuves étayent un résultat vocal ?** Leurs premières versions utilisent des fichiers locaux et des jeux de données synthétiques. Elles ne déploient aucune configuration domestique et ne certifient aucun appareil physique.

![Quatre étapes de revue et une limite distincte pour la réception physique](architecture.fr.svg)

[Parcours visuel : processus, sorties et résultats](process-and-results.fr.md) · [Diagramme de changement d'état](role-transfer.fr.svg) · [Graphique des preuves de test](validation.fr.svg)

## Les quatre projets

- [HA Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations) produit un plan de migration hors ligne. Des politiques explicites de rôle et de matériel, les capacités et les empreintes de fichiers empêchent un simple renommage d'attribuer silencieusement une automatisation d'éclairage à une prise réaffectée. Un plan prêt ne s'applique qu'au périmètre de configuration fourni et pris en charge.
- [HA Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts) vérifie le périmètre physique des mesures, leur provenance, les unités, la fraîcheur des échantillons et les règles d'addition. Renommer le compteur d'une multiprise n'en fait pas un compteur individuel de pompe. Plusieurs représentations d'un même transformateur de courant ne peuvent pas être additionnées comme des charges distinctes.
- [HA Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests) exécute un scénario synthétique restreint dans le véritable moteur d'automatisations et de scripts de Home Assistant. Il vérifie les appels dans l'ordre, les appels interdits et les états synthétiques finaux. Son environnement d'exécution actuel est fixé à HA 2026.10.1 et Python 3.14.2–3.14.x ; utilisez un environnement distinct de celui des autres outils.
- [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab) évalue des preuves vocales locales. Il distingue la justesse de la commande, la fin de l'API et la sortie audible. Tous les temps inclus sont synthétiques et les observations fournies ne sont pas vérifiées indépendamment.

Les projets ont leurs propres guides d'installation, une documentation en anglais et en russe et des messages CLI en anglais, russe, allemand et espagnol. La traduction de cette documentation n'ajoute aucune langue aux interfaces CLI ni aux fonctions vocales ; consultez les langues prises en charge par chaque projet. Suivez leurs contrats versionnés sans supposer que tous les codes de sortie ont la même signification. Les flèches des schémas représentent des **transmissions lors de la revue**, et non des intégrations automatiques implémentées. Il n'existe ni service central ni commande de déploiement universelle.

Wikis hébergés : [Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations/wiki) · [Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts/wiki) · [Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests/wiki) · [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab/wiki) · [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32/wiki)

<a id="validation-evidence--2026-10-16-utc"></a>

## Preuves de validation — 2026-10-16 UTC

Il s'agit de vérifications logicielles propres à certaines versions et utilisant des données synthétiques, pas d'une certification matérielle ni d'un banc d'essai domestique.

![Nombre de tests Linux enregistrés, avec notes sur leur périmètre et les tests ignorés](validation.fr.svg)

Les barres indiquent des nombres de tests, pas une couverture ni un classement de qualité. Les données sources datées figurent dans [validation-evidence.json](validation-evidence.json).

- **Entity Migrations :** 37 tests et 9 sous-tests ont réussi localement, y compris les régressions d'alias de source. L'[exécution Linux sur main](https://github.com/ha-homelab/ha-entity-migrations/actions/runs/38843701264) a réussi 36 tests et ignoré le cas du système de fichiers insensible à la casse, testé localement.
- **Meter Contracts :** [75 tests réussis dans la CI Linux](https://github.com/ha-homelab/ha-meter-contracts/actions/runs/38843671896), couvrant notamment les conflits de provenance, l'admission des fichiers sources et la sémantique des mesures.
- **Assist Scenario Lab :** [24 tests réussis dans la CI Linux](https://github.com/ha-homelab/assist-scenario-lab/actions/runs/38843304306). Ils valident les preuves fournies et les exemples synthétiques ; aucune comparaison vocale physique n'est revendiquée.
- **Scenario Tests :** [54 tests réussis sans aucun test ignoré dans la CI Linux](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199), sur CPython 3.14.8 avec le véritable Home Assistant 2026.10.0. Cela inclut sept cas d'exécution, dont un teste le scénario complémentaire de transfert de rôle. La suite complète s'est terminée en 21.42 secondes.

Linux est l'environnement d'exécution testé. L'[échec documenté du nettoyage final sous macOS natif](https://github.com/ha-homelab/ha-scenario-tests/blob/main/docs/validation.md) reste une limite ; un résultat JSON attendu suivi d'un plantage du processus reste une exécution en échec. Le relevé du 16 octobre ne revendique aucune exécution Docker ni réception d'appareil physique.

Mise à jour du 19 octobre 2026 : la [CI Linux](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/39264346721) a également réussi un test de fonctionnement de base de l'environnement empaqueté dans Docker. Cela ne démontre pas la réception d'appareils physiques.

## Processus et résultats illustrés

![Entrées, vérifications et résultats des quatre outils](results.fr.svg)

Suivez le [parcours visuel](process-and-results.fr.md) pour interpréter chaque sortie, retracer les états de l'appareil de remplacement et du matériel retiré de ce rôle, et distinguer les preuves logicielles de la réception physique. Les résultats illustrés résument les exemples synthétiques fournis ; ce ne sont pas des captures de rapports bruts.

<a id="a-concrete-migration-to-test-workflow"></a>

## Un processus concret de la migration au test

1. Dans `ha-entity-migrations`, exécutez l'exemple de changement de domaine fourni, après installation de ce dépôt :

   ```sh
   ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
   ```

   Examinez les changements proposés `light.table` → `switch.table` et `light.turn_off` → `switch.turn_off`. Les empreintes et les références prises en charge délimitent le périmètre. Un plan bloqué exige une investigation ; ne remplacez pas des preuves de capacité manquantes par un rechercher-remplacer sans condition.

2. Traduisez le comportement examiné en test synthétique. [role-transfer.scenario.json](role-transfer.scenario.json) est un scénario complémentaire rédigé manuellement, **pas un export automatique** du plan de migration. Il envoie un événement synthétique « éteindre la table », attend un appel au rôle de remplacement et interdit l'extinction du matériel retiré de ce rôle. Il vérifie également que ce matériel reste allumé. Depuis le répertoire de ce guide, avec l'exécuteur de scénarios installé dans son propre environnement :

   ```sh
   ha-scenario validate role-transfer.scenario.json
   ha-scenario run role-transfer.scenario.json
   ```

   Ce scénario est identique octet par octet au [jeu de test de transfert de rôle](https://github.com/ha-homelab/ha-scenario-tests/blob/0ea7e5a5d24dc89ebe896b1a2387396b3fce18f4/tests/fixtures/role_transfer.json) testé dans l'[exécution Linux réussie](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199). Son SHA-256 est `bb8544517eeb4895b80b049cf9e242d04635e7785bd198c1d57a7cf3f5fc8ab4`. L'échec antérieur du nettoyage final sous macOS reste documenté et n'est pas compté comme une réussite.

   Le scénario utilise le véritable moteur HA avec des fonctions de rappel d'actionneurs en mémoire. Une réussite prouve le comportement du moteur pour la séquence synthétique fournie, pas la transmission radio, la fermeture des contacts ni l'alimentation d'un appareil. Son événement unique ne couvre pas toute une configuration domestique.

3. Ajoutez les séquences d'échec pertinentes avant le déploiement : absence interrompue par l'indisponibilité d'un capteur, maintien manuel, rechargement de l'automatisation, déclenchements en double et état restauré. Les exemples fournis couvrent la présence, le maintien manuel, les données périmées et la réconciliation au rechargement. L'horloge mesurant le temps réellement écoulé, un jeu de test court ne valide pas un intervalle de vingt minutes en production. HA précise que les attentes `for` ne survivent pas à un redémarrage ou rechargement ; choisissez et testez une réconciliation explicite ou des échéances persistantes si nécessaire. [Documentation des déclencheurs HA](https://www.home-assistant.io/docs/automation/trigger/)

4. Examinez indépendamment les preuves de mesure. Depuis le dépôt des compteurs :

   ```sh
   ha-meter-contracts check examples/valid-three-meters.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/kmc-shared-meter.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/duplicate-emporia.json --at 2026-01-01T12:00:05Z --json
   ```

   L'exemple valide réussit. Les deux suivants se terminent volontairement avec le code 1 : respectivement une tentative d'attribution à une prise à partir d'un compteur de multiprise entière, puis des représentations dupliquées d'une seule source. Traitez-les comme des échecs attendus dans vos scripts d'exemples. N'utilisez pas les watts de toute une multiprise pour un seuil de protection initialement étalonné pour une pompe seule. Un étalonnage en tension n'est pas un étalonnage en courant ou en puissance. Les preuves absentes ou périmées restent indisponibles, et non égales à zéro. [Sémantique des capteurs et statistiques HA](https://developers.home-assistant.io/docs/core/entity/sensor/#long-term-statistics)

5. Si la voix déclenche une action ou fournit un retour, évaluez ses preuves séparément dans le dépôt vocal :

   ```sh
   assist-lab evaluate examples/synthetic-pass.json
   assist-lab evaluate examples/synthetic-incomplete.json
   ```

   L'exemple incomplet se termine volontairement avec le code 3, car la fin d'une API ne suffit pas à prouver l'audibilité. Un véritable banc d'essai exige le consentement à l'enregistrement, une horloge et une méthode déclarées, des conditions comparables et une observation indépendante de l'action et de la réponse audible. Ne publiez pas d'enregistrements domestiques, de transcriptions ni de jetons exportés. Le premier fragment audio d'un serveur n'est pas le premier son entendu par l'auditeur. [Pipelines Assist de HA](https://developers.home-assistant.io/docs/voice/pipelines/)

6. Conservez chaque rapport avec le changement examiné. Appliquez-le selon la procédure de revue et de déploiement du site, puis procédez à la réception propre à l'appareil. L'allumage et l'extinction physiques, la polarité des voyants, le comportement au redémarrage, l'heure de la source et l'étalonnage de chaque grandeur exigent des observations réelles. Ces quatre outils n'effectuent ni ne remplacent cette étape.

## Ce que les vérifications ne prouvent pas

Un état configuré, un appel de service accepté, une consommation électrique observée et un débit d'eau sont des preuves distinctes. Un compteur total pour trois charges ne permet pas d'identifier celle qui a consommé l'énergie. Un état synthétique « éteint » ne prouve pas l'ouverture des contacts d'un relais. Ni l'outil de mesure ni un test de scénario ne constituent un contrôleur de sécurité pour l'eau, les chauffages, les accès ou d'autres charges à conséquences importantes.

Ces outils n'imposent pas les résultats les uns des autres. Une future intégration pourra exploiter leur JSON stable, mais devra définir explicitement les niveaux d'avertissement acceptés, la compatibilité des versions et le sens de « preuves complètes ». Ne réduisez pas `ready`, `available`, `passed` et `audible` à un booléen interchangeable.

## Feuille de route : quatorze idées et leur état réel

Les quatre premiers livrables ci-dessous sont disponibles comme outils hors ligne initiaux. Tous les prolongements nommés restent proposés ; un nom de dépôt ou un schéma ne signifie pas que le matériel a été mis en service.

1. **Migrations de rôles — outil initial implémenté.** Étendre les formats de références pris en charge uniquement avec des tests aller-retour et de conflit ; conserver la limite explicite des entrées non prises en charge.
2. **Contrats de mesure — outil initial implémenté.** Expérimenter avec des observations réelles, privées et horodatées ; mesurer indépendamment courant et puissance avant d'affirmer leur étalonnage. Une attribution par prise exige toujours des preuves par prise.
3. **Tests de scénarios d'automatisation — outil initial implémenté.** Ajouter des politiques examinées et des cas de redémarrage et d'échéance ; tester séparément les durées de production si nécessaire.
4. **Preuves vocales — outil initial implémenté ; banc d'essai physique en attente.** Choisir les satellites, la méthode d'observation et le consentement à l'enregistrement avant de recueillir des sessions comparables. Aucun classement matériel à ce stade.
5. **Coordination de la qualité de l'air — vérification des capteurs et actionneurs en attente.** Vérifier si un appareil mesure le CO₂ ou les particules, son ancienneté et sa précision, ainsi que les effets possibles de la ventilation ou de la filtration. Confirmer les conditions extérieures avant d'établir une politique de ventilation.
6. **Preuves radar et présence — mise en service matérielle en attente.** Vérifier la carte LD2450, l'alimentation, le boîtier, le protocole et la couverture. Les cibles ne sont pas des identités humaines, et l'ancienneté de réception n'est pas une latence mesurée du capteur. Le CSI reste expérimental.
7. **Observabilité de l'eau et des pompes — preuves indépendantes en attente.** Distinguer l'autorisation d'alimenter une pompe, sa consommation électrique, le débit d'eau et le niveau d'eau. Un compteur agrégé de multiprise ne peut pas fournir un signal de protection manquant propre à la pompe. Éviter les politiques de répétition automatique de commandes critiques sans état observé ni revue propre au site.
8. **Télémétrie BLE — proxies compatibles et tests de couverture en attente.** Valider les capteurs réels, la plage de température, les batteries et l'emplacement. Les appareils ESP8266 ne sont pas des proxies BLE ; le RSSI n'est ni une identité ni un justificatif de déverrouillage. [Proxy Bluetooth ESPHome](https://esphome.io/components/bluetooth_proxy/)
9. **Explications fondées sur la présence et électroménager — vérification des capacités en attente.** Expliquer quelle observation a maintenu une lampe allumée ; utiliser les véritables événements de lave-linge ou sèche-linge s'ils sont pris en charge. Ne pas déduire un cycle d'appareil d'un seul compteur partagé ni inventer une confiance statistique à partir d'indicateurs de capteurs sans rapport.
10. **Passerelle Z-Wave — livraison, assemblage et réception radio en attente.** Le [guide ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) constitue un parcours matériel distinct. Vérifier le câblage, la fréquence régionale, le transport série et l'inclusion Z-Wave JS sur la carte réelle. Le support Long Range du contrôleur ne transforme pas un ancien capteur en appareil Long Range. [Guide Z-Wave JS](https://zwave-js.github.io/zwave-js/#/getting-started/index)
11. **Réception des prises ESPHome — tests matériels individuels en attente.** Consigner pour chaque révision les observations du bouton, du relais, des voyants et du redémarrage, ainsi que des étalonnages distincts en tension, courant et puissance. Un flash réussi n'achève pas la réception. Pas de cycles massifs d'alimentation sans surveillance sur les appareils connectés.
12. **Évaluation des prévisions — accumulation de données en attente.** Archiver les prévisions émises et les observations ultérieures, conserver l'heure d'émission et évaluer les horizons sans utiliser des informations futures. Cela demande du temps d'observation écoulé, pas une affirmation d'économies d'énergie issue d'un exemple synthétique.
13. **Commandes invitées à périmètre limité — revue des autorisations du serveur en attente.** Vérifier l'identité et l'autorisation côté serveur. Masquer des commandes dans le tableau de bord ne limite pas à lui seul l'accès. Ne pas affaiblir l'authentification pour simplifier une interface.
14. **Planification des charges différables — contraintes mesurées et capacités en attente.** Intégrer des outils de planification établis après validation des compteurs, des retours d'état et des prévisions. Confirmer quelles charges peuvent réellement être différées ou modulées, leurs échéances et les dérogations manuelles. Commencer par des recommandations examinées, sans économies spéculatives ni garanties de sécurité. [EMHASS](https://emhass.readthedocs.io/en/latest/emhass.html) · [evcc](https://docs.evcc.io/en/)

## Contribuer et reproduire ce guide

Cet aperçu, le scénario synthétique et les schémas sont des créations originales sous licence MIT ; voir [LICENSE](LICENSE). Régénérez les SVG dans toutes les langues disponibles avec `python3 render_architecture.py`. Ils ne contiennent ni images externes, ni scripts, ni identifiants domestiques, ni mesures d'un foyer. Le [parcours visuel](process-and-results.fr.md#reproduce-or-translate-the-illustrations) explique les données sources et les vérifications de régénération. Conservez des jeux de test publics synthétiques et les exports privés hors de Git. Pour les changements, suivez les consignes de sécurité et de contribution de chaque dépôt.
