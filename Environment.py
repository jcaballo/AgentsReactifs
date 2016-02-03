from Empty import Empty
from tkinter import *

class Environment: # Définition de notre classe Personne

    def __init__(self, _i, _j):
        for i in range(0, _i):
            for j in range(0, _j):
                self.matrice[i][j] = Empty(i,j);



    fenetre = Tk()
    champ_label = Label(fenetre, text="Salut les Zér0s !")
    champ_label.pack()
    fenetre.mainloop()

