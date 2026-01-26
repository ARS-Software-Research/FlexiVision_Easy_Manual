(troubleshooting_conf_tramoggia)=
# Configurazione Tramoggia 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Tramoggia non abilitabile**
  - • Hardware non connesso
    
    • Setup iniziale non completato
  - • Verificare connessioni elettriche/pneumatiche
    
    • Completare Hopper Setup
* - **CAPTURE disco vuoto fallisce**
  - • Componenti ancora presenti
    
    • Camera non funzionante
  - • Rimuovere **TUTTI** i componenti
    
    • Testare acquisizione camera
* - **CAPTURE disco pieno fallisce**
  - • Troppo pochi componenti
    
    • Illuminazione cambiata
  - • Posizionare numero adeguato di componenti
    
    • Stabilizzare illuminazione
* - **TEST sempre VERDE**
  - • CAPTURE pieno con troppi componenti
  - • Ripetere con numero minimo corretto
* - **TEST sempre ROSSO**
  - • CAPTURE vuoto con componenti
    
    • Area include zone spurie
  - • Ripetere con area completamente pulita
    
    • Ridefinire area escludendo riflessi
* - **Steps difficile da calcolare**
  - • Non chiaro quanti cicli servono
  - • Svuotare disco completamente
    
    • Attivare tramoggia manualmente
    
    • Contare cicli fino ai PRIMI componenti
* - **Time non produce effetto**
  - • Valore troppo basso/alto
    
    • Livello vasca variabile
  - • Iniziare con 500ms
    
    • Incrementare ±100ms
    
    • **CRITICO**: Mantenere carico costante
* - **Flusso irregolare**
  - • Vasca si svuota progressivamente
    
    • Superficie sporca
  - • Implementare riempimento periodico
    
    • Pulire superficie vibrante
* - **Modifiche non salvate**
  - • Ricetta non salvata
  - • **FONDAMENTALE**: SEMPRE salvare ricetta
```