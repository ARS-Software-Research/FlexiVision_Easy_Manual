
# **Configurazione guidata: FlexiBowl® Wizard**


L'interfaccia **FlexiBowl® Wizard** è uno strumento interattivo progettato per guidare l'utente nella configurazione dei parametri di alimentazione in base alla specifica famiglia di prodotti da gestire.

## Accesso al Wizard

Per avviare la procedura:
1. recarsi nella sezione **Setup** del software FlexiVision 
2. cliccare sul pulsante **FlexiBowl Setup**, si aprirà una pagina con tutti i FlexiBowl gestibili con FlexiVision Easy
3. cliccare sul pulsante **Config FlexiBowl**, si aprirà una pagina con tutte le movimentazioni disponibili per il flexibowl selezionato 
4. cliccare sul pulsante **FlexiBowl X Wizard**, si aprirà una pagina di benvenuto al Wizard
5. Cliccare su NEXT

```{note}
Cliccare "NEXT" in ogni pagina del wizard per andare avanti nella configurazione guidata
```

### **Step 1: Selezione Modello e Rotazione**

In questa fase si definiscono le caratteristiche hardware del sistema:

1. Selezionare la taglia del dispositivo (es. 200, 350, 500, ecc.).
2. Definire il senso di rotazione del disco (**Clockwise** o **CounterClockwise**).

### **Step 2: Caratterizzazione del Componente**

Il sistema richiede informazioni sulla morfologia dei pezzi per ottimizzare la separazione.

3. Selezionare la geometria che meglio descrive il componente:

* **FLAT**: Componenti piatti.
* **CYLINDRICAL**: Componenti cilindrici.
* **COMPLEX**: Geometrie articolate o irregolari.

4. Definire come i componenti interagiscono tra loro sulla superficie:

* **Overlapping**: I pezzi tendono a sovrapporsi.
* **Not Overlapping**: I pezzi non si sovrappongono.
* **Tangling / Stacking**: I pezzi tendono ad agganciarsi o impilarsi.
* **Not Tangling / Not Stacking** : I pezzi rimangono separati e non si incastrano

### **Step 3: Test degli Accessori**

5. Selezionare dal menu a tendina se il FlexiBowl® è equipaggiato con il modulo **Air-blow**.
6. Cliccare su **TEST Air-blow** per verificare il funzionamento.
7. Selezionare **USE** per abilitarlo nell'applicazione corrente, altrimenti cliccare su **DON'T USE**.

Il "Flip" è l'unità che genera l'impulso meccanico per ribaltare i pezzi.

8. Cliccare su **TEST FLIP** per verificare la vibrazione.
 
```{important}
Se l'impulso non è avvertibile, verificare che l'aria compressa sia collegata e agire sul regolatore di pressione meccanico posto sul pannello di controllo.
```
```{note}
   Il Flip è fondamentale per separare, districare o capovolgere i componenti durante il ciclo di alimentazione.
```

9. Al termine del Wizard, cliccando su **FINISH**, il sistema calcolerà automaticamente i parametri: 
    - Parametri di movimento (velocità, accelerazione, angolo)
    - Parametri di scuotimento (shake)
    - Temporizzazioni accessori (flip, blow)
10. Sarà quindi possibile affinarli nella dashboard riassuntiva.

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

### **Step 4: Validazione della Sequenza**

10. Utilizzare la funzione **Test Sequence** per verificare che il ciclo rispetti i seguenti criteri di efficienza:

1. **Sincronizzazione**: L'impulso di Flip deve terminare esattamente nello stesso istante in cui termina il movimento (*Move*). Regolare i valori di *Flip Count* e *Delay* per allinearli.
2. **Stabilità Immagine**: I componenti devono essere immobili al momento dello scatto della camera.
   * Se i pezzi si muovono, diminuire velocità/accelerazione o inserire una pausa (es. ``pause 200ms``).
   * Se il problema persiste, la superficie del disco (superficie di grip) potrebbe non essere corretta.
3. **Regolazione Soffio**:
   * **Tip**: Usare preferibilmente il soffio *pre-flip* per sparpagliare i pezzi. 
   * Usare il soffio *post-flip* (che raggruppa i pezzi) solo se strettamente necessario per cicli molto veloci.

```{warning}
   Cliccare sempre su **Synchronize Parameters** dopo ogni modifica manuale per rendere attive le variazioni nel controller.
```

### Strategie per problemi comuni

```{warning}
**Troubleshooting configurazione**

**Problema: Pezzi non si separano**
→ Soluzione: Aumentare Flip Count, incrementare Shake Accel, abilitare Air-blow Pre-Flip

**Problema: Pezzi vengono espulsi dal disco**
→ Soluzione: Ridurre Speed, ridurre Accel, ridurre Blow Time

**Problema: Ciclo troppo lento**
→ Soluzione: Aumentare Speed, ridurre Angle (rotazione più breve), ottimizzare Flip timing

**Problema: Pezzi rimangono aggregati in mucchi**
→ Soluzione: Aumentare Shake Speed, incrementare Flip Count, usare Air-blow Pre-Flip

**Problema: Immagini sfocate (pezzi in movimento)**
→ Soluzione: Ridurre Speed/Accel, aggiungere pause, verificare superficie grip
```
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