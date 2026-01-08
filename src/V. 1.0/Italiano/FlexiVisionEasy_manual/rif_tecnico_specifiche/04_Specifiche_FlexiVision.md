# **4.	Specifiche Dettagliate FlexiVision**
## *4.1.	Specifiche Camera* 
Il sistema FlexiVision utilizza telecamere ad alta risoluzione con interfaccia Gigabit Ethernet per garantire rapidità nell'acquisizione delle immagini e precisione nel riconoscimento dei componenti.
### 4.1.1.	Specifiche elettriche 
|Caratteristica	|Specifiche|
|---|---|
|Brand & Modello	|Cognex CAM-CIC-5000-20G |
|Risoluzione |5 MP (2448 × 2048 pixel)|
|Frame Rate 	|14 fps|
|Tipo Sensore	|CMOS|
|Dimensioni Sensore	|1/2.5"|
|Tipologia	|Monocromatica (Monochrome)|
|Protocollo di Connettività	|Gigabit Ethernet (GigE)|
  
  :::{admonition}  Nota
:class: info

La camera può anche essere alimentata e triggerata direttamente da una tracking board del robot per applicazioni di tracciamento circolare.

:::

 :::{admonition}  Avvertenza
:class: warning


   L'interfaccia Gigabit Ethernet è obbligatoria e richiede una infrastruttura di rete compatibile (switch Gigabit). La mancata osservanza di questo requisito compromette l'operatività della telecamera

:::
  
   
  |Metodo di Alimentazione|	Descrizione	|Requisiti di Cablaggio|  
  |--|--|--|
|1. PoE (Power over Ethernet) (opzionale)	|L'alimentazione e i dati vengono trasmessi tramite un unico cavo Ethernet. Consumo circa 3.3 W.	| Richiede un PoE Injector o uno Switch PoE compatibile.|
|2. Cavo Camera Esterno (incluso nel kit standard)|	L'alimentazione è fornita da una fonte CC esterna tramite cavo dedicato. |	Cavo Ethernet separato necessario solo per la comunicazione dati (PoE non richiesto).|  
  
  ### 4.1.2. Specifiche Fisiche     
  immagini con dimensioni camera, ingombro cavi, posizioni fori viti, grandezza fori viti e viti consigliate  
  ## *4.2. Specifiche VisionController*  
  Il sistema FlexiVision opera su un PC Industriale (VisionController) che funge da controller principale per il software di visione. Tra le opzioni disponibili acquistabili, ARS fornisce il suo VisionController già pre-configurato.   
  ### 4.2.1. Specifiche elettriche VisionController di ARS (da modificare nuovo pc)   

 
 |||   
|--|--| 
|Alimentazione (Input)	|9 ~ 36 V (tramite terminal block)|
|Consumo Energetico	|15 – 35 W|
|Porte di Rete (LAN)|	6x LAN (di cui 4x PoE)|
|Porte USB	|2x USB 3.0, 2x USB 2.0|
|Uscita Video|	1x DP (fino a 4096×2160 @ 60Hz)|

  ### 4.2.2. Specifiche Fisiche VisionController di ARS   
  |||   
|--|--| 
|Dimensioni (L x P x A)	|150 mm x 145 mm x 84 mm|
|Peso	|4 kg|
|Sistema Operativo|	Windows 11 IoT Enterprise 2021 LTSC VALUE 64 bit|
|Memoria (RAM)	|8GB DDR4-3200MHz SODIMM|
|Archiviazione|SSD 256GB SATA 2.5"|  
|Certificazioni|CE|  
## *4.3.	Specifiche Griglia di calibrazione* 
Una calibrazione eccellente è il requisito fondamentale per l'accuratezza del sistema FlexiVision (dei sistemi di visione in generale). Solo una calibrazione ad alta precisione garantisce che le coordinate rilevate dalla telecamera (pixel) vengano convertite in modo accurato nelle coordinate reali del robot (millimetri), assicurando così il successo dell'applicazione di picking.
### 4.3.1.	Griglia di Calibrazione Dedicata ARS
Sebbene sia tecnicamente possibile eseguire la calibrazione utilizzando una griglia stampata su carta, l'utilizzo della Griglia di Calibrazione Dedicata ARS (spesso utilizzata con l'opzione Laser Tool) innalza la precisione e semplifica il flusso di lavoro di manutenzione.  
La griglia ARS è realizzata con un'accuratezza estremamente elevata, impossibile da replicare con una stampa standard. Inoltre, la sua struttura è progettata per il montaggio ripetibile sul FlexiBowl®.  
|Caratteristica	|Griglia ARS Dedicata	|Griglia Stampata su Carta|  
|--|--| --|
|Precisione Fabbricativa	|Estremamente Alta (Manifattura dedicata)	|Bassa/Variabile (Dipende dalla stampante)|
|Ripetibilità di Montaggio	|Alta (Pin dedicati che si fissano in fori predefiniti sul FlexiBowl®)	|Bassa (Non ripetibile, richiede un riposizionamento manuale)|
|Punto di Riferimento Robot	Più Preciso (Se usata con Laser Tool, il contatto fisico è sostituito dall'allineamento visivo)	|Meno Preciso (Utilizza tip fisico o punta)|
|Vantaggio in Ricalibrazione	|Solo la visione richiede ricalibrazione. Il punto di riferimento del robot è mantenuto.	|Sia la visione che il robot richiedono una ricalibrazione completa.|  


Disegno griglia di calibrazione e dimensioni in base al modello di FlexiBowl [replicare griglia presente in documento vecchio]

Informazioni aggiuntive sulle modalità per una corretta calibrazione si trovano nella sezione [Calibrazione della Camera]  
## *4.4.	Resoconto principali caratteristiche kit/bundle base*
L'alimentazione (o altre caratteristiche più utili) dei componenti principali del sistema è la seguente:
|Componente|	Alimentazione|
|--|--|
|Camera 	||
|Lente ||	
|Griglia di calibrazione	||
|VisionController ||	
|Cavi ethernet 	||

## *4.5. Panoramica collegamenti*    
 ![Pan Coll](img/pan_collegamenti.png)


  :::{admonition} NOTA
  :class: info
  i cavi di comunicazione possono essere ordinati in lunghezze diverse, in base alle vostre esigenze. 
:::

## *4.6.	Protocollo di comunicazione*
Il robot deve avere la capacità di aprire e gestire uno o più server di comunicazione utilizzando il protocollo TCP/IP, al fine di ricevere e inviare stringhe tramite un task parallelo rispetto a quello principale, così da ricevere informazioni dal sistema di visione mentre il lavoro principale è in esecuzione  
|Data Terminator char	|Carattere di terminazione del dato|	CHR(13)|
|--|--|--|
|Stringa (Comando) |	Azione del Comando	|Valore di Ritorno (Return)|
|"set_Recipe=nome_ricetta"	|Viene caricata la ricetta corrispondente al "nome_ricetta" inviato.	|Nessuno|
|"get_Recipe"	|Viene mostrato il nome della ricetta attualmente caricata su FlexiVision.	|"nome_ricetta"|
|"start_Locator"|	Avvia il processo di localizzazione dei pezzi richiamando la routine di manipolazione FlexiBowl® nel caso in cui non ci siano pezzi prelevabili.	|"Pattern_1;x;y;r"|
|"stop_Locator"	|Ferma il processo di localizzazione dell'oggetto con l'ausilio del FlexiBowl®.	|Nessuno|
|"turn_Locator"	|Se nessun pezzo è stato prelevato, con questo comando l'operatore può far ruotare il FlexiBowl e avviare la routine "start_Locator".	|"Pattern_1;x;y;r"|
|"test_Locator"	|Avvia il processo di localizzazione dell'oggetto senza l'ausilio del FlexiBowl®.	|"Pattern_1;x;y;r"|
|"start_Control"	|Avvia il ciclo di ispezione.	|"Control_1;x;y;r"|
|"state_Locator"	|Viene mostrata la diagnostica dello stato del Localizzatore (Locator).	|"Locator is Running" (Localizzatore in Esecuzione)  "Locator is in Error" (Localizzatore in Errore)  "Locator is not Running" (Localizzatore non in Esecuzione)|
|"start_Empty"	|Avvia la sequenza di Svuotamento Rapido (Quick-Emptying) di FlexiBowl®.	|"start_Empty ended" (start_Empty terminato)|  

If hopper should be activated you will receive the string “Hopper;signalnumber;time”
