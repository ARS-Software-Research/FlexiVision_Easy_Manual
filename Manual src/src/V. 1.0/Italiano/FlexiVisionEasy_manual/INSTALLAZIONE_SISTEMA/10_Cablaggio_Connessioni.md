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
  - Alimentazione 110/220 Vdc

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

immagine con collegamenti elettrici della configurazione a due e tre flexibowl, due e tre camere e due e tre tramogge 