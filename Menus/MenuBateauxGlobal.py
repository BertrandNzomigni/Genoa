from Menus.Menu import Menu
from Menus.Patron.Affichage.AfficheurBateauxGlobaux import AfficheurBateauGlobaux
from Menus.Patron.Options.PatronBateauxGlobaux import PatronOptionsBateauxGlobaux

class MenuBateauxGlobal(Menu):
    def __init__(self,joueur,monde,jeu):
        Menu.__init__(self,monde,jeu)
        self.joueur = joueur
        self.afficheur = AfficheurBateauGlobaux(self.monde,self.joueur)
    def charger_options(self):
        self.ajouter_plusieurs_options(PatronOptionsBateauxGlobaux(self.jeu).options)
    def afficher_corps(self):
        self.afficheur.afficher()