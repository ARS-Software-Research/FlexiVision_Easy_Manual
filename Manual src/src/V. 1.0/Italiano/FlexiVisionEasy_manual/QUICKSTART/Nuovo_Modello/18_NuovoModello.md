# **Creare un Nuovo Modello**

In questa pagina vedremo come creare un modello di riferimento per il riconoscimento dei componenti.


## Fase 1: Preparazione del Setup Fisico

### **Step 1: Preparazione Robot**
1. Posizionare un componente al centro dell'area di visione
2. Dal **pendant del robot**:
   - Selezionare il **frame** e il **tool** calibrato su FlexiVision
   - Portare l'**ultimo asse** del tool a **rotazione zero** (Rz = 0°)
3. Rimuovere temporaneamente il componente

### **Step 2: Posizionamento Componente**   
4. Portare il robot a livello della superficie  
5. Riposizionare il componente e afferrarlo con la pinza  
6. Aprire e chiudere la pinza **2-3 volte** per centrare il componente  

```{tip}
**Perché centrare il pezzo?**

Aprire/chiudere la pinza più volte permette al pezzo di "assestarsi" nella posizione di presa ottimale. Questo:
- Compensa piccole imprecisioni nel posizionamento manuale
- Simula la presa reale che il robot farà in produzione
- Garantisce che le coordinate salvate corrispondano alla presa effettiva
```

### **Step 3: Simulazione Ingombro Pinza**
7. Posizionare **due oggetti** ai lati del componente per simulare l'ingombro della pinza (ai lati della pinza per avere, una volta rimosso il robot, l'area libera fra il componente di riferimento e i due oggetti rappresenterà l'area di ingombro della pinza del robot)

```{important}
Lasciare gli oggetti leggermente più distanti del necessario per evitare errori nella creazione del modello. (margine 2-3 mm)
``` 
```{figure} img/simulazione_ingombro_pinza.png
:alt: Simulazione ingombro pinza
:width: 70%
:align: center

Esempio di posizionamento simulatori ingombro pinza. Nota il margine di sicurezza lasciato tra pezzo e simulatori.
```

### **Step 4: Annotare le Coordinate**
8. Salvare le coordinate dell'ultimo asse del robot:
   - **X** (coordinata X)
   - **Y** (coordinata Y)  
   - **Rz** (rotazione attorno a Z)

```{important}
 Annotare queste coordinate! Saranno indispensabili nella fase di calibrazione robot.
```

### **Step 5: Rimozione Robot**
9. Allontanare il robot con il pendant **senza spostare nulla** sulla superficie

---

## Fase 2: Creazione del Modello in FlexiVision

Completata la preparazione fisica, si procede con l'acquisizione dell'immagine e la creazione del modello

### **Step 6: Abilitazione modello**

10. Dalla pagina "Recipes", con la giusta ricetta selezionata, cliccare su "Edit Recipe"
11. Il sistema mostra gli slot disponibili per i modelli (fino a 8 modelli per ricetta)
12. Cliccare sul **Modello 1** per accedere alla pagina "Train Model 1 Cam 1"
13. Cliccare su **Enable Model** per abilitare questo modello. Il modello è ora attivo e pronto per essere configurato.

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

### **Step 7: Procedura di Training**

14. Cliccare su **Grab Train Image** per scattare una foto del componente di riferimento che abbiamo posizionato sul FlexiBowl

```{warning}
il componente di riferimento dovrà rimanere fermo in quel punto per tutto il processo di creazione dell'applicazione
```

15. Spostare il **riquadro ROI** per inquadrare completamente il componente
16. Spostare l'**origine** (punto di riferimento) al centro dell'area del riquadro

```{tip}
**Dove posizionare l'origine?**

- **Centro geometrico**: Per pezzi simmetrici (viti, rondelle, ingranaggi circolari)
- **Punto di presa**: Per pezzi asimmetrici, posizionare dove la pinza afferra
- **Feature caratteristica**: Per pezzi complessi, su una caratteristica distintiva

L'origine definisce il punto (0,0) del sistema di coordinate del modello.
```

17. Usare il **Feature Threshold** per regolare il livello di dettaglio desiderato

```{admonition} Feature Threshold
:class: note
- **Valore vicino a 0** → Rileva PIÙ dettagli (modello più preciso)
- **Valore vicino a 1** → Rileva MENO dettagli (modello più semplice)
```
```{tip}
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
```

18. Nominare il modello
19. Cliccare su **Apply Train**

---

## Fase 3: Verifica e Ottimizzazione

Dopo aver generato il modello, è fondamentale verificarne la qualità prima di procedere.

### **Step 8: Controllo Visivo**
20. Fare **Zoom** sull'immagine per ispezionare i dettagli del modello creato e verificare che il modello sia corretto


```{admonition} Caratteristiche Modello Valido
:class: success
- ✓ Avere abbastanza linee per riconoscere il componente
- ✓ Non includere la trama della superficie retrostante
- ✓ Evitare riflessi di luce
- ✓ Escludere gli oggetti usati per simulare l'ingombro della pinza
```
```{figure} img/modello_corretto_vs_errato.png
:alt: Confronto modello corretto e errato
:width: 100%
:align: center

A sinistra: modello corretto (solo contorni pezzo). A destra: modello errato (include trama superficie e riflessi).
```


### **Step 9: Ottimizzazione (se necessario)**
Se il modello non è soddisfacente:
- Modificare il **Feature Threshold**
- Cliccare nuovamente su **Apply Train**
- Ripetere fino a ottenere un modello ottimale

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


### **Step 10: Salvataggio**
21. Nominare il modello con un nome descrittivo  
22. Cliccare su **Next** → si aprirà la pagina **Define Robot Pick Area**  

```{seealso}
Procedi alla [Definizione ROI](Nuovo_Modello/19_ROI_TEST.md) per continuare la configurazione.
```


```{toctree}  
18b_Expert.md
```