from __future__ import annotations
from typing import Any, Callable

from .Menu import Menu
from .Patrons.PatronMenuPrincipal import PatronPrincipal
from .Patrons.PatronMenuBateaux import PatronBateaux
from .Patrons.PatronMenuDeplacement import PatronDeplacement
from .Patrons.PatronBateauxGlobaux import PatronBateauxGlobaux
from .Patrons.PatronMarche import PatronMarche
from .Patrons.PatronMenuBateau import PatronBateau


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
            PatronPrincipal(self.monde, self.jeu, self.joueur))

    def construire_menu_bateaux(self) -> Menu:
        return self._construire(
            PatronBateaux(self.jeu, self.joueur))

    def construire_menu_bateaux_global(self) -> Menu:
        return self._construire(PatronBateauxGlobaux(self.jeu, self.joueur))

    def construire_menu_deplacement(self) -> Menu:
        return self._construire(PatronDeplacement(self.jeu, self.joueur))

    def construire_menu_bateau(self, bateau) -> Menu:
        return self._construire(PatronBateau(self.jeu, self.joueur, bateau))

    def construire_menu_marche(self) -> Menu:
        return self._construire(PatronMarche(self.jeu, self.joueur))

    def construire_menu_achat(self,biens) -> Menu:
        pass

    def construire_menu_vente(self,biens) -> Menu:
        pass
