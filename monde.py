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

        genes.prix_locaux = {"Soie": 50, "Épices": 20, "Vin": 10, "Bois": 5}
        venise.prix_locaux = {"Soie": 60, "Épices": 25, "Vin": 8, "Bois": 7}

        self.connecter_lieu(genes, mer_med, 5)
        self.connecter_lieu(venise, mer_med, 3)

        self.joueur = Joueur(genes)
        premier_bateau = Bateau("Caraque", BATEAUX["Caraque"]["Capacité"], BATEAUX["Caraque"]["Vitesse"], genes)
        genes.obtenir_lieu().ajouter_bateau(premier_bateau)
        self.joueur.acquerir_bateau(premier_bateau)

        self.temps = Temps(self)

    def obtenir_joueur(self): return self.joueur

    def obtenir_temps(self): return self.temps

    def connecter_lieu(self, lieu1, lieu2, distance):
        lieu1.obtenir_lieu().ajouter_voisin(lieu2, distance)
        lieu2.obtenir_lieu().ajouter_voisin(lieu1, distance)
