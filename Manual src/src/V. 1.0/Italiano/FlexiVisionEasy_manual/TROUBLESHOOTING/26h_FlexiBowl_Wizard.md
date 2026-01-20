# FlexiBowl Wizard

```{list-table}
:header-rows: 1
:widths: 30 35 35

* - Problema
  - Possibili Cause
  - Soluzioni
* - **Wizard non si avvia**
  - • Ricetta non caricata
    
    • FlexiBowl non connesso
    
    • Setup iniziale non completato
  - • Caricare o creare ricetta prima
    
    • Verificare connessione FlexiBowl
    
    • Completare configurazione base sistema
* - **Impossibile selezionare taglia FlexiBowl**
  - • Menu a tendina bloccato
    
    • Modello non disponibile in lista
  - • Riavviare Wizard
    
    • Contattare supporto per modelli custom
* - **Senso rotazione impostato non corrisponde**
  - • Errore di selezione CW/CCW
    
    • Installazione meccanica invertita
  - • Verificare visivamente senso rotazione reale
    
    • Correggere selezione nel Wizard
    
    • NON è modificabile via software se installazione è invertita
* - **Caratterizzazione componente difficile**
  - • Componente con caratteristiche miste
    
    • Geometria non rientra in categorie standard
  - • Scegliere categoria più simile
    
    • Per componenti FLAT/CYLINDRICAL misti → scegliere prevalente
    
    • Per componenti complessi → sempre COMPLEX
* - **Test Air-blow non funziona**
  - • Aria compressa non collegata
    
    • Pressione insufficiente
    
    • Modulo non presente fisicamente
  - • Verificare connessione aria compressa
    
    • Aumentare pressione a 5-6 bar
    
    • Selezionare "FlexiBowl NOT equipped" se modulo assente
* - **Test Flip non avvertibile**
  - • Aria compressa non collegata/insufficiente
    
    • Regolatore pressione chiuso
    
    • Perdite circuito pneumatico
  - • Verificare aria compressa collegata
    
    • Aprire regolatore su pannello controllo
    
    • Verificare pressione 5-6 bar
    
    • Ispezionare raccordi per perdite
* - **Parametri calcolati non ottimali**
  - • Caratterizzazione componente errata
    
    • Wizard usa valori generici
  - • Rivedere geometria e comportamento selezionati
    
    • Accettare parametri Wizard come punto di partenza
    
    • Affinare manualmente in dashboard riassuntiva
* - **Sincronizzazione Flip-Move non corretta**
  - • Flip Count errato
    
    • Flip Delay non ottimale
    
    • Tempi Move non compatibili
  - • Regolare Flip Count incrementalmente
    
    • Modificare Delay finché impulsi terminano insieme
    
    • Usare Test Sequence ripetutamente per verificare
* - **Componenti si muovono durante acquisizione**
  - • Velocità/accelerazione troppo alte
    
    • Pause stabilizzazione assente
    
    • Superficie grip non adatta
  - • Diminuire Speed e Accel
    
    • Inserire pause 200-500ms
    
    • Sostituire superficie grip con più aderente
* - **Soffio pre-flip non efficace**
  - • Blow Time troppo breve
    
    • Pressione aria insufficiente
    
    • Ugelli ostruiti
  - • Aumentare Blow Time
    
    • Verificare pressione 5-6 bar
    
    • Pulire ugelli air-blow
* - **Soffio post-flip raggruppa troppo**
  - • Blow Time troppo lungo
    
    • Non necessario per applicazione
  - • Diminuire Blow Time
    
    • Disabilitare post-flip e usare solo pre-flip
* - **Modifiche parametri non si applicano**
  - • "Synchronize Parameters" non premuto
    
    • Ricetta non salvata
  - • **SEMPRE** cliccare Synchronize Parameters dopo modifiche
    
    • Salvare ricetta per rendere permanenti le modifiche
```