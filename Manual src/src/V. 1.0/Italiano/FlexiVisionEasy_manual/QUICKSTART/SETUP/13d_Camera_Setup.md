(camerasetup)=
# **Passo 7: Camera Setup**

Questa sezione descrive la procedura per configurare e testare la telecamera industriale del sistema FlexiVision One. La corretta configurazione della camera è fondamentale per garantire l'acquisizione di immagini di qualità.

```{note}
**Prerequisiti**

Prima di procedere, assicurarsi che:
- La camera sia stata installata meccanicamente alla distanza corretta
- Il cavo Ethernet della camera sia connesso al VisionController
- La camera sia alimentata (tramite PoE o alimentazione esterna)
- FlexiBowl sia configurato e il backlight funzionante (per test acquisizione)
```

---

## Accesso alla configurazione Camera


**Navigazione**

1. Dalla pagina principale del software, cliccare su **SETUP**
2. Nella pagina SETUP, identificare e cliccare sull'icona **Camera Setup**
3. Si apre la pagina di configurazione della camera


---

## Panoramica interfaccia Camera Setup

La pagina Camera Setup presenta tre riquadri informativi principali e un'area di configurazione:

immagine schermata camera setup

```{list-table}
:header-rows: 1
:widths: 30 70

* - Sezione
  - Descrizione
* - **Camera Selected**
  - Mostra l'identificazione della camera attualmente selezionata (modello e numero seriale)
* - **Serial Camera**
  - Visualizza il numero seriale univoco della camera connessa
* - **Status**
  - Indica lo stato della connessione e dell'acquisizione
* - **Calibration Status**
  - Mostra se la camera è stata calibrata o meno
* - **Config Camera**
  - Pulsante per aprire la pagina di configurazione dettagliata
```

---

## Procedura di configurazione

inserire immagini delle schermate per ogni passaggio per renderli più chiari e visibili 

```{list-table}
* - **Accesso configurazione**
  - 1. Cliccare sul pulsante **Config Camera X** (dove X è il numero della camera)
    2. Si apre una nuova finestra con le impostazioni dettagliate della camera

* - **Attivazione modalità avanzata**
  - 3. Nella finestra di configurazione camera, localizzare e cliccare sul pulsante **Expert** (in basso a destra)
    4. Questa modalità fornisce accesso a tutte le impostazioni avanzate della camera necessarie per la configurazione iniziale
* - **Configurazione image acquisition device**
  - 5. Nel pannello **Expert**, cliccare sulla sezione **Image Acquisition** da **Settings**
    6. Cercare e cliccare su **Image Acquisition Device**
    7. Si apre un menu di selezione dei dispositivi di acquisizione disponibili
* -  **Identificazione camera specifica**
  - 8. Dal menu dei dispositivi, selezionare la camera fisica connessa
        - Cercare nell'elenco il numero seriale o il modello della vostra camera
        - Esempio: "CAM-CIC-5000-20G-XXXXX" (dove XXXXX è il seriale)
    9. Cliccare sulla camera per selezionarla
    10. Confermare la selezione 
```

```{tip}
**Identificazione del seriale corretto**

Se sono elencate multiple camere o dispositivi:
- Il numero seriale è riportato su un'etichetta sulla camera fisica
- Confrontare l'ultimo gruppo di caratteri del seriale per identificare la camera corretta
- In caso di dubbio, disconnettere fisicamente altre camere per identificare quella in uso
```


```{list-table} 
* - **Selezione video format**
  - 11. Cliccare su **Video Formats** 
    12. Dalla lista dei formati disponibili, selezionare **Generic GigEVision**
    13. Selezionare **Mono** (monocromatico) come tipo di sensore
```


```{warning}
**Formato corretto obbligatorio**

È fondamentale selezionare **Generic GigEVision Mono**:
- Altri formati potrebbero non funzionare o causare errori
- Formati a colori non sono compatibili con questa camera
- Se il formato non è disponibile, potrebbero mancare driver o configurazioni di sistema
```

```{list-table}
* - **Attivazione sistema di acquisizione**
  - 14. Dopo aver selezionato il formato corretto, cliccare su **Initialize Acquisition**  
  15.Attendere il completamento dell'inizializzazione (pochi secondi)
* - **Verifica funzionamento acquisizione**
  - 16. Localizzare il pulsante **Run** in alto a sinistra dell'interfaccia (icona "play" o simile)
    17. Cliccare su **Run** ripetutamente (5-10 volte) per acquisire immagini di test
    18. Osservare l'area di visualizzazione immagine:
        - Dovrebbe mostrare la vista della camera sul FlexiBowl
        - L'immagine dovrebbe aggiornarsi ad ogni click su Run
        - Verificare che l'illuminazione sia visibile
```

```{warning}
**Diagnosi schermo completamente blu**

Se durante i test l'immagine acquisita appare **completamente blu**  almeno una volta:

**Causa**: Problema di comunicazione GigE (latenza di rete o dimensione pacchetti non ottimale)

**Soluzione obbligatoria**:

1. Dal menu in alto, selezionare **GigE** (o **GigE Vision Settings**)

2. Modificare i seguenti parametri:
   - **Latency Level** (Livello di Latenza)
   - **Packet Size** (Dimensione Pacchetto)

Procedere con gli step successivi per la configurazione ottimale di questi parametri.
```

---

#### Latency Level (Livello di Latenza)

```{note}
**Regolazione latency**

Il parametro **Latency Level** controlla il buffer di comunicazione tra camera e VisionController.

**Valori tipici**:
- Valore predefinito: spesso 1 o 2
- Range disponibile: 1-10 (o 1-20 a seconda del driver)

**Come regolare**:

1. Aumentare gradualmente il valore (es: da 1 a 3, poi a 5)
2. Dopo ogni modifica, testare l'acquisizione (pulsante Run) 10-20 volte
3. Se non si verificano più schermate blu, il valore è corretto
4. Se le schermate blu persistono, aumentare ulteriormente

**Valore consigliato**: 
- Per reti dedicate (camera collegata direttamente al VisionController o tramite switch dedicato): 3-5
- Per reti condivise o con switch multipli: 5-10
```

#### Packet Size (Dimensione Pacchetto)

```{note}
**Regolazione packet size**

Il parametro **Packet Size** definisce la dimensione dei pacchetti dati trasmessi sulla rete Ethernet.

**Valori tipici**:
- Valore predefinito: 1500 byte (MTU standard Ethernet)
- Valore ottimale per GigE Vision: 8192-9000 byte (Jumbo Frames)

**Come regolare**:

1. Provare ad aumentare il valore a **9000** byte (Jumbo Frame massimo)
2. Se l'acquisizione fallisce completamente, ridurre gradualmente (8000, 7000, ecc.)
3. Se 9000 funziona, testare con 10-20 acquisizioni per conferma

**Nota importante**: 
- Jumbo Frames (> 1500 byte) richiedono che tutti i dispositivi di rete (switch, router) li supportino
- Se il packet size alto causa problemi, tornare a 1500 e utilizzare invece un Latency Level più alto
```

```{tip}
**Configurazione ottimale consigliata**

Per la maggior parte delle installazioni:

- **Latency Level**: 5
- **Packet Size**: 9000 (se la rete supporta Jumbo Frames) oppure 1500 (rete standard)

Con questi valori, le schermate blu dovrebbero scomparire completamente.

Se i problemi persistono, verificare:
- Qualità dei cavi Ethernet (utilizzare Cat6 o superiore)
- Performance dello switch di rete (deve essere Gigabit, non Fast Ethernet)
- Carico di rete (evitare altro traffico pesante sulla stessa rete)
```

---


```{important}
**Regolazioni immagine**

Nella sezione Expert/Settings sono disponibili anche parametri per regolare esposizone, luminosità e contrasto, ma NON è necessario modificare questi parametri in questa fase. Verra fatto poi automaticamente o manualmente durante le fasi successive.

Procedere quindi con i valori automatici per completare il setup iniziale.
```

---

```{list-table}
* - **Verifica finale e salvataggio**
  - 19. Cliccare su **Run** almeno 2-3 volte consecutivamente  
    20. Verificare che:  
      - Nessuna immagine appaia completamente blu o nera
      - Le immagini si aggiornino regolarmente
      - La superficie del FlexiBowl sia chiaramente visibile
      - L'illuminazione sia uniforme
    21. Se tutti i test sono positivi, la configurazione è corretta
```
---
```{tip}

A questo punto dovrebbero essere completati:
- [✓] Login e attivazione licenza
- [✓] Creazione ricetta base
- [✓] FlexiBowl Setup
- [✓] Hopper Setup 
- [✓] Robot Setup
- [✓] Camera Setup
```
---

## Passi successivi

Una volta completato il Camera Setup:

1. **Verifica setup completo**: Tornare alla pagina SETUP e verificare che tutti i componenti (FlexiBowl, Hopper se presente, Robot, Camera) siano configurati

2. **Procedere con calibrazione**: [Calibrazione Camera](calibrazione)

