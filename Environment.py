import Empty

class Environment: # Définition de notre classe Personne

    def __init__(self, _i, _j):
        for i in range(0, _i):
            for j in range(0, _j):
                self.matrice[i][j] = Empty();

