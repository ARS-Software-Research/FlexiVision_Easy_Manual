# **Specifiche Dettagliate FlexiVision**

Questa sezione fornisce le specifiche tecniche complete del sistema FlexiVision Easy, inclusi dettagli su camera industriale, VisionController, griglia di calibrazione, protocolli di comunicazione e configurazioni hardware.

Consultare questa sezione per:
- Verificare la compatibilità con la propria infrastruttura di rete
- Dimensionare correttamente l'alimentazione elettrica
- Pianificare l'integrazione meccanica dei componenti
- Configurare i protocolli di comunicazione robot-visione

---

## Camera 

Il sistema FlexiVision utilizza telecamere ad alta risoluzione con interfaccia Gigabit Ethernet per garantire rapidità nell'acquisizione delle immagini e precisione nel riconoscimento dei componenti.

### Specifiche elettriche

```{list-table}
:header-rows: 1
:widths: 40 60

* - Caratteristica
  - Specifiche
* - Brand & Modello
  - Cognex CAM-CIC-5000-20G
* - Risoluzione
  - 5 MP (2448 × 2048 pixel)
* - Frame Rate
  - 14 fps
* - Tipo Sensore
  - CMOS
* - Dimensioni Sensore
  - 1/2.5"
* - Tipologia
  - Monocromatica (Monochrome)
* - Protocollo di Connettività
  - Gigabit Ethernet (GigE)
```

```{warning}
**Requisiti di rete obbligatori**

L'interfaccia Gigabit Ethernet è obbligatoria e richiede un'infrastruttura di rete compatibile (switch Gigabit Ethernet).

La mancata osservanza di questo requisito compromette completamente l'operatività della telecamera. Verificare che tutti i componenti di rete (cavi, switch, porte) supportino lo standard GigE.
```

### Metodi di alimentazione

La camera supporta due modalità di alimentazione alternative:

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - Metodo
  - Descrizione
  - Requisiti
* - **PoE (Power over Ethernet)** - Opzionale
  - L'alimentazione e i dati vengono trasmessi tramite un unico cavo Ethernet. Consumo circa 3.3 W.
  - Richiede un PoE Injector o uno Switch PoE compatibile (IEEE 802.3af/at)
* - **Cavo Camera Esterno** - Standard
  - L'alimentazione è fornita da una fonte DC esterna tramite cavo dedicato (incluso nel kit).
  - Cavo Ethernet separato necessario solo per la comunicazione dati (PoE non richiesto)
```

```{tip}
**Quale metodo scegliere?**

- **PoE**: ideale per installazioni pulite con un solo cavo, ma richiede hardware di rete specifico
- **Alimentazione esterna**: soluzione standard più flessibile, consigliata per la maggior parte delle applicazioni
```

### Specifiche fisiche e dimensioni
immagini + pdf??

---

## VisionController

Il sistema FlexiVision opera su un PC Industriale (VisionController) che funge da controller principale per il software di visione. ARS fornisce il VisionController già pre-configurato e testato con il software FlexiVision Easy installato.

### Specifiche elettriche

```{list-table}
:header-rows: 1
:widths: 40 60

* - Caratteristica
  - Specifiche
* - Alimentazione (Input)
  - 9 ~ 36 V DC (tramite terminal block)
* - Consumo Energetico
  - 15 – 35 W (tipico 25 W)
* - Porte di Rete (LAN)
  - 6x LAN Gigabit Ethernet (di cui 4x PoE)
* - Porte USB
  - 2x USB 3.0, 2x USB 2.0
* - Uscita Video
  - 1x DisplayPort (fino a 4096×2160 @ 60Hz)
* - Protezione
  - Protezione da sovratensione e inversione polarità
```

```{note}


Il VisionController dispone di ... che possono alimentare direttamente la camera e altri dispositivi compatibili, eliminando la necessità di ....
```

### Specifiche fisiche e hardware

```{list-table}
:header-rows: 1
:widths: 40 60

* - Caratteristica
  - Specifiche
* - Dimensioni (L × P × A)
  - 150 mm × 145 mm × 84 mm
* - Peso
  - 4 kg
* - Sistema Operativo
  - Windows 11 IoT Enterprise 2021 LTSC VALUE 64 bit
* - Processore
  - Intel Core (specifiche su richiesta)
* - Memoria (RAM)
  - 8 GB DDR4-3200 MHz SODIMM
* - Archiviazione
  - SSD 256 GB SATA 2.5"
* - Grado di Protezione
  - IP40 (installazione in quadro elettrico consigliata)
* - Temperatura Operativa
  - 0°C ~ +50°C
* - Certificazioni
  - CE, FCC
```

```{tip}


Il VisionController è progettato per montaggio .....
```

---

## Griglia di calibrazione

Una calibrazione eccellente è il requisito fondamentale per l'accuratezza del sistema FlexiVision. Solo una calibrazione ad alta precisione garantisce che le coordinate rilevate dalla telecamera (pixel) vengano convertite in modo accurato nelle coordinate reali del robot (millimetri), assicurando così il successo dell'applicazione di picking.

### Importanza della griglia dedicata ARS

Sebbene sia tecnicamente possibile eseguire la calibrazione utilizzando una griglia stampata su carta, l'utilizzo della **Griglia di Calibrazione Dedicata ARS** (spesso utilizzata con l'opzione Laser Tool) innalza significativamente la precisione e semplifica il flusso di lavoro di manutenzione.

La griglia ARS è realizzata con un'accuratezza estremamente elevata, impossibile da replicare con una stampa standard. Inoltre, la sua struttura è progettata per il montaggio ripetibile sul FlexiBowl.

### Confronto: Griglia ARS vs Griglia Stampata

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Caratteristica
  - Griglia ARS Dedicata
  - Griglia Stampata su Carta
* - **Precisione Fabbricativa**
  - Estremamente Alta (Lavorazione CNC dedicata)
  - Bassa/Variabile (Dipende dalla qualità della stampante)
* - **Ripetibilità di Montaggio**
  - Alta (Pin dedicati che si fissano in fori predefiniti sul FlexiBowl)
  - Bassa (Non ripetibile, richiede riposizionamento manuale)
* - **Punto di Riferimento Robot**
  - Più Preciso (Con Laser Tool, il contatto fisico è sostituito dall'allineamento visivo)
  - Meno Preciso (Utilizza tip fisico o punta soggetta a usura)
* - **Vantaggio in Ricalibrazione**
  - Solo la visione richiede ricalibrazione. Il punto di riferimento del robot è mantenuto.
  - Sia la visione che il robot richiedono una ricalibrazione completa
* - **Durabilità**
  - Illimitata (metallo anodizzato)
  - Limitata (carta si deteriora, inchiostro sbiadisce)
```

```{tip}
**Investimento consigliato**

Per applicazioni di produzione, la griglia ARS dedicata  riduce drasticamente i tempi di ricalibrazione e aumenta la precisione complessiva del sistema.
```

### Specifiche tecniche griglia


- Griglia per FlexiBowl 200: 
- Griglia per FlexiBowl 350: 
- Griglia per FlexiBowl 500: 
- Griglia per FlexiBowl 650: 
- Griglia per FlexiBowl 800: 
- Griglia per FlexiBowl 1200: 

**Materiale:** Alluminio anodizzato con pattern inciso laser ad alta precisione (±0.05 mm)


Per informazioni dettagliate sulle procedure di calibrazione, consultare la sezione [Calibrazione della Camera](14_calibrazione_camera.md).

---

## Kit  base

Il kit standard FlexiVision Easy include tutti i componenti necessari per l'installazione e la messa in servizio del sistema.

```{list-table}
:header-rows: 1
:widths: 40 60

* - Componente
  - Descrizione e Note
* - **Camera Industriale**
  - Cognex CAM-CIC-5000-20G con lente preinstallata e calibrata
* - **Lente**
  - Ottica fissa ottimizzata per la distanza di lavoro standard (specificare modello)
* - **VisionController**
  - PC industriale con software FlexiVision Easy preinstallato e configurato
* - **Griglia di Calibrazione**
  - Griglia dedicata ARS per il modello di FlexiBowl specificato nell'ordine
* - **Cavo Camera - Alimentazione**
  - Lunghezza standard 3 m (lunghezze personalizzate disponibili su richiesta)

* - **Documentazione**
  - Manuale utente, guida rapida, certificati di conformità
```

```{note}
**Personalizzazione lunghezze cavi**

I cavi di comunicazione e alimentazione possono essere ordinati in lunghezze personalizzate in base alle specifiche esigenze dell'installazione. Specificare le lunghezze desiderate al momento dell'ordine.

Lunghezze standard disponibili: 3m, 5m, 10m, 15m
```

## Componenti opzionali    forse ridondante qui?

Componenti aggiuntivi disponibili separatamente:
:::{div} admonition
<a href="rif_tecnico_specifiche/08_Opzioni.md" style="text-decoration: none; color: inherit;">**Toplight**: Illuminatore LED dedicato per applicazioni con scarsa illuminazione ambientale</a>
:::

:::{div} admonition
<a href="rif_tecnico_specifiche/08_Opzioni.md" style="text-decoration: none; color: inherit;">**Backlight**: Illuminatore LED</a>
:::

:::{div} admonition
<a href="rif_tecnico_specifiche/08_Opzioni.md" style="text-decoration: none; color: inherit;">**Laser Tool**: strumento laser per calibrazione ad alta precisione</a>
:::

:::{div} admonition
Cavi di ricambio e di lunghezza personalizzata
:::

---

## Panoramica collegamenti

![Panoramica Collegamenti](img/pan_collegamenti.png)

*Schema di collegamento completo del sistema FlexiVision Easy con robot e FlexiBowl*

```{note}
**Legenda collegamenti**

1. **Camera → VisionController**: Cavo Ethernet GigE (dati) + Cavo alimentazione DC
2. **VisionController → Robot**: Cavo Ethernet (comunicazione TCP/IP)
3. **VisionController → Rete/PC**: Cavo Ethernet (configurazione e monitoraggio)
4. **VisionController → Alimentazione**: 9-36V DC
5. **FlexiBowl → Robot/PLC**: Segnali digitali di controllo

Per schemi elettrici dettagliati, consultare la sezione [Cablaggio e Connessioni](10_Cablaggio_Connessioni.md).
```

---

## Protocollo di comunicazione robot-visione

FlexiVision Easy comunica con il robot tramite protocollo **TCP/IP** su rete Ethernet. Il robot deve essere in grado di aprire e gestire uno o più server di comunicazione per ricevere e inviare stringhe tramite un task parallelo rispetto a quello principale, così da ricevere informazioni dal sistema di visione mentre il lavoro principale è in esecuzione.

### Specifiche protocollo

```{list-table}
:header-rows: 1
:widths: 35 65

* - Parametro
  - Valore
* - Protocollo
  - TCP/IP
* - Porta
  - Configurabile (default: 2000)
* - Carattere di terminazione
  - CHR(13) - Carriage Return
* - Formato dati
  - Stringa ASCII
* - Timeout
  - Configurabile (default: 5000 ms)
* - Encoding
  - UTF-8
```

### Comandi disponibili

Il sistema supporta i seguenti comandi tramite stringhe di testo inviate sulla connessione TCP/IP:

#### Gestione ricette

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `set_Recipe=nome_ricetta`
  - Carica la ricetta corrispondente al "nome_ricetta" specificato
  - Nessuno
* - `get_Recipe`
  - Restituisce il nome della ricetta attualmente caricata
  - `nome_ricetta`
```

#### Comandi di localizzazione

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `start_Locator`
  - Avvia il processo di localizzazione dei pezzi. Richiama automaticamente la routine di manipolazione FlexiBowl se non ci sono pezzi prelevabili
  - `Pattern_1;x;y;r`
* - `stop_Locator`
  - Ferma il processo di localizzazione
  - Nessuno
* - `turn_Locator`
  - Se nessun pezzo è stato prelevato, fa ruotare il FlexiBowl e riavvia la ricerca
  - `Pattern_1;x;y;r`
* - `test_Locator`
  - Avvia la localizzazione senza attivare il FlexiBowl (solo acquisizione immagine)
  - `Pattern_1;x;y;r`
* - `state_Locator`
  - Restituisce lo stato diagnostico del localizzatore
  - `Locator is Running` / `Locator is in Error` / `Locator is not Running`
```

#### Comandi di controllo qualità

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `start_Control`
  - Avvia il ciclo di ispezione qualità sul pezzo
  - `Control_1;x;y;r`
```

#### Comandi FlexiBowl

```{list-table}
:header-rows: 1
:widths: 30 40 30

* - Comando
  - Azione
  - Valore di Ritorno
* - `start_Empty`
  - Avvia la sequenza di svuotamento rapido (Quick-Emptying) del FlexiBowl
  - `start_Empty ended`
```


#### Segnali hopper opzionale

```{note}
If hopper should be activated you will receive the string “Hopper;signalnumber;time”

```



Per informazioni dettagliate sull'installazione fisica e i collegamenti elettrici, procedere con le sezioni successive:
- [Calcolo Distanza Ottimale Camera](05_Calcolo_distanza_ottimale.md)
- [Installazione Meccanica](QUICKSTART/09_Installazione_Meccanica.md)
- [Cablaggio e Connessioni](QUICKSTART/10_Cablaggio_Connessioni.md)