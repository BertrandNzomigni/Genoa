from Jeu.Position import Position
from Jeu.Mouvement.CoordinationMouvement import CoordinationMouvement
from Jeu.Mouvement.Itineraire import Itineraire
from Jeu.Mouvement.Deplaceur import Deplaceur


# Connait les informations du joueur
class Joueur:
    def __init__(self,lieu_de_depart):
        self.florins = 2000
        self.itineraire = Itineraire(self)
        self._position = Position(lieu_de_depart)
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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self,lieu):
        self._position.lieu = lieu
    
    def obtenir_coordinateur(self):
        return self.coord
    def acquerir_bateau(self,bateau):
        self.bateaux.append(bateau)
    def obtenir_bateaux(self):
        return self.bateaux
    def rejoint_bateau(self,bateau):
        self._bateau_dirige = bateau
        self.position.attacher_entite(bateau)
    def quitte_bateau(self):
        self.position.retirer_entite(self.bateau_dirige)
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
    
    @property
    def position(self):
        return self._position