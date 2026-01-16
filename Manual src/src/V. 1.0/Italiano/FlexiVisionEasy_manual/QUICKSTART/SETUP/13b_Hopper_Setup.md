# **Passo 5: Hopper Setup**

Questa sezione descrive la procedura per configurare la tramoggia esterna (Hopper). L'Hopper è il componente che alimenta automaticamente pezzi sul FlexiBowl quando il livello scende sotto una soglia minima.

```{note}
**Prerequisiti**

Prima di procedere, assicurarsi che:
- L'Hopper sia stata installata meccanicamente sopra il FlexiBowl
- I collegamenti elettrici siano stati completati (segnali di controllo e alimentazione)
- Il FlexiBowl sia già configurato e funzionante (Passo 4)
```
---

## Accesso alla configurazione Hopper

```{list-table}
* - **1** 
  - Dalla pagina principale del software, cliccare su **SETUP**
* - **2**
  - Nella pagina SETUP, identificare e cliccare sull'icona **Hopper Setup**
* - **3** 
  - Si apre la pagina di configurazione dell'Hopper
```

---

## Panoramica interfaccia Hopper Setup

La pagina Hopper Setup presenta diverse sezioni per la configurazione dei parametri operativi:

```{list-table}
:header-rows: 1
:widths: 30 70

* - Sezione
  - Descrizione
* - **Enable Hopper**
  - Interruttore per abilitare/disabilitare l'utilizzo dell'Hopper nel sistema
* - **Steps**
  - Numero di sequenze necessarie con cui il FlexiBowl arriva sotto l'area di scarico della tramoggia
* - **Time**
  - Durata dell'attivazione del segnale in millisecondi
* - **Signal**
  - Numero del segnale digitale utilizzato per controllare l'Hopper
* - **Config Hopper**
  - Pulsante per configurare la tramoggia (da utilizzare in seguito)
```
---

## Procedura di configurazione

### Step 1: Abilitazione Hopper

Il primo passo è abilitare l'Hopper nel sistema:

```{list-table}
* - Spuntare la checkbox **Enable Hopper**
```
immagini schermate

```{important}

Abilitare l'Hopper solo se:
- Il dispositivo è fisicamente presente e installato
- I collegamenti elettrici sono stati verificati
- Si desidera che il sistema richiami automaticamente pezzi quando necessario
```

### Step 2: Configurazione Signal (segnale)
Impostazione numero segnale di controllo

```{list-table}
* - Nel campo **Signal**, inserire il numero del segnale digitale (DO - Digital Output) utilizzato per controllare l'Hopper
```
immagini schermate e valori tipici??

```{warning}
**Verifica cablaggio**

È fondamentale inserire il numero di segnale corretto corrispondente al cablaggio fisico:
- Un numero errato attiverà il segnale sbagliato (potenzialmente pericoloso)
- Consultare lo schema elettrico realizzato durante l'installazione
- In caso di dubbio, contattare chi ha effettuato il cablaggio

Verificare SEMPRE con un test controllato prima dell'uso in produzione.
```

### Step 3: Salvataggio e completamento

```{list-table}
* - Tornare alla pagina **SETUP** principale per procedere con il setup successivo
```

```{tip}
**Ottimizzazione futura**

I parametri impostati in questa fase sono sufficienti per il funzionamento base del sistema.

Per ottimizzazioni avanzate dell'Hopper (soglie di attivazione, strategie di riempimento, coordinamento con produzione), consultare la sezione [Config Hopper](23_Config_Hopper.md) dopo aver completato la calibrazione e creato i primi modelli pezzo.
```

---

```{note}
**Attivazione automatica durante picking**

Una volta configurato, l'Hopper viene richiamato automaticamente dal sistema FlexiVision quando:

1. Il software rileva che non ci sono abbastanza pezzi prelevabili sul FlexiBowl
2. Il numero di tentativi di localizzazione falliti supera una soglia
3. Il FlexiBowl ha completato un ciclo completo senza trovare pezzi validi

Quando queste condizioni si verificano, il sistema:
- Invia automaticamente il comando di attivazione all'Hopper
- Attende che i pezzi si distribuiscano sul FlexiBowl
- Riprende la ricerca e il picking

Questo processo è completamente automatico e non richiede intervento dell'operatore.
```

```{tip}
**Coordinamento con FlexiBowl**

Durante il funzionamento normale, il sistema coordina FlexiBowl e Hopper:

1. Robot richiede un pezzo
2. FlexiVision cerca pezzi sul FlexiBowl
3. Se trova un pezzo → comunica coordinate al robot
4. Se NON trova pezzi → attiva FlexiBowl per distribuire i pezzi presenti
5. Dopo N tentativi falliti → attiva Hopper per aggiungere pezzi
6. Attende distribuzione → riprende ricerca

I parametri di questa logica (numero tentativi, temporizzazioni) possono essere ottimizzati nella sezione [Config Hopper](23_Config_Hopper.md) specifica per ricetta.
```

---


## Problemi comuni e soluzioni

### Hopper non si attiva

```{warning}
**Diagnosi mancata attivazione**

Se l'Hopper non si attiva quando si preme Config Hopper:

1. Verificare che in **Enable Hopper** sia presente la spunta
2. Controllare il cablaggio elettrico del segnale digitale
3. Verificare che il numero **Signal** corrisponda al DO fisicamente connesso
4. Controllare l'alimentazione dell'Hopper 
5. Testare il segnale digitale con un multimetro (presenza tensione quando attivato)
6. Consultare il manuale dell'Hopper per verifiche specifiche del dispositivo
```

---

## Passi successivi

Una volta completato l'Hopper Setup (o saltato se non presente), procedere con:

**[Passo 6: Robot Setup](13c_Robot_Setup.md)** - Configurazione comunicazione con il robot

