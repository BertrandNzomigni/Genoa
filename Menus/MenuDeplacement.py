from Menus.Menu import Menu

from Menus.Patron.Options.PatronMenuDeplacement import PatronOptionsMenuDeplacement

class MenuDeplacement(Menu):
    def __init__(self,monde,jeu,joueur):
        Menu.__init__(self,monde,jeu)
        self.joueur = joueur
    def charger_options(self):
        self.ajouter_plusieurs_options(PatronOptionsMenuDeplacement(self.jeu,self.joueur).options)
    def afficher_corps(self):
        if not self.joueur.a_destination() :
            print(f"Liste des destinations accesibles depuis {self.joueur.obtenir_lieu().obtenir_nom()}.")
    