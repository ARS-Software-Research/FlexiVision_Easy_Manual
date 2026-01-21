# Setup Iniziale
(troubleshooting_FB_setup)=
## Troubleshooting per la sezione Passo 4: FlexiBowl Setup 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **FlexiBowl non risponde ai comandi software**
  - • Indirizzo IP non configurato o errato
    
    • FlexiBowl non connesso in rete
    
    • Firewall blocca comunicazione
    
    • FlexiBowl non acceso
  - • Verificare e configurare correttamente IP in FlexiBowl Setup
    
    • Testare connessione con ping da VisionController
    
    • Disabilitare firewall temporaneamente per test
    
    • Verificare LED READY acceso su FlexiBowl
* - **Impossibile salvare configurazione FlexiBowl**
  - • Permessi insufficienti su VisionController
    
    • Disco pieno
    
    • Ricetta non caricata
  - • Verificare permessi utente Windows
    
    • Liberare spazio su disco
    
    • Caricare o creare una ricetta prima di salvare configurazione
* - **Parametri FlexiBowl non si applicano**
  - • Pulsante "Synchronize Parameters" non premuto
    
    • Connessione FlexiBowl persa
    
    • Controller FlexiBowl in errore
  - • Cliccare sempre "Synchronize Parameters" dopo modifiche
    
    • Verificare stabilità connessione Ethernet
    
    • Riavviare FlexiBowl e VisionController
* - **Wizard FlexiBowl calcola parametri errati**
  - • Caratterizzazione componente non corretta (geometria/comportamento)
    
    • Modello FlexiBowl selezionato errato
    
    • Senso rotazione impostato male
  - • Rivedere selezione geometria (FLAT/CYLINDRICAL/COMPLEX)
    
    • Verificare taglia FlexiBowl installato vs selezionato
    
    • Verificare senso rotazione fisico e confrontare con impostazione
```
(troubleshooting_Hopper_setup)=
## Troubleshooting per la sezione Passo 5: Hopper Setup 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Tramoggia non si attiva mai automaticamente**
  - • Hopper non abilitato in software
    
    • Area di controllo non definita
    
    • Soglie non calibrate
    
    • Tramoggia non collegata elettricamente/pneumaticamente
  - • Abilitare checkbox "Enable Hopper X"
    
    • Definire area di controllo in "Define Area Check"
    
    • Eseguire calibrazione soglie con CAPTURE vuoto/pieno
    
    • Verificare collegamenti elettrici ed aria compressa
* - **Tramoggia si attiva continuamente**
  - • Soglie calibrate in modo errato
    
    • Area di controllo troppo grande
    
    • Tempo vibrazione insufficiente (scarica troppo pochi pezzi)
    
    • Parameter "Steps" errato
  - • Ripetere calibrazione rimuovendo TUTTI i pezzi per CAPTURE vuoto
    
    • Ridurre area di controllo per monitorare solo zona rilevante
    
    • Aumentare parametro "Time" (es: da 500ms a 700ms)
    
    • Ricalcolare "Steps" contando cicli effettivi
* - **Test hopper sempre rosso (non si attiva)**
  - • Troppi componenti nell'area durante calibrazione
    
    • Illuminazione cambiata tra calibrazione e test
    
    • Riflessi/ombre nell'area di controllo
  - • Ripetere calibrazione con numero minimo corretto di pezzi
    
    • Eseguire calibrazione e test con illuminazione stabile
    
    • Riposizionare area escludendo zone con riflessi
* - **Test hopper sempre verde (si attiva sempre)**
  - • Area di controllo include zone non pertinenti
    
    • Calibrazione vuoto eseguita con pezzi presenti
    
    • Expression Builder non calcolato correttamente
  - • Ridefinire area di controllo più stretta
    
    • Ripetere CAPTURE vuoto assicurandosi area completamente pulita
    
    • Cliccare nuovamente su AUTO per ricalcolare Mean e Std Dev
* - **Flusso componenti non uniforme**
  - • Livello vasca tramoggia variabile
    
    • Tempo vibrazione non calibrato
    
    • Superficie vibrante sporca/ostruita
  - • Mantenere carico costante nella vasca tramoggia
    
    • Ottimizzare "Time" con incrementi ±100ms
    
    • Pulire superficie vibrante della tramoggia
```
(troubleshooting_Robot_setup)=
## Troubleshooting per la sezione Passo 6: Robot Setup

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Robot non riceve coordinate da FlexiVision**
  - • Indirizzo IP robot errato
    
    • Porta TCP/IP non configurata
    
    • Firewall robot blocca comunicazione
    
    • Protocollo comunicazione non compatibile
  - • Verificare e configurare IP robot corretto in Robot Setup
    
    • Configurare porta TCP/IP (tipicamente 5000 o secondo robot)
    
    • Disabilitare firewall robot per test
    
    • Selezionare protocollo compatibile con robot in [Protocol Setup](QUICKSTART/xx_Protocol_Setup.md)
* - **Timeout comunicazione robot**
  - • Valore timeout troppo basso
    
    • Robot lento a rispondere
    
    • Connessione Ethernet instabile
  - • Aumentare valore timeout in Robot Setup
    
    • Verificare prestazioni robot e ottimizzare programmi
    
    • Stabilizzare connessione Ethernet (vedere sezione Cablaggio)
* - **Robot va in posizioni sbagliate**
  - • Calibrazione robot non eseguita
    
    • Frame/Tool robot non corretto
    
    • Offset gripper errato
    
    • Coordinate salvate sbagliate durante setup modello
  - • Eseguire calibrazione robot completa
    
    • Verificare Frame e Tool selezionati sul robot
    
    • Ripetere calibrazione Robot Pick con coordinate corrette
    
    • Rifare training modello salvando coordinate precise
* - **Impossibile connettersi al robot**
  - • Robot spento o in modalità manuale
    
    • Cavo Ethernet non collegato
    
    • Robot e VisionController su subnet diverse
    
    • Server socket robot non avviato
  - • Accendere robot e portare in automatico
    
    • Verificare connessione fisica Ethernet robot-VisionController
    
    • Configurare robot e VisionController stessa rete
    
    • Avviare programma server socket sul robot
```
(troubleshooting_cam_setup)=
## Troubleshooting per la sezione Passo 7: Camera Setup 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Immagine troppo scura**
  - • Esposizione camera troppo bassa
    
    • Toplight spento o guasto
    
    • Toplight con potenza insufficiente
    
    • Lente con tappo protettivo
  - • Aumentare esposizione in Camera Setup
    
    • Verificare alimentazione toplight
    
    • Verificare corrente toplight secondo specifiche
    
    • Rimuovere tappo protettivo lente
* - **Immagine troppo chiara (sovraesposta)**
  - • Esposizione camera troppo alta
    
    • Toplight troppo potente
    
    • Riflessioni da superficie FlexiBowl
  - • Diminuire esposizione in Camera Setup
    
    • Ridurre potenza toplight se regolabile
    
    • Sostituire superficie grip con una meno riflettente
* - **Immagine sfocata**
  - • Lente non a fuoco (distanza di lavoro errata)
    
    • Lente non avvitata completamente
    
    • Lente sporca
    
    • Camera in movimento/vibrazioni
  - • Correggere distanza di lavoro a 950-1000mm
    
    • Avvitare lente fino a contatto metal-metal
    
    • Pulire lente con panno in microfibra
    
    • Fissare meglio camera e ridurre vibrazioni
* - **Immagine con artefatti o linee**
  - • Interferenze elettromagnetiche
    
    • Cavo camera danneggiato
    
    • Sincronizzazione camera non corretta
    
    • Sensore camera danneggiato
  - • Allontanare cavo camera da fonti EMI, usare cavo schermato
    
    • Sostituire cavo Ethernet camera
    
    • Verificare impostazioni sincronizzazione camera
    
    • Sostituire camera
* - **Camera non acquisisce durante ciclo**
  - • Trigger non configurato
    
    • Componenti in movimento durante scatto
    
    • Pause insufficiente dopo movimento disco
  - • Configurare trigger acquisizione correttamente
    
    • Inserire pause di stabilizzazione (es: 200ms)
    
    • Ridurre velocità/accelerazione disco
```