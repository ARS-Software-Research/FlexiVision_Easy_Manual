(troubleshooting_protocol_setup)=
# Protocol Setup
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Protocollo non compatibile con robot**
  - • Protocollo selezionato errato
    
    • Versione firmware robot non supportata
    
    • Configurazione protocollo non standard
  - • Verificare protocollo supportato dal robot (documentazione robot)
    
    • Aggiornare firmware robot se necessario
    
    • Contattare supporto per protocolli custom
* - **Dati inviati non interpretati correttamente dal robot**
  - • Formato dati non corretto
    
    • Ordine coordinate errato
    
    • Unità di misura non corrispondenti
    
    • Separatore decimale diverso (punto vs virgola)
  - • Verificare formato stringa dati in Protocol Setup
    
    • Configurare ordine coordinate secondo robot (XYZ vs ZYX, etc.)
    
    • Verificare unità (mm vs pollici)
    
    • Impostare separatore decimale corretto (tipicamente punto)
* - **Robot riceve dati ma non esegue movimento**
  - • Programma robot non in ascolto
    
    • Flag di acknowledge non gestito
    
    • Robot in errore o modalità manuale
  - • Avviare programma socket server sul robot
    
    • Implementare gestione acknowledge in programma robot
    
    • Verificare stato robot e portare in automatico
* - **Perdita di pacchetti dati**
  - • Connessione TCP/IP instabile
    
    • Buffer overflow robot
    
    • Timeout troppo basso
  - • Stabilizzare connessione Ethernet
    
    • Aumentare dimensione buffer robot
    
    • Incrementare valore timeout
```
