# mon_super_jeu/joueur.py

from mouvement import Itineraire, Deplaceur, CoordinationMouvement


class Joueur:
    """Représente le joueur."""

    def __init__(self, lieu_de_depart):
        self.florins = 2000
        self.lieu = lieu_de_depart
        self.itineraire = Itineraire(self)
        self.deplaceur = Deplaceur(self.itineraire, self)
        self.coord = CoordinationMouvement(self, self.deplaceur, self.itineraire)
        self.bateaux = list()
        self.bateau_dirige = None

    def obtenir_florins(self):
        return self.florins

    def payer(self, montant):
        self.florins -= montant

    def gagner(self, montant):
        self.florins += montant

    def obtenir_itineraire(self):
        return self.itineraire

    def obtenir_lieu(self):
        return self.lieu

    def changer_lieu(self, lieu):
        self.lieu = lieu

    def obtenir_coordinateur(self):
        return self.coord

    def acquerir_bateau(self, bateau):
        self.bateaux.append(bateau)

    def obtenir_bateaux(self):
        return self.bateaux

    def obtenir_bateaux_a_lieu(self, lieu):
        return [b for b in self.bateaux if b.obtenir_lieu() == lieu]

    def obtenir_bateau_dirige(self):
        return self.bateau_dirige

    def rejoindre_bateau(self, bateau):
        if bateau.obtenir_lieu() == self.lieu:
            self.bateau_dirige = bateau
            print(f"Vous prenez le commandement du {bateau.obtenir_nom()}.")
        else:
            print("Le bateau n'est pas ici.")

    def quitter_bateau(self, bateau=None):
        if self.bateau_dirige:
            print(f"Vous quittez le commandement du {self.bateau_dirige.obtenir_nom()}.")
            self.bateau_dirige = None