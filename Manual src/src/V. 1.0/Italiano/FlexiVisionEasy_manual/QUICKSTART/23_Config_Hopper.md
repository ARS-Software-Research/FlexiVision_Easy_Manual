
# Configurazione della Tramoggia (Hopper)

La configurazione della tramoggia permette di gestire il rifornimento automatico dei componenti sul disco del FlexiBowl®. Il sistema utilizza la visione artificiale per determinare quando il livello di riempimento è insufficiente e attivare la vibrazione di scarico.

## Accesso alla Configurazione

1. Cliccare sulla sezione "SETUP"
2. Dalla sezione **Hopper Setup**, è possibile visualizzare e gestire le unità di carico collegate.
3. Selezionare la casella **Enable Hopper X** per attivare la tramoggia corrispondente.
4. Cliccare sul pulsante **Config Hopper X** per accedere alla configurazione specifica 

### **Step 1: Definizione dell'Area di Controllo**

In questa fase si definisce la porzione di disco che la telecamera deve monitorare per lo scarico.

5. Modificare il riquadro blu a schermo per inquadrare l'area in cui verranno rilevati i componenti.

 **Strumenti di supporto**:
   * **Info**: Cliccare per visualizzare dettagli sulle funzionalità della pagina.
   * **Expert**: Accesso a impostazioni avanzate.

### **Step 2: Definizione dei Valori di Soglia**

6. Nella pagina **Define Value Hopper Cam**, si istruisce il sistema a distinguere tra disco vuoto e disco pieno.
7. Rimuovere tutti i componenti dall'area di visione e cliccare sul primo pulsante **CAPTURE**.
8. Posizionare il numero minimo di componenti che si desidera mantenere sul disco. Se il numero scende sotto questa soglia, la tramoggia si attiverà.
9. Cliccare sul secondo pulsante **CAPTURE**.
10. Cliccando su **AUTO** nell'Expression Builder, il sistema calcola automaticamente i valori di **Mean** (Media) e **Standard Deviation**.
11. Rimuovere alcuni pezzi e cliccare su **TEST**. L'indicatore diventa **Verde** se la tramoggia si attiva (scarico necessario), **Rosso** altrimenti.

### **Step 3: Parametri Operativi**

Tornare alla schermata principale di Hopper Setup per definire il comportamento meccanico.

```{list-table} Parametri di Funzionamento
   :widths: 20 80
   :header-rows: 1

   * - Parametro
     - Descrizione e Procedura
   * - **Steps**
     - Numero di sequenze necessarie per portare i pezzi dallo scarico all'area di prelievo. Per calcolarlo: svuotare il disco, eseguire la sequenza e contare quanti cicli servono perché i pezzi arrivino alla camera.
   * - **Time**
     - Millisecondi di vibrazione della tramoggia. Valore consigliato: **100 - 1000 ms** (Media: **500 ms**). Regolare di +/- 100 ms in base al flusso desiderato.
```

```{tip}
   Il tempo di vibrazione dipende non solo dal valore impostato, ma anche dal volume di componenti attualmente presenti nella vasca della tramoggia. È essenziale mantenere un carico costante per un flusso uniforme.
```

```{important}
   **Salvataggio della Ricetta**: Al termine di ogni blocco di modifiche, è fondamentale **Salvare la Ricetta**. Ogni variazione apportata viene memorizzata solo se la ricetta viene salvata correttamente prima di uscire o cambiare pagina.
```