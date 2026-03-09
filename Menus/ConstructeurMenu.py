from .Menu import Menu
from .Patron.Options.PatronMenuPrincipal import PatronOptionsMenuPrincipal
from .Patron.Options.PatronMenuBateau import PatronOptionsMenuBateau
from .Patron.Options.PatronMenuDeplacement import PatronOptionsMenuDeplacement
from .Patron.Options.PatronBateauxGlobaux import PatronOptionsBateauxGlobaux

from .Patron.Affichage.AfficheurMenuPrincipal import AfficheurMenuPrincipal
from .Patron.Affichage.AfficheurMenuBateaux import AfficheurMenuBateau
from .Patron.Affichage.AfficheurMenuDeplacement import AfficheurMenuDeplacement
from .Patron.Affichage.AfficheurMenuBateauxGlobaux import AfficheurMenuBateauGlobaux


class ConstructeurMenu:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
        self.joueur = monde.obtenir_joueur()
        self.temps = monde.obtenir_temps()
    def construire_menu_principal(self):
        return Menu(PatronOptionsMenuPrincipal(self.temps,self.monde,self.jeu),AfficheurMenuPrincipal(self.joueur,self.temps))
    def construire_menu_bateaux(self):
        return Menu(PatronOptionsMenuBateau(self.joueur.obtenir_lieu(),self.monde,self.jeu),AfficheurMenuBateau(self.joueur.obtenir_lieu()))
    def construire_menu_bateaux_global(self):
        return Menu(PatronOptionsBateauxGlobaux(self.jeu),AfficheurMenuBateauGlobaux(self.monde,self.joueur))
    def construire_menu_deplacement(self):
        return Menu(PatronOptionsMenuDeplacement(self.jeu,self.joueur),AfficheurMenuDeplacement(self.joueur))
