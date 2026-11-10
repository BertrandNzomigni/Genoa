from Menus.Option import Option
from .Patron import Patron

class PatronOptionsBateauxGlobaux(Patron):
    def __init__(self,jeu,joueur):
        super().__init__(jeu)
        self.joueur = joueur
        
    def creer_options(self):
        super().creer_options()

        self.ajouter_quitter()

    def afficher(self):
        print("Liste des bateaux")
        for bateau in self.joueur.obtenir_bateaux():
            print(f"{bateau.obtenir_nom()} : {bateau.lieu.obtenir_nom()}")