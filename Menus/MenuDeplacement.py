from Menus.Menu import Menu

from Menus.Patron.Affichage.AfficheurMenuDeplacement import AfficheurMenuDeplacement
from Menus.Patron.Options.PatronMenuDeplacement import PatronOptionsMenuDeplacement

class MenuDeplacement(Menu):
    def __init__(self,monde,jeu,joueur):
        Menu.__init__(self,monde,jeu)
        self.joueur = joueur
        self.afficheur = AfficheurMenuDeplacement(self.joueur)
    def charger_options(self):
        self.ajouter_plusieurs_options(PatronOptionsMenuDeplacement(self.jeu,self.joueur).options)
    def afficher_corps(self):
        self.afficheur.afficher()
    