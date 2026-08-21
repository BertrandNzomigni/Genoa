

from Menus.Patron.Options.PatronMenuBateau import PatronMenuBateau

from .Menu import Menu
from .Patron.Options.PatronMenuPrincipal import PatronOptionsMenuPrincipal
from .Patron.Options.PatronMenuBateaux import PatronOptionsMenuBateaux
from .Patron.Options.PatronMenuDeplacement import PatronOptionsMenuDeplacement
from .Patron.Options.PatronBateauxGlobaux import PatronOptionsBateauxGlobaux

from .Patron.Affichage.AfficheurMenuPrincipal import AfficheurMenuPrincipal
from .Patron.Affichage.AfficheurMenuBateaux import AfficheurMenuBateaux
from .Patron.Affichage.AfficheurMenuDeplacement import AfficheurMenuDeplacement
from .Patron.Affichage.AfficheurMenuBateauxGlobaux import AfficheurMenuBateauGlobaux
from .Patron.Affichage.AfficheurMenuBateau import AfficheurMenuBateau

from .Patron.Affichage.AfficheurMarche import AfficheurMenuMarche

from .Patron.Options.PatronMarche import PatronMarche

class ConstructeurMenu:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
        self.joueur = monde.obtenir_joueur()
        self.temps = monde.obtenir_temps()
    def construire_menu_principal(self):
        return Menu(PatronOptionsMenuPrincipal(self.temps,self.monde,self.jeu,self.joueur),AfficheurMenuPrincipal(self.joueur,self.temps))
    def construire_menu_bateaux(self):
        return Menu(PatronOptionsMenuBateaux(self.jeu,self.joueur),AfficheurMenuBateaux(self.joueur.lieu))
    def construire_menu_bateaux_global(self):
        return Menu(PatronOptionsBateauxGlobaux(self.jeu),AfficheurMenuBateauGlobaux(self.monde,self.joueur))
    def construire_menu_deplacement(self):
        return Menu(PatronOptionsMenuDeplacement(self.jeu,self.joueur),AfficheurMenuDeplacement(self.joueur))
    def construire_menu_bateau(self,bateau):
        return Menu(PatronMenuBateau(self.jeu,self.joueur,bateau),AfficheurMenuBateau(bateau))
    def construire_menu_marche(self):
        return Menu(PatronMarche(self.jeu),AfficheurMenuMarche(self.joueur))

