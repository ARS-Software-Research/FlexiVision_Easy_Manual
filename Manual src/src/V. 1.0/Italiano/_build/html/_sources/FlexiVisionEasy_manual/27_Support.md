# **Appendici e Contatti** 

## Contatti e Supporto ars automation.

Per assistenza tecnica, informazioni commerciali o segnalazioni relative a questo manuale:

**ARS S.r.l. - Ars Automation**  
📧 Email: [info@arsautomation.com](mailto:info@arsautomation.com)  
🌐 Web: [www.arsautomation.com](https://www.arsautomation.com)  
📞 Telefono: consultare il sito web per i contatti aggiornati

Per feedback specifici su questo manuale: [contattaci qui](https://www.flexibowl.it/contatti)

## Glossario dei Termini Tecnici 

```{list-table}
:header-rows: 1
:widths: 25 75

* - Termine
  - Definizione
* - **Accept Threshold**
  - Soglia di accettazione nell'algoritmo di pattern matching. Determina il livello minimo di similitudine (score 0.0-1.0) necessario affinché un oggetto rilevato venga considerato valido. Valori tipici: 0.70-0.90.
* - **Accel (Acceleration)**
  - Parametro che definisce l'accelerazione del disco FlexiBowl durante la fase di movimento. Influenza la dolcezza dell'avvio e dell'arresto della rotazione.
* - **Air-blow**
  - Modulo pneumatico opzionale che utilizza getti d'aria compressa per separare i componenti sul disco prima o dopo l'operazione di flip. Richiede alimentazione pneumatica a 5-6 bar.
* - **Artifact (Artefatto)**
  - Difetto visibile nell'immagine acquisita dalla camera, causato da interferenze elettromagnetiche, problemi di cablaggio o malfunzionamenti del sensore.
* - **Calibrazione Camera**
  - Processo che permette di correlare i pixel dell'immagine acquisita con le coordinate reali nello spazio. Utilizza un target di calibrazione con pattern noto per calcolare i parametri intrinseci ed estrinseci della camera.
* - **Camera POE**
  - Camera industriale che riceve sia i dati che l'alimentazione elettrica attraverso un unico cavo Ethernet, secondo gli standard IEEE 802.3af (15.4W) o 802.3at (30W).
* - **CAPTURE**
  - Comando utilizzato durante la configurazione della tramoggia per acquisire immagini di riferimento del disco vuoto e pieno, necessarie per il calcolo automatico delle soglie di controllo.
* - **Cat5e / Cat6**
  - Categorie di cavi Ethernet. Cat5e supporta fino a 1 Gbps, Cat6 fino a 10 Gbps. Lunghezza massima consigliata: 100m per evitare perdita di segnale.
* - **COMPLEX**
  - Categoria di componenti con geometria irregolare o asimmetrica che non rientra nelle categorie FLAT o CYLINDRICAL. Richiede parametri FlexiBowl specifici.
* - **CW / CCW**
  - Clockwise (orario) / Counter-Clockwise (antiorario). Senso di rotazione del disco FlexiBowl da configurare nel Wizard.
* - **CYLINDRICAL**
  - Categoria di componenti con forma prevalentemente cilindrica o tubolare (es: perni, boccole, viti).
* - **DIN Rail**
  - Sistema di montaggio standardizzato (DIN EN 60715) a profilo 35mm utilizzato per fissare il VisionController all'interno dei quadri elettrici.
* - **Distanza di Lavoro**
  - Distanza ottimale tra la lente della camera e la superficie del disco FlexiBowl. Tipicamente 950-1000mm per le configurazioni standard.
* - **Distorsione Ottica**
  - Deformazione geometrica dell'immagine causata dalle caratteristiche ottiche della lente. Viene compensata durante la calibrazione camera.
* - **EMI**
  - Electromagnetic Interference. Interferenze elettromagnetiche che possono disturbare camera, comunicazioni Ethernet e sensori. Richiedono cavi schermati (STP).
* - **Esposizione**
  - Tempo durante il quale il sensore della camera raccoglie luce per formare l'immagine. Misurato in microsecondi (μs) o millisecondi (ms).
* - **Feature Threshold**
  - Soglia utilizzata durante il training del modello per determinare quali caratteristiche (linee, bordi) del componente devono essere estratte. Valori tipici: 0.3-0.8.
* - **Flip**
  - Operazione pneumatica che genera un impulso d'aria sotto il disco FlexiBowl per riposizionare i componenti. Configurabile con parametri Count e Delay.
* - **Flip Count**
  - Numero di impulsi pneumatici consecutivi eseguiti durante un'operazione di flip.
* - **Flip Delay**
  - Intervallo di tempo (in millisecondi) tra impulsi pneumatici consecutivi durante l'operazione di flip.
* - **FLAT**
  - Categoria di componenti con forma piatta o a disco (es: rondelle, guarnizioni, dischetti).
* - **FlexiBowl**
  - Sistema di alimentazione flessibile per componenti che utilizza un disco rotante vibrante per posizionare e orientare i pezzi in modo casuale per il prelievo robotico.
* - **FlexiBowl Wizard**
  - Procedura guidata che calcola automaticamente i parametri ottimali di funzionamento del FlexiBowl in base alle caratteristiche geometriche e comportamentali dei componenti.
* - **Frame (Robot)**
  - Sistema di coordinate di riferimento utilizzato dal robot per definire la posizione degli oggetti nello spazio di lavoro.
* - **Frenafiletti**
  - Prodotto chimico applicato sulle filettature delle viti per prevenire l'allentamento dovuto a vibrazioni. Disponibile in diverse resistenze (basso, medio, alto).
* - **Fusibile**
  - Dispositivo di protezione elettrica che interrompe il circuito in caso di sovracorrente. Il FlexiBowl ha fusibili interni accessibili solo al supporto tecnico.
* - **Grab Train Image**
  - Comando che acquisisce un'immagine dalla camera da utilizzare per il training di un nuovo modello di riconoscimento.
* - **Gripper**
  - Pinza robotica utilizzata per afferrare e manipolare i componenti. Può essere pneumatica, elettrica o a vuoto.
* - **Gripper Offset**
  - Vettore di correzione (ΔX, ΔY, ΔRZ) che compensa la differenza tra il centro del sistema di visione e il punto di presa effettivo del gripper robot.
* - **Hopper (Tramoggia)**
  - Sistema di caricamento automatico che alimenta i componenti sul disco FlexiBowl tramite vibrazione. Può essere configurato con controllo visivo.
* - **Hotspot**
  - Zona di riflessione diretta della luce nell'immagine, che appare come un'area molto luminosa e può compromettere il riconoscimento.
* - **IP Rating**
  - International Protection Rating. Classifica il grado di protezione contro solidi e liquidi. Il VisionController richiede installazione in quadro minimo IP40, consigliato IP54.
* - **Istogramma**
  - Strumento di analisi che verifica la presenza o assenza di oggetti in un'area specifica dell'immagine basandosi sulla distribuzione dei livelli di grigio. Utilizzato per controllo pinza e area libera.
* - **LED READY**
  - Indicatore luminoso sul pannello FlexiBowl che segnala il corretto funzionamento del sistema. Deve essere acceso (verde) durante il normale funzionamento.
* - **Lente**
  - Componente ottico della camera che focalizza la luce sul sensore. Caratterizzata da focale (es: 16mm, 25mm) e deve essere avvitata completamente (contatto metal-metal).
* - **M3 / M4**
  - Diametri metrici standard delle viti. M3 (3mm) per camera con coppia 0.5 Nm, M4 (4mm) per VisionController con coppia 1.2 Nm.
* - **Mean (Media)**
  - Valore medio dei livelli di grigio calcolato su un'area dell'immagine. Utilizzato negli istogrammi per determinare le soglie di rilevamento.
* - **Model (Modello)**
  - Template di riferimento creato durante il training che contiene le caratteristiche geometriche del componente da riconoscere. Ogni ricetta può contenere fino a 8 modelli.
* - **Nm (Newton metro)**
  - Unità di misura della coppia di serraggio. Critica per evitare danni: 0.5 Nm per camera, 1.2 Nm per VisionController.
* - **Origine Modello**
  - Punto di riferimento sul componente utilizzato come centro del sistema di coordinate per il calcolo delle posizioni. Solitamente corrisponde al punto di presa del gripper.
* - **Ortogonalità**
  - Condizione in cui la camera è perfettamente perpendicolare (90°) alla superficie del disco FlexiBowl. Tolleranza: ±1°. Verificabile con livella di precisione.
* - **Pattern Matching**
  - Algoritmo di visione artificiale che cerca e localizza oggetti nell'immagine confrontandoli con un modello di riferimento pre-registrato.
* - **POE (Power over Ethernet)**
  - Tecnologia che permette di trasmettere alimentazione elettrica e dati attraverso un unico cavo Ethernet. Standard: IEEE 802.3af (15.4W), IEEE 802.3at (30W).
* - **Protocol (Protocollo)**
  - Formato standardizzato di comunicazione tra VisionController e robot. Definisce la struttura dei messaggi, l'ordine delle coordinate e le unità di misura.
* - **Recipe (Ricetta)**
  - File di configurazione che contiene tutti i parametri di setup: modelli, soglie, calibrazioni, configurazioni FlexiBowl e robot. Salvata come file XML.
* - **Region Search**
  - Area rettangolare nell'immagine dove l'algoritmo di pattern matching cerca i componenti. Limita la zona di ricerca per migliorare velocità e precisione.
* - **Results Panel**
  - Pannello software che mostra l'elenco di tutti i componenti rilevati con le loro coordinate (X, Y, Rotation) e score di confidenza.
* - **RGB / Grayscale**
  - RGB: immagine a colori con 3 canali (rosso, verde, blu). Grayscale: immagine in scala di grigi con 1 canale. FlexiVision utilizza tipicamente grayscale per maggiore velocità.
* - **RJ45**
  - Connettore standard utilizzato per i cavi Ethernet. Deve essere crimpato correttamente per garantire connessioni stabili.
* - **ROI (Region of Interest)**
  - Regione di Interesse. Area rettangolare selezionata nell'immagine che delimita il componente durante il training del modello.
* - **RZ / Rotation Z**
  - Angolo di rotazione attorno all'asse verticale (Z). Utilizzato per comunicare l'orientamento del componente al robot. Misurato in gradi (0-360°).
* - **Score**
  - Valore numerico (0.0-1.0) che indica il grado di similitudine tra il modello e l'oggetto rilevato. Score alto = maggiore confidenza nel riconoscimento.
* - **Simulatori Ingombro Pinza**
  - Oggetti fisici posizionati attorno al componente durante il training per rappresentare le dimensioni della pinza robot ed evitare di includerla nel modello.
* - **Speed**
  - Parametro che definisce la velocità di rotazione del disco FlexiBowl durante la fase di movimento. Influenza il tempo ciclo complessivo.
* - **Steps**
  - Numero di cicli di vibrazione della tramoggia necessari affinché i primi componenti raggiungano l'area di prelievo. Parametro critico per la sincronizzazione.
* - **Std Dev (Standard Deviation)**
  - Deviazione standard. Misura la variabilità dei livelli di grigio in un'area. Utilizzata negli istogrammi per calcolare le soglie di rilevamento.
* - **STP (Shielded Twisted Pair)**
  - Cavo Ethernet schermato che protegge il segnale dalle interferenze elettromagnetiche. Raccomandato in ambienti industriali.
* - **Subnet**
  - Sotto-rete. Gruppo di dispositivi con indirizzi IP che condividono gli stessi primi tre numeri (es: 192.168.1.x). FlexiBowl e VisionController devono essere sulla stessa subnet.
* - **Switch AC**
  - Interruttore di alimentazione principale. Posizione "I" = ON, posizione "O" = OFF. Presente sul pannello di controllo FlexiBowl.
* - **Synchronize Parameters**
  - Comando che trasferisce i parametri configurati dal VisionController al FlexiBowl. Deve essere premuto dopo ogni modifica per applicare le impostazioni.
* - **Target di Calibrazione**
  - Pattern geometrico stampato (tipicamente cerchi o scacchiera) utilizzato per calibrare la camera. Deve avere dimensioni note e superficie piana.
* - **TCP/IP**
  - Transmission Control Protocol / Internet Protocol. Stack di protocolli di comunicazione utilizzato per la trasmissione dati in rete tra VisionController, FlexiBowl e robot.
* - **Threshold (Soglia)**
  - Valore limite utilizzato in vari algoritmi per discriminare tra condizioni diverse (es: oggetto presente/assente, componente valido/non valido).
* - **Timeout**
  - Tempo massimo di attesa per una risposta durante la comunicazione. Se superato, viene generato un errore di comunicazione.
* - **Time (Tramoggia)**
  - Durata in millisecondi della vibrazione della tramoggia. Determina la quantità di componenti scaricati. Valori tipici: 300-800ms.
* - **Tilt**
  - Inclinazione della camera rispetto al piano orizzontale. Deve essere 0° ± 1° per garantire immagini non distorte.
* - **Tool (Robot)**
  - Utensile montato al polso del robot, tipicamente il gripper. Definisce il sistema di coordinate del punto di lavoro (TCP - Tool Center Point).
* - **Toplight**
  - Illuminatore a LED posizionato sopra il disco FlexiBowl che fornisce illuminazione uniforme dall'alto. Alimentazione tipica: 24V DC.
* - **Training**
  - Processo di creazione di un modello di riconoscimento selezionando le caratteristiche distintive del componente da un'immagine di riferimento.
* - **Tramoggia (Hopper)**
  - Sistema vibrante che alimenta continuamente i componenti sul disco FlexiBowl. Controllabile automaticamente tramite visione.
* - **Trigger**
  - Segnale che avvia l'acquisizione di un'immagine da parte della camera. Può essere software (temporizzato) o hardware (segnale elettrico).
* - **Vision Result**
  - Risultato fornito dal sistema di visione contenente coordinate (X, Y, RZ) e score del componente rilevato, pronto per essere inviato al robot.
* - **VisionController**
  - Computer industriale che esegue il software FlexiVision Easy, gestisce le camere, elabora le immagini e comunica con FlexiBowl e robot.
* - **Wizard**
  - Procedura guidata passo-passo che semplifica la configurazione di sistemi complessi (es: FlexiBowl Wizard per calcolo automatico parametri).
* - **X, Y, Z**
  - Coordinate cartesiane nello spazio tridimensionale. X = asse orizzontale, Y = asse verticale nel piano, Z = asse verticale (altezza).
```
