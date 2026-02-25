from Menus.MenuPrincipal import MenuPrincipal
from Menus.MenuBateaux import MenuBateaux
from Menus.MenuBateauxGlobal import MenuBateauxGlobal
from Menus.MenuDeplacement import MenuDeplacement


class ConstructeurMenu:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
        self.joueur = monde.obtenir_joueur()
    def construire_menu_principal(self):
        return MenuPrincipal(self.monde,self.jeu,self.monde.obtenir_temps())
    def construire_menu_bateaux(self):
        return MenuBateaux(self.monde,self.jeu)
    def construire_menu_bateaux_global(self):
        return MenuBateauxGlobal(self.monde.obtenir_joueur(),self.monde,self.jeu)
    def construire_menu_deplacement(self):
        return MenuDeplacement(self.monde,self.jeu,self.joueur)
