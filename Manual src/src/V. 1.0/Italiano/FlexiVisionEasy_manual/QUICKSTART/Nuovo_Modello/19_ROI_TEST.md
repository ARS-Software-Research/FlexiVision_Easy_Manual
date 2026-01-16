# Definizione ROI e Tolleranze

```{admonition} In questa pagina
:class: tip
Definirai l'area di lavoro e le tolleranze di riconoscimento per il modello.
```

## Parte 1: Define Robot Pick Area

### Cos'è la Region Search?
La **Region Search** è l'area all'interno della quale FlexiVision cercherà e rileverà i componenti da prelevare.

### Procedura

**Step 1: Definizione Area**
1. Nella pagina **Define Robot Pick Area**, modificare il riquadro per delimitare l'area di ricerca
2. Cliccare su **Next** → si aprirà la pagina **Locator Model**

```{tip}
Dimensiona l'area in base allo spazio effettivo di lavoro del robot, evitando zone non raggiungibili.
```

---

## Parte 2: Locator Model - Impostazione Tolleranze

### Parametri Principali

| Parametro | Descrizione |
|-----------|-------------|
| **Test** | Esegue un test di riconoscimento |
| **Accept Threshold** | Soglia minima di fedeltà (score) |

### Procedura di Test

**Step 1: Preparazione Scena**
1. Posizionare **altri componenti** nell'area di visione
   
```{warning}
Non toccare il componente di riferimento usato per il training!
```

**Step 2: Esecuzione Test**
2. Cliccare su **Test** per verificare il riconoscimento

---

## Configurazione Accept Threshold

### Cos'è l'Accept Threshold?
È il **grado minimo di fedeltà** (score) che un componente rilevato deve avere rispetto al modello di riferimento per essere accettato.

### Come Funziona

```{admonition} Logica dello Score
:class: note
- **Valore 0.95** → Accetta solo componenti con fedeltà ≥ 95%
- **Valore 0.80** → Accetta componenti con fedeltà ≥ 80%
- **Valore più alto** → Più restrittivo (meno falsi positivi)
- **Valore più basso** → Più permissivo (rileva anche componenti meno perfetti)
```

**Step 3: Regolazione Soglia**
3. Modificare l'**Accept Threshold** in base alle esigenze dell'applicazione

---

## Interpretazione Risultati

### Visualizzazione Componenti Rilevati

Nel riquadro verranno mostrati i componenti con le seguenti informazioni:

| Campo | Descrizione |
|-------|-------------|
| **Id** | Identificativo univoco (0 = score più alto) |
| **X, Y** | Coordinate del componente |
| **Rotation** | Angolo di rotazione |
| **Score** | Percentuale di fedeltà al modello |

### Ordinamento Automatico

```{admonition} Sistema di Priorità
:class: info
FlexiVision ordina automaticamente tutti i componenti riconosciuti per **score decrescente**:
- **Id 0** → Componente con score più alto (più fedele al modello)
- **Id 1** → Secondo miglior componente
- **Id 2** → Terzo miglior componente
- E così via...
```

---

## Finalizzazione

**Step 4-5: Pulizia e Proseguimento**
4. Rimuovere **tutti i componenti** dall'area, **tranne il componente di riferimento**
5. Cliccare su **Next** → si aprirà la pagina degli **Histogram**

```{seealso}
Procedi alla [Configurazione Istogrammi](#pagina-5-configurazione-istogrammi) per definire le aree libere.
```

---
---
```{toctree}  
19b_Expert.md
```