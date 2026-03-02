(configfb)=
# **Configurazione guidata: FlexiBowl® Wizard**


L'interfaccia **FlexiBowl® Wizard** è uno strumento interattivo progettato per guidare l'utente nella configurazione dei parametri di alimentazione in base alla specifica famiglia di prodotti da gestire.

## **Step 1: Accesso al Wizard**

Per avviare la procedura:

```{list-table}
:widths: 5 95

* - **1.**
  - Recarsi nella sezione **Setup** del software FlexiVision

* - **2.**
  - Cliccare sul pulsante **FlexiBowl Setup**, si aprirà una pagina con tutti i FlexiBowl gestibili con FlexiVision Easy

* - **3.**
  - Cliccare sul pulsante **Config FlexiBowl**, si aprirà una pagina con tutte le movimentazioni disponibili per il FlexiBowl selezionato

* - **4.**
  - Cliccare sul pulsante **FlexiBowl X Wizard**, e poi **FlexiBowl Interface** si aprirà una pagina di benvenuto al Wizard

* - **5.**
  - Cliccare su NEXT
    
    :::{note}
    Cliccare "NEXT" in ogni pagina del wizard per andare avanti nella configurazione guidata
    :::
```

## **Step 2: Selezione Modello e Rotazione**

In questa fase si definiscono le caratteristiche hardware del sistema:
```{list-table}
* - 6. 
  - Selezionare la taglia del dispositivo (es. 200, 350, 500, ecc.).
* - 7. 
  - Definire il senso di rotazione del disco (**Clockwise** o **CounterClockwise**).
```
## **Step 3: Caratterizzazione del Componente**

Il sistema richiede informazioni sulla morfologia dei pezzi per ottimizzare la separazione.
```{list-table}
* - 8. 
  - Selezionare la geometria che meglio descrive il componente:
      * **FLAT**: Componenti piatti.
      * **CYLINDRICAL**: Componenti cilindrici.
      * **COMPLEX**: Geometrie articolate o irregolari.
* - 9. 
  - Definire come i componenti interagiscono tra loro sulla superficie:
      * **Overlapping**: I pezzi tendono a sovrapporsi.
      * **Not Overlapping**: I pezzi non si sovrappongono.
      * **Tangling / Stacking**: I pezzi tendono ad agganciarsi o impilarsi.
      * **Not Tangling / Not Stacking** : I pezzi rimangono separati e non si incastrano
```
## **Step 4: Test degli Accessori**
```{list-table}
* - 10. 
  - Selezionare dal menu a tendina se il FlexiBowl® è equipaggiato con il modulo **Air-blow**.
* - 11. 
  - Cliccare su **TEST Air-blow** per verificare il funzionamento.
* - 12. 
  - Selezionare **USE** per abilitarlo nell'applicazione corrente, altrimenti cliccare su **DON'T USE**.
* - 13. 
  - Cliccare su **TEST FLIP** per verificare la vibrazione.
      Il "Flip" è l'unità che genera l'impulso meccanico per ribaltare i pezzi, è fondamentale per separare, districare o capovolgere i componenti durante il ciclo di alimentazione.
 
      :::{important}
      Se l'impulso non è avvertibile, verificare che l'aria compressa sia collegata e agire sul regolatore di pressione meccanico posto sul pannello di controllo.
      :::
* - 14. 
  - Al termine del Wizard, cliccando su **FINISH**, il sistema calcolerà automaticamente i parametri: 
    - Parametri di movimento (velocità, accelerazione, angolo)
    - Parametri di scuotimento (shake)
    - Temporizzazioni accessori (flip, blow)
* - 15. 
  - Sarà quindi possibile affinarli nella dashboard riassuntiva.
```

```{list-table} Panoramica Parametri
   :widths: 20 30 50
   :header-rows: 1

   * - Gruppo
     - Parametro
     - Descrizione
   * - **Move**
     - Accel, Decel, Speed, Angle
     - Parametri del movimento principale del disco.
   * - **Option**
     - Flip Count, Flip Delay, Blow Time
     - Gestione dei tempi di attivazione degli accessori.
   * - **Shake**
     - Accel, Speed, Angle CW/CCW
     - Parametri della vibrazione di scuotimento (separazione).
```

## **Step 5: Validazione della Sequenza**

Utilizzare la funzione **Test Sequence** per verificare che il ciclo rispetti i seguenti criteri di efficienza:
```{list-table}
:widths: 5 95
:header-rows: 0

* - **Sincronizzazione**
  - L'impulso di Flip deve terminare esattamente nello stesso istante in cui termina il movimento (*Move*). Regolare i valori di *Flip Count* e *Delay* per allinearli.

* - **Stabilità Immagine**
  - I componenti devono essere immobili al momento dello scatto della camera.
    - Se i pezzi si muovono, diminuire velocità/accelerazione o inserire una pausa (es. `pause 200ms`).
    - Se il problema persiste, la superficie del disco (superficie di grip) potrebbe non essere corretta.

* - **Regolazione Soffio**
  - 
    - **Tip**: Usare preferibilmente il soffio *pre-flip* per sparpagliare i pezzi.
    - Usare il soffio *post-flip* (che raggruppa i pezzi) solo se strettamente necessario per cicli molto veloci.
    
    :::{warning}
    Cliccare sempre su **Synchronize Parameters** dopo ogni modifica manuale per rendere attive le variazioni nel controller.
    :::
```

## Strategie per problemi comuni

**Troubleshooting configurazione**

| **Problema** | **Soluzione** |
|--------------|---------------|
| Pezzi non si separano | Aumentare Flip Count, incrementare Shake Accel, abilitare Air-blow Pre-Flip |
| Pezzi vengono espulsi dal disco | Ridurre Speed, ridurre Accel, ridurre Blow Time |
| Ciclo troppo lento | Aumentare Speed, ridurre Angle (rotazione più breve), ottimizzare Flip timing |
| Pezzi rimangono aggregati in mucchi | Aumentare Shake Speed, incrementare Flip Count, usare Air-blow Pre-Flip |
| Immagini sfocate (pezzi in movimento) | Ridurre Speed/Accel, aggiungere pause, verificare superficie grip |

## Prossimi Passi

Una volta completata la configurazione del FlexiBowl, procedere con:

**→ [Configurazione Hopper](23_Config_Hopper.md)** - Se presente tramoggia esterna

**→ [Verifica Risultati](24_Verifica_Risultati.md)** - Monitoraggio applicazione completa

```{tip}
**Test produzione**

Prima di utilizzare in produzione:
1. Eseguire 50-100 cicli di test per verificare consistenza
2. Monitorare tasso di riempimento disco (deve essere costante)
3. Verificare che non ci siano accumuli anomali o zone vuote persistenti
4. Annotare eventuali necessità di regolazione fine
5. Incrementare gradualmente verso velocità produttiva

La configurazione ottimale può richiedere 2-3 sessioni di fine-tuning con il pezzo reale in quantità significativa.
```