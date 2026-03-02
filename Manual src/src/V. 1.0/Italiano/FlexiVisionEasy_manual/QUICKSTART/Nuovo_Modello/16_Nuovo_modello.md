# **Creazione Ricette e Modelli - Panoramica**

Questa sezione guida l'utente attraverso il processo completo di creazione di una ricetta applicativa e dei modelli pezzo necessari per il riconoscimento e il picking robotizzato.

```{note}
**Prerequisiti**

Prima di procedere con la creazione di ricette e modelli, assicurarsi che:
- Tutti i setup hardware siano completati ([Setup Componenti](setupcomponenti))
- La calibrazione camera sia stata eseguita con successo ([Calibrazione Camera](calibrazione))
- La calibrazione robot sia completata
- Si disponga dei pezzi fisici da riconoscere
```

---

## Ricetta vs Modello: Differenze fondamentali

Prima di iniziare, è importante comprendere la differenza tra **Ricetta** e **Modello**:

```{list-table}
   :widths: 50 50
   :header-rows: 1

   * - Cos'è una Ricetta?
     - Cos'è un Modello?
   * - Il contenitore globale dell'intera applicazione di picking.
     - La definizione specifica di un singolo componente da riconoscere.
   * - Include fino a 8 modelli, parametri FlexiBowl, Hopper e logiche di comunicazione.
     - Include immagini di training, ROI, feature visive, filtri e offset robot.
   * - Gestisce parametri hardware (vibrazioni, velocità) e rete (porta TCP/IP, timeout).
     - Gestisce parametri di visione (threshold, score minimo) e coordinate di prelievo (gripper).
   * - Può gestire più tipi di pezzi simultaneamente (multi-modello).
     - Focalizzato su un unico pattern visivo specifico.
```


```{tip}
Una ricetta può contenere fino a 8 modelli diversi, permettendo al robot di riconoscere e prelevare diversi tipi di pezzi dalla stessa applicazione senza cambiare configurazione.
```


---

## Panoramica del processo completo

Il processo di creazione di una ricetta completa e funzionante si articola in diverse fasi sequenziali:

```{figure} img/newmodel4.jpg
:alt: Workflow creazione ricetta e modelli
:width: 100%
:align: center

Schema completo del processo di creazione ricetta e modelli
```

### Fasi principali

```{list-table}
:header-rows: 1
:widths: 10 30 60

* - Fase
  - Nome
  - Descrizione
* - **1**
  - Creazione Ricetta
  - Definizione della ricetta applicativa con nome, tipo e FlexiBowl utilizzato
* - **2**
  - Preparazione Fisica
  - Posizionamento pezzo con robot e salvataggio coordinate di riferimento
* - **3**
  - Training Modello
  - Acquisizione immagine e creazione del pattern di riconoscimento
* - **4**
  - Definizione ROI
  - Definizione dell'area di ricerca dove cercare i pezzi
* - **5**
  - Impostazione Filtri
  - Configurazione accept threshold e tolleranze di riconoscimento
* - **6**
  - Creazione Istogrammi
  - Definizione zone che devono rimanere libere (area pinza, ostacoli)
* - **7**
  - Coordinate Robot
  - Calcolo offset gripper per prelievo corretto
* - **8**
  - Test e Validazione
  - Verifica funzionamento completo e salvataggio ricetta
```

---

## Guida alla navigazione sezioni dettagliate

Per informazioni complete su ogni fase del processo, consultare le sezioni dedicate:

- **[Creazione Nuova Ricetta](nuovaricetta)** - Come creare e configurare una nuova ricetta
- **[Training Modello]((nuovomodello))** - Acquisizione immagine e creazione pattern
- **[Definizione ROI e Filtri]((roitest))** - Configurazione area di ricerca e tolleranze
- **[Creazione Istogrammi](istogrammi)** - Definizione zone protette
- **[Coordinate Robot Pick](robotpick)** - Calcolo offset gripper

---

## Consigli pratici prima di iniziare

### Preparazione materiale

```{tip}
**Checklist preparazione**

Prima di iniziare la creazione di modelli, preparare:

- [ ] Almeno 10-20 pezzi del tipo da riconoscere (per test)
- [ ] Pezzi puliti e in buone condizioni (rappresentativi della produzione)
- [ ] Simulatori ingombro pinza (possono essere pezzi dello stesso tipo)
- [ ] Foglio per annotare coordinate robot (X, Y, RZ)
- [ ] FlexiBowl vuoto e pulito
- [ ] Backlight/Toplight acceso e stabile
```

### Ambiente ottimale

```{note}
**Condizioni ideali per training**

- Illuminazione stabile (evitare luce solare diretta variabile)
- FlexiBowl fermo (non in vibrazione durante acquisizione immagini)
- Robot in posizione sicura (non deve interferire durante le acquisizioni)
- Software FlexiVision Easy aperto e ricetta base caricata
```

### Errori comuni da evitare

```{error}
**Evitare questi errori frequenti**

❌ **Non salvare le coordinate robot** durante la preparazione fisica → impossibile calcolare offset gripper

❌ **Spostare il pezzo** dopo aver salvato le coordinate → offset errato

❌ **Feature threshold troppo basso** → modello troppo dettagliato, riconosce trama superficie

❌ **ROI troppo stretta** → pezzi ai bordi non vengono rilevati

❌ **Istogrammi troppo piccoli** → collisioni pinza con pezzi adiacenti

❌ **Non testare con pezzi multipli** → problemi non rilevati fino alla produzione

Seguire attentamente le procedure dettagliate nelle prossime sezioni per evitare questi problemi.
```

---

## Supporto e risorse aggiuntive

```{note}
**i Tasti INFO**

- **Video tutorial**: 
- **Spiegazione Passo-Passo**:
- **Supporto tecnico**: [support@arsautomation.com](mailto:support@arsautomation.com) per assistenza

Per problemi specifici durante la creazione di modelli, consultare la sezione [Troubleshooting](troubleshooting).
```

---

## Prossimi passi

Una volta compresa la panoramica del processo, procedere con la creazione effettiva:

**→ [Inizia: Creazione Nuova Ricetta](nuovaricetta)**

```{tip}
**Approccio consigliato**

Per il primo modello:
1. Leggere completamente questa panoramica
2. Seguire passo-passo la guida dettagliata iniziando da "Nuova Ricetta"
3. Tenere aperte le pagine di riferimento durante il lavoro
4. Annotare le coordinate e i parametri utilizzati per riferimento futuro
```


```{toctree}
:hidden:
17_NuovaRicetta.md
18_NuovoModello.md
19_ROI_TEST.md
20_Istogrammi.md
21_RobotPick.md
```