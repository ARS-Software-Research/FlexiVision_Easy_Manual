(calibrazione)=
# **Calibrazione della Camera**

La calibrazione è il passaggio cruciale che stabilisce la relazione geometrica esatta tra il mondo reale (coordinate in millimetri) e l'immagine acquisita dalla telecamera (pixel). Senza una calibrazione precisa, la precisione del sistema di picking risulta compromessa, rendendo inaffidabile l'intera applicazione.

```{warning}
**Prerequisito fondamentale**

Prima di procedere con la calibrazione, assicurarsi che tutti i setup hardware siano stati completati correttamente:
- [FlexiBowl Setup](SETUP/13a_FB_Setup.md) ✓
- [Hopper Setup](SETUP/13b_Hopper_Setup.md) ✓
- [Robot Setup](SETUP/13c_Robot_Setup.md) ✓
- [Camera Setup](SETUP/13d_Camera_Setup.md) ✓

La calibrazione deve essere ripetuta ogni volta che un elemento fisico della telecamera o del suo setup ottico viene modificato (es. messa a fuoco, apertura o posizione).
```

---

## **Perché la calibrazione è necessaria?**

La calibrazione è necessaria perché ogni combinazione di sensore e lente introduce alterazioni specifiche nell'immagine. Il suo obiettivo principale è correggere queste distorsioni.

### Tipi di distorsioni ottiche

```{figure} img/distorsioni_new.png
:alt: Tipi di distorsioni ottiche
:width: 80%
:align: center

Esempi di distorsioni ottiche: nessuna distorsione (sinistra), distorsione a barile (centro), distorsione a cuscinetto (destra)
```

```{note}

La calibrazione calcola i parametri matematici per compensare queste distorsioni e "raddrizzare" l'immagine virtualmente.
```

---


## **Step 1: La griglia di calibrazione**
La griglia di calibrazione dedicata ARS deve essere posizionata sul FlexiBowl:

```{list-table}
* - 0. 
  - Se presenti, rimuovere i deviatori montati sul FlexiBowl.
* - 1. 
  - **Allentare le quattro viti** della flangia centrale del FlexiBowl
* - 2. 
  - **Ruotare leggermente la flangia** centrale e **Rimuoverla**
* - 3. 
  - **Sollevare** con cura e **Rimuovere la superficie**  
* - 4. 
  - **Posizionare la griglia ARS** sul FlexiBowl allineando i perni di posizionamento con i fori predefiniti 
```

```{figure} img/griglia_posizionamento.png
:alt: Posizionamento griglia calibrazione
:width: 60%
:align: center

Corretto posizionamento della griglia di calibrazione ARS sul FlexiBowl
```

```{warning}
**Utilizzo griglia corretta**

Assicurarsi di utilizzare la griglia di calibrazione corretta per il vostro modello di FlexiBowl:
- FB 200 → Griglia 200
- FB 350 → Griglia 350
- FB 500 → Griglia 500
- FB 650 → Griglia 650
- FB 800 → Griglia 800
- FB 1200 → Griglia 1200

L'utilizzo di una griglia non corrispondente al modello di FlexiBowl invalida completamente la calibrazione.
```

## **Step 2: Regolazioni fondamentali**

```{list-table}

* - 5. 
  - Accedere alla sezione Camera SETUP dalla sezione SETUP 
* - 6. 
  - Cliccare il pulsante Config Camera della camera corrispondente 
* - 7. 
  - Cliccare EXPERT dalla pagina Camera FLB 
* - 8. 
  - Dalla sezione Settings, seguire questi passaggi: 
    - Cliccare **Image Acuisition Device**
    - Selezionare la Camera 
    - Cliccare **Video Formats** 
    - Selezionare **Generic GigEVision** e **Mono**
    - Cliccare *Initialize Acquisition*
* - 9.
  - **Mettere la camera in modalità "live display"**
      Prima di regolare l'apertura, attivare la modalità di visualizzazione continua:
* - 10. 
  - **Impostare l'apertura del diaframma**
    - Svitare leggermente la vite dell'anello superiore della camera 
    - Ruotare l'anello osservando l'immagine live, fino a che la giusta quantità di luce non entra nella camera 
    - Stringere la vite dell'anello superiore della camera 
* - 11.
  - **Regolare manualmente il fuoco della camera**
    - Svitare leggermente la vite dell'anello inferiore della camera
    - Ruotare l'anello lentamente osservando l'immagine live
    - Quando il pattern appare nitido, il fuoco è corretto
    - Stringere la vite dell'anello inferiore della camera 
    - Chiudere la schermata
* - 12. 
  - Cliccare Back 
```

```{warning}
**Attenzione alla profondità di campo**

La messa a fuoco deve garantire nitidezza su **tutta la superficie** del FlexiBowl, non solo al centro.

Se il centro è nitido ma i bordi sono sfocati:
- Verificare che la camera sia perfettamente parallela al piatto
- Verificare la distanza di lavoro (deve essere quella calcolata)
- Chiudere leggermente il diaframma (es. f/6.3 o f/7.1) per aumentare la profondità di campo

Se il problema persiste, potrebbe essere necessario rivedere il montaggio meccanico della camera.
```

```{list-table}
* - 13. 
  - **Regolare l'esposizione della camera**
    - Dalla pagina **Camera FLB x**, individuare il parametro **Cam Exposure** (Esposizione della Camera):
    - Regolare il parametro "Cam Exposure" e cliccare su "TEST", ripetere questo passaggio fino a che non viene trovata la giusta esposizione per l'immagine: 
   		- Pattern della griglia chiaramente visibile (nero su bianco o viceversa)
   		- Contrasto elevato tra quadrati bianchi e neri
   		- Nessuna sovraesposizione (aree completamente bianche "bruciate")
   		- Nessuna sottoesposizione (immagine troppo scura)
* - 14. 
  - Cliccare NEXT
```

```{figure} img/esposizione_corretta.png
:alt: Esempio esposizione corretta
:width: 60%
:align: center

Esempio di esposizione corretta: contrasto elevato, pattern ben definito, nessuna area bruciata
```

```{tip}
**Ottimizzazione esposizione**

**Più alto sarà il tempo, più luce entrerà nell'ottica**

- **Tempo troppo breve**: Immagine scura, pattern poco visibile
- **Tempo troppo lungo**: Immagine sovraesposta, perdita di dettagli
- **Tempo ottimale**: Massimo contrasto senza saturazione

**Esempio di impostazione corretta:**

Se l'immagine con esposizione 20ms appare:
- Troppo scura → aumentare a 25-30ms
- Troppo chiara → ridurre a 15-18ms
- Contrasto insufficiente → regolare intensità backlight/toplight
```



## **Step 3: Calibrazione Camera**

```{list-table}
:widths: 5 95

* - **15.**
  - Cliccare su "NEXT" per accedere alla pagina "Calibration camera Flb1"

* - **16.**
  - Impostare i valori "Tile Size X" e "Tile Size Y" entrambi a 10

* - **17.**
  - Cliccare su "Grab Image Calib" per scattare una foto della griglia di calibrazione.
    
    Verificare visivamente che:
    - L'intera griglia sia visibile
    - Il pattern sia nitido
    - Non ci siano ombre o riflessi

* - **18.**
  - Cliccare su "Compute Calib" per effettuare la calibrazione

* - **19.**
  - **Valutare la qualità della calibrazione**
    
    Il parametro "Result Calibration" restituirà un valore:
    
    🟢 **Excellent (Verde)**: Calibrazione eccellente, precisione ottimale. Procedere con fiducia.
    
    🟠 **Acceptable (Arancione)**: Calibrazione accettabile, precisione buona ma non ottimale.
    
    🔴 **Bad (Rosso)**: Calibrazione scadente, precisione insufficiente. Da ripetere obbligatoriamente.
    
    :::{important}
    Accettare solo calibrazioni Eccellenti 🟢, altri risultati comprometteranno il funzionamento dell'intera applicazione.
    :::
```

```{note}
**Criterio di accettabilità**

Un risultato soddisfacente comprende il settaggio dell'apertura, la messa a fuoco, e il settaggio dell'esposizione migliore per l'applicazione.

```

```{warning}
**Errori durante il calcolo**

Se il calcolo della calibrazione fallisce:

**Possibili cause**:
- Pattern non rilevato (immagine troppo scura o sovraesposta)
- Quadrati della griglia parzialmente oscurati
- Distorsione eccessiva (camera troppo vicina o lontana)
- Tile Size inserito errato

**Soluzione**:
- Verificare e migliorare la qualità dell'immagine acquisita
- Assicurarsi che l'intera griglia sia visibile e ben illuminata
- Verificare il valore Tile Size
- Ripetere l'acquisizione immagine (Grab Image) e tentare nuovamente
```

```{warning}
**Accettare solo buone calibrazioni**

Non accontentarsi di calibrazioni "Acceptable" (arancione). Una calibrazione subottimale causa:
- Errori di posizionamento del robot 
- Picking falliti o imprecisi
- Necessità di correzioni manuali ripetute

Investire tempo per ottenere una calibrazione "Good" (verde) ripaga immediatamente in termini di affidabilità del sistema.
In caso di risultato **Acceptable** o **Bad**:

1. Tornare alla pagina precedente "Camera FLB x"
2. Verificare e migliorare la messa a fuoco del pattern
3. Regolare l'esposizione per massimizzare il contrasto
4. Verificare l'uniformità dell'illuminazione
5. Tornare alla pagina "Calibration Camera FLB x"
6. Acquisire una nuova immagine "Grab Image"
7. Ripetere il calcolo della calibrazione "Compute Calib"
```


```{note}
**Nota: la calibrazione viene salvata in automatico**

Una volta completata con successo (risultato Good o Acceptable), la calibrazione viene automaticamente salvata:
- Associata alla ricetta corrente
- Memorizzata nel profilo della camera
- Caricata automaticamente all'avvio successivo del software

Non è necessario effettuare salvataggi manuali.
```


**Nota: spiegare che per i dubbi si può aprire info**

In quali casi si apre Expert? Expert si apre per la configurazione della luminosità o per altri parametri.


---

### Quando è necessario ripetere la calibrazione
```{list-table}
:widths: 50 50
:header-rows: 0

* - **Ricalibrare quando:**
  - * Primo setup del sistema (obbligatorio)
    * Dopo aver modificato la posizione della camera
    * Dopo aver regolato il fuoco o l'apertura dell'obiettivo
    * Dopo aver spostato il FlexiBowl
    * Dopo manutenzione meccanica della cella robotica
    * Se si riscontrano errori sistematici di picking
    * Dopo un urto o vibrazione significativa

* - **Non è necessario ricalibrare quando:**
  - * Si cambia tipo di pezzo (stesso FlexiBowl, stessa camera)
    * Si modifica la ricetta software
    * Si regolano parametri di riconoscimento
    * Si aggiornano i programmi robot
```

---
# **Calibrazione Robot**

## **Step 4: Montaggio Laser**

```{list-table}
* - 20. 
  - Una volta ottenuta una calibrazione di ottima qualità, Cliccare "NEXT". 
    Apparirà una finestra che richiede la calibrazione del robot prima di proseguire, **NON** cliccare su "Sì" e seguire i prossimi passaggi
* - 21. 
  - Montare il Laser Tool con il suo supporto personalizzato 
* - 22. 
  - Posizionare lo Spacer Bracket sotto il laser 
* - 23. 
  - Abbassare il laser fino al livello dello spacer, così il laser avrà un'altezza di esattamente 3cm dalla griglia di calibrazione
* - 24. 
  - Rimuovere lo Spacer Bracket 
* - 25. 
  - Accendere il laser 
```

## **Step 5: Disegnare un piano a 3 punti**
```{list-table}
* - 26.
  - Portare il laser sul punto di origine 
* - 27. 
  - Portare il laser nel punto finale dell'asse X
* - 28.
  - Portare il laser nel punto finale dell'asse Y 
```

## **Step 6: Verifica della traiettoria del robot**
```{list-table}
* - 29. 
  - Riportare il laser sul punto di origine
* - 30. 
  - Muovere il robot dalla sua teach pendant lungo gli assi X e Y. 
* - 31. 
  - Verificare che la corretta traiettoria sia seguita: il robot, muovendosi esclusivamente lungo gli assi X e Y, deve seguire correttamente le linee della griglia 
  ```
## **Step 7: Salvataggio Ricetta Base** - da verificare
L'ultimo step della procedura è il salvataggio della rietta base
Cliccare su Recipes
controllare di avere la ricetta contenente tutti i setup e la calibrazione selezionata nel menu a sinistra e cliccare su Save Recipe   
Questa ci permetterà di avere salvati a parte tutti i passaggi fatti fin'ora, in modo da avere una base per tutte le future ricette che conterranno i vari modelli  
Per continuare con la creazione dei modelli, duplicare la ricetta base, rinominarla come si preferisce e cliccare su Edit Recipe, si aprirà una pagina con l'elenco di tutti i modelli disponibili 



---

# **Problemi comuni durante la calibrazione**

## **Pattern non rilevato**

```{warning}
**Errore: "Unable to detect calibration pattern"**

Causa: Il software non riesce a identificare il pattern della griglia.

**Soluzioni**:
- Aumentare il contrasto (regolare esposizione o illuminazione)
- Verificare che l'intera griglia sia visibile nell'immagine
- Migliorare la messa a fuoco
- Pulire la superficie della griglia (polvere o impronte possono interferire)
- Verificare che la griglia sia quella corretta (quadrati, non cerchi o altri pattern)
```

## **Calibrazione sempre "Bad" o "Acceptable"**

```{warning}
**Qualità calibrazione insufficiente**

Se nonostante le regolazioni la calibrazione rimane sotto "Excellent":

1. Verificare la distanza di lavoro camera-FlexiBowl (deve essere quella calcolata)
2. Controllare il paralleli della camera rispetto al piatto (deve essere perfettamente orizzontale)
3. Verificare la planarità della griglia (non deve essere deformata o piegata)
4. Assicurarsi che la camera sia stabile (no vibrazioni durante acquisizione)
5. Verificare che l'obiettivo sia avvitato completamente (contatto metal-metal con corpo camera)

Se il problema persiste, potrebbe esserci un problema meccanico nel montaggio. Consultare [Installazione Meccanica](09_Installazione_Meccanica.md) per revisione.
```

## **Errori dopo cambio illuminazione**

```{tip}
**Ri-calibrazione dopo cambio backlight/toplight**

Se si passa da backlight a toplight (o viceversa):

1. La calibrazione geometrica rimane valida (non serve rifarla)
2. È necessario solo regolare l'esposizione per il nuovo tipo di illuminazione
3. Acquisire un'immagine di test per verificare che il pattern sia ancora ben visibile
4. Se il contrasto è molto diverso, considerare di rifare la calibrazione per massima precisione

In generale, è consigliabile decidere fin dall'inizio il tipo di illuminazione da utilizzare e mantenere quella configurazione.
```

---

# **Passi successivi**





###  backlight a toplight?
quando attivo frontlight?

```{warning}
**Impatto sul riconoscimento pezzi**

La scelta tra backlight e frontlight/toplight influenza significativamente il riconoscimento:

- **Backlight**: Ottimo per profili/sagome, pezzi appaiono come silhouette scure su sfondo chiaro
- **Toplight**: Necessario per riconoscere dettagli superficiali, texture, feature interne

La calibrazione deve essere eseguita con lo stesso tipo di illuminazione che verrà utilizzato durante il picking in produzione.
```