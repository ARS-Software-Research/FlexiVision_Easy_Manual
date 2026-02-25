# **Configurazione Iniziale del Sistema**

Questa sezione guida l'utente attraverso la configurazione completa dei componenti hardware e software del sistema FlexiVision Easy. È fondamentale seguire i passaggi nell'ordine indicato per garantire il corretto funzionamento del sistema.

```{note}
**Prerequisiti**

Prima di iniziare la configurazione software, assicurarsi che:
- L'installazione meccanica di tutti i componenti sia completata ([Installazione Meccanica](09_Installazione_Meccanica.md))
- Tutti i cavi siano collegati correttamente ([Cablaggio e Connessioni](10_Cablaggio_Connessioni.md))
- Il software FlexiVision Easy sia stato installato sul VisionController ([Installazione Software](11_Installazione_Software.md))
- Si disponga della licenza software fornita da ARS Automation
```

---

## Panoramica del processo di setup

Il processo di configurazione iniziale è composto da sette passaggi principali:

1. **Login** - Accesso al software con credenziali utente
2. **Attivazione licenza** - Inserimento della chiave di licenza
3. **Creazione ricetta base** - Configurazione del profilo applicativo
4. **FlexiBowl Setup** - Connessione e configurazione dell'alimentatore vibrante
5. **Hopper Setup** (opzionale) - Configurazione tramoggia esterna
6. **Robot Setup** - Configurazione comunicazione con il robot
7. **Camera Setup** - Configurazione e test della telecamera

![Flowchart setup](img/flowchartSetup.jpg)

```{warning}
**Ordine dei passaggi**

L'ordine dei setup è importante! Non saltare passaggi o modificare la sequenza, poiché alcune configurazioni dipendono da quelle precedenti.
```

---

## Operazioni preliminari

### Passo 1: Login al sistema

All'avvio del software FlexiVision Easy, viene presentata la schermata di login.
```{list-table} 
   :widths: 10 90
   :header-rows: 0

   * - **1**
     - **Selezionare l'utente** dal menu a tendina.
   * - **2**
     - **Inserire la password** fornita da ARS Automation.
       *(Nota: il campo è case-sensitive)*.
   * - **3**
     - Cliccare sul pulsante **LOGIN** per accedere all'interfaccia.
```

```{tip}
**Gestione utenti**

FlexiVision Easy supporta profili utente multipli con diversi livelli di permessi:
- **Administrator**: accesso completo a tutte le funzionalità
- **Operator**: accesso alle funzioni operative (esecuzione ricette, monitoraggio)
- **Viewer**: solo visualizzazione (nessuna modifica consentita)
```

---

### Passo 2: Attivazione licenza software

Dopo il primo login, è necessario attivare la licenza software.

```{list-table}
:header-rows: 0
:widths: 10 90

* - **1.**
  - Inserire la chiavetta fornita nel kit

* - **2.**
  - Accedere alla sezione SETUP e cliccare su **Software License**
    ```{dropdown} Pagina Software License 
       ![Pagina Software License](../SETUP/img/pagina_softwareL.png)
    ```

* - **3.**
  - Inserire la chiave di licenza fornita da ARS Automation nel campo dedicato.
    La chiave è composta da caratteri alfanumerici (es: ``XXXX-XXXX-XXXX-XXXX``).
    Copiare e incollare la chiave per evitare errori di digitazione.

* - **4.**
  - Cliccare su **Activate**

* - **5.**
  - Attendere che l'indicatore di stato diventi verde
```

```{warning}
**Chiave di licenza non valida**

Se la licenza non viene accettata:
- Verificare di aver inserito la chiave corretta (controllare maiuscole/minuscole)
- Assicurarsi che il VisionController sia connesso a Internet (alcune licenze richiedono validazione online)
- Verificare la data di scadenza della licenza
- Contattare il supporto ARS se il problema persiste
```

---

### Passo 3: Creazione ricetta base

Prima di configurare i componenti hardware, è necessario creare una ricetta di base che definisca i parametri dell'applicazione.

```{list-table}
:header-rows: 0
:widths: 10 90

* - **1.**
  - Accedere alla sezione **RECIPES** dal pulsante in alto

* - **2.**
  - Cliccare su **New Recipe**

* - **3.**
  - Inserire il nome della ricetta.
    Utilizzare un nome descrittivo (es: "Ricetta_Base").
    Evitare caratteri speciali o spazi (usare underscore ``_`` al posto degli spazi).

* - **4.**
  - Selezionare il **tipo di applicazione**: **Standard** per applicazioni ... oppure **Mix** per applicazioni ...

* - **5.**
  - Selezionare il **FlexiBowl** utilizzato

* - **6.**
  - Cliccare su **Save** per salvare la ricetta
```

```{tip}
**Organizzazione ricette**

FlexiVision Easy permette di creare ricette multiple per diversi tipi di pezzi o configurazioni. Convenzioni consigliate:

- Utilizzare nomi che identificano chiaramente il pezzo (es: "Vite_M6_Zincata")

Per maggiori dettagli sulla gestione ricette, consultare la sezione [Creare una nuova ricetta](Nuovo_Modello/17_NuovaRicetta.md).
```

---

## Configurazione componenti hardware

Una volta completate le operazioni preliminari, procedere con la configurazione dei componenti hardware nell'ordine seguente.

Tutti i setup hardware sono accessibili dalla pagina centrale **SETUP** del software.


```{list-table} 
* - 1. 
  - Dal menu principale, cliccare su **SETUP**
* - 2. 
  - Vengono visualizzate le icone dei diversi componenti da configurare
* - 3. 
  - Cliccare sull'icona del componente desiderato per accedere alla sua configurazione specifica
```

### Sequenza setup consigliata

```{list-table}
:header-rows: 1
:widths: 15 35 50

* - Passo
  - Componente
  - Descrizione
* - **4**
  - [FlexiBowl Setup](SETUP/13a_FB_Setup.md)
  - Connessione e test comunicazione con l'alimentatore vibrante
* - **5**
  - [Hopper Setup](SETUP/13b_Hopper_Setup.md)
  - (Opzionale) Configurazione tramoggia esterna se presente
* - **6**
  - [Robot Setup](SETUP/13c_Robot_Setup.md)
  - Configurazione porta TCP/IP e test comunicazione con il robot
* - **7**
  - [Camera Setup](SETUP/13d_Camera_Setup.md)
  - Configurazione acquisizione immagini e test camera
```

```{warning}
**Importanza della sequenza**

Seguire l'ordine indicato è importante perché:
- La camera ha bisogno che il FlexiBowl sia configurato per testare l'illuminazione
- Il robot setup richiede che la ricetta base sia già creata
- Alcuni parametri dipendono dalle configurazioni precedenti
```
---

## Risoluzione problemi comuni

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

Per dettagli sulla configurazione di rete, vedere [Cablaggio e Connessioni](10_Cablaggio_Connessioni.md).
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
---

```{toctree}
:hidden:
13a_FB_Setup.md
13b_Hopper_Setup.md
13c_Robot_Setup.md
13d_Camera_Setup.md
```