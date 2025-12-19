# creare un nuovo modello   
Creazione modello/i da edit recipe   
a.	Per ogni modello, il primo step è quello di posizionare un componente al centro dell’area di visione   
b.	Selezionare il frame e il tool del robot calibrato sull’area di visione di FlexiVision dal pendant del robot stesso   
c.	Portare l’ultimo asse del tool del robot a rotazione zero   
d.	Rimuovere il componente  
e.	Portare il robot a livello della superficie   
f.	Riposizionare il componente all’interno della presa   
g.	Aprire e chiudere la pinza un paio di volte in modo da allineare il componente al centro del tool  
h.	Posizionare due oggetti ai due lati al componente per simulare l’ingombro della pinza   
Importante: nel posizionare i due componenti, restare leggermente più larghi per evitare errori nella creazione del modello   
i.	Salvare le coordinate X Y e rotazione attorno a Z dell’ultimo asse del robot   
Importante segnarle!! Serviranno dopo   
j.	Rimuoviamo il robot con il pendant senza spostare nulla   
k.	Aprire Edit recipe  
l.	Selezionare il FlexiBowl  
m.	Selezionare il modello   
n.	Abilitare il modello   
o.	Cliccare su grab Train Image   
p.	Spostare il riquadro che rappresenta la ROI e inquadrare il componente   
q.	Cliccare su Apply Train   
r.	Facendo Zoom, controllare che il modello sia corretto   
Per modello corretto si intende un modello:   
i.	con abbastanza linee per riconoscere il componente.  
ii.	Che non include parti della trama della superficie retrostante   
iii.	Che evita il riconoscimento di riflessi di luce   
iv.	Che evita il riconoscimento dei componenti che sono stati utilizzati per la simulazione dell’ingombro della pinza  
s.	Nel caso in cui il modello non fosse soddisfacente, modificare il feature threshold.   
i.	Un valore più vicino allo zero mi restituirà un modello più dettagliato   
ii.	Un valore più vicino a 1 mi restituirà un modello meno dettagliato   
t.	Nominare il modello   
u.	Cliccare su next   
