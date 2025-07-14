# mon_super_jeu/joueur.py

import position
import lieu
import constantes
import bateau


class Joueur:
    """Représente le joueur."""

    def __init__(self, lieu_de_depart,monde):
        self.florins_liquides = 2000 #renommé
        self.position = position.Position(lieu_de_depart)

        self.bateaux = list()
        self.bateau_dirige = None
        self.monde = monde
        self.verifier_invariants()
    
    def est_parti(self):
        return self.position.est_en_voyage()

    def obtenir_florins(self):
        return self.florins_liquides

    def payer(self, montant):
        self.florins_liquides -= montant
        self.verifier_invariants()

    def gagner(self, montant):
        self.florins_liquides += montant
        self.verifier_invariants()

    def obtenir_lieu(self):
        return self.position.obtenir_depart()

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
        self.position = self.bateau_dirige.obtenir_position()
        print(f"Vous prenez le commandement du {bateau.obtenir_nom()}.")
        self.verifier_invariants()

    def quitter_bateau(self, bateau=None):
        assert(self.bateau_dirige), "Le joueur ne peut pas quitter un bateau si il n'est pas sur un bateau."
        print(f"Vous quittez le commandement du {self.bateau_dirige.obtenir_nom()}.")
        self.bateau_dirige = None
        self.position = position.Position(self.position.obtenir_depart())
        self.verifier_invariants()
    
    def a_destination(self):
        return self.position.a_destination()

    def changer_destination(self,dest):
        self.position.changer_destination(dest)
        self.verifier_invariants()
    
    def obtenir_destination(self):
        return self.position.obtenir_destination()
    
    def obtenir_distance_voyage(self):
        return self.position.obtenir_distance()

    def faire_demi_tour(self):
        self.position.faire_demi_tour()
        self.verifier_invariants()

    def acheter_bateau(self,type_bateau,nom):
        assert isinstance(self.position.obtenir_depart(),lieu.Port), "Le joueur peut acheter un bateau seulement dans les ports."
        prix = self.position.obtenir_prix_bateau(type_bateau)
        
        vitesse = constantes.BATEAUX[type_bateau]["Vitesse"]
        capacite = constantes.BATEAUX[type_bateau]["Capacité"]
        nouveau_bateau = bateau.Bateau(nom,capacite,vitesse,self.position.obtenir_depart(),type_bateau,self.monde)
        self.acquerir_bateau(nouveau_bateau)
        self.position.ajouter_bateau(nouveau_bateau)
        self.payer(prix)
        self.verifier_invariants()
    def peut_acheter_bateau(self,type_bateau):
        prix = self.position.obtenir_prix_bateau(type_bateau)
        if self.obtenir_florins() < prix:
            return "Pas assez d'argent"
        return
    def obtenir_voisins_lieu(self):
        return self.position.obtenir_voisins_lieu()
    def obtenir_nom_lieu(self):
        return self.position.obtenir_nom_lieu()
    def verifier_invariants(self):
        if self.bateau_dirige:
            assert self.bateau_dirige.obtenir_position() == self.position, "Le joueur n'est pas à la même position que le bateau qu'il dirige."
        assert self.florins_liquides >= 0, "Le joueur a un solde de florins négatif."
        if self.a_destination():
            assert not(isinstance(self.position.obtenir_destination(),lieu.Mer)) or self.bateau_dirige, "Le joueur a pour destination une mer alors qu'il ne dirige pas de bateau."
