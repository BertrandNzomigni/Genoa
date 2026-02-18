from Game.Mouvement.CoordinationMouvement import CoordinationMouvement
from Game.Mouvement.Itineraire import Itineraire
from Game.Mouvement.Deplaceur import Deplaceur


# Connait les informations du joueur
class Joueur:
    def __init__(self,lieu_de_depart):
        self.florins = 2000
        self.itineraire = Itineraire(self)
        self.lieu = lieu_de_depart
        self.deplaceur = Deplaceur(self.itineraire,self)
        self.coord = CoordinationMouvement(self,self.deplaceur,self.itineraire)
        self.bateaux = list()
        self.bateau_dirige = None
    def obtenir_florins(self):
        return self.florins
    def obtenir_itineraire(self):
        return self.itineraire
    def obtenir_lieu(self):
        return self.lieu
    def changer_lieu(self,lieu):
        self.lieu = lieu
    def obtenir_coordinateur(self):
        return self.coord
    def acquerir_bateau(self,bateau):
        self.bateaux.append(bateau)
    def obtenir_bateaux(self):
        return self.bateaux
    def rejoint_bateau(self,bateau):
        self.bateau_dirige = bateau
    def quitte_bateau(self):
        self.bateau_dirige = None