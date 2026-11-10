from .Patron import Patron


def nothing():
    pass

class PatronBateaux(Patron):
    def __init__(self, jeu, joueur):
        super().__init__(jeu)
        self.joueur = joueur
        self.lieu_joueur = self.joueur.lieu
    def creer_options(self):
        super().creer_options()

        for bateau in self.lieu_joueur.obtenir_bateaux():
            self.ajouter_option(bateau.obtenir_nom(),self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateau(bateau))

        self.ajouter_quitter()
        
    def afficher(self):
        print(f"Liste des bateaux à {self.lieu_joueur.obtenir_nom()} :")

        