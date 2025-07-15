# mon_super_jeu/monde.py

from lieu import Port, Mer
from joueur import Joueur
from bateau import Bateau


from constantes import BATEAUX
class Monde:
    """Contient toutes les entités du jeu (lieux, joueur, etc.)."""

    def __init__(self):
        prix_genes = {"Soie": 50, "Épices": 20, "Vin": 10, "Bois": 5}
        prix_venise = {"Soie": 60, "Épices": 25, "Vin": 8, "Bois": 7}
        genes = Port("Gênes",prix_genes)
        venise = Port("Venise",prix_venise)
        mer_med = Mer("Mer Méditerranée")
        self.ports = [genes, venise]
        self.mers = [mer_med]
        self.bateaux = list()

        #genes.prix_locaux_bateaux = {"Nef": 1000, "Galère": 2000, "Caraque": 3000, "Cocha": 2500}
        #venise.prix_locaux_bateaux = {"Nef": 1000, "Galère": 2000, "Caraque": 3000, "Cocha": 2500}
        
        genes.ajouter_voisin(mer_med,100)
        venise.ajouter_voisin(mer_med,60)

        self.joueur = Joueur(genes,self)
        from temps import Temps
        premier_bateau = Bateau("Bateau de base", BATEAUX["Bateau de test"]["Capacité"], BATEAUX["Bateau de test"]["Vitesse"], genes,"Bateau de test",self)
        genes.ajouter_bateau(premier_bateau)
        self.joueur.acquerir_bateau(premier_bateau)

        self.temps = Temps(self)

    def obtenir_joueur(self): return self.joueur

    def obtenir_temps(self): return self.temps

    def nouveau_bateau(self,bateau):
        self.bateaux.append(bateau)

    def obtenir_ports(self):
        return self.ports
        
    def obtenir_mers(self):
        return self.mers
    def avancer_temps(self):
        for bateau in self.bateaux:
            condition = bateau.a_un_itineraire() and not bateau.itineraire_est_termine()
            if condition:
                bateau.avancer()

        for port in self.ports:
            port.banque.calculer_interets_journaliers()

        self.temps.avancer()
        print("Un jour passe...")
        input("Appuyez sur Entrée pour continuer...")