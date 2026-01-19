# Calibrazione Robot Pick
In questa pagina vedremo come collegare le coordinate della visione con quelle del robot per consentire un prelievo preciso dei componenti.


## Cos'è il Robot Pick?

La funzione **Robot Pick** calcola l'offset tra le coordinate rilevate da FlexiVision e le coordinate reali del robot, permettendo al robot di prelevare i componenti nella posizione corretta.

---

## Parametri Principali

|Sezione | Parametro | Funzione |
|-----------|-----------|----------|
| Enable | **Enable Robot Pick** | Attiva la calibrazione del robot |
|Vision Result| **X cord** | Coordinata X rilevata dalla visione |
|Vision Result| **Y cord** | Coordinata Y rilevata dalla visione |
|Vision Result| **RZ cord** | Rotazione Z rilevata dalla visione |
|Insert Robot Coordinate| **X cord** | Coordinata X del robot (da inserire) |
|Insert Robot Coordinate| **Y cord** | Coordinata Y del robot (da inserire) |
|Insert Robot Coordinate| **RZ cord** | Rotazione Z del robot (da inserire) |


| Funzione | Descrizione |
|----------|-------------|
| **Find Object** | Rileva il componente e mostra coordinate visione |
| **Gripper Offset** | Calcola l'offset per il prelievo corretto |

---

## Procedura di Calibrazione

### **Step 1: Attivazione e Rilevamento Componente**
1. Cliccare su **Enable Robot Pick**
2. Cliccare su **Find Object**
   - Il sistema rileverà il componente di riferimento
   - Le coordinate appariranno nella sezione **Vision Result**

```{note} Vision Result
Queste sono le coordinate che FlexiVision "vede" nell'immagine. Non sono ancora collegate al sistema di coordinate del robot.
```

### **Step 2: Inserimento Coordinate Robot e calcolo Offset**
3. Nel riquadro **Insert Robot Coordinates**, inserire le coordinate salvate durante la creazione del modello:
   - **X cord** → Coordinata X annotata al punto 8 della [Creazione Modello](#fase-1-preparazione-del-setup-fisico)
   - **Y cord** → Coordinata Y annotata al punto 8 della [Creazione Modello](#fase-1-preparazione-del-setup-fisico)
   - **RZ cord** → Rotazione Z annotata al punto 8 della [Creazione Modello](#fase-1-preparazione-del-setup-fisico)

```{danger}
Usa le coordinate salvate durante il setup del modello. Senza queste coordinate, la calibrazione sarà errata!
```
4. Cliccare su **Gripper Offset**
   - Il sistema calcolerà automaticamente la trasformazione tra coordinate visione e coordinate robot
   - Questo offset verrà applicato a tutti i futuri rilevamenti

---

## Come Funziona il Gripper Offset?

```{admonition} Principio di Funzionamento
:class: info
Il sistema confronta:
- **Coordinate Visione**: dove FlexiVision "vede" il componente
- **Coordinate Robot**: dove il robot ha effettivamente afferrato il componente

Calcola la differenza e la memorizza come **offset**. Questo offset verrà applicato a tutti i componenti rilevati in futuro, garantendo che il robot prelevi sempre nella posizione corretta.
```

### Esempio Pratico

```
Vision Result:        X=100, Y=200, RZ=0°
Robot Coordinate:     X=350, Y=450, RZ=0°
Gripper Offset:       ΔX=+250, ΔY=+250, ΔRZ=0°

Quando FlexiVision rileva un nuovo componente a X=120, Y=220
Il robot andrà a prelevarlo a X=370, Y=470
```

---

## Finalizzazione e Salvataggio

### Step 3: Proseguimento e Salvataggio Ricetta
5. Cliccare su **Next**
6. Cliccare su **Save Recipe** per salvare l'intera configurazione

```{admonition} Salvataggio Completo
:class: success
Il salvataggio include:
- ✓ Modello creato
- ✓ Area di lavoro (ROI)
- ✓ Tolleranze (Accept Threshold)
- ✓ Istogrammi configurati
- ✓ Calibrazione robot (Gripper Offset)
```

---

## Modelli Multipli

### Aggiungere Altri Modelli

**Step 7: Modelli Aggiuntivi (opzionale)**
7. Per creare altri modelli nella stessa ricetta:
   - Tornare su **Edit Recipe**
   - Selezionare un nuovo modello
   - Ripetere l'intera procedura dalla [Creazione Modello](#pagina-3-creare-un-nuovo-modello)

```{tip}
Ogni modello nella ricetta può avere configurazioni diverse (ROI, istogrammi, offset), permettendo di gestire componenti con caratteristiche diverse nella stessa applicazione.
```

---

## Verifica Finale

### Checklist Completamento

Prima di utilizzare la ricetta in produzione, continua con :

- [Configurazione del FlexiBowl ] (QUICKSTART/22_Config_FlexiBowl.md)
- [Configurazione della Tramoggia ] (QUICKSTART/23_Config_Hopper.md)
- [Monitoraggio Applicazione ] (QUICKSTART/24_Verifica_Risultati.md)

```{seealso}
Per modifiche successive, consulta:
- [Modifica Modelli Esistenti](#modifica-modelli)
- [Ottimizzazione Parametri](#ottimizzazione)
- [Troubleshooting](#risoluzione-problemi)
```

---

```{toctree}  
21b_Expert.md
```