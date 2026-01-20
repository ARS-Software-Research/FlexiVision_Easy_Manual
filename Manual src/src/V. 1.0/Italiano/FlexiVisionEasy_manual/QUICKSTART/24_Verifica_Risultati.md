
# Monitoraggio Applicazione: Dashboard

La **Dashboard** è l'interfaccia principale per il monitoraggio in tempo reale del sistema FlexiVision. In questa pagina è possibile verificare l'efficienza del processo, analizzare i tempi di ciclo e validare il riconoscimento dei componenti.

```{note}
   Il numero di componenti visualizzati nel riquadro *Detected Vision Parts* dipende direttamente dai parametri di comunicazione configurati in **Protocol Setup**.
```

## Descrizione dell'Interfaccia

L'interfaccia si divide in sezioni operative, dati analitici e grafici di performance.

### Controllo Operativo

```{list-table} Comandi e Stato di Esecuzione
   :widths: 25 75
   :header-rows: 1

   * - Elemento
     - Descrizione
   * - **In Run**
     - Indicatore di stato che segnala se il sistema è attualmente in funzione (Verde) o arrestato (Rosso).
   * - **In Run Time**
     - Visualizza il tempo totale di attività del sistema dalla pressione del tasto Start.
   * - **Selettore FlexiBowl**
     - Menu a tendina per selezionare l'unità FlexiBowl® specifica da monitorare in sistemi multi-dispositivo.
   * - **Test**
     - Avvia un ciclo continuo di movimentazione (disco e tramoggia) fino al rilevamento dei componenti nell'area di visione.
   * - **One Run**
     - Esegue un singolo ciclo: movimentazione disco, acquisizione immagine e analisi dei dati del modello.
```
--- 

### Analisi del Riconoscimento (Visione)

Al centro della dashboard vengono riportati i dati relativi ai componenti identificati dal sistema di visione:

```{list-table}
* - **Detected Vision Parts**: Visualizza l'immagine acquisita con l'overlay dei componenti riconosciuti. Include un grafico dello storico dei rilevamenti negli ultimi 30 secondi.
* - **Tabella Modelli Rilevati**: Elenco dettagliato dei componenti presenti nell'area di pick con i relativi parametri:

  - **X / Y**: Coordinate cartesiane del componente nel sistema di riferimento.
  - **Rot (Rotation)**: Angolo di rotazione del componente rispetto all'orientamento del modello originale.
  - **Score**: Valore percentuale che esprime il grado di affidabilità del riconoscimento (vicinanza al modello di riferimento).
```

### Indicatori di Stato e Performance

#### Connettività

* **FlexiBowl**: Stato della connessione hardware tra il PC di visione e il controller del FlexiBowl®.
* **Robot**: Stato della comunicazione con il robot o PLC incaricato del prelievo.

#### Analisi dei Tempi 

Il sistema fornisce un breakdown dettagliato dei tempi di ciclo per individuare eventuali colli di bottiglia:

```{list-table} Distribuzione dei Tempi di Processo
   :widths: 30 70
   :header-rows: 1

   * - Voce
     - Descrizione
   * - **Camera Processing Time**
     - Tempo impiegato per l'acquisizione dell'immagine dal sensore.
   * - **Locator Processing Time**
     - Tempo necessario all'algoritmo di visione per localizzare i componenti.
   * - **Total Vision Processing**
     - Somma dei tempi di Camera e Locator.
   * - **Total FlexiBowl Time**
     - Tempo impiegato dal sistema per eseguire una sequenza di movimentazione completa.
   * - **Total Robot Time**
     - Tempo stimato o rilevato per l'operazione di Pick & Place.
   * - **Total Processing Time**
     - Tempo totale del ciclo (Visione + FlexiBowl + Robot).
```

#### Analisi Grafica 

I grafici nella parte inferiore della dashboard permettono un'analisi predittiva e diagnostica:

1. **Parts Per Minute (PPM)**: Mostra la produttività media del sistema espressa in componenti prelevati al minuto.
2. **Fill Hopper**: Rappresenta lo storico degli impulsi di scarico inviati alla tramoggia, utile per monitorare l'autonomia del magazzino componenti.
3. **Vision - FlexiBowl - Robot**: Un grafico comparativo a tre funzioni che sovrappone i tempi dei singoli processi.
   
```{tip}
      Questo grafico è fondamentale per il tuning: permette di capire istantaneamente quale processo (visione, meccanica o movimentazione robot) sta influenzando maggiormente il tempo di ciclo totale.
```

```{important}
   Assicurarsi che lo **Score** dei componenti sia costantemente sopra la soglia di tolleranza impostata per evitare scarti o mancate prese da parte del robot.
```
