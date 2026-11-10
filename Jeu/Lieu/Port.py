from Jeu.Lieu.Lieu import Lieu

class Port(Lieu):
    def __init__(self,nom,marche):
        super().__init__(nom)
        self.marche = marche

    def biens_disponibles(self):
        return self.marche.biens_disponibles()

    def obtenir_prix(self,bien):
        return self.marche.obtenir_prix(bien)