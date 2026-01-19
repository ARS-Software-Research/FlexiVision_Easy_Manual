# Creare un Nuovo Modello

```{admonition} In questa pagina
:class: tip
Imparerai a creare un modello di riferimento per il riconoscimento dei componenti.
```

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

### **Step 3: Simulazione Ingombro Pinza**
7. Posizionare **due oggetti** ai lati del componente per simulare l'ingombro della pinza

```{important}
Lasciare gli oggetti leggermente più distanti del necessario per evitare errori nella creazione del modello.
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

Dopo la configurazione iniziale, il wizard propone di creare il primo modello:

### **Step 6: Abilitazione modello**

10. Dalla pagina "Recipes", con la giusta ricetta selezionata, cliccare su "Edit Recipe"
11. Il sistema mostra gli slot disponibili per i modelli (fino a 8 modelli per ricetta)
12. Cliccare sul **Modello 1** per accedere alla pagina "Train Model 1 Cam 1"
13. Cliccare su **Enable Model** per abilitare questo slot. Il modello è ora attivo e pronto per essere configurato.

```{tip}
**Gestione modelli multipli**

In questa fase si attiva solo il primo modello. Dopo averlo completato, sarà possibile:
- Abilitare slot aggiuntivi (Modello 2, Modello 3, ecc.) per pezzi diversi nella stessa ricetta
- Modificare modelli esistenti
- Disabilitare modelli non più necessari

Per ora, concentrarsi sul completamento del primo modello.
```

#### Parametri Train Model

| Parametro | Funzione |
|-----------|----------|
| **Enable Model** | Attiva il modello |
| **Grab Train Image** | Scatta la foto di riferimento |
| **Feature Threshold** | Regola il livello di dettaglio |
| **Apply Train** | Genera il modello |
| **Name Model** | Assegna un nome al modello |

### **Step 7: Procedura di Training**

14. Cliccare su **Grab Train Image** per scattare una foto del componente di riferimento che abbiamo posizionato sul FlexiBowl

```{warning}
il componente di riferimento dovrà rimanere fermo in quel punto per tutto il processo di creazione dell'applicazione
```

15. Spostare il **riquadro ROI** per inquadrare completamente il componente
16. Spostare l'**origine** (punto di riferimento) al centro dell'area del riquadro
17. Usare il **Feature Threshold** per regolare il livello di dettaglio desiderato

```{admonition} Feature Threshold
:class: note
- **Valore vicino a 0** → Rileva PIÙ dettagli (modello più preciso)
- **Valore vicino a 1** → Rileva MENO dettagli (modello più semplice)
```
18. Nominare il modello
19. Cliccare su **Apply Train**

---

## Fase 3: Finalizzazione

### **Step 8: Controllo Visivo**
20. Fare **Zoom** e verificare che il modello sia corretto


```{admonition} Caratteristiche Modello Valido
:class: success
- ✓ Avere abbastanza linee per riconoscere il componente
- ✓ Non includere la trama della superficie retrostante
- ✓ Evitare riflessi di luce
- ✓ Escludere gli oggetti usati per simulare l'ingombro della pinza
```

### **Step 9: Ottimizzazione (se necessario)**
Se il modello non è soddisfacente:
- Modificare il **Feature Threshold**
- Cliccare nuovamente su **Apply Train**
- Ripetere fino a ottenere un modello ottimale


### **Step 10: Salvataggio**
21. Nominare il modello con un nome descrittivo  
22. Cliccare su **Next** → si aprirà la pagina **Define Robot Pick Area**  

```{seealso}
Procedi alla [Definizione ROI](Nuovo_Modello/19_ROI_TEST.md) per continuare la configurazione.
```


```{toctree}  
18b_Expert.md
```