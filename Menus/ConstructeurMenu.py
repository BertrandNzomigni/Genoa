from __future__ import annotations
from typing import Any, Callable

from .Menu import Menu
from .Patrons.PatronMenuPrincipal import PatronOptionsMenuPrincipal
from .Patrons.PatronMenuBateaux import PatronOptionsMenuBateaux
from .Patrons.PatronMenuDeplacement import PatronOptionsMenuDeplacement
from .Patrons.PatronBateauxGlobaux import PatronOptionsBateauxGlobaux
from .Patrons.PatronMarche import PatronMarche
from .Patrons.PatronMenuBateau import PatronMenuBateau


class ConstructeurMenu:
    """Builds the game's menus from their patrons."""

    def __init__(self, monde, jeu, fabrique_menu: Callable[[Any], Menu] = Menu):
        self.monde = monde
        self.jeu = jeu
        self._fabrique_menu = fabrique_menu

    @property
    def joueur(self):
        return self.monde.obtenir_joueur()

    def _construire(self, patron) -> Menu:
        return self._fabrique_menu(patron)

    def construire_menu_principal(self) -> Menu:
        return self._construire(
            PatronOptionsMenuPrincipal(self.monde, self.jeu, self.joueur))

    def construire_menu_bateaux(self) -> Menu:
        return self._construire(
            PatronOptionsMenuBateaux(self.jeu, self.joueur))

    def construire_menu_bateaux_global(self) -> Menu:
        return self._construire(PatronOptionsBateauxGlobaux(self.jeu, self.joueur))

    def construire_menu_deplacement(self) -> Menu:
        return self._construire(PatronOptionsMenuDeplacement(self.jeu, self.joueur))

    def construire_menu_bateau(self, bateau) -> Menu:
        return self._construire(PatronMenuBateau(self.jeu, self.joueur, bateau))

    def construire_menu_marche(self) -> Menu:
        return self._construire(PatronMarche(self.jeu, self.joueur))

    def construire_menu_achat(self,biens) -> Menu:
        pass

    def construire_menu_vente(self,biens) -> Menu:
        pass
