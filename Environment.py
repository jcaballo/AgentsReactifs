from Empty import Empty

class Environment: # Définition de notre classe Personne

    matrice = []
    def __init__(self, _i, _j):
        for i in range(0, _i):
            self.matrice.append([])
            for j in range(0, _j):
                self.matrice[i].append(Empty(i,j))


