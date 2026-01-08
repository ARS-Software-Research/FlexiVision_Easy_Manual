# ROI e test 
v.	Definire la region search (area in cui flexivision andrà a rilevare i componenti) modificando il riquadro  
w.	Cliccare su next   
x.	Posizionare altri componenti nell’area di visione, senza toccare il componente di riferimento   
y.	Cliccare su test per fare un test del riconoscimento dei modelli   
z.	Modificare l’accept threshold (grado minimo di fedeltà (score) del componente rilevato rispetto al modello di riferimento)  
i.	 Impostando un valore più vicino a uno, il riquadro mostrerà solo i componenti con score uguale o maggiore al valore impostato in accept threshold   
Ad esempio, un valore di 0.95 nell’accept threshold mi restituirà solo i componenti con uno score di fedeltà dal 95% in su rispetto al modello di riferimento.    
aa.	Nel riquadro verranno mostrati i componenti rilevati con informazioni su Id, coordinate X Y, Rotazione e score rilevato   
FlexiVision ordinerà tutti i componenti riconosciuti nell’immagine e li ordinerà per score decrescente. Ad ognuno assegnerà un Id diverso in modo crescente. (il componente più fedele all’originale avrà Id pari a zero)  
bb.	Rimuovere tutti i componenti dall’area, fatta eccezione per il componente di riferimento!!!  
cc.	Cliccare su next   

```{toctree}  
19b_Expert.md
```