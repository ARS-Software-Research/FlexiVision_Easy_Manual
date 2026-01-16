# Creare un Nuovo Modello

```{admonition} In questa pagina
:class: tip
Imparerai a creare un modello di riferimento per il riconoscimento dei componenti.
```

## Fase 1: Preparazione del Setup Fisico

### Posizionamento Iniziale

**Step 1-3: Preparazione Robot**
1. Posizionare un componente al centro dell'area di visione
2. Dal **pendant del robot**:
   - Selezionare il **frame** e il **tool** calibrato su FlexiVision
   - Portare l'**ultimo asse** del tool a **rotazione zero** (Rz = 0°)
3. Rimuovere temporaneamente il componente

**Step 4-6: Posizionamento Componente**
4. Portare il robot a livello della superficie
5. Riposizionare il componente e afferrarlo con la pinza
6. Aprire e chiudere la pinza **2-3 volte** per centrare il componente

### Simulazione Ingombro Pinza

**Step 7: Oggetti Laterali**
7. Posizionare **due oggetti** ai lati del componente per simulare l'ingombro della pinza

```{warning}
Importante: Lasciare gli oggetti leggermente più distanti del necessario per evitare errori nella creazione del modello.
```

### Salvataggio Coordinate

**Step 8: Annotare le Coordinate**
8. Salvare le coordinate dell'ultimo asse del robot:
   - **X** (coordinata X)
   - **Y** (coordinata Y)  
   - **Rz** (rotazione attorno a Z)

```{danger}
⚠️ IMPORTANTE: Annotare queste coordinate! Saranno indispensabili nella fase di calibrazione robot.
```

**Step 9: Rimozione Robot**
9. Allontanare il robot con il pendant **senza spostare nulla** sulla superficie

---

## Fase 2: Creazione del Modello in FlexiVision

### Accesso alla Funzione Train Model

**Step 1-3: Apertura Editor**
1. Aprire **Edit Recipe**
2. Selezionare il **FlexiBowl**
3. Selezionare il **modello** → si aprirà la pagina **Train Model**

### Parametri Train Model

| Parametro | Funzione |
|-----------|----------|
| **Enable Model** | Attiva il modello |
| **Grab Train Image** | Scatta la foto di riferimento |
| **Feature Threshold** | Regola il livello di dettaglio |
| **Apply Train** | Genera il modello |
| **Name Model** | Assegna un nome al modello |

### Procedura di Training

**Step 4: Attivazione**
4. Cliccare su **Enable Model**

**Step 5: Acquisizione Immagine**
5. Cliccare su **Grab Train Image**

**Step 6-7: Posizionamento ROI**
6. Spostare il **riquadro ROI** per inquadrare completamente il componente
7. Spostare l'**origine** (punto di riferimento) al centro dell'area del riquadro

**Step 8: Regolazione Dettaglio**
8. Usare il **Feature Threshold** per regolare il livello di dettaglio

```{admonition} Feature Threshold
:class: note
- **Valore vicino a 0** → Rileva PIÙ dettagli (modello più preciso)
- **Valore vicino a 1** → Rileva MENO dettagli (modello più semplice)
```

**Step 9: Generazione Modello**
9. Cliccare su **Apply Train**

---

## Verifica Qualità del Modello

**Step 10: Controllo Visivo**
10. Fare **Zoom** e verificare che il modello sia corretto

### ✅ Un Modello Corretto Deve:

```{admonition} Caratteristiche Modello Valido
:class: success
- ✓ Avere abbastanza linee per riconoscere il componente
- ✓ Non includere la trama della superficie retrostante
- ✓ Evitare riflessi di luce
- ✓ Escludere gli oggetti usati per simulare l'ingombro della pinza
```

### 🔧 Correzione del Modello

**Step 11: Ottimizzazione (se necessario)**
Se il modello non è soddisfacente:
- Modificare il **Feature Threshold**
- Cliccare nuovamente su **Apply Train**
- Ripetere fino a ottenere un modello ottimale

---

## Finalizzazione

**Step 12-13: Salvataggio**
12. Nominare il modello con un nome descrittivo
13. Cliccare su **Next** → si aprirà la pagina **Define Robot Pick Area**

```{seealso}
Procedi alla [Definizione ROI](#pagina-4-definizione-roi) per continuare la configurazione.
```

---
---

```{toctree}  
18b_Expert.md
```