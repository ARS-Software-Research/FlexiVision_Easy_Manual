# **Passo 6 : Robot Setup** 

Questa sezione descrive la procedura per configurare la comunicazione TCP/IP tra il sistema FlexiVision Easy e il robot industriale. Una comunicazione corretta è essenziale per permettere lo scambio di coordinate e comandi tra i due sistemi.

```{note}
**Prerequisiti**

Prima di procedere, assicurarsi che:
- Il robot sia acceso e operativo
- Il cavo Ethernet tra VisionController e robot sia collegato
- Il robot sia configurato per accettare connessioni TCP/IP (consultare manuale robot)
- Si conosca l'indirizzo IP del robot e la porta di comunicazione configurata
```

---

## Accesso alla configurazione Robot

```{list-table}

* - **1** 
  - Dalla pagina principale del software, cliccare su **SETUP**
* - **2**
  - Nella pagina SETUP, identificare e cliccare sull'icona **Robot Setup**
* - **3**
  - Si apre la pagina di configurazione della comunicazione robot
```

---

## Panoramica interfaccia Robot Setup

La pagina Robot Setup presenta diverse sezioni per configurare e testare la comunicazione:

```{list-table}
:header-rows: 1
:widths: 30 70

* - Sezione
  - Descrizione
* - **Port**
  - Porta TCP/IP con cui il robot comunica (configurata sul controller robot)
* - **Reconfigure Server**
  - Pulsante per riconfigurare il server di comunicazione con nuovi parametri
* - **Server Online**
  - Indicatore di stato del server FlexiVision (verde = server attivo e accessibile)
* - **Messaggi robot-flexivision**
  - Finestra di log che mostra i messaggi scambiati tra robot e FlexiVision (utilizzata per debugging)
```

---
## Procedura di configurazione

### Step 1: Inserimento porta di comunicazione

La porta TCP/IP è il parametro critico che deve corrispondere tra robot e FlexiVision:

```{list-table}
* - **1** 
  - Nel campo **Port**, inserire il numero della porta TCP/IP con cui il robot comunicherà
```
```{note}
Valore predefinito: **2000** (porta standard FlexiVision)
Il numero di porta deve essere:
   - Lo stesso configurato nel programma robot
   - Compreso tra 1024 e 65535 (porte utente)
   - Non in conflitto con altri servizi sulla rete
```

```{warning}
**Corrispondenza porta critica**

È **fondamentale** che il numero di porta sia identico su entrambi i lati:
- **FlexiVision**: Porta configurata in questa pagina
- **Robot**: Porta configurata nel programma robot (variabile di connessione TCP)

Se i numeri non corrispondono, la connessione fallirà sempre.

Esempio:
- ❌ ERRATO: FlexiVision porta 2000, Robot porta 2001 → Nessuna comunicazione
- ✅ CORRETTO: FlexiVision porta 2000, Robot porta 2000 → Comunicazione funzionante
```

```{tip}
**Porta standard per brand robot**

Alcuni brand robot utilizzano porte predefinite diverse:
- **ABB**: Tipicamente 2000-2010
- **KUKA**: Tipicamente 2000 o 59152
- **Fanuc**: Tipicamente 2000 o 60000-60010
- **Universal Robots**: Tipicamente 30000-30010
- **Yaskawa/Motoman**: Tipicamente 2000 o 10001
```

### Step 2: Riconfigurazione server

Dopo aver impostato la porta corretta, è necessario riavviare il server di comunicazione:

```{list-table}
* - **1** 
  - Cliccare sul pulsante **Reconfigure Server**
* - **2**
  - Attendere alcuni secondi per il completamento della riconfigurazione
```

```{note}

È necessario cliccare su **Reconfigure Server** ogni volta che:
- Si modifica il numero di porta
- Si desidera riavviare il server dopo un errore
- Si è modificata la configurazione di rete del VisionController
- Si vuole forzare la chiusura di connessioni esistenti

Il server si avvia automaticamente all'apertura del software FlexiVision, ma richiede riconfigurazione manuale dopo modifiche.
```

### Step 3: Verifica stato server

Dopo la riconfigurazione, verificare che il server sia attivo:

```{list-table}

* - **1**
  - Osservare l'indicatore **Server Online**:
   - **Verde**: Server attivo e in ascolto (pronto per connessioni)
   - **Rosso**: Server non attivo (problema di configurazione)
   - **Giallo**: Server in fase di avvio o riconfigurazione
```
```{note}
Se l'indicatore è verde, il server FlexiVision è pronto a ricevere connessioni dal robot

Se l'indicatore è rosso, verificare:
   - Che la porta non sia già in uso da un altro programma
   - I log di sistema per messaggi di errore
```
### Step 4: Salvataggio e completamento

```{note}
**Completamento configurazione**

1. Verificare che la connessione robot → FlexiVision sia stabile
2. Testare almeno 2-3 comandi diversi (get_Recipe, state_Locator, test_Locator)
3. I parametri di comunicazione sono automaticamente salvati
4. Tornare alla pagina **SETUP** principale
```

---
## Problemi comuni e soluzioni

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

## Passi successivi

Una volta completato il Robot Setup, procedere con:

**[Passo 7: Camera Setup](13d_Camera_Setup.md)** - Configurazione e test acquisizione camera
