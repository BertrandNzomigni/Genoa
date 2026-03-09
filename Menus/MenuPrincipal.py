from Menus.Menu import Menu
from Menus.Patron.Affichage.AfficheurMenuPrincipal import AfficheurMenuPrincipal
from Menus.Patron.Options.PatronMenuPrincipal import PatronOptionsMenuPrincipal

# Afficher le menu principal
# Traiter les entrées du menu principal
class MenuPrincipal(Menu):
    def __init__(self,monde,jeu,temps,joueur):
        Menu.__init__(self,monde,jeu)
        self.temps = temps
        self.afficheur = AfficheurMenuPrincipal(joueur,temps)
    def charger_options(self):
        self.ajouter_plusieurs_options(PatronOptionsMenuPrincipal(self.temps,self.monde,self.jeu).options)
        
    def afficher_corps(self):
        self.afficheur.afficher()
