# **Gli istogrammi** 
 In questa pagina vedremo come configurare gli istogrammi per verificare che le aree critiche siano libere da ostacoli.

## Cos'è un Istogramma?

Un **istogramma** in FlexiVision è uno strumento che monitora un'area specifica dell'immagine per verificare che sia libera. Viene utilizzato per controllare, ad esempio, che lo spazio necessario alla pinza per afferrare il componente non sia occupato da altri oggetti.


```{admonition} Principio di Funzionamento. MEGLIO ANCHE QUI O SOLO DOPO?
:class: note
L'istogramma analizza i livelli di bianco e nero in un'area definita:
- 🟢 **Verde** → Area libera (OK per il prelievo)
- 🔴 **Rosso** → Area occupata (presenza di ostacoli)
```

---

## Creazione Istogrammi

Dalla pagina **Locator Model**, dopo aver cliccato su **Next**, si aprirà l'elenco degli istogrammi disponibili (fino a 8 per modello).

### Panoramica interfaccia

```{list-table}
:header-rows: 1
:widths: 30 70

* - Elemento
  - Descrizione
* - **Histogram 1...8**
  - Slot disponibili per creare fino a 8 istogrammi diversi per lo stesso modello
* - **Test (globale)**
  - Pulsante per testare simultaneamente tutti gli istogrammi abilitati
* - **Next**
  - Avanzamento alla fase successiva (Robot Pick) dopo configurazione istogrammi
```

---


### **Step 1: Selezione Istogramma**
1. Cliccare su **Histogram 1**, si aprirà la pagina relativa alla configurazione del primo istogramma "Histogram 1"

#### Panoramica interfaccia configurazione

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parametro
  - Funzione
* - **Enable Histogram**
  - Attiva questo istogramma rendendolo operativo
* - **Expression Builder**
  - Strumento per configurare automaticamente le soglie di rilevamento
* - **Mean and Standard Deviation**
  - Valori statistici calcolati sull'area selezionata (media e deviazione standard dei livelli di grigio)
* - **Test**
  - Verifica immediata del funzionamento dell'istogramma
* - **Result**
  - Indicatore visivo dello stato (Verde = OK, Rosso = Triggered)
```


### **Step 2: Attivazione e Posizionamento Area**
2. Cliccare su **Enable Histogram** per attivare l'istogramma 
3. Spostare il **riquadro** dell'istogramma nell'area che deve rimanere libera
   - Tipicamente: area di presa della pinza (un istogramma per ogni area di presa della pinza)
   - Margini attorno al componente
   - Zone di passaggio del robot

```{important}
 Creare sempre un istogramma leggermente più grande dello stretto necessario per evitare falsi errori.
```


### **Step 3: Configurazione Automatica**
4. Cliccare su **AUTO** in Expression Builder
5. Cliccare su **TEST**
6. Verificare che il riquadro diventi **verde** 
7. Cliccare su **Next**

```{warning}
**Cosa fare se il test fallisce (riquadro rosso)?**

Se dopo AUTO e TEST il riquadro rimane rosso:

**Possibili cause:**
- C'è effettivamente qualcosa nell'area (pezzo, ombra, sporcizia)
- L'illuminazione è variata tra configurazione AUTO e TEST
- L'area selezionata include bordi del FlexiBowl o artefatti

**Soluzioni:**
1. Verificare visivamente che l'area sia completamente libera
2. Pulire la superficie del FlexiBowl se necessario
3. Riposizionare leggermente il riquadro escludendo bordi/artefatti
4. Ripetere AUTO con condizioni di illuminazione stabili
5. Ripetere TEST per verificare
```

---

## Istogrammi Multipli

### Quando Usarli

Crea più istogrammi quando:
- Il tool del robot è una pinza: serve un istogramma per ognuna delle due aree occupate dalla pinza ai lati del componente di riferimento 
- Ci sono più punti critici da monitorare
- L'area di presa ha geometrie particolari

### **Step 1-3: Ripetizione**
Selezionare un nuovo istogramma dalla pagina elenco degli istogrammi, tipo "Histogram 2" e Ripetere gli Step 1-3.
Ripetere la procedura per ogni istogramma necessario (fino a 8 per modello). 

### **Step 4: Test Complessivo**
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


---

## Finalizzazione

### **Step 10: Proseguimento**
10. Dopo aver configurato tutti gli istogrammi necessari, cliccare su **Next**
11. Si aprirà la pagina **Robot Model Pick Cam**

```{seealso}
Procedi alla [Calibrazione Robot](#pagina-6-calibrazione-robot-pick) per completare la configurazione.
```

```{toctree}  
20b_Expert.md
```