# mon_super_jeu/mouvement.py

from lieu import *
from bateau import *
class Position:
    def __init__(self, lieu_initial):
        assert lieu_initial is not None, "Le lieu initial ne peut pas être None."
        self._lieu_depart = lieu_initial
        self._prochain_lieu = None
        self._distance_totale = None
        self._distance_restante = None
        self.verifier_invariants()

    def obtenir_lieu_actuel(self):
        return self._lieu_depart

    def obtenir_nom_lieu(self):
        return self._lieu_depart.obtenir_nom()

    def obtenir_voisins_lieu(self):
        return self._lieu_depart.obtenir_voisins()

    def est_en_transit(self):
        return self._prochain_lieu is not None and self._distance_restante > 0

    def est_a_mis_chemin_ou_plus(self):
        return self._distance_restante <= self._distance_totale/2

    def debuter_deplacement(self, prochain_lieu, distance = None):
        if distance is None:
            distance = self.calculer_distance_vers(prochain_lieu)
        assert distance > 0, "La distance doit être strictement positive."
        self._prochain_lieu = prochain_lieu
        self._distance_totale = distance
        self._distance_restante = distance
        self.verifier_invariants()

    def calculer_distance_vers(self, autre_lieu):
        if autre_lieu == self._lieu_depart:
            print("⚠️ Appel incorrect à calculer_distance_vers() avec même lieu")
            print(f"    _lieu_depart: {self._lieu_depart}")
            print(f"    autre_lieu  : {autre_lieu}")
            import traceback
            traceback.print_stack(limit=5)  # Affiche la pile d'appels (5 dernières lignes)
            raise ValueError("Appel à calculer_distance_vers avec le même lieu en paramètre.")
        if autre_lieu not in self._lieu_depart.obtenir_voisins():
            raise ValueError(f"{autre_lieu} n’est pas un voisin de {self._lieu_depart}.")
        return self._lieu_depart.obtenir_distance(autre_lieu)

    def avancer(self, vitesse : int):
        if not self.est_en_transit():
            return  0
        assert self._distance_restante, "Impossible d'avancer si la distance restante n'est pas définie"
        distance_parcourue = min(vitesse, self._distance_restante)
        self._distance_restante -= distance_parcourue
        
        if self._distance_restante <= 0:
            assert self._prochain_lieu, "Impossible de passer au noeud suivant si le noeud suivant n'est pas défini"
            self._lieu_depart = self._prochain_lieu
            self._prochain_lieu = None
            self._distance_restante = None
            self._distance_totale = None
        self.verifier_invariants()
        return distance_parcourue

    def est_arrete(self):
        return not self.est_en_transit()

    def est_arrive(self):
        return self._prochain_lieu is None

    # Méthodes d'accès
    def obtenir_lieu_depart(self):
        return self._lieu_depart

    def obtenir_prochain_lieu(self):
        return self._prochain_lieu

    def obtenir_distance_restante(self):
        return self._distance_restante

    def obtenir_distance_totale(self):
        return self._distance_totale
    
    def a_une_destination(self):
        return self._prochain_lieu is not None

    def obtenir_prix_bateau(self, type_bateau : str):
        assert isinstance(self._lieu_depart,Port), "Impossible d'acheter un bateau hors du port."
        return self._lieu_depart.obtenir_prix_bateau(type_bateau)

    def ajouter_bateau(self, bateau):
        self._lieu_depart.ajouter_bateau(bateau)
        self.verifier_invariants()

    def __eq__(self, other):
        return (self._lieu_depart == other._lieu_depart and
                self._prochain_lieu == other._prochain_lieu and
                self._distance_totale == other._distance_totale and
                self._distance_restante == other._distance_restante)

    def verifier_invariants(self):
        if self._distance_restante and self._distance_totale:
            assert self._distance_restante <= self._distance_totale, "Position : La distance restante est supérieure à la distance totale."
        if self._prochain_lieu is None:
            assert self._distance_totale is None, "Position : La distance totale est définie alors qu'il n'y a pas de prochain lieu."
