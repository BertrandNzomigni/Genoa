# mon_super_jeu/joueur.py

import position
import lieu
from entite import Entite
import bateau


class Joueur(Entite):
    """Représente le joueur."""

    def __init__(self, lieu_de_depart,monde):
        super().__init__(lieu_de_depart)
        self.florins_liquides = 2000 #renommé

        self.bateaux = list()
        self.bateau_dirige = None
        self.monde = monde
        self.verifier_invariants()

    def obtenir_florins(self):
        return self.florins_liquides

    def payer(self, montant):
        self.florins_liquides -= montant
        self.verifier_invariants()

    def gagner(self, montant):
        self.florins_liquides += montant
        self.verifier_invariants()

    def acquerir_bateau(self, bateau):
        self.bateaux.append(bateau)
        self.verifier_invariants()

    def obtenir_bateaux(self):
        return self.bateaux

    def obtenir_bateaux_a_lieu(self, lieu):
        return [b for b in self.bateaux if b.obtenir_lieu() == lieu]

    def obtenir_bateau_dirige(self):
        return self.bateau_dirige

    def dirige_bateau(self):
        return self.bateau_dirige != None

    def rejoindre_bateau(self, bateau):
        
        self.bateau_dirige = bateau
        bateau.ajouter_passager(self)
        print(f"Vous prenez le commandement du {bateau.obtenir_nom()}.")
        self.verifier_invariants()

    def quitter_bateau(self):
        assert(self.bateau_dirige), "Le joueur ne peut pas quitter un bateau si il n'est pas sur un bateau."
        print(f"Vous quittez le commandement du {self.bateau_dirige.obtenir_nom()}.")
        self.bateau_dirige.retirer_passager(self)
        self.bateau_dirige = None
        self.verifier_invariants()

    def acheter_bateau(self,type_bateau,nom):
        from constantes import BATEAUX
        from bateau import Bateau
        from lieu import Port
        assert isinstance(self.position.obtenir_lieu_actuel(),Port), "Le joueur peut acheter un bateau seulement dans les ports."
        prix = self.position.obtenir_prix_bateau(type_bateau)
        
        vitesse = BATEAUX[type_bateau]["Vitesse"]
        capacite = BATEAUX[type_bateau]["Capacité"]
        nouveau_bateau = Bateau(nom,capacite,vitesse,self.position.obtenir_lieu_actuel(),type_bateau,self.monde)
        self.acquerir_bateau(nouveau_bateau)
        self.position.ajouter_bateau(nouveau_bateau)
        self.payer(prix)
        self.verifier_invariants()

    def peut_acheter_bateau(self,type_bateau):
        prix = self.position.obtenir_prix_bateau(type_bateau)
        if self.obtenir_florins() < prix:
            return "Pas assez d'argent"
        return

    def suivre_bateau(self,position):
        from copy import copy
        self.position = copy(position)
        self.verifier_invariants()

    def changer_destination(self,destination):
        if self.bateau_dirige:
            self.bateau_dirige.changer_destination(destination)
        else:
            super().changer_destination(destination)
        self.verifier_invariants()
    
    def obtenir_prochaine_etape(self):
        if self.bateau_dirige:
            return self.bateau_dirige.obtenir_prochaine_etape()
        else:
            return super().obtenir_prochaine_etape()

    def a_une_destination_proche(self):
        if self.bateau_dirige:
            return self.bateau_dirige.a_une_destination_proche()
        else:
            return super().a_une_destination_proche()
    
    def obtenir_distance_prochaine_etape(self):
        if self.bateau_dirige:
            return self.bateau_dirige.obtenir_distance_prochaine_etape()
        else:
            return super().obtenir_distance_restante_prochaine_etape()

    def avancer(self):
        super().avancer()
        self.verifier_invariants()
    
    def verifier_invariants(self):
        from bateau import Bateau
        from position import Position

        super().verifier_invariants()
        assert isinstance(self.position, Position), "La position du joueur doit être une instance de Position."
        assert self.bateau_dirige is None or isinstance(self.bateau_dirige, Bateau), "Le bateau dirigé par le joueur doit être une instance de Bateau."
        for bateau in self.bateaux:
            assert isinstance(bateau, Bateau), "Tous les bateaux du joueur doivent être des instances de Bateau."
        assert self.florins_liquides >= 0, "Le joueur ne peut pas avoir un montant négatif de florins."
        if self.bateau_dirige:
            assert self.bateau_dirige in self.bateaux, "Le bateau dirigé par le joueur doit être dans sa liste de bateaux."
            assert self.bateau_dirige.obtenir_lieu() == self.position.obtenir_lieu_actuel(), "Le bateau dirigé par le joueur doit être au même lieu que la position du joueur."