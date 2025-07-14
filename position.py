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
        self.verifier_invariants()

    def est_en_voyage(self):
        if self.lieuB != None:
            return self.distance != self.lieuA.obtenir_distance(self.lieuB)
        else:
            return False

    def obtenir_depart(self):
        return self.lieuA
        self.verifier_invariants()
    
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
        self.verifier_invariants()

    def a_atteint_destination(self):
        return self.distance == 0 or self.distance is None

    def avancer(self,vitesse):
        assert self.a_destination(), "L'entité doit avoir une destination."
        self.distance = max(self.distance - vitesse, 0)

        if self.a_atteint_destination():
            self.lieuA = self.lieuB
            self.lieuB = None
            self.distance = None
        self.verifier_invariants()

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
        self.verifier_invariants()
    def obtenir_prix_bateau(self,type_bateau):
        assert isinstance(self.lieuA,Port),"Les prix des bateaux sont définis seulement dans les ports."
        return self.lieuA.obtenir_prix_bateau(type_bateau)
    def ajouter_bateau(self,bateau):
        self.lieuA.ajouter_bateau(bateau)
        self.verifier_invariants()
    def obtenir_voisins_lieu(self):
        return self.lieuA.obtenir_voisins()
    def obtenir_nom_lieu(self):
        return self.lieuA.obtenir_nom()

    def __eq__(self,autre_position):

        if self.obtenir_depart() == autre_position.obtenir_depart():
            if self.a_destination() and autre_position.a_destination():
                return self.obtenir_destination() == autre_position.obtenir_destination() and self.obtenir_distance() == autre_position.obtenir_distance()
            elif not self.a_destination() and not autre_position.a_destination():
                return True
            else:
                return False
        else:
            return False
    
    def verifier_invariants(self):
        assert not(self.lieuB) or self.distance, "La position a une destination alors que la distance restante est indéfinie."
        assert not(self.distance) or self.lieuB, "La position a une distance restante alors qu'elle n'a pas de destination."

        