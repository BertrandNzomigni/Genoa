from .Menu import Menu
from .Patrons.PatronMenuPrincipal import PatronOptionsMenuPrincipal
from .Patrons.PatronMenuBateaux import PatronOptionsMenuBateaux
from .Patrons.PatronMenuDeplacement import PatronOptionsMenuDeplacement
from .Patrons.PatronBateauxGlobaux import PatronOptionsBateauxGlobaux
from .Patrons.PatronMarche import PatronMarche
from Menus.Patrons.PatronMenuBateau import PatronMenuBateau

class ConstructeurMenu:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
        self.joueur = monde.obtenir_joueur()
        self.temps = monde.obtenir_temps()
    def construire_menu_principal(self):
        return Menu(PatronOptionsMenuPrincipal(self.temps,self.monde,self.jeu,self.joueur))
    def construire_menu_bateaux(self):
        return Menu(PatronOptionsMenuBateaux(self.jeu,self.joueur,self.joueur.lieu))
    def construire_menu_bateaux_global(self):
        return Menu(PatronOptionsBateauxGlobaux(self.jeu,self.joueur))
    def construire_menu_deplacement(self):
        return Menu(PatronOptionsMenuDeplacement(self.jeu,self.joueur))
    def construire_menu_bateau(self,bateau):
        return Menu(PatronMenuBateau(self.jeu,self.joueur,bateau))
    def construire_menu_marche(self):
        return Menu(PatronMarche(self.jeu,self.joueur))

