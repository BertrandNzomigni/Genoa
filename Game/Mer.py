from Game.Lieu import Lieu

class Mer:
    def __init__(self,nom):
        self.nom = nom
        self.lieu = Lieu()
    def obtenir_nom(self):
        return self.nom
    def obtenir_lieu(self):
        return self.lieu
    def __str__(self):
        return self.nom