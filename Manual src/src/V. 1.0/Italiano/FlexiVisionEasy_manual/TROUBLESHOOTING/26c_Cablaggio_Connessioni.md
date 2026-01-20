# Cablaggio e Connessioni
(troubleshooting_alimentazione)=
## Problemi di Alimentazione FlexiBowl 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **LED READY non si accende dopo accensione switch**
  - • Alimentazione non collegata correttamente
    
    • Switch AC in posizione "O" invece di "I"
    
    • Cavo alimentazione danneggiato
    
    • Tensione errata
    
    • Fusibile interno bruciato
  - • Verificare connessione alimentazione secondo manuale FlexiBowl
    
    • Portare switch in posizione "I" (ON)
    
    • Ispezionare cavo per danni e sostituire se necessario
    
    • Verificare tensione conforme a specifiche (consultare manuale)
    
    • Contattare supporto tecnico per sostituzione fusibile
* - **FlexiBowl si spegne casualmente**
  - • Connessione alimentazione allentata
    
    • Cavo sottodimensionato
    
    • Interferenze elettriche
    
    • Sovraccarico termico
  - • Serrare connessioni alimentazione
    
    • Utilizzare cavo con sezione adeguata
    
    • Collegare a linea dedicata con filtro EMI
    
    • Verificare ventilazione controller FlexiBowl
```
(troubleshooting_ethernet)=
## Problemi di Connessione Ethernet 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **FlexiBowl non comunica con VisionController**
  - • Cavo Ethernet non collegato correttamente
    
    • Cavo Ethernet danneggiato
    
    • Indirizzo IP non configurato o errato
    
    • FlexiBowl e VisionController su subnet diverse
  - • Verificare connessione fisica cavo Ethernet su entrambi i lati
    
    • Testare cavo con cable tester o sostituire
    
    • Verificare configurazione IP in [FlexiBowl Setup](QUICKSTART/xx_FlexiBowl_Setup.md)
    
    • Configurare FlexiBowl e VisionController nella stessa rete (es: 192.168.1.x)
* - **Connessione intermittente**
  - • Cavo Ethernet di categoria insufficiente (< Cat5e)
    
    • Cavo troppo lungo (> 100m)
    
    • Connettore RJ45 danneggiato o mal crimpato
    
    • Interferenze elettromagnetiche
  - • Utilizzare cavo Cat5e o superiore
    
    • Ridurre lunghezza cavo sotto 100m o usare switch intermedio
    
    • Sostituire connettori o cavo completo
    
    • Utilizzare cavo schermato (STP) lontano da fonti EMI
* - **VisionController non rileva FlexiBowl sulla rete**
  - • FlexiBowl non acceso (LED READY spento)
    
    • Firewall blocca comunicazione
    
    • Porta Ethernet VisionController guasta
  - • Verificare LED READY acceso sul FlexiBowl
    
    • Disabilitare temporaneamente firewall per test
    
    • Provare altra porta Ethernet del VisionController
```
(troubleshooting_pneumatica)=
## Problemi Pneumatici (Aria Compressa)

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Flip non funziona o impulso molto debole**
  - • Aria compressa non collegata
    
    • Pressione insufficiente (< 5 bar)
    
    • Regolatore di pressione chiuso o su minimo
    
    • Perdite nel circuito pneumatico
    
    • Tubo pneumatico danneggiato o ostruito
  - • Collegare aria compressa alla connessione FlexiBowl (vedere manuale)
    
    • Aumentare pressione a 5-6 bar
    
    • Aprire regolatore di pressione sul pannello di controllo
    
    • Ispezionare raccordi con acqua saponata, serrare o sostituire
    
    • Verificare tubo per pieghe/ostruzioni, sostituire se necessario
* - **Air-blow non funziona**
  - • Modulo Air-blow non alimentato
    
    • Pressione aria insufficiente
    
    • Ugelli ostruiti
    
    • Elettrovalvola guasta
  - • Verificare alimentazione elettrica modulo air-blow
    
    • Controllare pressione aria (5-6 bar)
    
    • Pulire ugelli con aria compressa
    
    • Testare elettrovalvola, sostituire se difettosa
* - **Tramoggia non vibra per scarico componenti**
  - • Aria compressa non collegata alla tramoggia
    
    • Pressione insufficiente
    
    • Vibratore pneumatico guasto
    
    • Comando elettrico non arriva
  - • Verificare connessione pneumatica tramoggia
    
    • Aumentare pressione a valore consigliato
    
    • Testare vibratore manualmente, sostituire se necessario
    
    • Verificare segnale di comando da VisionController
```
(troubleshooting_connessione_camera)=
## Problemi di Connessione Camera

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Camera non rilevata dal VisionController**
  - • Cavo Ethernet camera non collegato
    
    • Camera collegata a porta non POE del VisionController
    
    • Camera non POE-compatibile (richiede alimentazione separata)
    
    • Porta POE VisionController guasta
    
    • Indirizzo IP camera in conflitto
  - • Verificare connessione fisica cavo camera
    
    • Collegare camera SOLO a porta POE del VisionController
    
    • Verificare compatibilità POE camera, altrimenti alimentare separatamente
    
    • Provare altra porta POE del VisionController
    
    • Reimpostare IP camera o configurare IP statico univoco
* - **Immagine camera nera o assente**
  - • Camera non alimentata (POE non attivo)
    
    • Lente con tappo protettivo non rimosso
    
    • Lente non installata
    
    • Esposizione camera troppo bassa
    
    • Camera guasta
  - • Verificare LED camera acceso (indicatore POE attivo)
    
    • Rimuovere tappo protettivo lente
    
    • Installare lente con focale corretta
    
    • Aumentare esposizione in [Camera Setup](QUICKSTART/xx_Camera_Setup.md)
    
    • Sostituire camera
* - **Immagine disturbata o con artefatti**
  - • Cavo Ethernet camera troppo lungo (> 100m)
    
    • Cavo non schermato vicino a fonti EMI
    
    • Connettore RJ45 mal crimpato
    
    • Interferenze da alimentatori switching
  - • Ridurre lunghezza cavo o usare switch POE intermedio
    
    • Utilizzare cavo schermato (STP)
    
    • Rifare crimpatura connettore o sostituire cavo
    
    • Allontanare cavo camera da fonti di disturbo
* - **Camera si disconnette casualmente**
  - • Alimentazione POE insufficiente (potenza < richiesta camera)
    
    • Cavo danneggiato
    
    • Surriscaldamento camera
    
    • Porta POE instabile
  - • Verificare potenza POE disponibile (standard 802.3af: 15.4W, 802.3at: 30W)
    
    • Sostituire cavo Ethernet
    
    • Migliorare ventilazione area camera
    
    • Sostituire switch POE o porta VisionController
```
(troubleshooting_connessione_toplight)=
## Problemi di Connessione Toplight 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Toplight non si accende**
  - • Alimentazione 24V DC non collegata
    
    • Cavo alimentazione danneggiato
    
    • Tensione errata (≠ 24V)
    
    • Toplight guasto
    
    • Fusibile/protezione scattata
  - • Verificare connessione alimentazione 24V DC
    
    • Ispezionare cavo, sostituire se danneggiato
    
    • Misurare tensione con multimetro, deve essere 24V DC (±10%)
    
    • Sostituire toplight
    
    • Verificare protezioni nel quadro elettrico
* - **Luminosità toplight variabile**
  - • Alimentazione instabile
    
    • Connessioni allentate
    
    • Alimentatore sottodimensionato
    
    • Toplight a fine vita
  - • Verificare stabilità tensione alimentazione
    
    • Serrare tutte le connessioni elettriche
    
    • Verificare corrente assorbita vs capacità alimentatore
    
    • Sostituire toplight
* - **Toplight si surriscalda**
  - • Ventilazione insufficiente
    
    • Corrente eccessiva
    
    • Ciclo di lavoro continuo 100%
  - • Migliorare circolazione aria attorno a toplight
    
    • Verificare corrente assorbita non superi specifiche
    
    • Implementare ciclo lavoro intermittente se possibile
```
(troubleshooting_multi)=
## Problemi Cpnfigurazioni Multi-Dispositivo
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Sistema con 2-3 FlexiBowl: solo uno comunica**
  - • Indirizzi IP duplicati
    
    • FlexiBowl sullo stesso hub Ethernet
    
    • Cavi incrociati
    
    • Switch Ethernet insufficiente
  - • Assegnare IP univoci a ogni FlexiBowl (es: 192.168.1.10, .11, .12)
    
    • Collegare ogni FlexiBowl a porta dedicata VisionController
    
    • Verificare corretto cablaggio stella (no daisy-chain)
    
    • Utilizzare switch managed per configurazione avanzata
* - **Sistema con 2-3 camere: solo una acquisisce**
  - • Porte POE insufficienti su VisionController
    
    • Potenza POE totale superata
    
    • Indirizzi IP camere in conflitto
    
    • Configurazione software non corretta
  - • Verificare numero porte POE disponibili, aggiungere switch POE se necessario
    
    • Calcolare potenza POE totale richiesta vs disponibile
    
    • Configurare IP statico univoco per ogni camera
    
    • Abilitare tutte le camere in [Camera Setup](QUICKSTART/xx_Camera_Setup.md)
* - **Sistema con 2-3 tramogge: controllo errato**
  - • Tramogge non abilitate individualmente in software
    
    • Cablaggio pneumatico incrociato
    
    • Comandi elettrici sovrapposti
    
    • Aree di controllo sovrapposte
  - • Abilitare ogni tramoggia in [Hopper Setup](SETUP/xx_Hopper_Setup.md)
    
    • Verificare schema pneumatico, ogni tramoggia deve avere linea dedicata
    
    • Controllare cablaggio elettrovalvole
    
    • Definire aree di controllo separate per ogni tramoggia
```

