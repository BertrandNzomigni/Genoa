# mon_super_jeu/monde.py

from lieu import Port, Mer
from joueur import Joueur
from bateau import Bateau
from temps import Temps
from constantes import *

class Monde:
    """Contient toutes les entités du jeu (lieux, joueur, etc.)."""

    def __init__(self):
        genes = Port("Gênes")
        venise = Port("Venise")
        mer_med = Mer("Mer Méditerranée")
        self.ports = [genes, venise]
        self.mers = [mer_med]
        self.bateaux = list()
        genes.prix_locaux_marchandises = {"Soie": 50, "Épices": 20, "Vin": 10, "Bois": 5}
        venise.prix_locaux_marchandises = {"Soie": 60, "Épices": 25, "Vin": 8, "Bois": 7}

        #genes.prix_locaux_bateaux = {"Nef": 1000, "Galère": 2000, "Caraque": 3000, "Cocha": 2500}
        #venise.prix_locaux_bateaux = {"Nef": 1000, "Galère": 2000, "Caraque": 3000, "Cocha": 2500}
        
        self.connecter_lieu(genes, mer_med, 100)
        self.connecter_lieu(venise, mer_med, 60)

        self.joueur = Joueur(genes,self)
        premier_bateau = Bateau("Bateau de base", BATEAUX["Caraque"]["Capacité"], BATEAUX["Caraque"]["Vitesse"], genes,"Caraque",self)
        genes.ajouter_bateau(premier_bateau)
        self.joueur.acquerir_bateau(premier_bateau)

        self.temps = Temps(self)

    def obtenir_joueur(self): return self.joueur

    def obtenir_temps(self): return self.temps

    def nouveau_bateau(self,bateau):
        self.bateaux.append(bateau)

    def connecter_lieu(self, lieu1, lieu2, distance):
        lieu1.ajouter_voisin(lieu2, distance)
        lieu2.ajouter_voisin(lieu1, distance)
    def avancer_temps(self):
        for bateau in self.bateaux:
            if bateau.a_destination():
                bateau.avancer()
        self.temps.avancer()
        print("Un jour passe...")
        input("Appuyez sur Entrée pour continuer...")