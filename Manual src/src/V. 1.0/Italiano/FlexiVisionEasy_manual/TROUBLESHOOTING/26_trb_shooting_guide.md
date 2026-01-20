# Risoluzione Problemi 

## Troubleshooting per la sezione "installazione del sistema"

```{list-table} 
:widths: 20 25 55
:header-rows: 1

* - Sezione
  - Componente
  - link alla pagina
* - **Installazione Meccanica**
  - 1. **VisionController**  
    2. **Camera**  
    3. **Toplight**  
    4. **Luce Ambientale**  
  - 1. [Vai alla Sezione](troubleshooting_vision_controller)
    2. [Vai alla Sezione](troubleshooting_camera)   
    3. [Vai alla Sezione](troubleshooting_toplight)
    4. [Vai alla Sezione](troubleshooting_luce_ambientale)  
* - **Cablaggio e Connessioni**
  - 1. **Alimentazione**  
    2. **Ethernet**  
    3. **Pneumatica**  
    4. **Connessione Camera**
    5. **Connessione Toplight**
    6. **Multi-Dispositivo**  
  - 1. [Vai alla Sezione](troubleshooting_alimentazione)
    2. [Vai alla Sezione](troubleshooting_ethernet) 
    3. [Vai alla Sezione](troubleshooting_pneumatica)
    4. [Vai alla Sezione](troubleshooting_connessione_camera)
    5. [Vai alla Sezione](troubleshooting_connessione_toplight)
    6. [Vai alla Sezione](troubleshooting_multi)  
```
---

## Troubleshooting per la sezione "Quickstart"

```{list-table} 
:widths: 20 25 55
:header-rows: 1

* - Sezione
  - Passo Setup
  - Criticità Riscontrate
* - **Configurazione Iniziale**
  - **FlexiBowl (P4)**
  - Parametri di accelerazione errati, mancata risposta seriale/TCP.
* - **Configurazione Iniziale**
  - **Hopper (P5)**
  - Sovraccarico del disco, mancata attivazione fotocellula.
* - **Configurazione Iniziale**
  - **Robot (P6)**
  - Timeout comunicazione, errore handshake protocollo.
* - **Configurazione Iniziale**
  - **Camera (P7)**
  - Errore apertura stream GigE, timeout esposizione.
* - **Calibrazione e Ricette**
  - **Calibrazione Camera**
  - Errore riproiezione elevato, target non rilevato.
* - **Calibrazione e Ricette**
  - **Protocol Setup**
  - Stringhe dati troncate, errori di sintassi nel payload.
* - **Calibrazione e Ricette**
  - **Modelli e ROI**
  - ROI troppo stretta, tolleranze di score troppo elevate.
* - **Calibrazione e Ricette**
  - **Istogrammi**
  - Saturazione dei bianchi, soglie di binarizzazione instabili.
* - **Calibrazione e Ricette**
  - **Robot Pick**
  - Offset X-Y costante, errore calibrazione mano-occhio.
* - **Avanzate e Monitoraggio**
  - **FlexiBowl Wizard**
  - Ottimizzazione parametri di vibrazione fallita.
* - **Avanzate e Monitoraggio**
  - **Tramoggia**
  - Tempi di scarico non sincronizzati con il vuoto del disco.
* - **Avanzate e Monitoraggio**
  - **Monitoraggio**
  - Log non salvati, calo di frame rate (FPS) durante l'esecuzione.
```


:::{card} IP Adress
    :class-card: shadow
    :link: 
    :link-type: 
:::


```{toctree}  
:hidden:
26b_Installazione_Mecc.md
26c_Cablaggio_Connessioni.md
26d_Conf_Iniziale.md
26e_Calib_Cam.md
26f_Protocol_Setup.md
26g_Creazione_Ricette_Modelli.md
26h_FlexiBowl_Wizard.md
26i_Conf_Tramoggia.md
```

