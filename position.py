# mon_super_jeu/mouvement.py

from lieu import *
from bateau import *
import joueur

class Position:
    def __init__(self, lieu_initial):
        assert isinstance(lieu_initial, Lieu), "Le lieu initial doit être un lieu."
        self.lieuA = lieu_initial
        self.lieuB = None
        self.distance = None  # Distance entre l'entité et le point B

    def est_en_voyage(self):
        if self.lieuB != None:
            return self.distance != self.lieuA.obtenir_distance(self.lieuB)
        else:
            return False

    def obtenir_depart(self):
        return self.lieuA
    
    def obtenir_destination(self):
        assert self.lieuB != None, "Requête impossible, il n'y a pas de destination."
        return self.lieuB

    def a_destination(self):
        return self.lieuB != None
    
    def obtenir_distance(self):
        assert self.lieuB != None, "Requête impossible, il n'y a pas de destination."
        return self.distance

    def changer_destination(self, destination):
        assert isinstance(destination, Lieu), "La destination doit être un lieu."
        assert self.distance is None, "Impossible de changer la destination en cours de voyage."
        self.lieuB = destination
        self.distance = self.lieuA.obtenir_distance(self.lieuB)

    def a_atteint_destination(self):
        return self.distance == 0 or self.distance is None

    def avancer(self,vitesse):
        assert self.a_destination(), "L'entité doit avoir une destination."
        self.distance = max(self.distance - vitesse, 0)

        if self.a_atteint_destination():
            self.lieuA = self.lieuB
            self.lieuB = None
            self.distance = None

    def faire_demi_tour(self):
        if self.lieuB is None:
            return  # Rien à faire si pas de destination
        self.distance = self.lieuA.obtenir_distance(self.lieuB) - self.distance
        x = self.lieuA
        self.lieuA = self.lieuB
        self.lieuB = x
        if self.a_atteint_destination():
            self.lieuA = self.lieuB
            self.lieuB = None
            self.distance = None
    def obtenir_prix_bateau(self,type_bateau):
        assert isinstance(self.lieuA,Port),"Les prix des bateaux sont définis seulement dans les ports."
        return self.lieuA.obtenir_prix_bateau(type_bateau)
    def ajouter_bateau(self,bateau):
        self.lieuA.ajouter_bateau(bateau)
