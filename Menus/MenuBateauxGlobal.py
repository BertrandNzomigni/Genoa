from Menus.Menu import Menu
from Menus.Option import Option
from Menus.Patron.PatronBateauxGlobaux import PatronOptionsBateauxGlobaux

class MenuBateauxGlobal(Menu):
    def __init__(self,joueur,monde,jeu):
        Menu.__init__(self,monde,jeu)
        self.joueur = joueur
    def charger_options(self):
        self.ajouter_plusieurs_options(PatronOptionsBateauxGlobaux(self.jeu).options)
    def afficher_corps(self):
        print("Liste des bateaux")
        for bateau in self.joueur.obtenir_bateaux():
            print(f"{bateau.obtenir_nom()} : {bateau.obtenir_lieu().obtenir_nom()}")