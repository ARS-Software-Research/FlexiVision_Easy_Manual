# Gli istogrammi 
Configurazione Istogrammi

```{admonition} In questa pagina
:class: tip
Imparerai a configurare gli istogrammi per verificare che le aree critiche siano libere da ostacoli.
```

## Cos'è un Istogramma?

Un **istogramma** in FlexiVision è uno strumento che monitora un'area specifica dell'immagine per verificare che sia libera. Viene utilizzato per controllare, ad esempio, che lo spazio necessario alla pinza per afferrare il componente non sia occupato da altri oggetti.

### Funzionamento

```{admonition} Principio di Funzionamento
:class: note
L'istogramma analizza i livelli di bianco e nero in un'area definita:
- 🟢 **Verde** → Area libera (OK per il prelievo)
- 🔴 **Rosso** → Area occupata (presenza di ostacoli)
```

---

## Creazione Istogrammi

### Accesso alla Funzione

Dalla pagina **Locator Model**, dopo aver cliccato su **Next**, si aprirà l'elenco degli istogrammi disponibili (fino a 8 per modello).

### Parametri Principali

| Parametro | Funzione |
|-----------|----------|
| **Enable Histogram** | Attiva l'istogramma |
| **Expression Builder** | Configura automaticamente le soglie |
| **Mean and Standard Deviation** | Valori statistici dell'area |
| **Test** | Verifica il funzionamento |
| **Result** | Mostra il risultato (verde/rosso) |

---

## Procedura di Configurazione

### Istogramma Singolo

**Step 1: Selezione**
1. Cliccare su **Histogram 1**

**Step 2: Attivazione**
2. Cliccare su **Enable Histogram**

**Step 3: Posizionamento Area**
3. Spostare il **riquadro** dell'istogramma nell'area che deve rimanere libera
   - Tipicamente: area di presa della pinza
   - Margini attorno al componente
   - Zone di passaggio del robot

```{warning}
Importante: Creare sempre un istogramma leggermente più grande dello stretto necessario per evitare falsi errori.
```

**Step 4: Configurazione Automatica**
4. Cliccare su **AUTO** in Expression Builder

**Step 5: Verifica**
5. Cliccare su **TEST**
6. Verificare che il riquadro diventi **verde** ✅

**Step 6: Conferma**
7. Cliccare su **Next**

---

## Istogrammi Multipli

### Quando Usarli

Crea più istogrammi quando:
- La pinza ha una forma complessa
- Ci sono più punti critici da monitorare
- L'area di presa ha geometrie particolari

### Procedura

**Step 1-7: Ripetizione**
Ripetere la procedura per ogni istogramma necessario (fino a 8 per modello)

**Step 8: Test Complessivo**
8. Nella pagina di elenco di tutti gli istogrammi, cliccare su **TEST**
9. Visualizzare tutti gli istogrammi contemporaneamente

---

## Interpretazione Stati

### Stati dell'Istogramma

```{list-table}
:header-rows: 1
:widths: 15 35 50

* - Colore
  - Stato
  - Significato
* - 🟢 Verde
  - OK
  - Area libera, prelievo possibile
* - 🔴 Rosso
  - Triggered
  - Area occupata, prelievo non sicuro
```

### Cosa Significa "Triggered"?

Un istogramma diventa rosso (triggered) quando rileva al suo interno:
- Presenza di altri componenti
- Ombre o riflessi significativi
- Qualsiasi elemento che rende l'area non libera

```{admonition} Esempio Pratico
:class: example
**Scenario:** Pinza con larghezza di 20mm che deve afferrare un componente

**Soluzione:** Creare un istogramma di 25-30mm attorno al componente per assicurarsi che la pinza non urti altri pezzi durante la presa.
```

---

## Finalizzazione

**Step 10: Proseguimento**
10. Dopo aver configurato tutti gli istogrammi necessari, cliccare su **Next**
11. Si aprirà la pagina **Robot Model Pick Cam**

```{seealso}
Procedi alla [Calibrazione Robot](#pagina-6-calibrazione-robot-pick) per completare la configurazione.
```

---
---

```{toctree}  
20b_Expert.md
```