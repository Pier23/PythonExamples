import tkinter
import os

window = tkinter.Tk()
window.title("Calcola Cose Varie")
leftLayout = tkinter.PanedWindow(orient='vertical')
leftLayout.pack(fill='both', side=tkinter.LEFT ,expand=1)
rightLayout = tkinter.PanedWindow(orient='vertical')
rightLayout.pack(fill='both', side=tkinter.RIGHT ,expand=1)

b = ' '
buttons = ['Prezzo', 'Sconto', 'Kilo']

for i in buttons:
    btn = tkinter.Button(window, text=i, command= lambda b=i: callback(b))
    leftLayout.add(btn)
    #btn.pack(side=tkinter.LEFT)
#risultato.pack()

for i in buttons:
    var = i
def callback(b):
    t = 0
    if b == 'Sconto':
        lbl2.configure(text="Inserisci Prezzo Intero", fg='black')
        lbl.configure(text="Inserisci Prezzo Scontato", fg='black')
        t = 1
        if t == 1:
            try:
                p1= float(ent2.get())
                p2= float(ent.get())
                _calcolaPercentualeSconto(p1,p2)
            except:
                print('Inserisci un valore Numerico')
                lbl.configure(fg='red')
                lbl2.configure(fg='red')
    elif b == 'Prezzo':
        lbl2.configure(text="Inserisci Prezzo Scontato", fg='black')
        lbl.configure(text="Inserisci Sconto", fg='black')
        t = 1
        if t == 1:
            try:
                pscont = float(ent2.get())
                sconto = float(ent.get())
                _calcolaPrezzoIniziale(pscont,sconto)
            except:
                print('Inserisci un valore Numerico')
                lbl.configure(fg='red')
                lbl2.configure(fg='red')
    elif b == 'Kilo':
        lbl.configure(text="Inserisci Prezzo Unitario",fg='black')
        lbl2.configure(text="Inserisci Grammatura", fg='black')
        t = 1
        if t == 1:
            try:
                pUnita = float(ent.get())
                grUnita = float(ent2.get())
                _calcolaPrezzoAlKilo(pUnita,grUnita)
            except:
                print('Inserisci un valore Numerico')
                lbl.configure(fg='red')
                lbl2.configure(fg='red')

lbl = tkinter.Label(window, text="Seleziona opzione")
rightLayout.add(lbl)
#lbl.pack()
ent = tkinter.Entry(window)
rightLayout.add(ent)
lbl2 = tkinter.Label(window, text="Seleziona opzione")
rightLayout.add(lbl2)
ent2 = tkinter.Entry(window)
rightLayout.add(ent2)
risultato = tkinter.Label(window, text='Risultato')
rightLayout.add(risultato)

#btn = tkinter.Button(window, text='calcola', command= calcola)
#btn.pack()


def _calcolaPrezzoIniziale(pScont, sconto):
    formula = 1-(sconto / 100)
    prezzoIniziale = pScont/formula
    risultato.configure(text = "Prezzo Originale: " + "%1.1f" % prezzoIniziale)
    print('Perzzo Iniziale:\n',prezzoIniziale)
	
def _calcolaPercentualeSconto(p1, p2):
    formula = (1-(p2/p1))*100
    percSconto = "%1.1f" % formula + '%'
    risultato.configure(text = "Percentuale Sconto: " + str(percSconto))
    print(percSconto)

def _calcolaPrezzoAlKilo(pUnita,grUnita):
    pKilo = (pUnita * 1000)/grUnita
    risultato.configure(text = "Prezzo al kilo: " + "%1.2f" % pKilo)
    print("Prezzo al kilo: ", pKilo)



os.system('xterm -into %d -geometry 40x20 -sb &')
window.mainloop()    
#d = input('What you want to do?\n')
#r1 = 'Sconto'
#r2 = 'Prezzo'
#_calcolaPercentualeSconto(pscont,sconto)
