# **Informazioni di Sicurezza**

Le seguenti istruzioni di sicurezza, precauzioni generali e norme relative alla movimentazione e all'ambiente operativo devono essere scrupolosamente rispettate per garantire la sicurezza del personale, l'integrità del prodotto e il corretto funzionamento dell'impianto.

```{warning}
**Responsabilità dell'utente**

Il rispetto di tutte le norme di sicurezza riportate in questa sezione è obbligatorio e di responsabilità dell'utilizzatore finale. Il mancato rispetto può causare danni a persone, apparecchiature o compromettere il funzionamento del sistema.
```

---

## Sicurezza operativa

### Integrazione con sistemi robotizzati

```{warning}
**Requisiti di sicurezza della cella**

FlexiVision Easy opera in stretta connessione con sistemi robotizzati di terze parti. L'utente deve garantire che l'area di lavoro sia dotata di tutte le misure di sicurezza necessarie:

- Barriere perimetrali certificate secondo normativa vigente
- Sensori di presenza e sistemi di arresto di emergenza
- Segnaletica di sicurezza adeguata
- Formazione del personale sui rischi specifici della cella robotizzata
```

```{warning}
**Attenzione durante l'operatività**

Durante il funzionamento del sistema, tenere sempre conto di:

- Ingombri fisici del robot e del FlexiBowl
- Traiettorie e velocità dei movimenti robotici
- Possibili situazioni impreviste (caduta pezzi, errori di prelievo)
- Zone di pericolo durante le fasi di vibrazione del FlexiBowl
```

### Precauzioni generali prima degli interventi

```{warning}
**Disconnessione alimentazioni**

Prima di eseguire qualsiasi intervento di manutenzione, modifica o ispezione sul sistema, assicurarsi sempre che:

- Tutte le fonti di alimentazione elettrica siano disconnesse (VisionController, FlexiBowl, Camera, Illuminatore)
- L'alimentazione pneumatica sia scaricata e disconnessa (se presente)
- I cavi di collegamento siano fisicamente scollegati
- Il robot sia in modalità di sicurezza o completamente spento
```

```{warning}
**Procedure di sicurezza**

Non affidarsi esclusivamente agli interruttori: utilizzare procedure di lockout/tagout (LOTO) quando disponibili.
```

### Modifiche e manomissioni

```{warning}
**Divieto di modifiche non autorizzate**

Non modificare mai il prodotto o i suoi componenti senza espressa autorizzazione scritta di ARS S.r.l.
```

```{warning}
**Conseguenze delle modifiche**

Modifiche non autorizzate possono:

- Causare malfunzionamenti del sistema
- Invalidare la garanzia
- Creare rischi di lesioni, scosse elettriche o incendi
- Compromettere le certificazioni di sicurezza del prodotto
```

---

## Condizioni ambientali e protezione

### Protezione da liquidi

```{warning}
**Rischio contatto con liquidi**

Non utilizzare il prodotto in ambienti dove il VisionController, la camera o altri componenti elettronici possano entrare in contatto con:

- Gocce d'acqua o spruzzi
- Oli, lubrificanti o altri liquidi industriali
- Condensa o umidità eccessiva
- Polveri conduttive
```

```{note}
**Soluzioni per ambienti critici**

Se il sistema deve operare in ambienti con presenza di liquidi, prevedere adeguate protezioni (custodie IP65 o superiori) e consultare il servizio tecnico ARS per soluzioni personalizzate.
```

### Temperature operative

```{warning}
**Superfici calde - Temperature massime**

In condizioni di utilizzo intenso o ambienti caldi, alcuni componenti del sistema possono raggiungere temperature elevate:

- VisionController: fino a 50°C sulle superfici esterne
- Illuminatore LED: fino a 60°C sulla superficie frontale
- Camera industriale: fino a 45°C sul corpo metallico
```

```{warning}
**Responsabilità del cliente**

È responsabilità del cliente:

- Documentare i rischi termici nella propria valutazione dei rischi
- Istruire il personale sulle procedure per evitare contatti accidentali
- Prevedere segnaletica di avvertimento dove necessario
- Garantire adeguata ventilazione dei componenti
```

### Condizioni ambientali per installazione e stoccaggio

```{note}
**Requisiti ambientali - Tabella di riferimento**

Per garantire durata e affidabilità, il VisionController e la camera devono essere utilizzati e conservati nelle seguenti condizioni:

| Parametro | Condizioni operative | Condizioni di stoccaggio |
|-----------|---------------------|--------------------------|
| **Temperatura** | +5°C ÷ +45°C | -10°C ÷ +60°C |
| **Umidità relativa** | 20% ÷ 80% (senza condensa) | 10% ÷ 90% (senza condensa) |
| **Altitudine** | 0 ÷ 2000 m s.l.m. | 0 ÷ 3000 m s.l.m. |
| **Grado di inquinamento** | Pollution Degree 2 (IEC 61010-1) | - |
| **Categoria installazione** | Overvoltage Category II | - |
```

```{note}
**Precauzioni aggiuntive per l'ambiente**

Per preservare l'integrità dei componenti:

- Evitare l'esposizione diretta alla luce solare
- Proteggere da vibrazioni eccessive durante lo stoccaggio
- Mantenere in ambiente asciutto e privo di polveri aggressive
- La camera è sensibile agli shock meccanici: maneggiare con cura
```

---

## Trasporto e movimentazione

### Ricezione e ispezione

```{note}
**Ispezione all'arrivo**

Alla ricezione del prodotto, prima di firmare la bolla di consegna:

1. **Ispezione esterna dell'imballaggio**: Verificare l'integrità della scatola e dell'imballo esterno. Controllare la presenza di eventuali segni di urti, schiacciamenti o bagnature.

2. **Verifica contenuto**: Confrontare il contenuto con la nota di consegna. Verificare la presenza di tutti i componenti ordinati.
```

```{note}
**In caso di danni o discrepanze**

Se si riscontrano problemi:

- NON firmare la ricevuta come "conforme"
- Annotare i danni sul documento di trasporto
- Fotografare eventuali danni evidenti
- Contattare immediatamente il servizio assistenza ARS: [info@arsautomation.com](mailto:info@arsautomation.com)
```

### Movimentazione e stoccaggio

```{tip}
**Buone pratiche per la movimentazione**

Per prevenire danni durante trasporto e stoccaggio:

**Durante il trasporto:**
- Movimentare sempre l'imballaggio in posizione verticale (rispettare le frecce "ALTO" sull'imballo)
- Non far cadere o urtare la confezione
- Utilizzare carrelli o transpallet adeguati al peso
- Evitare sbalzi termici improvvisi

**Durante lo stoccaggio:**
- Conservare in luogo asciutto e coperto
- Non sovrapporre altri carichi sull'imballaggio
- Non salire o appoggiarsi sull'imballaggio
- Rispettare le condizioni ambientali indicate nella tabella precedente

**Durante il disimballaggio:**
- Aprire con cura per non danneggiare i componenti interni
- Conservare l'imballo originale per eventuali resi o trasporti futuri
- Verificare la presenza di tutti gli accessori e della documentazione
```

---

## Smaltimento e fine vita

### Dismissione del prodotto

```{note}
**Smaltimento responsabile**

Quando il prodotto raggiunge la fine del suo ciclo di vita, deve essere smaltito in conformità con le normative vigenti relative ai rifiuti di apparecchiature elettriche ed elettroniche (RAEE/WEEE).

**Componenti soggetti a smaltimento speciale:**
- Schede elettroniche (VisionController): RAEE categoria 6
- Camera industriale: RAEE categoria 6
- Illuminatori a LED: RAEE categoria 5
- Cavi e connettori: smaltimento con materiali elettrici

**Procedura consigliata:**
1. Contattare un ente certificato per lo smaltimento RAEE
2. Fornire la documentazione tecnica del prodotto
3. Assicurarsi che vengano rispettate tutte le normative locali e nazionali
4. Conservare la documentazione di avvenuto smaltimento

```

---

## Conformità e normative

Il sistema FlexiVision Easy è progettato per essere conforme alle seguenti direttive e normative (verificare la Dichiarazione di Conformità fornita con il prodotto):

- Direttiva Macchine 2006/42/CE
- Direttiva EMC 2014/30/UE
- Direttiva Bassa Tensione 2014/35/UE
- IEC 61010-1: Sicurezza apparecchi elettrici per misura, controllo e laboratorio

```{warning}
**Responsabilità dell'integratore**

L'integrazione di FlexiVision Easy in un sistema completo (cella robotizzata) è responsabilità dell'integratore di sistema, che deve:
- Effettuare una nuova valutazione dei rischi complessiva
- Garantire la conformità del sistema integrato alle normative applicabili
- Produrre la documentazione tecnica del sistema completo
- Apporre la marcatura CE sul sistema integrato (se applicabile)
```