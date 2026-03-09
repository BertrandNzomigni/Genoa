from Menus.Menu import Menu
from Menus.Option import Option
from Menus.Patron.Affichage.AfficheurBateaux import AfficheurBateau
from Menus.Patron.Options.PatronMenuBateau import PatronOptionsMenuBateau

class MenuBateaux(Menu):
    def __init__(self,monde,jeu):
        Menu.__init__(self,monde,jeu)
        self.afficheur = AfficheurBateau(self.monde.obtenir_joueur().obtenir_lieu())
    def charger_options(self):
        self.ajouter_plusieurs_options(PatronOptionsMenuBateau(self.monde.obtenir_joueur().obtenir_lieu(),self.monde,self.jeu).options)
    def afficher_corps(self):
        self.afficheur.afficher()