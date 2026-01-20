# **Creare una Nuova Ricetta**

Questa sezione descrive come creare una nuova ricetta applicativa in FlexiVision Easy. Una ricetta è il contenitore principale che include tutti i modelli pezzo, le configurazioni FlexiBowl/Hopper e i parametri robot necessari per un'applicazione completa di picking.

```{note}
**Creare una nuova ricetta quando:**

- Si lavora con un **tipo di pezzo completamente diverso**
- Si utilizza un **FlexiBowl di dimensione diversa**
- Si cambia **applicazione** (da picking standard a controllo qualità)
- Si desidera mantenere **configurazioni separate** per produzioni diverse

**NON serve creare una nuova ricetta quando:**
- Si aggiunge una variante dello stesso pezzo (creare nuovo modello nella stessa ricetta)
- Si fanno piccole regolazioni ai parametri esistenti
- Si modifica solo l'accept threshold o i filtri
```
---

## Panoramica interfaccia 

Prima di procedere con il training del modello, familiarizzare con l'interfaccia Edit Recipe:

### Elementi principali

```{list-table}
:header-rows: 1
:widths: 30 70

* - Sezione
  - Descrizione
* - **Models List**
  - Elenco di tutti i modelli abilitati nella ricetta (fino a 16). Cliccando su un modello si accede alla sua configurazione.
* - **FlexiBowl Configuration**
  - Accesso rapido ai parametri del FlexiBowl (vibrazione, velocità, temporizzazioni). Verrà configurato dopo il training modello.
* - **Hopper Configuration**
  - Parametri della tramoggia (se presente nel sistema). Opzionale.
* - **Robot Settings**
  - Impostazioni comunicazione e coordinate robot. Già configurate durante il setup.
* - **Save Recipe**
  - Pulsante per salvare tutte le modifiche effettuate alla ricetta.
```
---

## Salvataggio ricetta base

Prima di creare una nuova ricetta personalizzata, assicurarsi di aver salvato la ricetta base creata durante il setup iniziale:

```{important}
**Salvare la ricetta base**

1. Dalla pagina principale, cliccare su **Recipes**

2. Verificare che la ricetta corrente sia quella base (es: "Ricetta_Base" creata durante il setup)

3. Cliccare su **Save Recipe**

4. Mantenere lo stesso nome nel campo di salvataggio (si sta sovrascrivendo la ricetta con le configurazioni aggiornate)

5. Confermare il salvataggio
```

```{tip}
**Perché salvare la ricetta base?**

La ricetta base contiene tutte le configurazioni hardware completate durante il setup:
- Connessione FlexiBowl (IP, parametri)
- Connessione Hopper (se presente)
- Connessione Robot (porta TCP/IP)
- Calibrazione camera

Salvandola, si crea un punto di partenza sicuro per tutte le ricette future. In caso di problemi, si può sempre tornare a questa configurazione funzionante.
```

---

## Creazione nuova ricetta applicativa

Una volta salvata la ricetta base, procedere con la creazione della ricetta specifica per l'applicazione:

### Step 1: Accesso alla sezione Ricette

1. Dalla pagina principale del software FlexiVision Easy, cliccare su **Recipes**

2. Si apre la pagina di gestione ricette dove sono elencate tutte le ricette esistenti


### Step 2: Nominare la nuova ricetta

Prima di cliccare su "New Recipe", decidere un nome descrittivo per la ricetta.

**Convenzioni consigliate:**
- Utilizzare nomi che identificano chiaramente il pezzo o l'applicazione
- Evitare spazi (usare underscore `_` o trattini `-`)
- Includere informazioni rilevanti (tipo pezzo, dimensione, applicazione)


```{tip}
**Evitare nomi generici**

❌ Nomi da evitare:
- `Test`
- `Prova`
- `Ricetta1`, `Ricetta2`
- `Nuova_Ricetta`

✓ Nomi consigliati:
- `Prod_Viti_M8_Acciaio`
- `Assembly_Connettori_2024`
- `QC_Ingranaggi_Serie_X`

Un nome chiaro facilita la gestione quando si hanno molte ricette diverse.
```

### Step 3: Creazione ricetta

1. Cliccare sul pulsante **New Recipe**

2. Si apre una finestra di dialogo o un wizard guidato per la configurazione iniziale

3. Nel campo **Nome Ricetta**, inserire il nome scelto al passo precedente

4. Procedere con il pulsante **Next** o **Avanti**


### Step 4: Selezione modalità
Selezionare la modalità operativa dell'applicazione:

Per la maggior parte delle applicazioni di picking da FlexiBowl:

1. Selezionare **Standard** o **...**

2. Cliccare su **Next**

Quella Standard è la modalità più comune ed è anche quella che verrà descritta in dettaglio nelle sezioni successive.

```{tip}
**Quando usare le altre modalità**

```

### Step 5: Selezione modello FlexiBowl

1. Selezionare il FlexiBowl con cui stiamo lavorando:

2. Cliccare su **Next**

```{tip}
**Controllo ricetta selezionata**

1. Nella barra superiore o nel menu principale, verificare che sia visualizzato il nome della nuova ricetta creata

2. Se non è la ricetta corrente:
   - Tornare alla pagina **Recipes**
   - Cliccare sulla nuova ricetta nell'elenco
   - Cliccare su **Load Recipe** o **Seleziona**

3. Una volta caricata, il nome della ricetta attiva è sempre visibile nell'interfaccia
```

```{warning}
**Lavorare sempre sulla ricetta corretta**

Quando si lavora con multiple ricette, verificare sempre che sia selezionata quella corretta prima di iniziare modifiche.

Modifiche applicate alla ricetta sbagliata richiedono di rifare il lavoro o di esportare/importare configurazioni tra ricette.
```

---

### Step 6: creazione nuovo modello

Con la ricetta creata, abilitata e caricata, procedere con la configurazione dei modelli:
**→ [Creare un Modello](18_NuovoModello.md)**


---

## Riepilogo operazioni effettuate

A questo punto del processo, sono state completate le seguenti operazioni:

```{note}
**Checklist creazione ricetta**

- [x] Ricetta base salvata
- [x] Nuova ricetta creata con nome descrittivo
- [x] Modalità operativa selezionata (Standard/Locator)
- [x] Modello FlexiBowl configurato
- [x] Primo modello abilitato
- [x] Ricetta attiva selezionata
- [x] Edit Recipe aperto

**Prossimo passo**: Training del modello
```

---

## Suggerimenti pratici

### Naming convention ricette

```{tip}
**Organizzazione ricette aziendali**

Per aziende con molte applicazioni, considerare una naming convention strutturata:

**Formato suggerito**: `[LINEA]_[PRODOTTO]_[VARIANTE]_[ANNO]`

**Esempi:**
- `LineaA_Viti_M6_Zincate_2024`
- `LineaB_Connettori_TypeX_2024`
- `QC_Ingranaggi_SerieY_2025`

Vantaggi:
- Ricette facilmente identificabili
- Ordinamento alfabetico logico
- Tracciabilità storica (anno)
```

### Backup ricette

```{warning}
**Protezione del lavoro svolto**

Dopo aver creato e configurato una ricetta:
- Utilizzare la funzione di backup del software ([Backup Management](../rif_tecnico_specifiche/integrazione_software/07_Backup_management.md))
- Esportare periodicamente le ricette su supporto esterno
- Documentare parametri critici su supporto cartaceo/digitale

Una ricetta ben configurata rappresenta ore di lavoro. Proteggerla adeguatamente previene perdite di dati.
```

---

## Risoluzione problemi comuni

### Ricetta non salvata correttamente

```{warning}
**Errore durante salvataggio**

Se il salvataggio della ricetta fallisce:
- Verificare di avere permessi di scrittura sulla cartella del software
- Controllare lo spazio disponibile su disco
- Assicurarsi che il nome non contenga caratteri non ammessi (`/ \ : * ? " < > |`)
- Verificare che non esista già una ricetta con lo stesso nome

Riprovare il salvataggio dopo aver verificato questi punti.
```


---

## Prossimi passi

Una volta creata e configurata la ricetta di base, procedere con il training del primo modello:

**→ [Creare un Modello](18_NuovoModello.md)**

```{tip}
**Cosa serve per il prossimo step**

Per procedere con il training del modello, assicurarsi di avere:
- Pezzi fisici da riconoscere (almeno 10-15 pezzi)
- Robot disponibile per posizionamento pezzo di riferimento
- FlexiBowl vuoto e pulito
- Simulatori ingombro pinza (possono essere pezzi dello stesso tipo)
- Foglio per annotare coordinate robot (X, Y, RZ)
```

```{toctree}  
17b_Expert.md
```