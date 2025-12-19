# Guida Dettagliata all'Expert
I tasti Expert invece, compaiono nelle pagine in cui l’utente potrebbe avere bisogno di andare a modificare le impostazioni più complesse. 
Questa funzione è pensata per essere utilizzata solo in casi estremi, tipo per la definizione di componenti più complessi.   
Ecco una guida al suo utilizzo:   
12.6.1.	Selezionare Current train image dal menu a tendina in alto  
12.6.2.	Aprire Train params   
Parametri da impostare per “allenare” la visione a cercare riscontrare il modello nel componente   
Tip: il modello sarà più accurato se il componente si trova al centro dell’area di visione (questo evita di fare il training di modelli poco affidabili)  
12.6.2.1.	Cliccare GrabTrainImage per utilizzare l’ultima foto presente nel locator (ultima foto fatta) dei componenti presenti nell’area di visione  
12.6.2.2.	Impostare l’area di cui si vuole fare il modello (riquadro) sul componente   
12.6.2.3.	Spostare l’origine sul componente (è possibile farlo anche successivamente)  
12.6.2.4.	Controllare la selezione auto in Coarse Grain Limit   
12.6.2.5.	Controllare la selezione auto in Fine Grain Limit   
12.6.2.6.	Impostare il Feature Threshold: 	  
12.6.2.6.1.	Un valore più vicino allo zero mi restituirà un modello più dettagliato   
12.6.2.6.2.	Un valore più vicino a 1 mi restituirà un modello meno dettagliato   
12.6.2.7.	Selezionare il Train timeout solo nel caso in cui si volesse mettere in timeout il modello per i secondi riportati (questo si fa quando la camera impiega più di tot millisecondi e vogliamo bloccare l’esecuzione) se FlexiVision richiede più di tot millisecondi.   
12.6.2.8.	Cliccare su train per “allenare” la visione al riconoscimento del modello effettuato   
12.6.2.9.	Il modello sarà salvato in automatico   
12.6.2.10.	Se il modello ottenuto è soddisfacente e si volesse salvarlo, cliccare su save pattern e verrà salvato in un file   
12.6.2.11.	È possibile anche carcare un pattern già esistente cliccando su load pattern   
 Da finire E DA RIVEDERE (IL TASTO EXPERT NON è SEMPRE UGUALE)  
