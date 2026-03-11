(troubleshooting)=
# Risoluzione Problemi 

inserire qui tutti i "possibili problemi" delle varie pagine? o in entrambi?


## Troubleshooting per la sezione "installazione del sistema"

```{list-table} 
:widths: 45 45 25
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
:widths: 40 38 27
:header-rows: 1

* - Sezione
  - Componente
  - Link alla sezione
* - **Configurazione Iniziale**
  - 1. **Passo 4: FlexiBowl Setup**  
    2. **Passo 5: Hopper Setup** 
    3. **Passo 6: Robot Setup**   
    4. **Passo 7: Camera Setup** 
  - 1. [Vai alla Sezione](troubleshooting_FB_setup)  
    2. [Vai alla Sezione](troubleshooting_Hopper_setup)  
    3. [Vai alla Sezione](troubleshooting_Robot_setup)  
    4. [Vai alla Sezione](troubleshooting_cam_setup)
* - **Calibrazione e Ricette**
  - 1. **Calibrazione camera**  
    2. **Protocol Setup**  
    3. **Creazione Nuova Ricetta**  
    4. **Creazione Nuovo Modello**  
    5. **Modelli e ROI**  
    6. **Istogrammi**  
    7. **Robot Pick**
  - 1. [Vai alla Sezione](troubleshooting_calib_cam)  
    2. [Vai alla Sezione](troubleshooting_protocol_setup)  
    3. [Vai alla Sezione](troubleshooting_Nuova_Ricetta)  
    4. [Vai alla Sezione](troubleshooting_Nuovo_modello)  
    5. [Vai alla Sezione](troubleshooting_Modelli_ROI)  
    6. [Vai alla Sezione](troubleshooting_istogrammi)  
    7. [Vai alla Sezione](troubleshooting_robot_pick)
* - **Avanzate e Monitoraggio**
  - 1. **FlexiBowl Wizard**  
    2. **Tramoggia**  
    3. **Monitoraggio**
  - 1. [Vai alla Sezione](troubleshooting_FB_Wizard)  
    2. [Vai alla Sezione](troubleshooting_conf_tramoggia)  
    3. [Vai alla Sezione](troubleshooting_pneumatica)
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

## Risoluzione problemi comuni (Setup Iniziale)

### Problemi di connessione di rete

```{warning}
**Componenti non raggiungibili**

Se FlexiBowl, robot o camera non sono raggiungibili:

1. Verificare che tutti i cavi Ethernet siano collegati correttamente
2. Controllare che switch/router siano accesi
3. Verificare gli indirizzi IP di tutti i dispositivi:
   - Devono essere sulla stessa subnet (es: 192.168.1.x)
   - Non devono esserci conflitti di IP (due dispositivi con stesso IP)
4. Utilizzare il comando `ping` da terminale per testare la raggiungibilità
5. Disabilitare temporaneamente firewall sul VisionController per test

Per dettagli sulla configurazione di rete, vedere [Cablaggio e Connessioni](cablaggio).
```

### Licenza non attivabile

```{note}
**Problemi con la licenza**

Se la licenza non si attiva:
- Verificare la connessione Internet (alcune licenze richiedono validazione online)
- Controllare la data/ora del sistema operativo Windows (deve essere corretta)
- Assicurarsi di aver inserito la chiave esattamente come fornita

fare riferimento alla sezione [TroubleShooting]
```

```{tip}
**Prima configurazione completa**

Per una prima installazione, si consiglia di:
1. Completare tutti i setup di base (fino al Passo 7)
2. Effettuare la calibrazione camera seguendo la procedura guidata
3. Creare un modello di test con un pezzo semplice
4. Verificare il picking con il robot prima di procedere con la produzione
```

## Problemi comuni e soluzioni

### Illuminazione non uniforme

```{tip} non in questa fase ma utile?
**Ottimizzazione illuminazione**

Se l'illuminazione presenta zone più scure o più chiare:
- Verificare che backlight/toplight sia montato correttamente
- Pulire la superficie del piatto e dell'illuminatore
- Regolare l'intensità luminosa (parametro disponibile in configurazione avanzata)
- Verificare che non ci siano ostruzioni tra luce e superficie
```

## Problemi comuni e soluzioni (Hopper Setup)

### Hopper non si attiva

```{warning}
**Diagnosi mancata attivazione**

Se l'Hopper non si attiva:

1. Verificare che in **Enable Hopper** sia presente la spunta
2. Controllare il cablaggio elettrico del segnale digitale
3. Verificare che il numero **Signal** corrisponda al DO fisicamente connesso
4. Controllare l'alimentazione dell'Hopper 
5. Testare il segnale digitale con un multimetro (presenza tensione quando attivato)
6. Consultare il manuale dell'Hopper per verifiche specifiche del dispositivo
```


## Problemi comuni e soluzioni (Robot Setup)

### Robot non riesce a connettersi

```{warning}
**Diagnosi connessione fallita**

Se il robot non riesce a stabilire la connessione:

**Verifiche base**:
1. Server FlexiVision online (indicatore verde)
2. Indirizzo IP corretto nel programma robot
3. Porta corretta nel programma robot (uguale a FlexiVision)
4. Cavo Ethernet collegato correttamente

**Verifiche rete**:
1. Ping dal VisionController al robot:
   - Aprire Prompt comandi su VisionController
   - `ping <IP_ROBOT>` (es: `ping 192.168.1.10`)
   - Se fallisce: problema di rete fisica/configurazione IP

2. Ping dal robot al VisionController (se disponibile funzione ping sul robot)

3. Verificare che robot e VisionController siano sulla stessa subnet

**Verifiche firewall**:
1. Disabilitare temporaneamente firewall Windows per test
2. Se funziona, problema firewall → configurare eccezione

**Verifiche robot**:
1. Verificare sintassi corretta comando connessione TCP/IP (consultare manuale robot)
2. Controllare timeout connessione (aumentare se necessario)
3. Verificare permessi di rete sul controller robot
```

### Connessione instabile o si disconnette

```{note}
**Stabilizzazione connessione**

Se la connessione si interrompe frequentemente:

1. Verificare qualità cavo Ethernet (utilizzare Cat5e o Cat6)
2. Evitare cavi troppo lunghi (max 50m senza switch intermedio)
3. Verificare che non ci sia traffico di rete eccessivo sulla stessa subnet
4. Aumentare timeout sul robot (se configurabile)
5. Verificare alimentazione stabile del VisionController
6. Controllare log di Windows per errori di rete

Se il problema persiste, contattare supporto tecnico per analisi approfondita.
```

### Comandi non vengono riconosciuti

```{warning}
**Sintassi comandi errata**

Se FlexiVision risponde con "Invalid command":

1. Verificare la sintassi esatta del comando (case-sensitive, underscore, ecc.)
2. Assicurarsi di inviare il carattere terminatore CHR(13) dopo ogni comando
3. Non aggiungere spazi extra all'inizio o alla fine del comando
4. Verificare nel log messaggi il comando esattamente come ricevuto

Esempi corretti vs errati:
- ✅ `start_Locator` (con underscore, minuscolo)
- ❌ `Start_Locator` (maiuscola errata)
- ❌ `start Locator` (spazio invece di underscore)
- ❌ `startLocator` (manca underscore)

Consultare [Protocollo TCP/IP](../rif_tecnico_specifiche/04_Specifiche_FlexiVision.md#comandi-disponibili) per l'elenco completo e corretto dei comandi.
```

---
## Risoluzione problemi comuni (Camera Setup)

### Immagine sfocata o non nitida

```{warning}
**Problemi di messa a fuoco**

Se l'immagine appare sfocata:

1. Verificare che la camera sia alla distanza di lavoro corretta ([Calcolo Distanza Ottimale](../rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md))
2. Controllare che la lente sia avvitata completamente (contatto metal-metal)
3. Verificare che non ci siano sporcizia o impronte sulla lente
4. Assicurarsi che la camera sia montata perfettamente parallela al piatto FlexiBowl

La messa a fuoco fine verrà ottimizzata durante la calibrazione.
```

### Immagine troppo scura o troppo chiara

```{tip}
**Problemi di luminosità**

Se l'immagine acquisita è troppo scura o troppo chiara:

**Troppo scura**:
- Verificare che il backlight/toplight sia acceso (Config FlexiBowl)
- Aumentare l'intensità dell'illuminazione
- Aumentare il tempo di esposizione (parametro Exposure in modalità Expert)

**Troppo chiara (sovraesposta)**:
- Ridurre l'intensità dell'illuminazione
- Ridurre il tempo di esposizione
- Verificare che non ci sia luce ambientale eccessiva

Queste regolazioni verranno fatte in dettaglio durante la calibrazione e il training modello.
```

### Frame rate basso o acquisizione lenta

```{note}
**Performance acquisizione**

Se l'acquisizione immagini è lenta:
- Verificare che il cavo Ethernet sia Gigabit (Cat5e o Cat6)
- Controllare che lo switch di rete sia Gigabit Ethernet (non Fast Ethernet 100Mbps)
- Aumentare il Packet Size a 9000 se la rete supporta Jumbo Frames
- Ridurre il Latency Level se non ci sono problemi di schermate blu

Il frame rate massimo della camera è 14 fps (immagini al secondo), sufficiente per tutte le applicazioni di picking standard.
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
 ## Risoluzione problemi comuni (Nuova Ricetta)

### Ricetta non salvata correttamente
```{warning}
**Errore durante salvataggio**

Se il salvataggio della ricetta fallisce:
- Verificare di avere permessi di scrittura sulla cartella del software
- Controllare lo spazio disponibile su disco
- Assicurarsi che il nome non contenga caratteri non ammessi (`/ \ : * ? " < > |`)
- Verificare che non esista già una ricetta con lo stesso nome
```

---