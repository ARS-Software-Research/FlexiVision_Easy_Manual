# **Specifiche Dettagliate FlexiVision**

Questa sezione fornisce le specifiche tecniche complete del sistema FlexiVision Easy, inclusi dettagli su camera industriale, VisionController, griglia di calibrazione, protocolli di comunicazione e configurazioni hardware.

---
(specifiche_camera)=
## Camera 

```{figure} img/Camera2.png
:alt: Camera FlexiVision CAM-CIC-5000-20G-1
:align: center
:width: 50%
```

Il sistema FlexiVision utilizza telecamere ad alta risoluzione con interfaccia Gigabit Ethernet per garantire rapidità nell'acquisizione delle immagini e precisione nel riconoscimento dei componenti.

### Specifiche elettriche
```{list-table}
:header-rows: 1
:widths: 40 60

* - **Caratteristica**
  - **Specifiche**
* - Modello
  - CAM-CIC-5000-20G-1
* - Sensore
  - Sony IMX264 CMOS Global Shutter
* - Pixel Effettivi
  - 5 MP (2448 × 2048)
* - Pixel Size
  - 3.45 × 3.45 μm
* - Dimensione Sensore
  - 2/3"
* - Frame Rate
  - 24 fps
* - Bit Depth
  - 12 bit
* - SNR
  - \>38 dB
* - Dynamic Range
  - 70 dB
* - Formato Immagine
  - Mono8 / 10 / 10Packed
* - Gain
  - X1 ~ X32
* - Gamma
  - Da 0 a 4, supporto LUT
* - Tempo di Esposizione
  - 34.23 μS ~ 1S
* - Modalità Trigger
  - Software / Hardware / Free run
* - Buffer Immagine
  - 256 MB
* - Consumo Energetico
  - 12V ≈ 3.2 W
* - Attacco Obiettivo
  - C-mount
* - GPIO
  - Connettore Hirose 6-pin: 1 ingresso opto-isolato, 1 uscita opto-isolata, 1 I/O configurabile
* - Interfaccia
  - GigE Vision V2.0 / GenICam
* - Temperatura Operativa
  - -30°C ~ +50°C
* - Temperatura di Stoccaggio
  - -30°C ~ +80°C
* - Certificazioni
  - CE, FCC, RoHS
```
### Connettore GPIO (Hirose 6-pin)

```{figure} img/Pin_Cam.png
:alt: Connettore GPIO Hirose 6-pin
:align: center
:width: 70%

Vista posteriore della camera con connettori
```

```{list-table}
:header-rows: 1
:widths: 10 20 70

* - **Pin**
  - **Segnale**
  - **Descrizione**
* - 1
  - Power
  - Ingresso alimentazione DC 9V ~ 24V
* - 2
  - Line1
  - Ingresso opto-isolato
* - 3
  - Line2
  - GPIO (I/O configurabile senza opto-isolamento via software)
* - 4
  - Line0
  - Uscita opto-isolata
* - 5
  - IO GND
  - Massa opto-isolata
* - 6
  - GND
  - Massa
```

```{warning}
**Requisiti di rete obbligatori**

L'interfaccia Gigabit Ethernet è obbligatoria e richiede un'infrastruttura di rete compatibile (switch Gigabit Ethernet).

La mancata osservanza di questo requisito compromette completamente l'operatività della telecamera. Verificare che tutti i componenti di rete (cavi, switch, porte) supportino lo standard GigE.
```

### Metodi di alimentazione

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - **Metodo**
  - **Descrizione**
  - **Requisiti**
* - **PoE**
  - Alimentazione e dati su un unico cavo Ethernet. Consumo circa 3.2 W.
  - Richiede PoE Injector o Switch PoE compatibile (IEEE 802.3af/at)
* - **Cavo Camera Esterno**
  - Alimentazione DC esterna tramite connettore Hirose 6-pin (6V ~ 26V). Incluso nel kit.
  - Cavo Ethernet separato necessario solo per i dati
```

```{tip}
**Quale metodo scegliere?**

- **PoE**: ideale per installazioni pulite con un solo cavo, ma richiede hardware di rete specifico
- **Alimentazione esterna**: soluzione standard più flessibile, consigliata per la maggior parte delle applicazioni
```

### Specifiche fisiche e dimensioni
```{figure} img/Dimensioni_Cam.png
:alt: Dimensioni camera CAM-CIC-5000-20G-1
:align: center
:width: 100%

Dimensioni camera CAM-CIC-5000-20G-1 (mm)
```
```{list-table}
:header-rows: 1
:widths: 40 60

* - **Caratteristica**
  - **Valore**
* - Larghezza × Altezza (corpo)
  - 29 × 29 mm
* - Profondità (corpo)
  - 42.0 mm
* - Profondità totale (incluso connettore posteriore)
  - 48.9 mm
* - Sporgenza frontale (attacco obiettivo)
  - 12.60 mm
* - Interasse fori di fissaggio laterali (M2)
  - 20.0 × 23.7 mm
* - Fori di fissaggio frontali
  - 2× M2 profondità 3 mm
* - Fori di fissaggio laterali
  - 4× M2 profondità 3.5 mm + 3× M3 profondità 3.5 mm
* - Peso
  - 88 g
```
---
(specifiche_obiettivo)=
## Obiettivo

---
(specifiche_VC)=
## VisionController
```{figure} img/PC.png
:alt: VisionController FlexiVision
:align: center
:width: 50%
```

Il sistema FlexiVision opera su un PC Industriale (VisionController) che funge da controller principale per il software di visione. ARS fornisce il VisionController già pre-configurato e testato con il software FlexiVision Easy installato.

### Specifiche elettriche

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Caratteristica**
  - **Specifiche**
* - CPU
  - Intel Core i3-1115G4 1.7 (4.1) GHz
* - Memoria (RAM)
  - 8G DDR4 3200 MHz
* - Archiviazione
  - 256G 
* - TPM
  - TPM 2.0
* - Sistema Operativo
  - Win11 LTSC 2024
* - Pulsante di accensione
  - Sì (pannello frontale con spia luminosa)
* - Porte Ethernet
  - **J6412:** 4× 1Gb LAN — **i3/i7:** 3× Gb LAN
* - Porte USB
  -  6× USB 3.0 TypeA
* - Uscita Video
  - 1× HDMI + 1× DisplayPort
* - Audio
  - Line Out + MIC (Jack 2-in-1)
* - Alimentazione (V DC)
  - 12 ~ 32 V DC
* - Temperatura Operativa
  - 1°C ~ +50°C
* - Temperatura di Stoccaggio
  - -20°C ~ +65°C
* - Umidità
  - &lt;90% (senza condensa)
* - Materiale Scocca
  - Lega di alluminio + acciaio
* - Grado di Protezione
  - IP20
* - Metodo di Installazione
  - Montaggio a parete (DIN Rail opzionale)
* - Consumo Energetico
  - 25 W
* - Dimensioni (L × A × P)
  - 59.8 × 200 × 119.5 mm
* - Peso
  - 2 kg
* - Certificazioni
  - CE, UL
```

```{note}
Il VisionController dispone di ... che possono alimentare direttamente la camera e altri dispositivi compatibili, eliminando la necessità di ....
```
### Porte PC
```{figure} img/Spec_Elettriche_PC.png
:alt: Schema elettrico VisionController
:align: center
:width: 80%
```


```{list-table}
:header-rows: 1
:widths: 10 25 65

* - **Ref.**
  - **Connettore**
  - **Descrizione**
* - A
  - Pulsante di accensione
  - Accensione e spegnimento del dispositivo
* - B
  - ETH 10/100/1000 Mbit – RJ45 (LAN 1)
  - Porta Ethernet Gigabit 1
* - C
  - ETH 10/100/1000 Mbit – RJ45 (LAN 2)
  - Porta Ethernet Gigabit 2
* - D
  - Porta Seriale (RS232) COM1
  - Interfaccia seriale RS232 COM1
* - E
  - Porta Seriale (RS232) COM2
  - Interfaccia seriale RS232 COM2
* - F
  - Connettore di ingresso alimentazione
  - Ingresso alimentazione 12–32V DC (terminal block 3-pin)
* - G
  - Uscita Audio + MIC (Jack 3.5 mm)
  - 1× uscita audio di linea + ingresso microfono (jack 3.5 mm)
* - H
  - 6× USB-A
  - Porte USB (USB 3.0 TypeA per versioni i3/i7)
* - I
  - Porta video 2
  - **B2B12/B2B14:** HDMI 2 — **B2B15/B2B16:** DisplayPort
* - L
  - Porta HDMI 1
  - Uscita video HDMI 1
* - M
  - ETH 10/100/1000 Mbit – RJ45 (LAN 3)
  - Porta Ethernet Gigabit 3
```
### Specifiche fisiche 

```{figure} img/Dim_PC.png
:alt: Dimensioni VisionController
:align: center
:width: 80%
```

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Caratteristica**
  - **Valore**
* - Larghezza (totale con staffe)
  - 245.00 mm
* - Larghezza (corpo)
  - 227.00 mm
* - Larghezza pannello connettori
  - 200.00 mm
* - Altezza (totale con staffe)
  - 123.00 mm
* - Altezza (corpo)
  - 120.00 mm
* - Profondità
  - 61.10 mm
```

```{tip}


Il VisionController è progettato per montaggio .....
```

---
(specifiche_griglia)=
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


## Componenti opzionali 

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

```{list-table}

* - **FlexiBowl → Alimentazione**
  - Cavo di alimentazione dedicato
* - **Tramoggia → FlexiBowl**
  - Cavo di segnale/alimentazione 
* - **Camera → VisionController**
  - Cavo Ethernet GigE (dati) + Cavo alimentazione DC
* - **Robot → VisionController**
  - Cavo Ethernet (comunicazione TCP/IP)
* - **VisionController → Alimentazione**
  - 9-36V DC
```

Per schemi elettrici dettagliati, consultare la sezione [Cablaggio e Connessioni](10_Cablaggio_Connessioni.md).


---

