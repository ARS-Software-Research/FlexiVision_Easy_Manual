(nuovomodello)=
# **Creare un Nuovo Modello**

In questa pagina vedremo come creare un modello di riferimento per il riconoscimento dei componenti.


## **Step 1: Preparazione del Setup Fisico**

```{list-table}
* - 0. 
  - Smontare la griglia di calibrazione e ripristinare il layout iniziale:
    - Riposizionare la superficie
    - riposizionare la flangia centrale 
    - fissare la flangia centrale con le sue quattro viti
* - 1. 
  - Posizionare un oggetto al centro dell'area di visione
```
---

## **Step 2: Accesso al Modello** 

Completata la preparazione fisica, si procede con l'acquisizione dell'immagine e la creazione del modello

```{list-table}
* - 2. 
  - Dalla pagina "Recipes", con la giusta ricetta selezionata, cliccare su "Edit Recipe"
* - 3. 
  - Il sistema mostra gli slot disponibili per i modelli (fino a 8 modelli per ricetta)
* - 4. 
  - Cliccare sul **Modello 1** per accedere alla pagina "Train Model 1 Cam 1"
```

#### Panoramica interfaccia Train Model

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parametro
  - Funzione
* - **Enable Model**
  - Attiva questo slot di modello rendendolo utilizzabile
* - **Grab Train Image**
  - Scatta una foto del componente di riferimento per il training
* - **Feature Threshold**
  - Regola il livello di dettaglio del modello (da 0 = massimo dettaglio a 1 = minimo dettaglio)
* - **Apply Train**
  - Genera effettivamente il modello elaborando l'immagine acquisita
* - **Name Model**
  - Campo di testo per assegnare un nome descrittivo al modello
```

```{tip}
**Gestione modelli multipli**

In questa fase si attiva solo il primo modello. Dopo averlo completato, sarà possibile:
- Abilitare slot aggiuntivi (Modello 2, Modello 3, ecc.) per pezzi diversi nella stessa ricetta
- Modificare modelli esistenti
- Disabilitare modelli non più necessari

Per ora, concentrarsi sul completamento del primo modello.
```
---

## **Step 3: Procedura di Training**

```{video} video/TastoInfo_TrainModel_1280x720.mp4
:width: 100%
:align: center 
```

```{list-table}
:widths: 5 95

* - **5. **
  - Cliccare su **Enable Model** per abilitare questo modello. Il modello è ora attivo e pronto per essere configurato.

* - **6.**
  - Cliccare su **Grab Train Image** per scattare una foto del componente di riferimento che abbiamo posizionato sul FlexiBowl
    
    :::{warning}
    Il componente di riferimento dovrà rimanere fermo in quel punto per tutto il processo di creazione dell'applicazione
    :::

* - **7.**
  - Spostare il **riquadro ROI** per inquadrare completamente il componente

* - **8.**
  - Spostare l'**origine** (punto di riferimento) al centro dell'area del riquadro
    
    :::{tip}
    **Dove posizionare l'origine?**
    
    - **Centro geometrico**: Per pezzi simmetrici (viti, rondelle, ingranaggi circolari)
    - **Punto di presa**: Per pezzi asimmetrici, posizionare dove la pinza afferra
    - **Feature caratteristica**: Per pezzi complessi, su una caratteristica distintiva
    
    *L'origine definisce il punto (0,0) del sistema di coordinate del modello.*
    :::

* - **9.**
  - Usare il **Feature Threshold** per regolare il livello di dettaglio desiderato
    
    :::{note}
    **Feature Threshold**
    
    **Valore vicino a 0** → Rileva PIÙ dettagli (modello più preciso)
    
    **Valore vicino a 1** → Rileva MENO dettagli (modello più semplice)
    :::
    
    :::{tip}
    **Come scegliere il Feature Threshold ottimale?**
    
    **Usare valore BASSO (0.1-0.3) quando:**
    - Il pezzo ha molti dettagli distintivi (incisioni, loghi, texture)
    - I pezzi sono sempre molto simili tra loro (tolleranze strette)
    - Si vuole massima precisione anche con orientamenti difficili
    
    **Usare valore MEDIO (0.4-0.6) quando:**
    - Il pezzo ha forma distintiva ma semplice
    - Si desidera equilibrio tra precisione e tolleranza
    - Prima configurazione di un modello (punto di partenza)
    
    **Usare valore ALTO (0.7-0.9) quando:**
    - Il pezzo ha forma molto semplice (cerchi, quadrati)
    - Ci sono variazioni significative tra i pezzi (tolleranze larghe)
    - La superficie del pezzo è molto riflettente o variabile
    :::

* - **10.**
  - Cliccare su **Apply Train**
```
---

## **Step 4: Controllo Visivo**

Dopo aver generato il modello, è fondamentale verificarne la qualità prima di procedere.

````{list-table}

* - **11.**
  - Fare **Zoom** sull'immagine per ispezionare i dettagli del modello creato e verificare che il modello sia corretto
    
    :::{tip}
      **Caratteristiche Modello Valido**
      ✓ Avere abbastanza linee per riconoscere il componente
      ✓ Non includere la trama della superficie retrostante
      ✓ Evitare riflessi di luce
      ✓ Escludere gli oggetti usati per simulare l'ingombro della pinza
    :::

    :::{figure} img/modello_corretto_vs_errato.png
        :alt: Confronto modello corretto e errato
        :width: 100%
        :align: center
        
        A sinistra: modello corretto (solo contorni pezzo). A destra: modello errato (include trama superficie e riflessi).
    :::
````

```{attention}
Se il modello non è soddisfacente:
- Modificare il **Feature Threshold**
- Cliccare nuovamente su **Apply Train**
- Ripetere fino a ottenere un modello ottimale
```

```{tip}
**Strategia di ottimizzazione**

**Problema: Modello include trama superficie**
→ Soluzione: Aumentare Feature Threshold (es: da 0.4 a 0.6)

**Problema: Modello ha troppo poche linee, non distintivo**
→ Soluzione: Diminuire Feature Threshold (es: da 0.6 a 0.4)

**Problema: Modello include riflessi**
→ Soluzione: Aumentare Feature Threshold oppure regolare esposizione camera

Effettuare modifiche graduali (step di 0.1-0.2) e testare ogni volta.
```
---

## **Step 5: Salvataggio**
```{list-table}
* - 12. 
  - Nominare il modello con un nome descrittivo  
* - 13. 
  - Cliccare su **Next** → si aprirà la pagina **Define Robot Pick Area**  
```

```{seealso}
Procedi alla [Definizione ROI](roitest) per continuare la configurazione.
```
```{toctree}  
18b_Expert.md
```