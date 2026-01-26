# Cablaggio e Connessioni

(troubleshooting_alimentazione)=
## Alimentazione FlexiBowl 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **LED READY non si accende**
  - • Switch in posizione "O"
    
    • Alimentazione non collegata
    
    • Fusibile bruciato
  - • Portare switch su "I"
    
    • Verificare connessione alimentazione
    
    • Contattare supporto per fusibile
* - **FlexiBowl si spegne casualmente**
  - • Connessione allentata
    
    • Interferenze elettriche
  - • Serrare connessioni
    
    • Collegare a linea dedicata con filtro EMI
```

(troubleshooting_ethernet)=
## Connessione Ethernet 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **FlexiBowl non comunica**
  - • Cavo non collegato/danneggiato
    
    • IP non configurato
    
    • Subnet diverse
  - • Verificare connessione fisica
    
    • Configurare IP correttamente
    
    • Impostare stessa rete (es: 192.168.1.x)
* - **Connessione intermittente**
  - • Cavo categoria insufficiente (< Cat5e)
    
    • Cavo troppo lungo (> 100m)
    
    • Interferenze EMI
  - • Usare Cat5e o superiore
    
    • Ridurre lunghezza o usare switch
    
    • Usare cavo schermato (STP)
```

(troubleshooting_pneumatica)=
## Pneumatica

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Flip debole o assente**
  - • Pressione insufficiente (< 5 bar)
    
    • Regolatore chiuso
    
    • Perdite nel circuito
  - • Aumentare pressione a 5-6 bar
    
    • Aprire regolatore
    
    • Ispezionare raccordi con acqua saponata
* - **Air-blow non funziona**
  - • Pressione insufficiente
    
    • Ugelli ostruiti
  - • Controllare pressione (5-6 bar)
    
    • Pulire ugelli con aria compressa
```

(troubleshooting_connessione_camera)=
## Connessione Camera

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Camera non rilevata**
  - • Non collegata a porta POE
    
    • Camera non POE-compatibile
    
    • Porta POE guasta
  - • Collegare SOLO a porta POE
    
    • Verificare compatibilità POE
    
    • Provare altra porta POE
* - **Immagine nera**
  - • POE non attivo
    
    • Tappo lente non rimosso
    
    • Esposizione troppo bassa
  - • Verificare LED camera acceso
    
    • Rimuovere tappo protettivo
    
    • Aumentare esposizione in Camera Setup
* - **Immagine disturbata**
  - • Cavo troppo lungo (> 100m)
    
    • Interferenze EMI
  - • Ridurre lunghezza o usare switch POE
    
    • Usare cavo schermato (STP)
```

(troubleshooting_connessione_toplight)=
## Connessione Toplight 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Toplight non si accende**
  - • 24V DC non collegati
    
    • Tensione errata
  - • Verificare connessione 24V DC
    
    • Misurare tensione: deve essere 24V ±10%
* - **Luminosità variabile**
  - • Alimentazione instabile
    
    • Connessioni allentate
  - • Verificare stabilità tensione
    
    • Serrare tutte le connessioni
```

(troubleshooting_multi)=
## Configurazioni Multi-Dispositivo

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Solo un FlexiBowl comunica**
  - • IP duplicati
    
    • Cavi incrociati
  - • Assegnare IP univoci (192.168.1.10, .11, .12)
    
    • Collegare ogni FlexiBowl a porta dedicata
* - **Solo una camera acquisisce**
  - • Potenza POE insufficiente
    
    • IP in conflitto
  - • Verificare potenza POE disponibile
    
    • Configurare IP univoci per ogni camera
```

