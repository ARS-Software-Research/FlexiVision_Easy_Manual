(fbsetup)=
# **Passo 4: FlexiBowl Setup**

Questa sezione descrive la procedura per connettere e configurare il FlexiBowl con il sistema FlexiVision One. 

```{note}
**Prerequisiti**

Assicurarsi che:
- L'installazione meccanica di tutti i componenti sia completata ([Installazione Meccanica](Installazione_Meccanica))
- Tutti i cavi siano collegati correttamente ([Cablaggio e Connessioni](cablaggio)) 
```

---

## Accesso alla configurazione FlexiBowl
```{list-table}
* - 1. 
  - Dalla pagina principale del software, cliccare su <img src="../SETUP/img/tasto_setup1.png" class="inline-icon">
* - 2. 
  - Nella pagina SETUP, identificare e cliccare sull'icona **FlexiBowl Setup**
    ```{dropdown} Pagina Setup 
       ![Pagina Setup](../SETUP/img/pagina_setup1.png)
    ```
* - 3. 
  - Si apre la schermata di configurazione dei FlexiBowl
```
![Pagina FlexiBowl Setup](../SETUP/img/pagina_FBsetup.png)
---

## Procedura di connessione

### **Step 1: Configurazione indirizzo di rete**

```{list-table}
* - 1. 
  - Verificare che l'indirizzo sia sulla stessa subnet del VisionController
  
* - 2. 
  - Nel campo **FlexiBowl IP**, inserire l'indirizzo IP del FlexiBowl
      - Formato: `192.168.1.XXX` (o secondo la configurazione della vostra rete)
```
:::{tip}
Per comodità e coerenza, partire dal primo FlexiBowl disponibile 
:::
:::{note}
Il FlexiBowl viene spedito con indirizzo IP di default `192.168.1.10`
:::

### **Step 2: Test di connessione**

```{list-table}
:widths: 5 95

* - **1.**
  - Dopo aver inserito l'IP, cliccare sul pulsante **Connection Test**

* - **2.**
  - Il sistema esegue un test di comunicazione (ping) verso il FlexiBowl

* - **3.**
  - Osservare l'indicatore di **Status**:
    - 🟢 **Verde**: Connessione stabilita correttamente
    - 🔴 **Rosso**: Connessione fallita (verificare indirizzo IP e cablaggio)
```

```{warning}
**Connessione fallita**

Se l'indicatore rimane rosso o appare un messaggio di errore:

0. Verificare di aver acceso il FlexiBowl
1. Verificare che l'indirizzo IP inserito sia corretto
2. Controllare fisicamente il cavo Ethernet (deve essere inserito completamente)
3. Se presente,verificare che lo switch/router di rete sia acceso
4. Assicurarsi che FlexiBowl e VisionController siano sulla stessa subnet
5. Provare a pingare il FlexiBowl da terminale Windows:
   - Aprire Prompt dei comandi
   - Digitare: `ping 192.168.1.XXX` (sostituire con IP effettivo)
   - Se il ping fallisce, si tratta di un problema di rete

Se il problema persiste, consultare [Troubleshooting](troubleshooting).
```

---

## Configurazione parametri FlexiBowl

Una volta stabilita la connessione, procedere con la configurazione dei parametri operativi.

### **Step 3: Accesso configurazione**

```{list-table}
* - 1. 
  - Cliccare sul pulsante <img src="../SETUP/img/FB_config1.png" class="inline-icon icon-xl" >
* - 2. 
  - Si apre una finestra con i parametri configurabili del FlexiBowl
```

### **Step 4: Abilitazione illuminatore - Backlight**

```{list-table}

* - 3. 
  - Accendere il backlight spuntando la casella "Light ON"
```

### **Step 5: Sincronizzazione parametri**

```{list-table}

* - 1.
  - Cliccare su **Synchronize Parameters**
* - 2.
  - Tornare alla pagina SETUP principale per procedere con il setup successivo 
```

```{warning}
**Non saltare la sincronizzazione**

È fondamentale cliccare su **Synchronize Parameters** dopo ogni modifica. Senza questo passaggio:
- Le modifiche non vengono applicate al FlexiBowl 
- Il sistema potrebbe comportarsi in modo incoerente
- Le impostazioni non vengono salvate 
```

```
---

## Passi successivi

Una volta completato il FlexiBowl Setup, procedere con:

- [Passo 5: Hopper Setup](13b_Hopper_Setup.md)
- [Passo 6: Robot Setup](13c_Robot_Setup.md)

