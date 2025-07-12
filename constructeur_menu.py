# mon_super_jeu/constructeur_menu.py

from menus import (
    MenuPrincipal, MenuBateauxPort, MenuBateauxGlobal, MenuDeplacement,
    MenuMarche, MenuAchat, MenuVente
)


class ConstructeurMenu:
    """Classe 'Factory' pour créer les différents menus du jeu."""

    def __init__(self, monde, jeu):
        self.monde = monde
        self.jeu = jeu

    def construire_menu_principal(self):
        return MenuPrincipal(self.monde, self.jeu, self.monde.obtenir_temps())

    def construire_menu_bateaux_port(self):
        return MenuBateauxPort(self.monde, self.jeu)

    def construire_menu_bateaux_global(self):
        return MenuBateauxGlobal(self.monde.obtenir_joueur(), self.monde, self.jeu)

    def construire_menu_deplacement(self):
        return MenuDeplacement(self.monde, self.jeu)

    def construire_menu_marche(self, bateau):
        return MenuMarche(self.monde, self.jeu, bateau)

    def construire_menu_achat(self, bateau):
        return MenuAchat(self.monde, self.jeu, bateau)

    def construire_menu_vente(self, bateau):
        return MenuVente(self.monde, self.jeu, bateau)

    def construire_menu_achat_bateaux(self):
        return menuAchatBateaux(self.monde,self.jeu,self.monde.obtenir_joueur(),self.monde.obtenir_joueur().obtenir_lieu())





