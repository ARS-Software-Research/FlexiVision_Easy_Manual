# **Configurazione Protocollo Comunicazione: Protocol Setup**

La pagina **Protocol Setup** permette di configurare i parametri che regolano il flusso di comunicazione e lo scambio dati tra il sistema di visione FlexiVision Easy e il robot. Questi parametri determinano quanti oggetti vengono inviati, come vengono ordinati, e come il sistema gestisce le statistiche e gli stati operativi.

```{note}
**Quando configurare Protocol Setup**

La configurazione di Protocol Setup è consigliata:
- **Durante commissioning e startup**: Dopo aver completato calibrazione camera e robot
- **Dopo primi test produzione**: Per tuning fine basato su comportamento reale sistema
- **Prima di produzione continua**: Per ottimizzare statistiche e metriche Dashboard
```

---

## Funzione e Importanza Protocol Setup

### Ruolo nel sistema

I parametri di Protocol Setup definiscono:

1. **Quanti oggetti inviare al robot**: Numero massimo e minimo di coordinate per ciclo
2. **Come ordinarli**: Priorità di prelievo (score, posizione, ecc.)
3. **Calcolo statistiche**: Metriche di produttività e performance
4. **Gestione stati sistema**: Quando il sistema passa da RUN a IDLE

Questi parametri sono **fondamentali** per:
- Ottimizzare il throughput (pezzi/minuto)
- Calcolare correttamente le metriche di produzione
- Garantire sincronizzazione corretta robot-visione
- Visualizzare dati accurati nella Dashboard


### Impatto sulla Dashboard

Le modifiche ai parametri di Protocol Setup influenzano la Dashboard principalmente in termini di:

**Statistiche visualizzate:**
- Numero prese robot per ciclo
- Tempo ciclo totale
- Parts Per Minute (PPM)
- Grafici storici produttività

**Stati operativi:**
- Transizioni RUN → IDLE
- Tempo "In Run"
- Sincronizzazione visione-robot

**KPI (Key Performance Indicators):**
- Overall Equipment Effectiveness (OEE)
- Utilizzo robot
- Efficienza sistema

**Comportamento ciclo:**
- Stabilità comunicazione robot-visione
- Gestione timeout e code

---

## Accesso Protocol Setup

1. Dal menu principale, accedere alla sezione dedicata al protocollo di comunicazione
2. Selezionare **Protocol Setup**
3. Si apre l'interfaccia con i parametri configurabili

```{note}
La posizione esatta del menu Protocol Setup può variare leggermente in base alla versione del software. Consultare l'interfaccia o il supporto tecnico se non immediatamente visibile.
```
---

## Parametri Configurabili

### Panoramica parametri principali

I parametri di Protocol Setup si dividono in due categorie: parametri di flusso dati e parametri statistici.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Parametro
  - Descrizione e Funzione
* - **Max Object Count Return**
  - Indica il numero **massimo** di oggetti/coordinate che il sistema di visione può restituire al robot in una singola run (ciclo di elaborazione). Se la visione rileva più oggetti di questo limite, ne vengono inviati al massimo questo numero, selezionati in base al criterio di ordinamento configurato (Sorting Mode).
* - **Min Object Count Return**
  - Indica il numero **minimo** di oggetti che devono essere rilevati in una run del sistema di visione affinché il risultato venga considerato valido (OK). Se il numero di oggetti rilevati è inferiore a questa soglia, la run viene considerata non valida e tipicamente viene attivata una sequenza di recupero (es: movimentazione FlexiBowl, attivazione Hopper).
* - **Sorting Mode Results**
  - Definisce il **criterio di ordinamento** con cui viene ordinata la lista degli oggetti restituiti dalla visione. Opzioni tipiche: per score (dal più alto al più basso), per coordinata X crescente/decrescente, per coordinata Y crescente/decrescente, per distanza da un punto di riferimento. Questo parametro determina la priorità di prelievo degli oggetti e influisce direttamente su quali vengono inclusi nel "Max Object Count Return".
* - **Pickable parts by the robot detected by vision in each cycle**
  - Parametro utilizzato per il **calcolo delle statistiche di produzione**. Indica il numero di prese effettive che il robot effettua per ogni run della visione. Esempio: se il robot preleva 2 pezzi simultaneamente con una pinza doppia, impostare valore 2. **Importante**: Non rappresenta il numero di oggetti rilevati dalla visione, ma il numero di pezzi effettivamente prelevati dal robot per ciclo. Usato per calcolo PPM (Parts Per Minute).
* - **Maximum processing time per part with the robot (in seconds)**
  - Parametro utilizzato per **statistiche e gestione del flusso di lavoro**. Definisce il tempo massimo dopo il quale il sistema considera conclusa la gestione/invio delle coordinate relative a una run e passa tipicamente dallo stato RUN allo stato IDLE. **Non è un timeout di errore del robot**, ma un riferimento temporale per il calcolo del ciclo e per le metriche di produttività. Influenza la visualizzazione dello stato "In Run" nella Dashboard.
```

---

## Configurazione Dettagliata Parametri

### Max Object Count Return

#### **Funzione**: Limita quante coordinate vengono inviate al robot per ogni ciclo di visione.

#### **Valori tipici:**
- **1-3 oggetti**: Configurazione più comune per robot con picking singolo o doppio
- **4-8 oggetti**: Per sistemi con buffer o robot veloci che possono gestire code
- **>8 oggetti**: Raramente necessario, può saturare la comunicazione


```{tip}
**Come scegliere il valore:**
1. Considerare la velocità del robot (tempo pick&place per pezzo)
2. Considerare il tempo ciclo visione + FlexiBowl
3. Formula approssimativa: `Max Count = (Tempo ciclo visione+FB) / (Tempo pick robot)`

**Esempio pratico:**
- Ciclo visione+FlexiBowl: 3 secondi
- Tempo pick robot: 2 secondi/pezzo
- Max Count ottimale: 3/2 = 1.5 → Arrotondare a 2 oggetti
```

#### **Ottimizzazione Max Object Count**

**Valore troppo basso** (es: 1 quando robot è veloce):
- Effetto: Robot attende spesso la visione (idle time)
- Sintomo: Dashboard mostra robot time basso rispetto a vision time
- Soluzione: Aumentare gradualmente e monitorare throughput

**Valore troppo alto** (es: 10 quando robot è lento):
- Effetto: Sovraccarico comunicazione, coordinate mai utilizzate
- Sintomo: Molte coordinate inviate ma non tutte prelevate
- Soluzione: Ridurre a valore realistico

**Valore ottimale**:
- Robot sempre ha 1-2 coordinate disponibili
- Nessun idle time significativo
- Nessuna saturazione comunicazione

### Min Object Count Return

#### **Funzione**: Definisce quando una run di visione è considerata "successo" vs "fallimento".

#### **Valori tipici:**
- **1**: Configurazione più comune - anche un solo pezzo valido è accettabile
- **2-3**: Per applicazioni che richiedono efficienza alta (evitare cicli con pochi pezzi)
- **>3**: Raro, solo per applicazioni speciali con multi-pick obbligatorio

#### **Comportamento sistema:**
- **Oggetti rilevati ≥ Min Count**: Run OK, coordinate inviate a robot
- **Oggetti rilevati < Min Count**: Run NON OK, attivazione recupero (FlexiBowl shake, Hopper)

```{tip}
**Come scegliere il valore:**
- Se robot può lavorare anche con 1 pezzo → Min Count = 1
- Se si vuole forzare riempimento prima del picking → Min Count = 2-3
```

#### **Impatto sulla produttività**

**Min Count = 1** (più permissivo):
- ✓ Massima flessibilità, robot lavora sempre se c'è almeno 1 pezzo
- ✓ Throughput più alto in condizioni di scarso riempimento
- ✗ Possibili cicli con efficienza bassa (1 pezzo ogni N secondi)

**Min Count = 3** (più restrittivo):
- ✓ Garantisce efficienza minima per ciclo
- ✓ Riduce cicli "sprecati" con pochi pezzi
- ✗ Può causare attese se riempimento è variabile
- ✗ Throughput ridotto se sistema non mantiene sempre ≥3 pezzi

**Regola generale**: Iniziare con Min Count = 1, aumentare solo se si verificano troppi cicli con efficienza bassa.

### Sorting Mode Results


```{list-table}
:header-rows: 1
:widths: 30 70

* - Modalità Sorting
  - Descrizione e Quando Usare
* - **By Score (Descending)**
  - Ordina per score dal più alto al più basso. Oggetti con migliore corrispondenza al modello vengono inviati per primi. **Più comune e consigliato**: Garantisce sempre prelievo dei pezzi con riconoscimento più affidabile.
* - **By X Coordinate (Ascending)**
  - Ordina per coordinata X crescente (da sinistra a destra). Utile se robot ha preferenza di picking sequenziale lungo un asse.
* - **By X Coordinate (Descending)**
  - Ordina per coordinata X decrescente (da destra a sinistra).
* - **By Y Coordinate (Ascending)**
  - Ordina per coordinata Y crescente (dal basso verso l'alto nell'immagine).
* - **By Y Coordinate (Descending)**
  - Ordina per coordinata Y decrescente (dall'alto verso il basso).
* - **By Distance from Center**
  - Ordina per distanza dal centro del FlexiBowl. Pezzi più centrali vengono inviati per primi. Utile per massimizzare stabilità (pezzi centrali meno soggetti a movimento).
```

```{tip}
**Scelta Sorting Mode ottimale**

**Consigliato nella maggior parte dei casi: By Score (Descending)**

**Vantaggi**:
- Massima affidabilità: robot preleva sempre i pezzi riconosciuti meglio
- Riduce rischio di picking errati
- Indipendente dalla posizione fisica

**Alternative valide**:

1. **By Distance from Center**:
- Se i pezzi ai bordi tendono a muoversi durante il picking
- Per massimizzare stabilità meccanica

2. **By X/Y Coordinate**:
- Se il robot ha traiettorie ottimizzate per picking sequenziale
- Per minimizzare movimenti robot (picking "ordinato" invece che casuale)
- Raramente usato, solo per ottimizzazioni avanzate
```

```{note}
La modalità di sorting interagisce con Max Object Count. I primi N oggetti (secondo il criterio) vengono inviati.
```

### Pickable parts by the robot


**Prese robot per ciclo visione**

#### **Funzione**: Parametro statistico che indica quanti pezzi vengono **effettivamente prelevati** dal robot per ogni ciclo di visione.

#### **Valori tipici:**
- **1**: Robot con gripper singolo, preleva 1 pezzo alla volta (più comune)
- **2**: Robot con gripper doppio o pinza multi-punto che preleva 2 pezzi simultaneamente
- **>2**: Sistemi speciali con multi-pick (raro)

```{important}
Questo valore rappresenta le **prese fisiche**, non gli oggetti rilevati dalla visione.
```
**Esempio chiarificatore:**
Scenario: Visione rileva 5 oggetti, Max Count = 3, Gripper doppio

- Vision rileva: 5 oggetti
- Invia al robot: 3 oggetti (Max Count)
- Robot preleva: 2 pezzi per volta (gripper doppio)
- Pickable parts setting: 2

Calcolo PPM sarà basato su "2 pezzi ogni X secondi", non su 3 o 5.



#### **Impatto su statistiche Dashboard**

Questo parametro è **cruciale** per il calcolo accurato di:

**Parts Per Minute (PPM)**:
- Formula: `PPM = (Pickable parts × 60) / Tempo ciclo totale`
- Se impostato errato, PPM visualizzato non corrisponde a realtà

**Efficienza robot**:
- Calcola quanti pezzi vengono effettivamente prodotti vs tempo disponibile

**Pianificazione produzione**:
- Basandosi su PPM, si pianificano volumi produttivi
- Valore errato → pianificazione errata

**Come verificare il valore corretto**:
1. Eseguire 10 cicli di produzione
2. Contare fisicamente quanti pezzi il robot ha prelevato totali
3. Dividere per 10 cicli
4. Questo è il valore da impostare


### Maximum processing time per part


#### **Funzione**: Tempo di riferimento (in secondi) che il sistema usa per determinare quando un ciclo è considerato "completato" e passare da stato RUN a IDLE.

#### **Valori tipici:**
- **2-5 secondi**: Per robot veloci con cicli brevi
- **5-10 secondi**: Per robot medi con traiettorie standard
- **10-20 secondi**: Per robot lenti o con lunghe distanze di deposito

#### **Come calcolarlo**:
Tempo processing = Tempo medio pick&place robot × 1.2 (margine 20%)

Esempio:
- Robot impiega mediamente 4 secondi per pick&place
- Impostare: 4 × 1.2 = 4.8 → arrotondare a 5 secondi


#### **Cosa NON è**:
- ✗ Non è un timeout di errore (robot non si ferma se supera questo tempo)
- ✗ Non blocca operazioni se sforato
- ✓ È solo un riferimento per statistiche e gestione stati

#### **Impatto tempo processing su Dashboard**

**Valore troppo breve** (es: 2 secondi quando robot impiega 6):
- Sistema passa continuamente RUN → IDLE → RUN
- Dashboard mostra "In Run Time" inferiore al reale
- Statistiche distorte (sembra che robot sia idle quando in realtà lavora)

**Valore troppo lungo** (es: 20 secondi quando robot impiega 3):
- Sistema rimane in RUN anche quando robot ha finito
- Dashboard mostra "In Run Time" superiore al reale
- Metriche di efficienza appaiono migliori del reale

**Valore ottimale**:
- Sistema passa a IDLE circa 1-2 secondi dopo che robot ha effettivamente finito
- "In Run Time" corrisponde al tempo effettivo di lavoro robot
- Statistiche accurate e utilizzabili per analisi

---

## Configurazione Ottimale per Scenari Tipici

### Scenario 1: Robot singolo, picking standard

```{tip}
**Configurazione consigliata**

**Applicazione**: Robot con gripper singolo, preleva 1 pezzo alla volta, velocità media.

```
Max Object Count Return: 2
Min Object Count Return: 1
Sorting Mode: By Score (Descending)
Pickable parts: 1
Maximum processing time: 5 secondi
```

**Razionale**:
- Max 2: Robot ha sempre 1-2 pezzi disponibili, nessun idle
- Min 1: Massima flessibilità, lavora sempre se c'è almeno 1 pezzo
- By Score: Garantisce picking dei pezzi migliori
- Pickable 1: Gripper singolo
- 5 sec: Tempo medio pick&place standard
```

### Scenario 2: Robot veloce, gripper doppio

```{tip}
**Configurazione ottimizzata alta produttività**

**Applicazione**: Robot veloce, gripper doppio che preleva 2 pezzi simultaneamente.

```
Max Object Count Return: 4
Min Object Count Return: 2
Sorting Mode: By Score (Descending)
Pickable parts: 2
Maximum processing time: 3 secondi
```

**Razionale**:
- Max 4: Robot veloce, serve buffer di coordinate
- Min 2: Garantisce sempre almeno 1 ciclo doppio (2 pezzi)
- Pickable 2: Gripper doppio
- 3 sec: Robot veloce con cicli brevi
```

### Scenario 3: Robot lento, alta affidabilità

```{tip}
**Configurazione conservativa**

**Applicazione**: Robot lento o traiettorie lunghe, priorità affidabilità su throughput.

```
Max Object Count Return: 1
Min Object Count Return: 1
Sorting Mode: By Score (Descending)
Pickable parts: 1
Maximum processing time: 10 secondi
```

**Razionale**:
- Max 1: Robot lento, non serve buffer (visione ha tempo di processare tra un pick e l'altro)
- Min 1: Permissivo
- 10 sec: Traiettorie lunghe
```

---

## Procedura di Tuning Protocol Setup

### Approccio sistematico

```{note}
**Workflow ottimizzazione**

**Fase 1: Configurazione iniziale** (durante commissioning)

1. Impostare valori conservativi:
   - Max Count: 2
   - Min Count: 1
   - Sorting: By Score
   - Pickable: 1 (o valore effettivo gripper)
   - Processing time: Stima iniziale

2. Eseguire 10-20 cicli di test

3. Annotare:
   - Tempo medio pick&place robot effettivo
   - Quanti oggetti vengono effettivamente utilizzati
   - Eventuali idle time robot

**Fase 2: Primo tuning** (dopo primi test produzione)

4. Regolare Processing Time:
   - Impostare = Tempo medio pick&place × 1.2

5. Regolare Max Count:
   - Se robot attende spesso → Aumentare Max Count
   - Se molte coordinate non usate → Ridurre Max Count

6. Eseguire 50-100 cicli di produzione

7. Monitorare Dashboard:
   - PPM stabile?
   - "In Run Time" accurato?
   - Nessun comportamento anomalo?

**Fase 3: Ottimizzazione fine** (produzione continua)

8. Dopo 1-2 settimane produzione, analizzare:
   - Dati storici PPM
   - Efficienza robot media
   - Eventuali pattern di inefficienza

9. Regolazioni finali se necessarie

10. Documentare configurazione ottimale
```

---

## Salvataggio Configurazione

```{warning}
**Salvataggio obbligatorio**

Dopo aver configurato i parametri di Protocol Setup:

1. Verificare che tutti i valori siano impostati correttamente
2. Cliccare su **Save** o **Apply** (se presente pulsante dedicato)
3. I parametri vengono salvati nella configurazione sistema

**Nota**: A differenza di altri parametri che vengono salvati nella ricetta, i parametri di Protocol Setup sono tipicamente **globali** o associati alla configurazione della comunicazione robot.

Verificare nella documentazione specifica o con il supporto tecnico se richiedono salvataggio ricetta o sono salvati automaticamente.
```

---

## Verifica Configurazione

### Test validazione

```{note}
**Checklist verifica**

Dopo configurazione Protocol Setup, eseguire questi test:

**Test 1: Ciclo singolo**
- [ ] Eseguire 1 ciclo manuale (One Run)
- [ ] Verificare che coordinate inviate = Max Count (o numero rilevato se < Max)
- [ ] Verificare ordinamento corretto (primo oggetto = score più alto se By Score)

**Test 2: Ciclo continuo**
- [ ] Eseguire 10 cicli produttivi
- [ ] Monitorare Dashboard: "In Run Time" cresce correttamente?
- [ ] Verificare transizioni RUN → IDLE coerenti

**Test 3: Statistiche**
- [ ] Eseguire 50 cicli
- [ ] Calcolare PPM manualmente: (Pezzi prelevati totali / Tempo totale) × 60
- [ ] Confrontare con PPM mostrato in Dashboard
- [ ] Differenza dovrebbe essere < 5%

Se tutti i test sono positivi, configurazione è corretta.
```

---

## Troubleshooting Protocol Setup

### Problemi comuni

```{warning}
**PPM Dashboard non corrisponde a realtà**

**Causa più probabile**: Parametro "Pickable parts" errato

**Verifica**:
1. Contare manualmente pezzi prelevati in 10 cicli
2. Dividere per 10
3. Confrontare con valore impostato

**Soluzione**: Correggere "Pickable parts" con valore effettivo
```

```{warning}
**"In Run Time" sempre attivo (non passa mai a IDLE)**

**Causa**: "Maximum processing time" troppo lungo

**Soluzione**: Ridurre processing time gradualmente fino a quando sistema passa correttamente a IDLE tra un ciclo e l'altro
```

```{warning}
**Robot riceve troppe coordinate (non riesce a processarle tutte)**

**Causa**: "Max Object Count" troppo alto per velocità robot

**Soluzione**: Ridurre Max Count a valore realistico basato su tempo ciclo robot
```

---

## Checklist Completamento

```{note}
**Verifica configurazione Protocol Setup completa**

- [ ] Max Object Count Return configurato (valore realistico per velocità robot)
- [ ] Min Object Count Return configurato (tipicamente 1, o 2-3 se necessario)
- [ ] Sorting Mode selezionato (consigliato: By Score Descending)
- [ ] Pickable parts impostato (valore effettivo prese robot per ciclo)
- [ ] Maximum processing time configurato (tempo reale pick&place × 1.2)
- [ ] Test ciclo singolo eseguito con successo
- [ ] Test ciclo continuo (10+ cicli) verificato
- [ ] PPM Dashboard confrontato con calcolo manuale (< 5% differenza)
- [ ] Configurazione salvata

Se tutti i punti sono verificati, Protocol Setup è completato e ottimizzato.
```

---

## Prossimi Passi

Una volta completato Protocol Setup, il sistema è configurato completamente per l'operatività:

**→ [Config FlexiBowl](22_Config_FlexiBowl.md)** - Ottimizzazione movimentazione (se non già fatto)

**→ [Verifica Risultati (Dashboard)](24_Verifica_Risultati.md)** - Monitoraggio produzione e validazione configurazione

```{tip}
**Posizionamento Protocol Setup nel workflow**

Protocol Setup si configura tipicamente:
- **Dopo**: Calibrazione robot, creazione modelli
- **Prima**: Monitoraggio produzione continua

Questo perché:
- Richiede comprensione del comportamento robot (velocità, tipo gripper)
- Influenza le statistiche mostrate in Dashboard
- È l'ultimo step di configurazione prima della produzione vera

Una volta configurato correttamente, raramente richiede modifiche (solo se cambia robot o modalità operativa).
```