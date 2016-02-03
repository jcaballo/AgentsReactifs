from Environment import Environment
from tkinter import *

environnement = Environment(10,10)
for i in range(0, 10):
    for j in range(0, 10):
        print("{0} | {1}".format(environnement.matrice[i][j].x, environnement.matrice[i][j].y))
    print("\n")

fenetre = Tk()
champ_label = Label(fenetre, text="Salut les Zér0s !")
champ_label.pack()
fenetre.mainloop()