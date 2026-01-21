(troubleshooting_conf_tramoggia)=
# Configurazione Tramoggia 
```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Tramoggia non abilitabile**
  - • Hardware tramoggia non connesso
    
    • Ricetta non caricata
    
    • Configurazione base non completata
  - • Verificare connessioni elettriche/pneumatiche tramoggia
    
    • Caricare ricetta corretta
    
    • Completare Hopper Setup iniziale
* - **Area di controllo non definibile**
  - • Camera tramoggia non rilevata
    
    • Immagine non acquisita
    
    • Software in modalità sbagliata
  - • Verificare connessione camera hopper
    
    • Acquisire immagine test
    
    • Accedere tramite Config Hopper X
* - **Riquadro blu non modificabile**
  - • Modalità Expert attiva
    
    • Area bloccata
  - • Uscire da modalità Expert
    
    • Riavviare configurazione tramoggia
* - **CAPTURE disco vuoto fallisce**
  - • Componenti ancora presenti nell'area
    
    • Illuminazione insufficiente
    
    • Camera non funzionante
  - • Rimuovere **TUTTI** i componenti dall'area visibile
    
    • Verificare illuminazione camera hopper
    
    • Testare acquisizione camera
* - **CAPTURE disco pieno fallisce**
  - • Troppo pochi componenti posizionati
    
    • Componenti fuori area controllo
    
    • Illuminazione cambiata
  - • Posizionare numero adeguato di componenti nell'area
    
    • Verificare componenti dentro riquadro blu
    
    • Stabilizzare illuminazione
* - **AUTO non calcola Mean e Std Dev**
  - • CAPTURE non eseguiti
    
    • Ordine CAPTURE invertito
    
    • Area controllo troppo piccola
  - • Eseguire CAPTURE vuoto poi CAPTURE pieno
    
    • Ripetere nell'ordine corretto
    
    • Ingrandire area di controllo
* - **TEST sempre VERDE (tramoggia non si attiva mai)**
  - • Soglia troppo permissiva
    
    • CAPTURE pieno con troppi componenti
    
    • Mean calcolato errato
  - • Ripetere CAPTURE pieno con numero minimo corretto
    
    • Verificare AUTO ricalcola correttamente
    
    • Regolare manualmente soglia se necessario
* - **TEST sempre ROSSO (tramoggia si attiva sempre)**
  - • Soglia troppo restrittiva
    
    • CAPTURE vuoto con componenti presenti
    
    • Area include zone spurie
  - • Ripetere CAPTURE vuoto con area completamente pulita
    
    • Ridefinire area escludendo riflessi/ombre
    
    • Ripetere AUTO
* - **Turn FLB non funziona durante setup**
  - • FlexiBowl non connesso
    
    • Comando non configurato
    
    • FlexiBowl in errore
  - • Verificare connessione FlexiBowl
    
    • Controllare configurazione FlexiBowl Setup
    
    • Verificare LED READY FlexiBowl
* - **Steps parametro difficile da calcolare**
  - • Non chiaro quanti cicli servono
    
    • Componenti arrivano in momenti diversi
  - • Svuotare completamente disco
    
    • Attivare tramoggia manualmente
    
    • Contare cicli finché PRIMI componenti raggiungono camera
    
    • Usare valore conservativo (arrotondare per eccesso)
* - **Time vibrazione non produce effetto desiderato**
  - • Valore troppo basso (pochi componenti)
    
    • Valore troppo alto (troppi componenti)
    
    • Livello vasca tramoggia variabile
  - • Iniziare con 500ms
    
    • Incrementare ±100ms per regolare flusso
    
    • **CRITICO**: Mantenere carico costante nella vasca
* - **Flusso componenti irregolare**
  - • Vasca tramoggia si svuota progressivamente
    
    • Superficie vibrante sporca
    
    • Componenti di dimensioni molto variabili
  - • Implementare riempimento periodico vasca
    
    • Pulire superficie vibrante
    
    • Separare componenti per dimensione omogenea
* - **Tramoggia scarica in momenti sbagliati**
  - • Steps non corretto
    
    • Sincronizzazione errata con ciclo FlexiBowl
  - • Ricalcolare Steps
    
    • Verificare coordinazione Hopper-FlexiBowl
* - **Modifiche non salvate**
  - • **Salva Ricetta** non premuto
    
    • Uscita pagina prima di salvare
  - • **FONDAMENTALE**: SEMPRE salvare ricetta dopo modifiche
    
    • Verificare messaggio conferma salvataggio
    
    • Attendere completamento prima di uscire
```
