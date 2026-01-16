# Creare una Nuova Ricetta

## Obiettivo

Creare il contenitore principale (ricetta) che raggrupperà tutti gli elementi dell'applicazione: modelli, configurazioni FlexiBowl, impostazioni tramoggia e coordinate robot.

---

## Quando Creare una Nuova Ricetta

Crea una nuova ricetta quando:
- Inizi una nuova applicazione con componenti diversi
- Vuoi testare configurazioni alternative
- Devi gestire un nuovo tipo di pezzo o una nuova linea produttiva

---

## Procedura Completa

### Step 1: Accesso al Menu Ricette

1. Nel menu principale di FlexiVision, cliccare su **Recipes**

Questo aprirà l'interfaccia di gestione delle ricette, dove puoi visualizzare tutte le ricette esistenti o crearne di nuove.

---

### Step 2: Avvio Creazione

2. Cliccare su **New Recipe**

Si aprirà la procedura guidata per la creazione della nuova ricetta.

---

### Step 3: Assegnazione Nome

3. **Nominare la ricetta** con un identificativo chiaro e descrittivo

**Suggerimenti per la nomenclatura**:
- Usa nomi che identifichino il componente: `Vite_M8_Zincata`
- Includi il materiale se rilevante: `Ingranaggio_Plastica_Nera`
- Aggiungi l'applicazione: `Assemblaggio_Motore_A`
- Usa separatori coerenti: underscore `_` o trattini `-`
- Evita spazi e caratteri speciali

**Esempi**:
```
✓ Buoni:
  - Viti_M6_x_20_Inox
  - Guarnizione_Silicone_D32
  - Connettore_Elettrico_Tipo_A

✗ Da evitare:
  - ricetta1
  - test
  - nuova
```

---

### Step 4: Selezione Modalità Operativa

4. **Selezionare la modalità operativa** desiderata
5. Cliccare su **Next**

---

## Modalità Standard - Configurazione Dettagliata

Per la modalità **Standard** (la più comune), seguire questi passaggi aggiuntivi:

### Step 4a: Selezione FlexiBowl

1. Nella lista dei dispositivi disponibili, **selezionare il FlexiBowl** che si vuole configurare
2. Cliccare su **Next**

Il sistema mostrerà le informazioni del FlexiBowl selezionato e passerà alla fase di configurazione dei modelli.

### Step 4b: Selezione Modello da Creare

3. Dall'elenco dei modelli disponibili (Model 1, Model 2, ... Model N), **cliccare sul modello** che si vuole creare per primo

### Step 4c: Abilitazione Modello

4. Cliccare su **Enable Model**

Questo attiverà il modello selezionato e lo renderà disponibile per la configurazione.

**Note**:
- Puoi abilitare uno o più modelli per la stessa ricetta
- Ogni modello può rappresentare un componente diverso o un orientamento diverso dello stesso componente
- I modelli non abilitati non saranno disponibili durante l'operatività

---

## Stato della Ricetta

A questo punto hai creato la struttura base della ricetta:

✓ Nome ricetta assegnato  
✓ Modalità operativa selezionata  
✓ FlexiBowl associato  
✓ Modello/i abilitato/i  

La ricetta è ora **pronta per la creazione dei modelli** ma non è ancora operativa.

---

## Selezione della Ricetta per Lavorare sui Modelli

### Step 5: Apertura Ricetta per Editing

Prima di iniziare a creare i modelli, è necessario:

1. Dall'interfaccia principale, **selezionare la ricetta dell'applicazione** in cui si vogliono creare i modelli
2. Questa ricetta diventerà il contesto attivo per tutte le operazioni successive

---

## Gestione del Salvataggio

### Salvare una Nuova Ricetta

Quando hai completato la configurazione e vuoi salvare:

1. Cliccare su **Recipes** nel menu
2. Cliccare su **Save Recipe**
3. Inserire un **nome nuovo** per la ricetta
4. Confermare

La nuova ricetta viene aggiunta all'elenco delle ricette disponibili.

---

### Sovrascrivere una Ricetta Esistente

Se vuoi aggiornare una ricetta già salvata:

1. Cliccare su **Recipes**
2. Cliccare su **Save Recipe**
3. Inserire lo **stesso nome** della ricetta da sovrascrivere
4. Confermare

```
⚠️ ATTENZIONE: Sovrascrivere una ricetta

Quando sovrascrivi una ricetta con lo stesso nome, tutti i dati precedenti 
verranno PERSI definitivamente:
- Modelli creati
- ROI configurate
- Istogrammi impostati
- Calibrazioni robot
- Tutte le altre configurazioni

Assicurati di voler procedere prima di confermare.

Suggerimento: Se non sei sicuro, salva con un nome diverso
(es. aggiungi _v2, _backup, _test al nome).
```

---

## Modalità Operative Disponibili

### Standard Mode
La modalità più comune, utilizzata per applicazioni tipiche con FlexiBowl standard. Offre tutte le funzionalità di base per il riconoscimento e il prelievo.

### Advanced Mode
(Se disponibile) Per applicazioni che richiedono configurazioni speciali o funzionalità avanzate.

**Note**: Le modalità disponibili possono variare in base alla configurazione del sistema e alle licenze attive.

---

## Checklist Creazione Ricetta

Prima di procedere alla creazione dei modelli, verifica:

- [ ] Nome ricetta chiaro e descrittivo
- [ ] Modalità operativa corretta selezionata
- [ ] FlexiBowl giusto associato
- [ ] Modelli necessari abilitati
- [ ] Ricetta selezionata come contesto attivo

---

## Differenza tra Ricetta e Modello - Riepilogo

| Aspetto | Ricetta | Modello |
|---------|---------|---------|
| **Cosa è** | Contenitore completo dell'applicazione | Immagine di riferimento del componente |
| **Contiene** | Modelli + configurazioni sistema | Pattern visivo per riconoscimento |
| **Numero** | Una per applicazione | Uno o più per ricetta |
| **Include** | FlexiBowl, tramoggia, coordinate | ROI, threshold, istogrammi, offset |
| **Salvato come** | File ricetta completo | Elemento dentro la ricetta |

---

## Prossimi Passi

Ora che la ricetta è stata creata e i modelli abilitati, procedi a:

**→ [Creazione Nuovo Modello](#pagina-3-creare-un-nuovo-modello)**

dove apprenderai come configurare il setup fisico e creare il primo modello di riconoscimento.

---
---


```{toctree}  


17b_Expert.md
```