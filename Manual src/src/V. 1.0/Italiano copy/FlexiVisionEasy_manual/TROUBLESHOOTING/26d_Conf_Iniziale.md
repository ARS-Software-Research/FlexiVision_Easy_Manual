# Setup Iniziale

(troubleshooting_FB_setup)=
## FlexiBowl Setup 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **FlexiBowl non risponde**
  - • IP non configurato
    
    • FlexiBowl non acceso
    
    • Firewall attivo
  - • Configurare IP correttamente
    
    • Verificare LED READY acceso
    
    • Disabilitare firewall temporaneamente
* - **Parametri non si applicano**
  - • "Synchronize Parameters" non premuto
    
    • Connessione persa
  - • Cliccare sempre "Synchronize Parameters"
    
    • Verificare stabilità connessione
```

(troubleshooting_Hopper_setup)=
## Hopper Setup 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Tramoggia non si attiva mai**
  - • Hopper non abilitato
    
    • Area di controllo non definita
    
    • Soglie non calibrate
  - • Abilitare "Enable Hopper X"
    
    • Definire area con "Define Area Check"
    
    • Eseguire CAPTURE vuoto/pieno
* - **Tramoggia si attiva sempre**
  - • Soglie errate
    
    • Area troppo grande
    
    • Tempo vibrazione insufficiente
  - • Ripetere calibrazione con area VUOTA
    
    • Ridurre area di controllo
    
    • Aumentare parametro "Time"
* - **Test sempre rosso**
  - • Troppi componenti durante calibrazione
    
    • Riflessi nell'area
  - • Ripetere con numero minimo di pezzi
    
    • Riposizionare area escludendo riflessi
```

(troubleshooting_Robot_setup)=
## Robot Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Robot non riceve coordinate**
  - • IP robot errato
    
    • Porta TCP/IP non configurata
    
    • Protocollo incompatibile
  - • Verificare IP robot
    
    • Configurare porta (tipicamente 5000)
    
    • Selezionare protocollo corretto
* - **Robot va in posizioni sbagliate**
  - • Calibrazione non eseguita
    
    • Frame/Tool errato
    
    • Offset gripper errato
  - • Eseguire calibrazione robot
    
    • Verificare Frame e Tool
    
    • Ripetere calibrazione Robot Pick
* - **Timeout comunicazione**
  - • Timeout troppo basso
    
    • Connessione instabile
  - • Aumentare valore timeout
    
    • Stabilizzare connessione Ethernet
```

(troubleshooting_cam_setup)=
## Camera Setup 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Immagine troppo scura**
  - • Esposizione bassa
    
    • Toplight spento
  - • Aumentare esposizione
    
    • Verificare alimentazione toplight
* - **Immagine sovraesposta**
  - • Esposizione troppo alta
    
    • Toplight troppo potente
  - • Diminuire esposizione
    
    • Ridurre potenza toplight
* - **Immagine sfocata**
  - • Distanza errata (≠ 950-1000mm)
    
    • Lente non avvitata
    
    • Vibrazioni
  - • Correggere distanza di lavoro
    
    • Avvitare lente completamente
    
    • Fissare camera e ridurre vibrazioni
* - **Camera non acquisisce**
  - • Trigger non configurato
    
    • Pause insufficiente
  - • Configurare trigger correttamente
    
    • Inserire pause di 200ms
```