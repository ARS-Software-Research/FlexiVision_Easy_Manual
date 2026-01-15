# **Installazione Meccanica del Sistema**

Questa sezione descrive i requisiti di montaggio e posizionamento dei componenti chiave del sistema di visione FlexiVision Easy. L'installazione deve essere eseguita solo dopo aver completato l'installazione meccanica di base del FlexiBowl e dell'eventuale tramoggia.

```{warning}
**Prerequisiti obbligatori**

Prima di procedere con l'installazione dei componenti di visione, assicurarsi che:

- Il FlexiBowl sia stato montato e fissato alla struttura portante (cellula robotica)
- La tramoggia (Hopper), se presente, sia stata installata correttamente
- La struttura di supporto per camera e illuminatore sia stata preparata

Per l'installazione del FlexiBowl, consultare il Manuale Dedicato fornito con l'alimentatore vibrante.
```

```{note}
**Competenze richieste**

L'installazione meccanica richiede:
- Competenze di base in assemblaggio meccanico
- Utilizzo di strumenti di misura (calibro, livella, metro)
- Capacità di lettura di disegni tecnici
- Tempo stimato: 2-3 ore
```

---

## Montaggio VisionController

Il VisionController (PC Industriale) gestisce l'elaborazione delle immagini e la comunicazione con il robot. Essendo un componente elettronico sensibile, richiede un posizionamento attento per garantire ventilazione adeguata e protezione da contaminanti.

### Specifiche tecniche 
immagini + allegare pdf?

### Requisiti di montaggio

```{list-table}
:header-rows: 1
:widths: 35 65

* - Requisito
  - Specifiche
* - **Posizione consigliata**
  - Interno quadro elettrico o su pannello dedicato vicino alla cella robotica
* - **Orientamento**
  - Verticale (consigliato) o orizzontale con ventilazione forzata
* - **Spazio di ventilazione**
  - Minimo 50 mm su tutti i lati per circolazione aria
* - **Fissaggio**
  - Guida DIN 35 mm o viti M4 su pannello
* - **Temperatura ambiente**
  - 0°C ~ +50°C (verificare specifiche complete nella sezione [Specifiche VisionController](rif_tecnico_specifiche/04_Specifiche_FlexiVision.md#visioncontroller))
* - **Protezione**
  - IP40 minimo (consigliato montaggio in quadro elettrico IP54)
```

### Procedura di installazione

```{list-table} 
   :header-rows: 1
   :widths: 35 65

   * - Fase
     - Descrizione Operativa
   * - **1. Disimballaggio**
     - Estrarre il VisionController dalla confezione prestando attenzione a non danneggiare i connettori. Verificare l'integrità del prodotto.
   * - **2. Preparazione supporto**
     - * **Per montaggio su guida DIN**: verificare che la guida sia pulita e fissata saldamente.
       * **Per montaggio su pannello**: praticare fori M4 secondo il pattern fornito nei disegni tecnici.
   * - **3. Fissaggio**
     - **Guida DIN**: Agganciare il dispositivo facendolo scorrere sulla guida fino allo scatto.
       
       **Pannello**: Utilizzare 4 viti M4 con coppia di serraggio 1.2 Nm.
   * - **4. Orientamento**
     - Posizionare il controller con le prese di ventilazione libere da ostruzioni.
```

```{warning}
**Ventilazione critica**

Il VisionController genera calore durante il funzionamento. Una ventilazione inadeguata può causare:
- Surriscaldamento e spegnimenti automatici
- Riduzione delle prestazioni
- Danneggiamento dei componenti interni

Garantire sempre almeno 50 mm di spazio libero attorno al dispositivo.
```



---

## Montaggio Camera

Il posizionamento preciso e l'allineamento della telecamera sono passaggi critici che influenzano direttamente l'accuratezza della calibrazione e le prestazioni del sistema di picking.

### Distanza di lavoro ottimale

La telecamera deve essere montata in modo che la faccia frontale della lente sia posizionata a una distanza specifica (Working Distance) dalla superficie del piatto FlexiBowl.

```{note}
La distanza di lavoro dipende da:
- Modello di FlexiBowl (diametro superficie)
- Risoluzione richiesta (mm/pixel)
- Dimensioni dei pezzi da rilevare

Per il calcolo dettagliato della distanza ottimale per la vostra applicazione, consultare la sezione dedicata: [Calcolo Distanza Ottimale](rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md)

**Distanze tipiche per riferimento:**
- FlexiBowl 200: circa 350-400 mm
- FlexiBowl 350: circa 450-500 mm
- FlexiBowl 500: circa 550-600 mm
- FlexiBowl 650: circa 650-700 mm
```
### Specifiche tecniche Camera 
immagini + pdf??

### Posizionamento e allineamento

Il corretto allineamento della camera è fondamentale per ottenere immagini di qualità e garantire precisione nel picking.

```{warning}
**Centratura:**
- La camera deve essere posizionata esattamente al centro del FlexiBowl (asse ottico coincidente con l'asse di rotazione del piatto)
- Tolleranza massima di centratura: ±5 mm
```

```{warning}
**Ortogonalità:**
- La camera deve essere montata perfettamente parallela alla superficie del piatto
- Non sono ammesse inclinazioni laterali (tilt) o rotazioni rispetto alla verticale
- Tolleranza massima di inclinazione: ±1°
```

```{warning}
**Fissaggio:**
- Utilizzare i 4 fori di montaggio M3 presenti sul corpo camera
- Viti consigliate: M3 × 8 mm (acciaio inox)
- Coppia di serraggio: 0.5 Nm (non serrare eccessivamente per evitare deformazioni)
```

```{tip}
Per facilitare la messa a punto e permettere aggiustamenti futuri, si raccomanda fortemente di progettare il supporto meccanico della camera con possibilità di microregolazioni:
- **Asse Z (altezza)**: -10 mm / +30 mm (per adattamento distanza di lavoro)
- **Asse X (sinistra-destra)**: ±10 mm (per centratura fine)
- **Asse Y (avanti-indietro)**: ±10 mm (per centratura fine)
Questa flessibilità è particolarmente utile durante la calibrazione iniziale e per eventuali ricalibrazione future.
```

### Verifica montaggio lente

```{warning}
Prima di procedere con il fissaggio definitivo:
1. Verificare visivamente che la lente sia installata
2. Controllare che la lunghezza focale sia corretta per il vostro modello di FlexiBowl (etichetta sulla lente o documentazione dell'ordine)
3. Assicurarsi che la lente sia avvitata completamente (contatto metal-metal tra lente e corpo camera)
4. NON rimuovere o allentare la lente se già montata correttamente
```
---

## Montaggio Toplight

Se l'ordine include un Toplight (illuminatore dall'alto), questo deve essere montato sulla stessa struttura di supporto della telecamera per garantire un'illuminazione uniforme della superficie di lavoro.

### Specifiche Tecniche 
immagini + pdf??

### Procedura di installazione

```{list-table}
:header-rows: 1
:widths: 35 65

* - **Fase**
  - **Istruzioni operative**
* - **1. Posizionamento**
  - Fissare il Toplight sulla struttura di supporto in posizione concentrica rispetto alla camera.
* - **2. Distanza dalla superficie**
  - Posizionare l'illuminatore a una distanza dalla superficie del FlexiBowl simile a quella della camera per:
    
    * Minimizzare le ombre proiettate dai pezzi
    * Massimizzare l'uniformità luminosa
    * Evitare riflessioni dirette verso la camera
* - **3. Orientamento**
  - Assicurarsi che la superficie emittente del Toplight sia parallela al piatto del FlexiBowl.
* - **4. Angolo di illuminazione**
  - Perpendicolare alla superficie (0° tilt).
* - **5. Fissaggio**
  - Secondo specifiche del modello fornito (tipicamente M4).
```

```{tip}
Per ottenere i migliori risultati:

- Verificare l'uniformità luminosa acquisendo un'immagine di test (durante la fase di calibrazione)
- Se necessario, regolare leggermente la distanza o l'angolo del Toplight
- Considerare l'uso di diffusori se l'illuminazione presenta hotspot evidenti
```

### Cablaggio illuminatore
```{list-table} 
:header-rows: 1
:widths: 30 70

* - Parametro
  - Requisito / Azione
* - **Tensione**
  - Verificare specifica sull'etichetta dell'illuminatore (tipicamente **24V DC**).
* - **Corrente**
  - Verificare specifica (tipicamente **1-3A**).
* - **Cablaggio**
  - Predisporre un cavo di alimentazione dedicato dal quadro elettrico.
* - **Schermatura**
  - Utilizzare cavi schermati per ridurre le interferenze elettromagnetiche (EMI).
```

```{note}

Per dettagli sui collegamenti elettrici, consultare la sezione [Cablaggio e Connessioni](10_Cablaggio_Connessioni.md).
```

---

## Schermatura da luce ambientale

La stabilità del sistema di visione dipende fortemente dalla consistenza delle condizioni di illuminazione. La luce ambientale variabile può causare rilevazioni incoerenti.

```{warning}
**Protezione da fonti luminose esterne**

Si raccomanda fortemente di schermare la cella robotica da:
- Luce solare diretta o indiretta
- Illuminazione artificiale variabile (es. lampade con dimmer)
- Riflessi da superfici lucide circostanti
- Flash o luci intermittenti nell'area

```

---

## Riferimenti correlati

Per informazioni complementari all'installazione meccanica:

- **Calcolo della distanza ottimale camera**: [Calcolo Distanza Ottimale](rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md)
- **Specifiche tecniche complete**: [Specifiche FlexiVision](rif_tecnico_specifiche/04_Specifiche_FlexiVision.md)
- **Passo successivo - Collegamenti elettrici**: [Cablaggio e Connessioni](10_Cablaggio_Connessioni.md)
- **Calibrazione camera**: [Calibrazione della Camera](14_calibrazione_camera.md)
