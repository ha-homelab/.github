# Nejdříve důkazy, potom automatizace

<!-- language-navigation:start -->
<p dir="ltr">
<a href="README.md" lang="en" dir="ltr">English</a> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="README.es.md" lang="es" dir="ltr">Español</a> · <a href="README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="README.he.md" lang="he" dir="rtl">עברית</a> · <a href="README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Tyto překlady dokumentace nerozšiřují jazykovou podporu CLI ani hlasových funkcí; ověřte podporované jazyky jednotlivých projektů.

Čtyři malé nástroje pomáhají komunitnímu projektu Home Assistant odpovědět na čtyři různé otázky: **jaká má být role zařízení, co zahrnuje měření, co automatizační engine skutečně provede a jaké důkazy podporují hlasový výsledek?** První vydání pracují s místními soubory a syntetickými testovacími daty. Nenasazují konfiguraci domácnosti a necertifikují fyzická zařízení.

![Čtyři fáze revize a hranice samostatné fyzické přejímky](architecture.cs.svg)

[Vizuální průvodce: postup, výstupy a výsledky](process-and-results.cs.md) · [Diagram změny stavů](role-transfer.cs.svg) · [Graf testovacích důkazů](validation.cs.svg)

## Čtyři projekty

- [HA Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations) vytváří offline migrační plán. Výslovná pravidla pro role a hardware, schopnosti a otisky souborů brání tomu, aby běžné přejmenování potichu přiřadilo automatizaci osvětlení zásuvce používané k jinému účelu. Připravený plán platí pouze pro dodaný podporovaný rozsah konfigurace.
- [HA Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts) kontroluje fyzický rozsah měření, původ zdrojů, jednotky, aktuálnost vzorků a pravidla sčítání. Přejmenování měřidla prodlužovacího přívodu z něj neudělá samostatné měřidlo čerpadla. Duplicitní reprezentace jednoho proudového transformátoru nelze sčítat jako oddělené zátěže.
- [HA Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests) spouští omezený syntetický scénář ve skutečném automatizačním a skriptovacím enginu Home Assistant. Kontroluje pořadí volání, zakázaná volání a konečné syntetické stavy. První běhové prostředí je pevně nastaveno na HA 2026.10.0 a Python 3.14.2–3.14.x; použijte prostředí oddělené od ostatních nástrojů.
- [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab) vyhodnocuje místní hlasové důkazy. Odděluje správnost příkazu, dokončení API a slyšitelný výstup. Všechny přibalené časy jsou syntetické a dodaná pozorování se nezávisle neověřují.

Projekty mají vlastní instalační příručky, anglickou/ruskou dokumentaci a zprávy CLI v angličtině, ruštině, němčině a španělštině. Dodržujte jejich verzované kontrakty, nepředpokládejte stejný význam všech návratových kódů. Šipky představují **předání při revizi**, nikoli implementované automatické integrace. Neexistuje centrální démon ani univerzální příkaz pro nasazení.

Hostované wiki: [Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations/wiki) · [Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts/wiki) · [Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests/wiki) · [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab/wiki) · [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32/wiki)

<a id="validation-evidence--2026-10-16-utc"></a>

## Důkazy validace — 2026-10-16 UTC

Jde o softwarové kontroly konkrétních verzí se syntetickými daty, nikoli certifikaci hardwaru nebo benchmark domácnosti.

![Zaznamenané počty linuxových testů s poznámkami o rozsahu a přeskočených testech](validation.cs.svg)

Pruhy zobrazují počty, ne pokrytí ani žebříček kvality. Datované zdrojové záznamy jsou v [validation-evidence.json](validation-evidence.json).

- **Entity Migrations:** místně prošlo 37 testů a 9 podtestů včetně regresí zdrojových aliasů. [Linuxový běh na main](https://github.com/ha-homelab/ha-entity-migrations/actions/runs/38843701264) úspěšně dokončil 36 testů a přeskočil případ souborového systému nerozlišujícího velikost písmen, který byl ověřen místně.
- **Meter Contracts:** [75 testů prošlo v linuxovém CI](https://github.com/ha-homelab/ha-meter-contracts/actions/runs/38843671896), včetně konfliktů původu, přijetí zdrojových souborů a sémantiky měření.
- **Assist Scenario Lab:** [24 testů prošlo v linuxovém CI](https://github.com/ha-homelab/assist-scenario-lab/actions/runs/38843304306). Ověřují dodané důkazy a syntetické příklady; netvrdí fyzické porovnání hlasu.
- **Scenario Tests:** [54 testů prošlo bez přeskočení v linuxovém CI](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199) na CPython 3.14.8 se skutečným Home Assistant 2026.10.0, včetně sedmi běhových případů, z nichž jeden testuje doprovodný scénář přenosu role. Celá sada doběhla za 21.42 sekundy.

Ověřeným prostředím je Linux. [Zdokumentovaná chyba nativního ukončení na macOS](https://github.com/ha-homelab/ha-scenario-tests/blob/main/docs/validation.md) zůstává omezením; očekávaný JSON výsledek před pádem procesu stále znamená neúspěšný běh. Netvrdíme spuštění v Dockeru ani fyzickou přejímku zařízení.

## Postup a ilustrované výsledky

![Vstupy, kontroly a výsledky čtyř nástrojů](results.cs.svg)

[Vizuální průvodce](process-and-results.cs.md) vysvětluje jednotlivé výstupy, sleduje stavy náhradního zařízení a původního hardwaru a rozlišuje softwarové důkazy od fyzické přejímky. Ilustrace shrnují přibalené syntetické příklady; nejde o snímky nezpracovaných zpráv.

<a id="a-concrete-migration-to-test-workflow"></a>

## Konkrétní postup od migrace k testu

1. V `ha-entity-migrations` po instalaci repozitáře spusťte přibalený příklad změny domény:

   ```sh
   ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
   ```

   Zkontrolujte navržené změny `light.table` → `switch.table` a `light.turn_off` → `switch.turn_off`. Otisky a podporované odkazy považujte za hranici rozsahu. Zablokovaný plán vyžaduje prošetření; nenahrazujte chybějící důkazy o schopnostech bezpodmínečným hledáním a nahrazením.

2. Převádějte zkontrolované chování do syntetického testu. [role-transfer.scenario.json](role-transfer.scenario.json) je ručně napsaný doprovodný scénář, **nikoli automatický export** migračního plánu. Posílá syntetickou událost „vypnout stůl“, očekává jedno volání náhradní role a zakazuje vypnutí původního hardwaru. Také ověřuje, že původní hardware zůstává zapnutý. Z adresáře této příručky, s nástrojem pro scénáře nainstalovaným ve vlastním prostředí:

   ```sh
   ha-scenario validate role-transfer.scenario.json
   ha-scenario run role-transfer.scenario.json
   ```

   Tento scénář je bajtově shodný s [testovacími daty přenosu role](https://github.com/ha-homelab/ha-scenario-tests/blob/0ea7e5a5d24dc89ebe896b1a2387396b3fce18f4/tests/fixtures/role_transfer.json) ověřenými v [úspěšném linuxovém běhu](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199). Jeho SHA-256 je `bb8544517eeb4895b80b049cf9e242d04635e7785bd198c1d57a7cf3f5fc8ab4`. Dřívější chyba ukončení na macOS zůstává zdokumentovaná a nepočítá se jako úspěšný běh.

   Scénář používá skutečný engine HA se zpětnými voláními akčních členů v paměti. Úspěch prokazuje chování enginu pro dodanou syntetickou sekvenci, nikoli rádiové doručení, sepnutí kontaktů nebo napájení spotřebiče. Jedna událost nepokrývá celou konfiguraci domácnosti.

3. Před nasazením doplňte relevantní poruchové sekvence: nepřítomnost přerušenou nedostupností senzoru, ruční podržení stavu, opětovné načtení automatizace, duplicitní spouštěče a obnovený stav. Přibalené příklady pokrývají přítomnost, ruční podržení, zastaralé vstupy a sladění po opětovném načtení. Hodiny běží ve skutečném čase, takže krátký příklad neověřuje produkční dvacetiminutový interval. HA dokumentuje, že čekání `for` nepřežije restart či opětovné načtení; podle potřeby zvolte a otestujte výslovné sladění nebo trvale uložené termíny. [Dokumentace spouštěčů HA](https://www.home-assistant.io/docs/automation/trigger/)

4. Důkazy měření posuzujte nezávisle. Z repozitáře měřicího nástroje:

   ```sh
   ha-meter-contracts check examples/valid-three-meters.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/kmc-shared-meter.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/duplicate-emporia.json --at 2026-01-01T12:00:05Z --json
   ```

   Platný příklad uspěje. Zbývající dva úmyslně končí kódem 1: první se pokouší připsat měření celého přívodu jedné zásuvce, druhý obsahuje duplicitní reprezentace zdroje. Při skriptování je považujte za očekávané chyby. Nevkládejte výkon celého přívodu do ochranné meze původně kalibrované jen pro čerpadlo. Kalibrace napětí není kalibrací proudu ani výkonu. Chybějící či zastaralé důkazy zůstávají nedostupné, nikoli nulové. [Sémantika senzorů a statistik HA](https://developers.home-assistant.io/docs/core/entity/sensor/#long-term-statistics)

5. Pokud hlas slouží jako spouštěč nebo zpětná vazba, vyhodnoťte důkazy samostatně v hlasovém repozitáři:

   ```sh
   assist-lab evaluate examples/synthetic-pass.json
   assist-lab evaluate examples/synthetic-incomplete.json
   ```

   Neúplný příklad úmyslně končí kódem 3, protože dokončení API nestačí jako důkaz slyšitelnosti. Skutečný benchmark potřebuje souhlas s nahráváním, stanovené hodiny a metodu, srovnatelné podmínky a nezávislé pozorování akce i slyšitelné odpovědi. Nezveřejňujte domácí nahrávky, přepisy ani exportované tokeny. První zvukový blok serveru není první zvuk u posluchače. [Hlasové pipeline HA Assist](https://developers.home-assistant.io/docs/voice/pipelines/)

6. Každou zprávu uchovejte s revidovanou změnou. Změnu aplikujte zavedeným postupem revize a nasazení dané instalace, poté proveďte přejímku konkrétního zařízení. Fyzické zapnutí/vypnutí, polarita indikátoru, chování po restartu, čas zdroje a kalibrace jednotlivých veličin vyžadují skutečná pozorování. Čtyři nástroje tento krok neprovádějí ani nenahrazují.

## Co kontroly neprokazují

Nakonfigurovaný stav, přijaté volání služby, pozorovaný odběr a průtok vody jsou různé důkazy. Celkové měřidlo tří zátěží neurčí, která energii odebírala. Syntetický stav „vypnuto“ neprokazuje rozepnutí kontaktů relé. Měřicí nástroj ani test scénáře nejsou bezpečnostním řídicím systémem pro vodu, topidla, přístup nebo jiné zátěže s významnými následky.

Nástroje si navzájem nevynucují výsledky. Budoucí integrace může využít jejich stabilní JSON, ale musí výslovně definovat přijatelné úrovně varování, kompatibilitu verzí a význam „úplných důkazů“. Neredukujte `ready`, `available`, `passed` a `audible` na jedinou zaměnitelnou booleovskou hodnotu.

## Plán rozvoje: čtrnáct nápadů s poctivým stavem připravenosti

První čtyři níže uvedené softwarové výstupy jsou dostupné jako počáteční offline nástroje. Veškeré jmenované navazující práce zůstávají návrhem; název repozitáře nebo diagram neznamená, že hardware byl uveden do provozu.

1. **Migrace rolí — počáteční nástroj implementován.** Rozšiřujte podporované formáty odkazů pouze s testy zpětného převodu a konfliktů; zachovejte výslovnou hranici nepodporovaných vstupů.
2. **Kontrakty měřidel — počáteční nástroj implementován.** Vyzkoušejte soukromá reálná pozorování s časovými razítky; před tvrzením o kalibraci nezávisle změřte proud a výkon. Přiřazení jednotlivým zásuvkám stále vyžaduje důkazy pro jednotlivé zásuvky.
3. **Testování automatizačních scénářů — počáteční nástroj implementován.** Doplňte revidovaná pravidla a případy restartu či termínů; podle potřeby zvlášť otestujte časování v produkčních délkách.
4. **Hlasové důkazy — počáteční nástroj implementován; fyzický benchmark čeká.** Před sběrem srovnatelných relací vyberte satelity, metodu pozorování a souhlas s nahráváním. Zatím žádný žebříček hardwaru.
5. **Koordinace kvality vzduchu — čeká na ověření senzorů a akčních členů.** Ověřte, zda zařízení měří CO₂ nebo částice, jeho stáří a přesnost i to, co ovlivní větrání či filtrace. Před pravidly větrání potvrďte venkovní podmínky.
6. **Radarové důkazy a přítomnost — čeká na zprovoznění hardwaru.** Ověřte desku LD2450, napájení, kryt, protokol a pokrytí. Cíle nejsou lidské identity a stáří příjmu není změřená latence senzoru. CSI zůstává experimentální.
7. **Pozorovatelnost vody a čerpadla — čeká na nezávislé důkazy.** Rozlišujte povolení napájet čerpadlo, elektrický odběr, průtok a hladinu vody. Souhrnné měřidlo přívodu nenahradí chybějící ochranný signál samotného čerpadla. Neopakujte kritické příkazy automaticky bez pozorovaného stavu a revize konkrétní instalace.
8. **Telemetrie BLE — čeká na kompatibilní proxy a testy pokrytí.** Ověřte skutečné senzory, teplotní rozsah, baterie a umístění. Zařízení ESP8266 nejsou BLE proxy; RSSI není identita ani oprávnění k odemknutí. [Bluetooth proxy ESPHome](https://esphome.io/components/bluetooth_proxy/)
9. **Vysvětlení podle přítomnosti a spotřebiče — čeká na ověření schopností.** Vysvětlete, které pozorování udrželo světlo zapnuté; využijte skutečné události pračky či sušičky, pokud jsou podporovány. Neodvozujte cyklus spotřebiče jen ze sdíleného měřidla a nevymýšlejte statistickou jistotu z nesouvisejících příznaků senzorů.
10. **Most Z-Wave — čeká na dodání, sestavení a rádiovou přejímku.** [Průvodce ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) je samostatná hardwarová větev. Ověřte zapojení, regionální frekvenci, sériový přenos a zahrnutí do Z-Wave JS na skutečné desce. Podpora Long Range u řadiče nezmění starší senzor na zařízení Long Range. [Průvodce Z-Wave JS](https://zwave-js.github.io/zwave-js/#/getting-started/index)
11. **Přejímka zásuvek ESPHome — čeká na individuální hardwarové testy.** Pro každou revizi zaznamenejte důkazy o tlačítku, relé, indikátoru a restartu i samostatnou kalibraci napětí, proudu a výkonu. Úspěšné nahrání firmwaru není dokončená přejímka. Žádné hromadné cyklování napájení připojených spotřebičů bez dozoru.
12. **Porovnávání předpovědí — čeká na nashromážděná data.** Archivujte vydané předpovědi a pozdější skutečnost, zachovejte čas vydání a hodnoťte horizonty bez úniku budoucích informací. Je potřeba uplynulá doba pozorování, nikoli tvrzení o úsporách energie ze syntetického příkladu.
13. **Omezené ovládání pro hosty — čeká na revizi oprávnění backendu.** Ověřte identitu a autorizaci na serveru. Samotné skrytí ovládacích prvků neomezuje přístup. Neoslabujte autentizaci kvůli zjednodušení panelu.
14. **Plánování odložitelných zátěží — čeká na změřená omezení a schopnosti.** Zavedené plánovací nástroje integrujte po ověření měřidel, stavové zpětné vazby a předpovědí. Potvrďte, které zátěže lze opravdu odložit nebo modulovat, jejich termíny a ruční zásahy. Začněte revidovanými doporučeními bez spekulativních úspor či záruk bezpečnosti. [EMHASS](https://emhass.readthedocs.io/en/latest/emhass.html) · [evcc](https://docs.evcc.io/en/)

## Přispívání a reprodukce příručky

Tento přehled, syntetický scénář a diagram jsou původní materiály s licencí MIT; viz [LICENSE](LICENSE). Všechna lokalizovaná SVG znovu vytvoříte příkazem `python3 render_architecture.py`. Neobsahují externí obrázky, skripty, identifikátory domácnosti ani naměřená domácí data. [Vizuální průvodce](process-and-results.cs.md#reproduce-or-translate-the-illustrations) vysvětluje zdrojové záznamy a kontroly při generování. Veřejná testovací data ponechte syntetická a soukromé exporty mimo Git. Při změnách dodržujte bezpečnostní a příspěvkové pokyny jednotlivých repozitářů.
