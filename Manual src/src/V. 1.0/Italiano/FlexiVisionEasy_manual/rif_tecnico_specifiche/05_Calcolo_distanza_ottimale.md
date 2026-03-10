(distanza_lavoro)=
# **Calcolo Distanza di Lavoro Ottimale**

Questa sezione definisce la distanza di lavoro (Working Distance) raccomandata tra la telecamera e il piatto FlexiBowl, insieme alla conseguente selezione delle lenti necessarie per garantire il corretto Campo Visivo (Field of View, FOV).

La scelta corretta della distanza di lavoro e della lente è fondamentale per:
- Garantire che l'intera superficie utile del FlexiBowl sia visibile
- Ottenere la risoluzione necessaria per rilevare i pezzi
- Minimizzare le distorsioni ottiche
- Facilitare la calibrazione del sistema

---

## Distanze di lavoro raccomandate e selezione lenti

La scelta della lente è strettamente dipendente dalla distanza di montaggio raccomandata tra la telecamera e la superficie del piatto FlexiBowl. Mantenere la distanza di lavoro standard garantisce il corretto FOV e minimizza i problemi di distorsione ottica.

### Tabella riepilogativa per modello

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - Modello FlexiBowl
  - Distanza di Lavoro Raccomandata (Working Distance)
  - Lente Inclusa nel Kit (Lunghezza Focale)
* - **FB 200**
  - Circa 950 – 1000 mm
  - 35 mm
* - **FB 350**
  - Circa 950 – 1000 mm
  - 35 mm
* - **FB 500**
  - Circa 950 – 1000 mm
  - 25 mm
* - **FB 650**
  - Circa 950 – 1000 mm
  - 16 mm
* - **FB 800**
  - Circa 950 – 1000 mm
  - 12 mm
* - **FB 1200**
  - Circa 1200 mm
  - 8 mm
```

```{note}
**Lente già inclusa**

La lente appropriata per il modello FlexiBowl specificato nell'ordine è sempre inclusa nel pacchetto FlexiVision e viene pre-montata sulla camera. Non è necessario acquistarla separatamente.
```

### Schema distanze e campo visivo

Il seguente diagramma illustra la relazione tra distanza di lavoro, lunghezza focale della lente e area di visione risultante per i diversi modelli di FlexiBowl.


```{image} ../rif_tecnico_specifiche/img/working_distance.JPG
:alt: Distanza Di Lavoro
:width: 40%
:align: center
```

**Legenda schema:**
- **Distanza di Lavoro**: Distanza verticale tra la faccia frontale della lente e la superficie del piatto FlexiBowl
- **Area di visione**: Zona della superficie del FlexiBowl coperta dal campo visivo della camera


```{warning}
**Importanza della distanza corretta**

Deviazioni significative dalla distanza di lavoro raccomandata possono causare:

- **Distanza troppo breve**: FOV insufficiente (parte del FlexiBowl non visibile).
- **Distanza troppo lunga**: Risoluzione insufficiente per rilevare pezzi piccoli, sfocatura

Rispettare sempre le distanze indicate in tabella durante il montaggio meccanico della camera.
```
### Posizionamento Camera 
```{image} ../rif_tecnico_specifiche/img/config_giusta.JPG
:alt: Distanza Di Lavoro
:width: 40%
:align: center
```
```{image} ../rif_tecnico_specifiche/img/config_sbagliata.png
:alt: Distanza Di Lavoro
:width: 40%
:align: center
```
```{image} ../rif_tecnico_specifiche/img/config_sbagliata2.png
:alt: Distanza Di Lavoro
:width: 40%
:align: center
```
---

## Posizionamento TopLight 

Se il sistema include un TopLight (illuminatore dall'alto), il suo posizionamento deve essere coordinato con quello della camera per garantire un'illuminazione uniforme.

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parametro
  - Valore Consigliato
* - **Distanza dalla superficie FlexiBowl**
  - Simile alla Working Distance della camera (±100 mm)
* - **Posizione rispetto alla camera**
  - Concentrica (stesso asse ottico della camera)
* - **Orientamento**
  - Parallelo alla superficie del FlexiBowl
* - **Altezza relativa camera-TopLight**
  - TopLight leggermente più alto della camera (circa 50-100 mm)
```

```{tip}
Per ottenere la migliore uniformità di illuminazione:
1. Posizionare il TopLight alla stessa distanza della camera o leggermente più lontano
2. Mantenere il TopLight concentrico rispetto al FlexiBowl per evitare ombre asimmetriche
3. Durante la fase di test, acquisire immagini e verificare l'uniformità luminosa
4. Se necessario, regolare la distanza o aggiungere diffusori per eliminare hotspot
```

### Schema posizionamento integrato

immagine del sistema con toplight 

```{warning}
**Evitare riflessioni dirette**

Quando si posiziona il TopLight, assicurarsi che:

- La luce non si rifletta direttamente dalla superficie del FlexiBowl verso la camera (causando abbagliamento)
- Non ci siano ombre causate da componenti meccanici
- L'illuminazione sia il più uniforme possibile su tutta la superficie utile

```

---

## Riferimenti correlati

Per completare l'installazione e la configurazione del sistema:

- **Installazione meccanica camera**: [Installazione Meccanica](../QUICKSTART/09_Installazione_Meccanica.md)
- **Specifiche tecniche camera**: [Specifiche FlexiVision](04_Specifiche_FlexiVision.md)
- **Calibrazione sistema**: [Calibrazione della Camera](../QUICKSTART/14_calibrazione_camera.md)
- **Cablaggio elettrico**: [Cablaggio e Connessioni](../QUICKSTART/10_Cablaggio_Connessioni.md)