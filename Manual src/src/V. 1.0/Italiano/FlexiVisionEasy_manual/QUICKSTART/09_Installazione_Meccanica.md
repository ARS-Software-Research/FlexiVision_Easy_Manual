# **Installazione Meccanica del Sistema**
Questa sezione descrive i requisiti di montaggio e posizionamento dei componenti chiave del sistema di visione, che devono essere eseguiti solo dopo aver completato l'installazione meccanica di base del FlexiBowl® e della tramoggia.

:::{admonition} NOTA
:class: info 
 Prima di procedere con l'installazione dei componenti di visione, assicurarsi che il FlexiBowl® e la relativa tramoggia (Hopper) siano stati montati e fissati alla struttura portante (cellula robotica) in conformità con le istruzioni fornite nel Manuale Dedicato al FlexiBowl®.
:::
## *Montaggio VisionController* 
Il VisionController (PC Industriale) gestisce l'elaborazione delle immagini e la comunicazione con il robot.
:::{admonition} STEPS
* Disimballaggio:   
Estrarre il VisionController dalla confezione.
* Fissaggio:   
Fissare saldamente il Controller dove? Con che viti?
* Orientamento e Ventilazione:   
Si raccomanda di montare il Controller in verticale e di assicurare che sia adeguatamente ventilato per mantenere i componenti all'interno delle temperature operative [link alle specifiche tecniche]  
:::
Immagini!!

## *Montaggio Camera* 
Il posizionamento preciso e l'allineamento della telecamera sono passaggi critici che influenzano direttamente l'accuratezza della calibrazione e del picking.

### Distanza di Lavoro Ottimale
La telecamera deve essere montata in modo che la faccia frontale della lente sia posizionata a una distanza specifica (Working Distance) dalla superficie del piatto FlexiBowl®.
Riportare immagine della sezione sopra 
### Posizionamento e allineamento 
:::{admonition} IMPORTANTE
:class: warning 
* Centratura:  
La telecamera deve essere posizionata dove? rispetto al FlexiBowl® 
* Fissaggio:  
Fissare la telecamera utilizzando i fori di montaggio M? con viti?
* Ortogonalità?  Assicurarsi che la camera sia montata perfettamente parallela alla superficie del piatto, senza inclinazioni laterali (tilt). È necessario prestare la massima cura in questa fase.
* ????Regolazione Meccanica????: Per facilitare la messa a punto, si raccomanda di progettare il supporto meccanico con la possibilità di effettuare microregolazioni nelle direzioni X, Y e Z. Si suggerisce una tolleranza di aggiustamento di circa -10mm/+30mm in Z e -10mm/+10mm in X e Y.
:::

Immagini!!

:::{admonition} IMPORTANTE
:class: warning
La lente è solitamente già montata sulla telecamera al momento del disimballaggio. Verificare sempre che sia stata selezionata la lente con la corretta lunghezza focale per il modello di FlexiBowl® in uso.
:::

## *Montaggio toplight* 
Se è incluso un Toplight (illuminatore dall'alto), deve essere montato sulla stessa struttura di supporto della telecamera.

### Posizionamento 
Il Toplight deve essere fissato in modo da garantire che l'illuminazione sulla superficie del FlexiBowl® sia la più uniforme possibile
### Distanza  
Generalmente, il Toplight viene posizionato a una distanza dalla superficie del FlexiBowl® simile a quella della telecamera, per minimizzare le ombre e massimizzare l'uniformità luminosa.
### Cablaggi 
Predisporre il cablaggio per l'alimentazione esterna separata del Toplight.

Immagini!!  

:::{admonition} NOTA
:class: info 
Si raccomanda di schermare l'intera cella robotica da fonti luminose esterne per garantire la stabilità del sistema di visione, indipendentemente dal sistema di illuminazione (Backlight o Toplight) utilizzato.???
:::
