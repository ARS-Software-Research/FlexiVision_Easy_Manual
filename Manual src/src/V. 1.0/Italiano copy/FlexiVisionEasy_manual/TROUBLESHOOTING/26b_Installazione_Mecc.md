# Installazione Meccanica
(troubleshooting_vision_controller)=
## Problemi con il VisionController 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **VisionController si surriscalda e si spegne automaticamente**
  - • Ventilazione insufficiente (spazio < 50mm)
    
    • Orientamento non corretto
    
    • Temperatura ambiente > 50°C
    
    • Accumulo di polvere nelle prese d'aria
  - • Verificare spazio libero di almeno 50mm su tutti i lati
    
    • Riposizionare in verticale o con ventilazione forzata
    
    • Spostare in ambiente più fresco o aggiungere condizionamento
    
    • Pulire le prese di ventilazione
* - **VisionController non si fissa correttamente alla guida DIN**
  - • Guida DIN non conforme (non 35mm)
    
    • Meccanismo di aggancio danneggiato
    
    • Guida non fissata saldamente
  - • Verificare che la guida sia DIN 35mm standard
    
    • Ispezionare meccanismo di aggancio per danni
    
    • Fissare meglio la guida DIN al pannello
* - **VisionController si allenta dal pannello (montaggio con viti)**
  - • Coppia di serraggio insufficiente
    
    • Viti non idonee (non M4)
    
    • Foratura pannello non corretta
  - • Serrare le 4 viti M4 con coppia di 1.2 Nm
    
    • Utilizzare viti M4 come da specifiche
    
    • Verificare pattern di foratura secondo disegni tecnici
* - **Protezione IP insufficiente**
  - • Montaggio all'esterno del quadro elettrico
    
    • Quadro con IP < 40
    
    • Presenza di polvere/umidità
  - • Montare all'interno di quadro elettrico IP54
    
    • Verificare protezione minima IP40
    
    • Sigillare meglio il quadro elettrico
```
(troubleshooting_camera)=
## Problemi con la Camera 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Immagine non a fuoco**
  - • Distanza di lavoro non corretta (non 950-1000mm)
    
    • Lente non avvitata completamente
    
    • Lente con focale errata per il modello FlexiBowl
  - • Misurare e correggere distanza secondo [Calcolo Distanza Ottimale](rif_tecnico_specifiche/05_Calcolo_distanza_ottimale.md)
    
    • Avvitare completamente la lente (contatto metal-metal)
    
    • Verificare etichetta lente e documentazione ordine
* - **Immagine distorta o con prospettiva errata**
  - • Camera non centrata sull'asse FlexiBowl (errore > ±5mm)
    
    • Camera inclinata rispetto alla superficie (tilt > ±1°)
    
    • Camera ruotata attorno all'asse ottico
  - • Misurare centratura con metro/calibro e correggere
    
    • Verificare ortogonalità con livella di precisione
    
    • Allineare camera con asse di rotazione disco
* - **Impossibile regolare la posizione della camera**
  - • Supporto meccanico rigido senza microregolazioni
    
    • Viti di fissaggio serrate definitivamente
  - • Progettare supporto con regolazioni: Z(-10/+30mm), X(±10mm), Y(±10mm)
    
    • Allentare viti per permettere regolazioni
* - **Viti di fissaggio camera si allentano**
  - • Coppia di serraggio eccessiva (> 0.5 Nm)
    
    • Vibrazioni del sistema
    
    • Viti non idonee
  - • Serrare con coppia corretta 0.5 Nm per evitare deformazioni
    
    • Utilizzare frenafiletti medio
    
    • Verificare utilizzo viti M3 × 8mm inox come consigliato
* - **Camera danneggiata durante montaggio**
  - • Coppia di serraggio eccessiva
    
    • Manipolazione scorretta
    
    • Urti durante installazione
  - • Non superare 0.5 Nm di coppia
    
    • Maneggiare con cura evitando pressioni sul corpo ottico
    
    • Proteggere durante lavori meccanici circostanti
```
(troubleshooting_toplight)=
## Problemi con il Toplight 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Illuminazione non uniforme con ombre evidenti**
  - • Distanza toplight dalla superficie non corretta
    
    • Toplight non parallelo al disco FlexiBowl
    
    • Angolo di illuminazione non perpendicolare (tilt ≠ 0°)
  - • Posizionare toplight a distanza simile a quella della camera
    
    • Verificare parallelismo con livella
    
    • Correggere orientamento a 0° tilt
* - **Riflessioni dirette verso la camera (hotspot)**
  - • Toplight troppo vicino alla superficie
    
    • Angolazione non corretta
    
    • Superficie FlexiBowl troppo riflettente
  - • Aumentare distanza toplight
    
    • Regolare leggermente angolo
    
    • Considerare uso di diffusori
    
    • Valutare sostituzione superficie grip
* - **Toplight non concentrico con la camera**
  - • Errore di posizionamento su struttura supporto
    
    • Struttura non correttamente assemblata
  - • Verificare allineamento centri camera-toplight
    
    • Riposizionare toplight concentrico alla camera
* - **Cablaggio toplight non conforme**
  - • Tensione errata (≠ 24V DC)
    
    • Cavi non schermati
    
    • Alimentazione condivisa con altri dispositivi rumorosi
  - • Verificare tensione su etichetta (tipicamente 24V DC)
    
    • Utilizzare cavi schermati dedicati
    
    • Predisporre alimentazione separata dal quadro
```
(troubleshooting_luce_ambientale)=
## Problemi di Schermatura Luce Ambientale 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Rilevamenti incoerenti a diverse ore del giorno**
  - • Luce solare diretta o indiretta variabile
    
    • Finestre non schermate
    
    • Illuminazione artificiale con dimmer
  - • Installare tende oscuranti o pannelli opachi
    
    • Schermare completamente finestre nella cella
    
    • Utilizzare illuminazione fissa non regolabile
* - **Riflessioni da superfici circostanti**
  - • Superfici lucide nelle vicinanze (macchine, pannelli)
    
    • Parti metalliche riflettenti
  - • Coprire superfici riflettenti con materiale opaco
    
    • Riposizionare elementi riflettenti
    
    • Verniciare superfici con vernice opaca
* - **Interferenze da luci intermittenti**
  - • Luci di segnalazione robot/macchine
    
    • Flash da altre postazioni
    
    • Lampade di emergenza
  - • Schermare completamente la cella robotica
    
    • Spostare segnalatori fuori dall'area
    
    • Creare cabina chiusa per la cella
```
