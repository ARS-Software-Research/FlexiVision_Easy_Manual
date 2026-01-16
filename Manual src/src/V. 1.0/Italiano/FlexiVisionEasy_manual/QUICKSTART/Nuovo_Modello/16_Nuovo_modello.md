# Creare una nuova ricetta e un nuovo modello 
## Introduzione

Questa sezione fornisce una visione completa del processo di creazione di ricette e modelli in FlexiVision, dalla configurazione iniziale alla calibrazione finale del robot.

---

## Concetti Fondamentali

### Cos'è una Ricetta?

Una **ricetta** è il contenitore principale che include tutti gli elementi necessari per far funzionare un'applicazione FlexiVision. Nello specifico, una ricetta comprende:

- **Modelli dei componenti**: le immagini di riferimento per il riconoscimento
- **Configurazione dei parametri del FlexiBowl**: impostazioni operative del sistema di alimentazione
- **Configurazione dello scarico della tramoggia**: gestione del flusso dei componenti
- **Configurazione delle coordinate del robot**: calibrazione spaziale per il prelievo

Una ricetta è quindi l'insieme completo di tutte le configurazioni necessarie per un'applicazione specifica.

### Cos'è un Modello?

Un **modello** è l'immagine di riferimento che FlexiVision utilizza per riconoscere i componenti nell'area di visione. È essenzialmente un "template" visivo che il sistema confronta con le immagini acquisite in tempo reale per:

- Identificare i componenti corretti
- Determinare la loro posizione (coordinate X, Y)
- Rilevare il loro orientamento (rotazione Z)
- Calcolare il grado di somiglianza (score)

Ogni ricetta può contenere uno o più modelli, permettendo di gestire diverse varianti di componenti nella stessa applicazione.

---

## Il Processo Completo: 6 Fasi Principali

```
┌─────────────────┐
│  1. RICETTA     │  Creazione contenitore applicazione
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  2. MODELLO     │  Training immagine riferimento
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  3. ROI         │  Definizione area di lavoro
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  4. TOLLERANZE  │  Impostazione accept threshold
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  5. ISTOGRAMMI  │  Configurazione aree libere
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  6. ROBOT PICK  │  Calibrazione coordinate
└─────────────────┘
```

### Fase 1: Creazione della Ricetta

**Obiettivo**: Creare il contenitore principale per l'applicazione

**Attività principali**:
- Nominare la ricetta con un identificativo chiaro
- Selezionare la modalità operativa (Standard, Advanced, etc.)
- Scegliere il FlexiBowl da configurare
- Abilitare i modelli che verranno creati

**Risultato**: Una ricetta vuota pronta ad accogliere i modelli

---

### Fase 2: Creazione del Modello

**Obiettivo**: Insegnare a FlexiVision come riconoscere il componente

**Attività principali**:
- **Setup fisico**: Posizionamento del componente con robot e simulazione ingombro pinza
- **Acquisizione immagine**: Scatto della foto di riferimento (Grab Train Image)
- **Regolazione dettaglio**: Configurazione Feature Threshold per il livello di dettaglio ottimale
- **Verifica qualità**: Controllo che il modello rilevi le caratteristiche corrette

**Risultato**: Un modello validato che rappresenta accuratamente il componente

---

### Fase 3: Definizione Area di Lavoro (ROI - Region of Interest)

**Obiettivo**: Stabilire dove FlexiVision deve cercare i componenti

**Attività principali**:
- Delimitare la Region Search nell'area di visione
- Definire i confini operativi raggiungibili dal robot

**Risultato**: Un'area di ricerca ottimizzata per l'applicazione

---

### Fase 4: Impostazione Tolleranze (Accept Threshold)

**Obiettivo**: Definire quanto devono essere simili i componenti rilevati al modello di riferimento

**Attività principali**:
- Posizionare componenti di test nell'area
- Eseguire test di riconoscimento
- Regolare l'Accept Threshold (soglia di accettazione dello score)
- Verificare che solo i componenti validi vengano rilevati

**Risultato**: Un sistema di filtraggio che identifica solo i componenti corretti

---

### Fase 5: Configurazione Istogrammi

**Obiettivo**: Identificare le aree che devono rimanere libere da ostacoli

**Attività principali**:
- Posizionare riquadri di controllo nelle aree critiche
- Configurare le soglie di rilevamento automatico
- Testare il riconoscimento di aree libere vs occupate
- Creare fino a 8 istogrammi per modello se necessario

**Risultato**: Un sistema di sicurezza che previene collisioni durante il prelievo

---

### Fase 6: Calibrazione Robot Pick

**Obiettivo**: Collegare le coordinate della visione con quelle del robot

**Attività principali**:
- Attivare Enable Robot Pick
- Rilevare le coordinate visione del componente (Find Object)
- Inserire le coordinate robot salvate durante il setup
- Calcolare l'offset con Gripper Offset

**Risultato**: Una calibrazione completa che permette al robot di prelevare nella posizione esatta

---

## Flusso di Lavoro Completo

```
PREPARAZIONE
├── Creare nuova ricetta
├── Nominare e selezionare modalità
└── Abilitare modello

SETUP FISICO MODELLO
├── Posizionare componente al centro visione
├── Selezionare frame e tool robot (Rz=0)
├── Simulare ingombro pinza con oggetti laterali
├── Salvare coordinate X, Y, Rz robot
└── Rimuovere robot senza spostare nulla

TRAINING MODELLO SOFTWARE
├── Edit Recipe → Seleziona FlexiBowl → Seleziona Modello
├── Enable Model
├── Grab Train Image
├── Posizionare ROI sul componente
├── Regolare Feature Threshold
├── Centrare origine
├── Apply Train
├── Verificare qualità modello (zoom)
├── Eventuale correzione Feature Threshold
└── Nominare modello

DEFINIZIONE AREA LAVORO
├── Define Robot Pick Area
└── Definire Region Search

IMPOSTAZIONE TOLLERANZE
├── Posizionare componenti test
├── Test riconoscimento
├── Regolare Accept Threshold
├── Verificare Id, coordinate, rotazione, score
└── Rimuovere componenti test (tenere solo riferimento)

CONFIGURAZIONE ISTOGRAMMI
├── Histogram 1...8 (fino a 8 per modello)
│   ├── Enable Histogram
│   ├── Posizionare riquadro su area critica
│   ├── AUTO Expression Builder
│   ├── TEST (verificare verde)
│   └── Next
└── TEST complessivo tutti istogrammi

CALIBRAZIONE ROBOT
├── Enable Robot Pick
├── Find Object (coordinate visione)
├── Insert Robot Coordinates (da setup fisico)
├── Gripper Offset (calcolo trasformazione)
└── Next

SALVATAGGIO
└── Save Recipe
```

---

## Note Importanti per il Processo

### Ordine delle Operazioni

Le fasi devono essere seguite nell'ordine indicato perché:
- Il modello richiede un setup fisico preciso
- La ROI dipende dal modello creato
- Le tolleranze si basano sulla ROI definita
- Gli istogrammi si riferiscono a componenti riconosciuti
- Il Robot Pick necessita di tutti i parametri precedenti

### Modelli Multipli

Una stessa ricetta può contenere più modelli per gestire:
- Varianti dello stesso componente
- Orientamenti diversi
- Componenti differenti nella stessa applicazione

Per aggiungere modelli alla stessa ricetta, tornare su "Edit Recipe" e ripetere il processo dal punto 2 (Creazione Modello).

### Salvataggio e Sovrascrittura

- **Nuova ricetta**: Save Recipe con nome nuovo
- **Aggiornamento ricetta**: Save Recipe con stesso nome (sovrascrive)

---

## Prossimi Passi

Nelle pagine successive troverai le procedure dettagliate per ogni fase, con tutti i passaggi tecnici, parametri e controlli di qualità necessari per una configurazione ottimale.

---
---


```{toctree}
:hidden:
17_NuovaRicetta.md
18_NuovoModello.md
19_ROI_TEST.md
20_Istogrammi.md
21_RobotPick.md
```