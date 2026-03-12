(nuovaricetta)=
# **Creare una Nuova Ricetta**

Questa sezione descrive come creare una nuova ricetta applicativa in FlexiVision One. Una ricetta è il contenitore principale che include tutti i modelli pezzo, le configurazioni FlexiBowl/Hopper e i parametri robot necessari per un'applicazione completa di picking.
```{note}
**Creare una nuova ricetta quando:**

- Si lavora con un **tipo di pezzo completamente diverso**
- Si utilizza un **FlexiBowl di dimensione diversa**
- Si cambia **applicazione** 
- Si desidera mantenere **configurazioni separate** per produzioni diverse

**NON serve creare una nuova ricetta quando:**
- Si aggiunge una variante dello stesso pezzo (creare nuovo modello nella stessa ricetta)
- Si fanno piccole regolazioni ai parametri esistenti
- Si modifica solo l'accept threshold o i filtri
```

---

## Panoramica interfaccia

Prima di procedere con il training del modello, familiarizzare con l'interfaccia [Recipes](recipes).


## Salvataggio ricetta base

Prima di procedere, assicurarsi di aver salvato la ricetta base creata durante il setup iniziale:
:::{list-table}
  * - 1.
    - Dalla pagina principale, cliccare su **Recipes**
  * - 2.
    - Verificare che la ricetta corrente sia quella base (es: "Ricetta_Base" creata durante il setup)
  * - 3.
    - Cliccare su **Save Recipe**
  * - 4.
    - Mantenere lo stesso nome nel campo di salvataggio (si sta sovrascrivendo la ricetta con le configurazioni aggiornate)
  * - 5.
    - Confermare il salvataggio
:::

```{important}

**Perché salvare la ricetta base?**

La ricetta base contiene tutte le configurazioni hardware completate durante il setup:
- Connessione FlexiBowl (IP, parametri)
- Connessione Hopper 
- Connessione Robot (porta TCP/IP)
- Calibrazione camera

Avere una ricetta base già pronta consente di riutilizzare tutte queste configurazioni senza doverle ripetere.
```

---

## Scegliere come procedere

Con la ricetta base salvata, esistono **due strade** per creare la ricetta applicativa. La scelta dipende dalla necessità di ripetere o meno la calibrazione.
```{list-table}
:header-rows: 1
:widths: 10 45 45

* -
  - **Percorso A — Crea una nuova ricetta da zero**
  - **Percorso B — Duplica la ricetta base**
* - **Quando**
  - È necessario ripetere la calibrazione (camera, robot, o entrambe)
  - Si vuole mantenere setup e calibrazione già eseguiti
* - **Casi tipici**
  - Si cambia robot, si riconfigura la camera, si modifica l'ambiente fisico, oppure si vuole ripartire da zero.
  - Stesso FlexiBowl, stesso robot, stesso ambiente fisico. Si vuole solo lavorare su un pezzo o un'applicazione diversa.
* - **Vantaggio**
  - Configurazione completamente pulita, nessuna dipendenza da impostazioni precedenti.
  - Calibrazione e connessioni già pronte: si risparmia tempo e si evitano errori di setup.
* - **Come fare**
  - Vai a [Percorso A](#percorso-a-crea-una-nuova-ricetta-da-zero) ↓
  - Vai a [Percorso B](#percorso-b-duplica-la-ricetta-base) ↓
```
```{note}
**Caso speciale — Cambio della tramoggia (Hopper)**

Se cambi solo la tramoggia, non è necessario scegliere il Percorso A. È sufficiente duplicare la ricetta base (Percorso B) e aggiornare il campo **Signal** nella configurazione Hopper.
```

---

# Percorso A — Crea una nuova ricetta da zero

Segui questo percorso se è necessario ripetere la calibrazione o ricominciare completamente il setup.
```{warning}
**Questo percorso richiede di ripetere il setup completo**

Calibrazione camera, connessione robot e configurazione hardware dovranno essere rifatte. Se non è necessario, usa il [Percorso B](#percorso-b-duplica-la-ricetta-base).

Se vuoi ricominciare completamente dall'inizio: **→ [Creazione Ricetta Base](ricettabase)**
```
:::{attention}
**Cambio pezzo e ricalibrazione**
 
   Come spiegato nella sezione [Calibrazione Camera](calibrazione) , per ottenere la massima precisione la griglia di calibrazione deve essere posta alla stessa altezza del pezzo usato nell'applicazione.  
- Se il nuovo pezzo ha un'altezza **simile** all'originale e/o l'applicazione **non richiede la massima precisione**, non è necessario ripetere la calibrazione: è possibile procedere direttamente con il [Percorso B](percorsoB).  
- Se il nuovo pezzo **differisce in altezza** dall'originale in modo sostanziale, è necessario **ripetere la calibrazione** utilizzando i distanziali forniti con la griglia, come descritto in [Calibrazione Camera](calibrazione)
:::

## Step 1: Accesso alla sezione Ricette
```{list-table}
* - 1.
  - Dalla pagina principale del software FlexiVision One, cliccare su **Recipes**
* - 2.
  - Si apre la pagina di gestione ricette con l'elenco di tutte le ricette esistenti
```

## Step 2: Creare la ricetta e nominarla
```{list-table}
* - 3.
  - Cliccare sul pulsante **New Recipe**
* - 4.
  - Nel campo **Nome Ricetta**, inserire il nome scelto 
    :::{seealso} [Naming Convention Ricette](nominarericetta)
    :::
* - 5.
  - Cliccare su **Next**
```

## Step 3: Selezionare la modalità operativa
```{list-table}
* - 6.
  - Selezionare **Standard** o **...**
* - 7.
  - Cliccare su **Next**
```

Quella Standard è la modalità più comune ed è quella descritta in dettaglio nelle sezioni successive.
```{tip}
**Quando usare le altre modalità**

[da completare]
```

## Step 4: Selezione modello FlexiBowl
```{list-table}
* - 8.
  - Selezionare il FlexiBowl con cui si sta lavorando
* - 9.
  - Cliccare su **Next**
```
```{tip}
**Controllo ricetta selezionata**

  :::{list-table}
  * - 1.
    - Nella barra superiore, verificare che sia visualizzato il nome della nuova ricetta
  * - 2.
    - Se non è la ricetta corrente: tornare a **Recipes**, cliccare sulla nuova ricetta, poi su **Load Recipe**
  * - 3.
    - Il nome della ricetta attiva è sempre visibile nell'interfaccia
  :::
```

**→ Continua con [Step 5: Creazione nuovo modello](nuovomodello)**

---
(percorsoB)=
# Percorso B — Duplica la ricetta base

Segui questo percorso se vuoi mantenere calibrazione e configurazioni hardware esistenti.

## Step 1: Accesso alla sezione Ricette
```{list-table}
* - 1.
  - Dalla pagina principale del software FlexiVision One, cliccare su **Recipes**
* - 2.
  - Si apre la pagina di gestione ricette con l'elenco di tutte le ricette esistenti
```

## Step 2: Duplica la Ricetta Base 
```{list-table}
* - 3.
  - Selelzionare la Ricetta Base
* - 4.
  - Duplicare la Ricetta Base
* - 5.
  - Cliccare su Load Recipe 
* - 6.
  - Verificare nella barra superiore che il nome visualizzato sia quello della nuova ricetta
    :::{warning}
    **Lavorare sempre sulla ricetta corretta**

    Con più ricette presenti, verificare sempre che sia selezionata quella corretta prima di iniziare modifiche. Modifiche applicate alla ricetta sbagliata richiedono di rifare il lavoro.
    :::
```
## Step 3: Nominare la Ricetta

Prima di cliccare su "Save Recipe", scegli un nome descrittivo.
```{list-table}
* - 7. 
  - Rinominare la Ricetta duplicata   
    **Convenzioni consigliate:**
    - Nomi che identificano chiaramente il pezzo o l'applicazione
    - Niente spazi (usare `_` o `-`)
    - Includere informazioni rilevanti (tipo pezzo, dimensione, applicazione)
    
    :::{tip}
    **Evitare nomi generici**

    ❌ Nomi da evitare:
    - `Test`, `Prova`, `Ricetta1`, `Nuova_Ricetta`

    ✓ Nomi consigliati:
    - `Prod_Viti_M8_Acciaio`
    - `Assembly_Connettori_2024`
    - `QC_Ingranaggi_Serie_X`

    Un nome chiaro facilita la gestione quando si hanno molte ricette diverse.
    :::
```

---

## Creazione nuovo modello

Con la ricetta creata e caricata — indipendentemente dal percorso seguito — procedere con la configurazione dei modelli:

**→ [Creare un Modello](18_NuovoModello.md)**

---

## Riepilogo operazioni effettuate
```{note}
**Checklist creazione ricetta**

[x] Ricetta base salvata
[x] Percorso e modelaità operativa scelti (Nuova da zero / Duplicazione della Ricetta Base)
[x] Nuova ricetta creata con nome descrittivo funzionale


**Prossimo passo**: Training del modello
```

---

## Suggerimenti pratici

(nominarericetta)=
### Naming convention ricette

**Convenzioni consigliate:**
- Nomi che identificano chiaramente il pezzo o l'applicazione
- Niente spazi (usare `_` o `-`)
- Includere informazioni rilevanti (tipo pezzo, dimensione, applicazione)

```{tip}
**Evitare nomi generici**

❌ Nomi da evitare:
- `Test`, `Prova`, `Ricetta1`, `Nuova_Ricetta`

✓ Nomi consigliati:
- `Prod_Viti_M8_Acciaio`
- `Assembly_Connettori_2024`
- `QC_Ingranaggi_Serie_X`

Un nome chiaro facilita la gestione quando si hanno molte ricette diverse.
```
```{tip}
**Organizzazione ricette aziendali**

Per aziende con molte applicazioni, considerare una naming convention strutturata:

**Formato suggerito**: `[LINEA]_[PRODOTTO]_[VARIANTE]_[ANNO]`

**Esempi:**
- `LineaA_Viti_M6_Zincate_2024`
- `LineaB_Connettori_TypeX_2024`
- `QC_Ingranaggi_SerieY_2025`

Vantaggi: ricette facilmente identificabili, ordinamento alfabetico logico, tracciabilità storica.
```

### Backup ricette
```{warning}
**Protezione del lavoro svolto**

Dopo aver creato e configurato una ricetta:
- Utilizzare la funzione di backup del software ([Backup Management](backup))
- Esportare periodicamente le ricette su supporto esterno
- Documentare parametri critici su supporto cartaceo/digitale

Una ricetta ben configurata rappresenta ore di lavoro. Proteggerla adeguatamente previene perdite di dati.
```

---

## Prossimi passi

**→ [Creare un Modello](18_NuovoModello.md)**

```{tip}
**Cosa serve per il prossimo step**

- Pezzi fisici da riconoscere (almeno 10-15 pezzi)
- FlexiBowl vuoto e pulito
- Robot disponibile per posizionamento pezzo di riferimento
- Se il tool del robot che stiamo utilizzando è una pinza, ci occorreranno anche due oggetti (non necessariamente uguali ai pezzi di cui si vuole fare il modello) da utilizzare come simulatori per l'ingombro del tool. 
- Foglio per annotare coordinate robot (X, Y, RZ)
```