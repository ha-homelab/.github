# Verifiche prima dell'automazione

<!-- language-navigation:start -->
<p dir="ltr">
<a href="README.md" lang="en" dir="ltr">English</a> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.bn.md" lang="bn" dir="ltr">বাংলা</a> · <a href="README.cs.md" lang="cs" dir="ltr">Čeština</a> · <a href="README.de.md" lang="de" dir="ltr">Deutsch</a> · <a href="README.es.md" lang="es" dir="ltr">Español</a> · <a href="README.fa.md" lang="fa" dir="rtl">فارسی</a> · <a href="README.fr.md" lang="fr" dir="ltr">Français</a><br>
<a href="README.he.md" lang="he" dir="rtl">עברית</a> · <a href="README.hi.md" lang="hi" dir="ltr">हिन्दी</a> · <a href="README.id.md" lang="id" dir="ltr">Bahasa Indonesia</a> · <a href="README.it.md" lang="it" dir="ltr">Italiano</a> · <a href="README.ja.md" lang="ja" dir="ltr">日本語</a> · <a href="README.ko.md" lang="ko" dir="ltr">한국어</a> · <a href="README.nl.md" lang="nl" dir="ltr">Nederlands</a> · <a href="README.pl.md" lang="pl" dir="ltr">Polski</a><br>
<a href="README.pt.md" lang="pt" dir="ltr">Português</a> · <a href="README.ru.md" lang="ru" dir="ltr">Русский</a> · <a href="README.th.md" lang="th" dir="ltr">ไทย</a> · <a href="README.tr.md" lang="tr" dir="ltr">Türkçe</a> · <a href="README.uk.md" lang="uk" dir="ltr">Українська</a> · <a href="README.vi.md" lang="vi" dir="ltr">Tiếng Việt</a> · <a href="README.zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> · <a href="README.zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

Queste traduzioni della documentazione non estendono le lingue supportate dalla CLI o dalle funzioni vocali; verifica le lingue supportate da ogni progetto.

Quattro piccoli strumenti aiutano un progetto della community Home Assistant a rispondere a quattro domande diverse: **che cosa dovrebbe diventare il ruolo di un dispositivo, che cosa comprende una misura, che cosa fa realmente il motore di automazione e quali evidenze sostengono un risultato vocale?** Le prime release lavorano con file locali e dati di test sintetici. Non distribuiscono configurazioni domestiche e non certificano dispositivi fisici.

![Quattro fasi di revisione e il confine con l'accettazione fisica separata](architecture.it.svg)

[Percorso visuale: processo, output e risultati](process-and-results.it.md) · [Diagramma dei cambiamenti di stato](role-transfer.it.svg) · [Grafico delle evidenze dei test](validation.it.svg)

## I quattro progetti

- [HA Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations) produce un piano di migrazione offline. Policy esplicite per ruolo e hardware, capacità e impronte dei file impediscono che una normale rinomina assegni silenziosamente un'automazione di illuminazione a una presa destinata ad altro uso. Un piano pronto vale solo per l'ambito di configurazione fornito e supportato.
- [HA Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts) controlla l'ambito fisico della misura, la provenienza delle fonti, le unità, l'attualità dei campioni e le regole di addizione. Rinominare il misuratore di una ciabatta non lo trasforma nel misuratore individuale di una pompa. Rappresentazioni duplicate dello stesso trasformatore di corrente non possono essere sommate come carichi distinti.
- [HA Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests) esegue uno scenario sintetico limitato nel vero motore di automazioni e script Home Assistant. Controlla chiamate ordinate, chiamate vietate e stati sintetici finali. Il runtime attuale è fissato a HA 2026.10.1 e Python 3.14.2–3.14.x; usa un ambiente separato dagli altri strumenti.
- [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab) valuta evidenze vocali locali. Separa correttezza del comando, completamento dell'API e output udibile. Tutti i tempi inclusi sono sintetici e le osservazioni fornite non sono verificate in modo indipendente.

I progetti hanno guide di installazione proprie, documentazione inglese/russa e messaggi CLI in inglese, russo, tedesco e spagnolo. Segui i contratti versionati senza presumere che tutti i codici di uscita abbiano lo stesso significato. Le frecce nei diagrammi sono **passaggi di revisione**, non integrazioni automatiche implementate. Non esiste un demone centrale né un comando universale di distribuzione.

Wiki ospitati: [Entity Migrations](https://github.com/ha-homelab/ha-entity-migrations/wiki) · [Meter Contracts](https://github.com/ha-homelab/ha-meter-contracts/wiki) · [Scenario Tests](https://github.com/ha-homelab/ha-scenario-tests/wiki) · [Assist Scenario Lab](https://github.com/ha-homelab/assist-scenario-lab/wiki) · [ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32/wiki)

<a id="validation-evidence--2026-10-16-utc"></a>

## Evidenze di validazione — 2026-10-16 UTC

Sono verifiche software specifiche per versione, basate su dati sintetici, non certificazioni hardware o benchmark domestici.

![Conteggi documentati dei test Linux, con note su ambito e test saltati](validation.it.svg)

Le barre mostrano conteggi, non copertura o classifiche qualitative. I dati sorgente datati sono in [validation-evidence.json](validation-evidence.json).

- **Entity Migrations:** 37 test più 9 sottotest superati localmente, comprese le regressioni degli alias delle fonti. Il [run Linux su main](https://github.com/ha-homelab/ha-entity-migrations/actions/runs/38843701264) ha superato 36 test e saltato il caso del filesystem senza distinzione tra maiuscole e minuscole, verificato localmente.
- **Meter Contracts:** [75 test superati nella CI Linux](https://github.com/ha-homelab/ha-meter-contracts/actions/runs/38843671896), comprendenti conflitti di provenienza, ammissione dei file sorgente e semantica delle misure.
- **Assist Scenario Lab:** [24 test superati nella CI Linux](https://github.com/ha-homelab/assist-scenario-lab/actions/runs/38843304306). Validano evidenze fornite ed esempi sintetici; non viene rivendicato un confronto vocale fisico.
- **Scenario Tests:** [54 test superati senza casi saltati nella CI Linux](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199) su CPython 3.14.8 con Home Assistant 2026.10.0 reale, inclusi sette casi runtime, uno dei quali testa lo scenario di trasferimento del ruolo. L'intera suite è terminata in 21.42 secondi.

Linux è l'ambiente di esecuzione testato. Il [problema documentato di chiusura nativa su macOS](https://github.com/ha-homelab/ha-scenario-tests/blob/main/docs/validation.md) rimane un limite; un risultato JSON atteso prima di un arresto anomalo del processo resta un run fallito. Il resoconto del 16 ottobre non dichiara alcuna esecuzione Docker o accettazione di dispositivi fisici.

Aggiornamento del 19 ottobre 2026: la [CI Linux](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/39264346721) ha superato anche uno smoke test in Docker del runtime impacchettato. Ciò non dimostra l'accettazione dei dispositivi fisici.

## Processo e risultati illustrati

![Input, verifiche e risultati dei quattro strumenti](results.it.svg)

Segui il [percorso visuale](process-and-results.it.md) per interpretare ogni output, seguire gli stati del dispositivo sostitutivo e dell'hardware dismesso dal ruolo e distinguere evidenze software e accettazione fisica. I risultati illustrati riassumono esempi sintetici inclusi: non sono schermate di report grezzi.

<a id="a-concrete-migration-to-test-workflow"></a>

## Un flusso concreto dalla migrazione al test

1. In `ha-entity-migrations`, esegui l'esempio incluso di cambio dominio dopo aver installato il repository:

   ```sh
   ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
   ```

   Esamina le modifiche proposte `light.table` → `switch.table` e `light.turn_off` → `switch.turn_off`. Considera impronte e riferimenti supportati come confini dell'ambito. Un piano bloccato richiede indagini; non sostituire evidenze mancanti sulle capacità con un trova-e-sostituisci incondizionato.

2. Traduci il comportamento revisionato in un test sintetico. [role-transfer.scenario.json](role-transfer.scenario.json) è un esempio complementare scritto a mano, **non un'esportazione automatica** del piano. Invia un evento sintetico “spegni tavolo”, si aspetta una chiamata al ruolo sostitutivo e vieta di spegnere il vecchio hardware. Verifica inoltre che il vecchio hardware resti acceso. Dalla directory di questa guida, con il runner installato nel proprio ambiente:

   ```sh
   ha-scenario validate role-transfer.scenario.json
   ha-scenario run role-transfer.scenario.json
   ```

   Questo esempio è identico byte per byte al [fixture di trasferimento del ruolo](https://github.com/ha-homelab/ha-scenario-tests/blob/0ea7e5a5d24dc89ebe896b1a2387396b3fce18f4/tests/fixtures/role_transfer.json) testato nel [run Linux riuscito](https://github.com/ha-homelab/ha-scenario-tests/actions/runs/38843681199). Il suo SHA-256 è `bb8544517eeb4895b80b049cf9e242d04635e7785bd198c1d57a7cf3f5fc8ab4`. Il precedente errore di chiusura su macOS resta documentato e non viene contato come un run superato.

   Lo scenario usa il vero motore HA con callback degli attuatori in memoria. Il superamento dimostra il comportamento del motore per quella sequenza sintetica, non la consegna radio, la chiusura dei contatti o l'alimentazione di un apparecchio. Un solo evento non copre l'intera configurazione domestica.

3. Aggiungi sequenze di errore pertinenti prima della distribuzione: assenza interrotta dall'indisponibilità del sensore, mantenimento manuale, ricaricamento dell'automazione, trigger duplicati e stato ripristinato. Gli esempi del runner coprono presenza, mantenimento manuale, input obsoleti e riconciliazione dopo il ricaricamento. L'orologio misura tempo realmente trascorso: un fixture breve non valida un intervallo di venti minuti in produzione. HA documenta che le attese `for` non sopravvivono a riavvio/ricaricamento; scegli e testa riconciliazione esplicita o scadenze persistenti quando necessario. [Documentazione dei trigger HA](https://www.home-assistant.io/docs/automation/trigger/)

4. Esamina le evidenze dei misuratori in modo indipendente. Dal relativo repository:

   ```sh
   ha-meter-contracts check examples/valid-three-meters.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/kmc-shared-meter.json --at 2026-01-01T12:00:05Z --json
   ha-meter-contracts check examples/duplicate-emporia.json --at 2026-01-01T12:00:05Z --json
   ```

   L'esempio valido riesce. Gli altri due terminano intenzionalmente con codice 1: rispettivamente per l'attribuzione a una singola presa della misura dell'intera ciabatta e per rappresentazioni duplicate della stessa fonte. Considerali errori attesi negli script di esempio. Non usare i watt dell'intera ciabatta in una soglia di protezione calibrata solo per una pompa. Calibrare la tensione non significa calibrare corrente o potenza. Le evidenze mancanti o obsolete restano non disponibili, non diventano zero. [Semantica HA di sensori e statistiche](https://developers.home-assistant.io/docs/core/entity/sensor/#long-term-statistics)

5. Se la voce è un trigger o un canale di feedback, valuta separatamente le evidenze nel repository vocale:

   ```sh
   assist-lab evaluate examples/synthetic-pass.json
   assist-lab evaluate examples/synthetic-incomplete.json
   ```

   L'esempio incompleto termina intenzionalmente con codice 3 perché il completamento dell'API non basta a dimostrare l'udibilità. Un benchmark reale richiede consenso alla registrazione, orologio e metodo dichiarati, condizioni comparabili e osservazione indipendente dell'azione e della risposta udibile. Non pubblicare registrazioni domestiche, trascrizioni o token esportati. Il primo blocco audio del server non è il primo suono percepito dall'ascoltatore. [Pipeline HA Assist](https://developers.home-assistant.io/docs/voice/pipelines/)

6. Conserva ogni report con la modifica revisionata. Applica attraverso la procedura di revisione/distribuzione stabilita per l'installazione, poi esegui l'accettazione specifica del dispositivo. Accensione e spegnimento fisici, polarità dell'indicatore, riavvio, tempo della fonte e calibrazione per grandezza richiedono osservazioni reali. Questi quattro strumenti non eseguono né sostituiscono quel passaggio.

## Che cosa non dimostrano le verifiche

Stato configurato, chiamata di servizio accettata, assorbimento osservato e flusso d'acqua sono evidenze distinte. Un misuratore totale di tre carichi non identifica quale abbia assorbito potenza. Uno stato sintetico “spento” non dimostra che i contatti del relè si siano aperti. Né il misuratore né il test di scenario sono controllori di sicurezza per acqua, riscaldatori, accesso o altri carichi con conseguenze rilevanti.

Gli strumenti non impongono i risultati reciproci. Un'integrazione futura può utilizzare il loro JSON stabile, ma deve definire esplicitamente livelli di avviso accettati, compatibilità di versione e significato di “evidenze complete”. Non ridurre `ready`, `available`, `passed` e `audible` a un unico booleano intercambiabile.

## Roadmap: quattordici idee con uno stato realistico

I primi quattro risultati software seguenti sono disponibili come strumenti offline iniziali. Tutti gli sviluppi successivi nominati rimangono proposte; il nome di un repository o un diagramma non significa che l'hardware sia stato messo in servizio.

1. **Migrazioni dei ruoli — strumento iniziale implementato.** Estendi i formati di riferimento supportati solo con test di andata e ritorno e dei conflitti; conserva il confine esplicito per input non supportati.
2. **Contratti dei misuratori — strumento iniziale implementato.** Sperimenta osservazioni reali private con timestamp; misura corrente e potenza indipendentemente prima di dichiararne la calibrazione. L'attribuzione per presa richiede ancora evidenze per presa.
3. **Test degli scenari di automazione — strumento iniziale implementato.** Aggiungi policy revisionate e casi di riavvio/scadenza; verifica separatamente i tempi di durata produttiva quando necessario.
4. **Evidenze vocali — strumento iniziale implementato; benchmark fisico in attesa.** Seleziona satelliti, metodo di osservazione e consenso alla registrazione prima di raccogliere sessioni comparabili. Nessuna classifica hardware per ora.
5. **Coordinamento della qualità dell'aria — verifica di sensori/attuatori in attesa.** Controlla se il dispositivo misura CO₂ o particelle, età e accuratezza e che cosa possano influenzare ventilazione o filtraggio. Conferma le condizioni esterne prima di definire una policy di ventilazione.
6. **Evidenze radar/presenza — messa in servizio hardware in attesa.** Verifica scheda LD2450, alimentazione, involucro, protocollo e copertura. I bersagli non sono identità umane e l'età della ricezione non è la latenza misurata del sensore. CSI resta sperimentale.
7. **Osservabilità di acqua/pompa — evidenze indipendenti in attesa.** Distingui autorizzazione ad alimentare la pompa, assorbimento elettrico, flusso e livello dell'acqua. Un misuratore aggregato della ciabatta non può fornire un segnale di protezione mancante specifico della pompa. Evita tentativi automatici ripetuti per comandi critici senza stato osservato e revisione specifica dell'installazione.
8. **Telemetria BLE — proxy compatibili e test di copertura in attesa.** Valida sensori effettivi, intervallo di temperatura, batterie e posizionamento. I dispositivi ESP8266 non sono proxy BLE; RSSI non è identità né credenziale di sblocco. [Proxy Bluetooth ESPHome](https://esphome.io/components/bluetooth_proxy/)
9. **Spiegazioni basate sulla presenza ed elettrodomestici — verifica delle capacità in attesa.** Spiega quale osservazione ha mantenuto accesa una luce; usa eventi reali di lavatrice/asciugatrice se supportati. Non dedurre un ciclo solo da un misuratore condiviso e non inventare confidenza statistica da flag di sensori non correlati.
10. **Bridge Z-Wave — consegna/assemblaggio e accettazione radio in attesa.** La [guida ZAC93 + ESP32](https://github.com/ha-homelab/zac93-esp32) è un percorso hardware separato. Verifica cablaggio, frequenza regionale, trasporto seriale e inclusione Z-Wave JS sulla scheda reale. Il supporto Long Range del controller non trasforma un sensore precedente in un dispositivo Long Range. [Guida Z-Wave JS](https://zwave-js.github.io/zwave-js/#/getting-started/index)
11. **Accettazione delle prese ESPHome — test individuali hardware in attesa.** Registra evidenze di pulsante, relè, indicatore e riavvio per ogni revisione, oltre a calibrazioni distinte di tensione/corrente/potenza. Un flashing riuscito non completa l'accettazione. Nessun ciclo di alimentazione di massa non sorvegliato sugli apparecchi collegati.
12. **Benchmark delle previsioni — dati accumulati in attesa.** Archivia le previsioni emesse e i valori reali successivi, conserva l'ora di emissione e valuta gli orizzonti senza contaminazione da dati futuri. Serve tempo di osservazione trascorso, non una dichiarazione di risparmio energetico ricavata da un esempio sintetico.
13. **Comandi ospite limitati — revisione dei permessi backend in attesa.** Verifica identità e autorizzazione lato server. Nascondere i comandi nella dashboard non limita l'accesso. Non indebolire l'autenticazione per semplificare un pannello.
14. **Pianificazione dei carichi differibili — vincoli e capacità misurati in attesa.** Integra strumenti di pianificazione consolidati dopo aver validato misuratori, feedback di stato e previsioni. Conferma quali carichi possano essere differiti o modulati, le scadenze e gli override manuali. Inizia con raccomandazioni revisionate, senza risparmi speculativi o garanzie di sicurezza. [EMHASS](https://emhass.readthedocs.io/en/latest/emhass.html) · [evcc](https://docs.evcc.io/en/)

## Contribuire e riprodurre questa guida

Questa panoramica, lo scenario sintetico e il diagramma sono materiale originale con licenza MIT; vedi [LICENSE](LICENSE). Ricrea tutti gli SVG localizzati con `python3 render_architecture.py`. Non contengono immagini esterne, script, identificatori domestici o dati domestici misurati. Il [percorso visuale](process-and-results.it.md#reproduce-or-translate-the-illustrations) spiega i dati sorgente e le verifiche di rigenerazione. Mantieni sintetici i fixture pubblici e le esportazioni private fuori da Git. Per modifiche, segui le indicazioni di sicurezza e contribuzione del repository.
