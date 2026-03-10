from Jeu.Mouvement.CoordinationMouvement import CoordinationMouvement
from Jeu.Mouvement.Itineraire import Itineraire
from Jeu.Mouvement.Deplaceur import Deplaceur


# Connait les informations du joueur
class Joueur:
    def __init__(self,lieu_de_depart):
        self.florins = 2000
        self.itineraire = Itineraire(self)
        self.lieu = lieu_de_depart
        self.deplaceur = Deplaceur(self.itineraire,self)
        self.coord = CoordinationMouvement(self,self.deplaceur,self.itineraire)
        self.bateaux = list()
        self._bateau_dirige = None
    def obtenir_florins(self):
        return self.florins
    def obtenir_itineraire(self):
        return self.itineraire
    def a_destination(self):
        return self.itineraire.a_destination()
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
        self._bateau_dirige = bateau
    def quitte_bateau(self):
        self._bateau_dirige = None

    def dirige_actuellement_un_bateau(self):
        return self._bateau_dirige is not None


    @property
    def bateau_dirige(self):
        return self._bateau_dirige
    
    @property
    def vitesse(self):
        if self._bateau_dirige:
            return self._bateau_dirige.vitesse
        else:
            return 20