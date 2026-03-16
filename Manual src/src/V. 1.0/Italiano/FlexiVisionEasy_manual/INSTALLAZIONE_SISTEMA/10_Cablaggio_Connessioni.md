(cablaggio)=
# **Cablaggio e Connessioni**
immagine panoramica connessione elettriche 
tipo:  
![Pan Coll](img/panoramicacollegamenti.png)
```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **Da**
  - **A**
  - **Collegamento**

* - Rete elettrica
  - FlexiBowl
  - Alimentazione 110/220 Vdc

* - Rete elettrica
  - Robot
  - Alimentazione secondo le specifiche del robot in vostro possesso

* - Rete elettrica
  - Camera
  - Alimentazione 24 Vdc

* - Rete elettrica
  - Illuminatore (luce)
  - Alimentazione 24 Vdc

* - Rete elettrica
  - Controller Tramoggia
  - Alimentazione 110/220 Vdc

* - Controller Tramoggia
  - Tramoggia
  - Alimentazione e segnale

* - Robot
  - Controller Tramoggia
  - I/O Digitali

* - VisionController
  - Camera
  - Ethernet TCP

* - VisionController
  - FlexiBowl
  - Ethernet TCP

* - VisionController
  - Robot
  - Ethernet TCP
```


dal vecchio manuale:

```{list-table} 
:header-rows: 1
:widths: 10 70 20

* - **Step**
  - **Azione**
  - **Immagine**

* - 1
  - Collegare l'alimentazione alla connessione del FlexiBowl®.  
    [🔗 Fare riferimento al manuale per le specifiche di alimentazione](http://link-al-manuale.com)
  - (Immagine 1)

* - 2
  - Collegare il cavo Ethernet alla presa Ethernet del FlexiBowl®.
  - (Immagine 2)

* - 3
  - Collegare l'aria compressa alla connessione del FlexiBowl®.  
    [🔗 Fare riferimento al manuale per le specifiche pneumatiche](http://link-al-manuale.com)
  - (Immagine 3)

* - 4
  - Accendere l'interruttore AC del FlexiBowl® (posizione "I"). Il led READY è **ON**.
  - (Immagine 4)

* - 5
  - Collegare il FlexiBowl® al VisionController.
  - (Immagine 5)

* - 6
  - Collegare il VisionController (PC) tramite la connessione Ethernet.
  - (Immagine 6)

* - 7
  - Collegare la telecamera (compatibile POE). Deve essere collegata al VisionController.
  - (Immagine 7)
```

### Cablaggio illuminatore


![Pin Toplight](./img/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Parametro
  - Requisito / Azione
* - **Tensione**
  - 24V DC (±10%). Tensione minima di funzionamento: 20V DC sull'ingresso luce.
* - **Connettore**
  - M12 5 poli (T-coding).
* - **Pinout connettore**
  - Pin 1: +24V (marrone) — Pin 3: GND (blu) — Pin 4: STROBE PNP (nero)
* - **Modalità STROBE (PNP)**
  - Da 5V a 24V per accensione al 100%. Da 0V a 1V per spegnimento al 100%.
* - **Modalità CONTINUA**
  - Pin 1 (+24V) e Pin 3 (GND) collegati; Pin 4 (PNP) collegato a Pin 1.
* - **Caduta di tensione (cavo M12, 10m)**
  - 1.15V @ 5A — 2.3V @ 10A — 3.5V @ 15A — 4.6V @ 20A (max 20A)
* - **Schermatura**
  - Utilizzare cavi schermati per ridurre le interferenze elettromagnetiche (EMI).
```
```{warning}
**Sicurezza elettrica**

- Rispettare le tensioni di alimentazione e i morsetti di connessione indicati.
- Non modificare né smontare il prodotto.
- Non collegare o pulire l'apparecchio quando è sotto tensione.
- Non guardare direttamente la sorgente luminosa.
```
```{note}
Per dettagli sui collegamenti elettrici, consultare la sezione [Cablaggio e Connessioni](10_Cablaggio_Connessioni.md).
```

