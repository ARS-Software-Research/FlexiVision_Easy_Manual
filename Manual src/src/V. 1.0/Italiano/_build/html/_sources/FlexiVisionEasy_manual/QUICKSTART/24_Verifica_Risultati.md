
# **Monitoraggio Applicazione: Dashboard**

La **Dashboard** è l'interfaccia principale per il monitoraggio in tempo reale del sistema FlexiVision Easy. In questa pagina è possibile verificare l'efficienza del processo, analizzare i tempi di ciclo, validare il riconoscimento dei componenti e identificare eventuali colli di bottiglia nel sistema.

```{note}
**Accesso Dashboard**

La Dashboard è accessibile dal menu principale del software FlexiVision Easy.

Utilizzare questa interfaccia durante:
- Test iniziali di validazione sistema
- Ottimizzazione parametri in fase di messa a punto
- Monitoraggio produzione per verifica performance
- Troubleshooting problemi di produttività
```

---

## Panoramica Interfaccia

L'interfaccia della Dashboard si divide in quattro sezioni principali:

1. **Controllo Operativo**: Comandi e stato esecuzione
2. **Analisi Riconoscimento**: Visualizzazione pezzi rilevati e dettagli
3. **Indicatori Performance**: Connettività e tempi ciclo
4. **Analisi Grafica**: Grafici storici produttività e tempi

---

## Controllo Operativo

### Comandi e stato esecuzione

```{list-table}
:header-rows: 1
:widths: 25 75

* - Elemento
  - Descrizione e Funzione
* - **In Run**
  - Indicatore di stato che segnala se il sistema è attualmente in funzione.  
    **Verde** 🟢: Sistema attivo e operativo.  
    **Rosso** 🔴: Sistema arrestato o in pausa.
* - **In Run Time**
  - Visualizza il tempo totale di attività del sistema dalla pressione del tasto Start. Utile per calcolare produttività oraria e uptime del sistema.
* - **Selettore FlexiBowl**
  - Menu a tendina per selezionare l'unità FlexiBowl specifica da monitorare. Utilizzato in sistemi multi-dispositivo con più FlexiBowl gestiti dalla stessa istanza FlexiVision.
* - **Test**
  - Avvia un ciclo continuo di movimentazione (disco FlexiBowl e tramoggia Hopper se presente) fino al rilevamento dei componenti nell'area di visione.   
    Utile per test rapidi senza integrazione robot.
* - **One Run**
  - Esegue un singolo ciclo completo: movimentazione disco → acquisizione immagine → analisi modello. 
    Utile per debug e verifica step-by-step del processo.
```

```{tip}
**Utilizzo comandi di test**

**Test (ciclo continuo)**:
- Usare durante ottimizzazione parametri FlexiBowl
- Permette di vedere effetto immediato delle modifiche
- Fermare manualmente quando soddisfatti

**One Run (ciclo singolo)**: resterà nella versione finale?
- Usare per analisi dettagliata di ogni step
- Ideale per troubleshooting problemi specifici
- Permette ispezione accurata di ogni immagine acquisita

In produzione normale, questi comandi non vengono utilizzati (il robot comanda i cicli tramite TCP/IP).
```

---

## Analisi della Visione

Al centro della dashboard vengono riportati i dati relativi ai componenti identificati dal sistema di visione.

### Detected Vision Parts

**Detected Vision Parts** mostra:
- Immagine acquisita in tempo reale dalla camera
- Overlay grafico dei componenti riconosciuti (riquadri colorati)
- Identificativi (Id) di ogni componente rilevato
- Region Search visibile come contorno
- Istogrammi visualizzati come riquadri colorati (verde/rosso)

Include anche un **grafico storico** dei rilevamenti negli ultimi 30 secondi che mostra l'andamento del numero di pezzi riconosciuti per acquisizione.


```{note}

Il numero di componenti visualizzati nel riquadro *Detected Vision Parts* dipende direttamente dai parametri di comunicazione configurati in **Protocol Setup**.

Per modificare quanti pezzi vengono processati e visualizzati, consultare [Protocol Setup](15_Protocol_Setup.md).
```

### Tabella Modelli Rilevati

**Dettaglio componenti riconosciuti**

La tabella sotto l'immagine elenca tutti i componenti presenti nell'area di pick con i seguenti parametri:

```{list-table}
:header-rows: 1
:widths: 15 20 65

* - Campo
  - Tipo Dato
  - Descrizione
* - **Id**
  - Intero
  - Identificativo univoco progressivo del componente (0, 1, 2, ...).   
  Id 0 = componente con score più alto (migliore corrispondenza al modello).
* - **X**
  - Millimetri
  - Coordinata X del componente nel sistema di riferimento camera/FlexiBowl. Origine tipicamente al centro del disco.
* - **Y**
  - Millimetri
  - Coordinata Y del componente nel sistema di riferimento camera/FlexiBowl.
* - **Rot (Rotation)**
  - Gradi
  - Angolo di rotazione del componente rispetto all'orientamento del modello originale. Range 0-360°.
* - **Score**
  - Percentuale
  - Valore percentuale (0.00-1.00 o 0%-100%) che esprime il grado di affidabilità del riconoscimento. Rappresenta la vicinanza/fedeltà rispetto al modello di riferimento. Score più alto = corrispondenza migliore.
```

```{list-table}
**Interpretazione Score**

**Score > 0.90 (90%)**:
- Eccellente corrispondenza al modello
- Pezzo sicuramente corretto e ben orientato
- Picking ad alta confidenza

**Score 0.80-0.90 (80-90%)**:
- Buona corrispondenza
- Pezzo probabilmente corretto con lievi variazioni
- Picking sicuro se Accept Threshold configurato appropriatamente

**Score 0.70-0.80 (70-80%)**:
- Corrispondenza accettabile
- Potrebbe essere variante dimensionale o orientamento limite
- Verificare consistenza nel tempo

**Score < 0.70 (< 70%)**:
- Corrispondenza scarsa
- Potrebbe essere pezzo sbagliato o molto diverso dal training
- Se ricorrente, rivedere modello o Accept Threshold

**Best practice**: Monitorare che gli score siano consistentemente sopra la soglia di Accept Threshold impostata durante la configurazione modello.
```

---

## Indicatori di Stato e Performance

### Connettività

Indicatori di stato delle comunicazioni con i dispositivi esterni:

```{list-table}
:header-rows: 1
:widths: 25 75

* - Indicatore
  - Descrizione
* - **FlexiBowl**
  - Stato della connessione hardware tra il VisionController (PC) e il controller del FlexiBowl. **Verde**: Connesso e comunicante. **Rosso**: Disconnesso o errore comunicazione.
* - **Robot**
  - Stato della comunicazione TCP/IP con il robot o PLC incaricato del prelievo. **Verde**: Connessione TCP stabilita. **Rosso**: Disconnesso o timeout comunicazione.
```

```{warning}
**Azioni in caso di disconnessione**

**FlexiBowl rosso**:
- Verificare cavo Ethernet FlexiBowl → VisionController
- Controllare alimentazione FlexiBowl
- Verificare IP FlexiBowl in FlexiBowl Setup
- Tentare reconnect o riavvio software

**Robot rosso**:
- Verificare cavo Ethernet Robot → VisionController
- Controllare che robot abbia aperto connessione TCP
- Verificare porta TCP/IP in Robot Setup
- Controllare programma robot (deve aprire socket)

In produzione, entrambi gli indicatori devono essere sempre verdi.
```

### Analisi dei Tempi

Il sistema fornisce un breakdown dettagliato dei tempi di ciclo per individuare eventuali colli di bottiglia e ottimizzare il processo.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Voce Temporale
  - Descrizione
* - **Camera Processing Time**
  - Tempo impiegato per l'acquisizione dell'immagine dal sensore camera. Include tempo di esposizione e trasferimento dati. 
    >Tipico: 50-150 ms.
* - **Locator Processing Time**
  - Tempo necessario all'algoritmo di visione per localizzare e riconoscere i componenti nell'immagine acquisita. Dipende da: numero modelli attivi, complessità modelli, numero istogrammi. 
    >Tipico: 100-500 ms.
* - **Total Vision Processing**
  - Somma dei tempi di Camera e Locator. Rappresenta il tempo totale che il sistema di visione impiega per elaborare un'immagine.       
    >Tipico: 150-650 ms.
* - **Total FlexiBowl Time**
  - Tempo impiegato dal FlexiBowl per eseguire una sequenza di movimentazione completa (Move + Shake + Flip + eventuali pause). Include tempo movimento fisico del disco. 
    >Tipico: 1-5 secondi.
* - **Total Robot Time**
  - Tempo stimato o rilevato per l'operazione di Pick & Place completa del robot. Include: avvicinamento → presa → sollevamento → deposito → ritorno. 
    >Tipico: 2-10 secondi (dipende fortemente da robot e applicazione).
* - **Total Processing Time**
  - Tempo totale del ciclo completo (Vision + FlexiBowl + Robot). Rappresenta il tempo dall'inizio di un ciclo all'inizio del successivo. Determina la produttività massima teorica (PPM).
```

```{tip}
**Interpretazione tempi per ottimizzazione**

Il grafico dei tempi permette di identificare il **collo di bottiglia** del sistema:

**Se Total Vision Processing è il maggiore**:
- Troppi modelli attivi → Disabilitare modelli non necessari
- Modelli troppo complessi → Semplificare con Feature Threshold più alto
- Troppi istogrammi → Ridurre numero o dimensione istogrammi
- Camera Processing alto → Ridurre risoluzione o tempo esposizione

**Se Total FlexiBowl Time è il maggiore**:
- Sequenza movimentazione troppo lenta → Aumentare velocità in Config FlexiBowl
- Angolo rotazione eccessivo → Ridurre Move Angle
- Troppe pause → Ottimizzare sincronizzazione Flip/Move
- Shake troppo lungo → Ridurre cicli shake

**Se Total Robot Time è il maggiore**:
- Traiettoria robot non ottimizzata → Ottimizzare path planning robot
- Velocità robot troppo bassa → Aumentare velocità movimento (se sicuro)
- Distanza deposito eccessiva → Riposizionare punto deposito più vicino
- Tempi di presa troppo lunghi → Ottimizzare apertura/chiusura gripper

**Obiettivo ottimizzazione**: Bilanciare i tre tempi per ridurre Total Processing Time complessivo.
```

---

## Analisi Grafica

I grafici nella parte inferiore della dashboard permettono un'analisi predittiva e diagnostica delle performance del sistema nel tempo.

### 1. Parts Per Minute (PPM)

**Grafico produttività**

Mostra la produttività media del sistema espressa in **componenti prelevati al minuto** (Parts Per Minute).

**Caratteristiche**:
- Asse X: Tempo (ultimi minuti/ore)
- Asse Y: PPM (pezzi/minuto)
- Linea trend: Media mobile per identificare tendenze

**Utilizzo**:
- Monitorare stabilità produttività nel tempo
- Identificare degradazioni performance
- Calcolare throughput effettivo vs teorico


```{tip}
**Interpretazione PPM**

**PPM costante e stabile**:
- ✓ Sistema ben configurato
- ✓ Parametri ottimizzati
- ✓ Nessun collo di bottiglia critico

**PPM in diminuzione progressiva**:
- ⚠️ Possibile usura componenti (superficie grip FlexiBowl)
- ⚠️ Hopper che si svuota (se presente, meno pressione = scarico più lento)
- ⚠️ Accumulo sporcizia su camera/illuminazione

**PPM con fluttuazioni ampie**:
- ⚠️ Instabilità nel processo
- ⚠️ Problemi intermittenti di riconoscimento
- ⚠️ Interferenze esterne (vibrazioni, luce variabile)

**Azioni correttive**:
- Analizzare correlazione con grafici tempi
- Identificare quale componente (Vision/FlexiBowl/Robot) causa variazioni
- Intervenire su parametri specifici
```

### 2. Fill Hopper

**Grafico attivazioni tramoggia**

Rappresenta lo storico degli impulsi di scarico inviati alla tramoggia (Hopper), utile per monitorare l'autonomia del magazzino componenti.

**Caratteristiche**:
- Asse X: Tempo
- Asse Y: Attivazioni Hopper (eventi)
- Picchi: Ogni picco rappresenta un'attivazione scarico

**Utilizzo**:
- Prevedere quando ricaricare Hopper fisicamente
- Verificare efficacia configurazione Hopper
- Identificare anomalie nel comportamento scarico


```{tip}
**Analisi pattern Fill Hopper**

**Attivazioni regolari e costanti**:
- ✓ Configurazione Hopper ottimale
- ✓ Flusso pezzi stabile e prevedibile
- ✓ Autonomia calcolabile (es: attivazione ogni 10 min)

**Attivazioni sempre più frequenti**:
- ⚠️ Hopper si sta svuotando (meno pezzi = più attivazioni per mantenere livello)
- ⚠️ Time scarico insufficiente per volume ridotto
- **Azione**: Pianificare ricarica Hopper a breve

**Nessuna attivazione per lungo periodo**:
- ⚠️ Robot fermo o rallentato (pezzi non vengono consumati)
- ⚠️ Possibile problema sistema che non richiede pezzi
- **Azione**: Verificare stato produzione

**Attivazioni molto ravvicinate (burst)**:
- ⚠️ Soglia Hopper mal configurata (troppo alta)
- ⚠️ Steps insufficienti (pezzi non arrivano in tempo)
- **Azione**: Rivedere Config Hopper
```

### 3. Vision - FlexiBowl - Robot (Grafico Comparativo)

**Grafico tempi sovrapposti**

Un grafico comparativo a tre linee che sovrappone i tempi dei singoli processi nel tempo.

**Linee visualizzate**:
- **Linea blu**: Total Vision Processing
- **Linea verde**: Total FlexiBowl Time
- **Linea rossa**: Total Robot Time

**Utilizzo**: Identificare istantaneamente quale processo influenza maggiormente il tempo di ciclo totale e come varia nel tempo.

```{tip}
**Questo grafico è fondamentale per il tuning**

Permette di capire istantaneamente:

**Quale processo domina il ciclo**:
- Se linea Robot sempre più alta → Robot è collo di bottiglia
- Se linea FlexiBowl sempre più alta → Movimentazione da ottimizzare
- Se linea Vision sempre più alta → Elaborazione immagini troppo lenta

**Variazioni nel tempo**:
- Linea Vision che cresce gradualmente → Possibile degrado performance (memoria, CPU)
- Linea FlexiBowl che oscilla → Comportamento pezzi non costante
- Linea Robot instabile → Problemi intermittenti robot (interferenze, ritardi comunicazione)

**Bilanciamento ottimale**:
- Idealmente, le tre linee dovrebbero essere relativamente bilanciate
- Nessuna linea dovrebbe dominare eccessivamente (>2x le altre)
- Se una linea è 3-5x le altre, concentrare ottimizzazione su quel processo

**Esempio lettura**:

Vision: 300 ms (costante)
FlexiBowl: 2000 ms (costante)
Robot: 8000 ms (variabile 6000-10000)

Interpretazione: Robot è chiaro collo di bottiglia. 
Azione: Ottimizzare programma robot, ridurre traiettorie, aumentare velocità.

```

---

## Monitoraggio Qualità

### Indicatori critici da monitorare

**Score dei componenti**

Assicurarsi che lo **Score** dei componenti rilevati sia costantemente sopra la soglia di tolleranza (Accept Threshold) impostata durante la configurazione modello.

**Monitoraggio Score**:
- Controllare periodicamente tabella Modelli Rilevati
- Verificare che score tipici siano 0.85-0.95
- Investigare se score scendono sotto 0.80 regolarmente

**Score in diminuzione progressiva**:
- ⚠️ Pezzi reali diversi da quello di training (variazioni produzione)
- ⚠️ Illuminazione cambiata (backlight più debole, sporcizia)
- ⚠️ Camera non più a fuoco (vibrazioni, urti)
- ⚠️ Superficie FlexiBowl sporca (pattern interferente)

**Azioni correttive**:
- Pulire camera, illuminazione, superficie FlexiBowl
- Verificare messa a fuoco camera
- Considerare re-training modello se pezzi sono cambiati
- Ridurre Accept Threshold se score sono comunque affidabili ma più bassi


---

## Best Practices Monitoraggio Produttivo

### Check giornalieri

**All'avvio produzione** (5 minuti):
- Verificare indicatori connettività FlexiBowl e Robot (verdi)
- Controllare che primi cicli mostrino score normali (>0.85)
- Osservare che PPM si stabilizzi su valore atteso

**Durante produzione** (check ogni 1-2 ore):
- Dare un'occhiata a PPM per verificare stabilità
- Controllare Fill Hopper per prevedere ricarica necessaria
- Verificare assenza errori o warning nel log

**A fine turno** (2 minuti):
- Annotare PPM medio del turno
- Controllare numero attivazioni Hopper
- Verificare eventuali anomalie o eventi
- Confrontare con dati giorno precedente

Questa routine minima garantisce identificazione rapida di problemi e mantiene tracciabilità performance.

### Report performance

```{tip}
**Metriche chiave da tracciare**

Per valutazione performance nel tempo, tracciare:

**Giornalmente**:
- PPM medio del turno
- Numero pezzi totali prelevati
- Numero attivazioni Hopper
- Downtime totale (e cause)

**Settimanalmente**:
- Trend PPM (in aumento/diminuzione?)
- Confronto PPM teorico vs reale
- Score medio componenti rilevati
- Eventuali modifiche configurazione e loro impatto

**Mensilmente**:
- Overall Equipment Effectiveness (OEE)
- Analisi colli di bottiglia principali
- Necessità di manutenzione predittiva
- ROI del sistema

Questi dati permettono ottimizzazione continua e giustificano investimenti in miglioramenti.
```

---

## Prossimi Passi

Una volta validato il sistema tramite Dashboard:

**→ [Troubleshooting](26_trb_shooting_guide.md)** - Guida risoluzione problemi comuni

**→ [Support](27_Support.md)** - Contatti assistenza tecnica

```{tip}
**Sistema operativo!**

Congratulazioni! Il sistema FlexiVision Easy è ora completamente configurato, ottimizzato e validato per la produzione.

**Riepilogo percorso completato:**
- ✓ Setup hardware (FlexiBowl, Robot, Camera)
- ✓ Calibrazione completa (Camera, Robot)
- ✓ Modelli pezzo creati e ottimizzati
- ✓ FlexiBowl configurato per movimentazione ottimale
- ✓ Hopper configurato per alimentazione automatica (se presente)
- ✓ Sistema validato con monitoraggio Dashboard
- ✓ Performance verificate e stabili

Il sistema è pronto per operare in produzione con supervisione minima. Utilizzare la Dashboard per monitoraggio continuo e ottimizzazione nel tempo.

**Tempo totale investito**: 4-8 ore (primo sistema completo)

**Risultato**: Sistema di picking robotizzato completamente autonomo e ottimizzato!
```