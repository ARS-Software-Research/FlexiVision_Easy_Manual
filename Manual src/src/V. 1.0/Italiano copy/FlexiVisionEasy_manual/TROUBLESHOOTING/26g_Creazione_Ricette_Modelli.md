# Creazione Ricette e modelli 

(troubleshooting_Nuova_Ricetta)=
## Creare una Nuova Ricetta 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Impossibile creare ricetta**
  - • Permessi insufficienti
    
    • Disco pieno
    
    • Nome con caratteri speciali
  - • Verificare permessi cartella
    
    • Liberare spazio disco
    
    • Evitare caratteri: / \ : * ? " < > |
* - **Ricetta non appare**
  - • Salvataggio non completato
    
    • File corrotto
  - • Ripetere creazione e salvataggio
    
    • Verificare integrità file
* - **Impossibile caricare ricetta**
  - • File corrotto
    
    • Versione software incompatibile
  - • Ripristinare da backup
    
    • Aggiornare software
```

(troubleshooting_Nuovo_modello)=
## Creare un Nuovo Modello 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Impossibile abilitare modello**
  - • Limite massimo raggiunto (8)
    
    • Slot occupato
  - • Disabilitare modelli non usati
    
    • Selezionare slot libero
* - **Grab Image acquisisce nero**
  - • Camera non connessa
    
    • Toplight spento
    
    • Tappo lente presente
  - • Verificare Camera Setup
    
    • Accendere toplight
    
    • Rimuovere tappo lente
* - **Apply Train non genera modello**
  - • Feature Threshold non impostato
    
    • ROI troppo piccolo
    
    • Contrasto insufficiente
  - • Impostare Feature Threshold (iniziare con 0.5)
    
    • Ingrandire ROI
    
    • Migliorare illuminazione
* - **Modello include superficie**
  - • Feature Threshold troppo basso
    
    • Superficie texturizzata
  - • Aumentare Threshold (0.3 → 0.6)
    
    • Sostituire superficie grip
* - **Modello con poche linee**
  - • Threshold troppo alto
    
    • Immagine sfocata
  - • Diminuire Threshold (0.8 → 0.5)
    
    • Verificare fuoco camera
```

(troubleshooting_Modelli_ROI)=
## Definizione ROI e Tolleranze 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Test non rileva componenti**
  - • Accept Threshold troppo alto
    
    • Componenti fuori Region Search
    
    • Illuminazione cambiata
  - • Diminuire Threshold (0.90 → 0.75)
    
    • Allargare Region Search
    
    • Stabilizzare illuminazione
* - **Troppi falsi positivi**
  - • Threshold troppo basso
    
    • Modello troppo generico
  - • Aumentare Threshold (0.70 → 0.85)
    
    • Rifare modello più dettagliato
* - **Score componenti bassi**
  - • Variabilità componenti
    
    • Componenti sporchi
    
    • Modello troppo dettagliato
  - • Pulire componenti
    
    • Scartare componenti danneggiati
    
    • Rifare modello meno dettagliato
* - **Coordinate non corrette**
  - • Calibrazione camera non eseguita
    
    • Camera spostata
  - • Eseguire calibrazione camera
    
    • Ripetere calibrazione
```

(troubleshooting_istogrammi)=
## Istogrammi 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Impossibile abilitare istogramma**
  - • Limite massimo (8) raggiunto
    
    • Modello non completato
  - • Disabilitare istogrammi non usati
    
    • Completare configurazione modello
* - **AUTO non calcola valori**
  - • Area troppo piccola
    
    • Istogramma fuori immagine
  - • Ingrandire area istogramma
    
    • Spostare dentro area visibile
* - **Test sempre ROSSO**
  - • Calibrazione con area occupata
    
    • Ombra/riflesso nell'area
  - • Ripetere AUTO con area VUOTA
    
    • Escludere zone con ombre
* - **Test sempre VERDE**
  - • Calibrazione con componenti presenti
    
    • Contrasto insufficiente
  - • Ripetere AUTO con area vuota
    
    • Migliorare illuminazione
* - **Triggera casualmente**
  - • Area troppo grande
    
    • Illuminazione instabile
  - • Ridurre area al minimo
    
    • Stabilizzare illuminazione
```

(troubleshooting_robot_pick)=
## Calibrazione Robot Pick 

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Coordinate robot perse**
  - • Non annotate durante setup
  - • **OBBLIGATORIO**: Ripetere preparazione fisica completa
    
    • Salvare coordinate in file digitale
* - **Find Object non rileva**
  - • Componente riferimento spostato
    
    • Threshold troppo alto
  - • Verificare posizione riferimento
    
    • Abbassare temporaneamente Threshold
* - **Gripper Offset valori assurdi**
  - • Coordinate inserite erroneamente
    
    • X e Y scambiati
    
    • Segno ± errato
  - • **CRITICO**: Verificare ogni coordinata
    
    • Controllare ordine X, Y, RZ
    
    • Copiare valori esattamente come annotati
* - **Robot preleva male**
  - • Coordinate annotate errate
    
    • Frame/Tool cambiato
    
    • Offset non salvato
  - • Ripetere con Frame/Tool corretti
    
    • Salvare ricetta dopo calcolo Offset
* - **Rotazione RZ errata**
  - • RZ non era a 0° durante setup
  - • Ripetere con ultimo asse a RZ=0°
```
