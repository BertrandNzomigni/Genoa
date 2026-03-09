from .Patron import Patron
from Menus.Option import Option


def nothing():
    pass

class PatronOptionsMenuBateau(Patron):
    def __init__(self, bateau, monde, jeu):
        super().__init__()

        constructeur_menu = jeu.obtenir_constructeur_menu()
        lieu_joueur = monde.obtenir_joueur().obtenir_lieu()
        for bateau in lieu_joueur.obtenir_bateaux():
            self.options.append(Option(bateau.obtenir_nom(),[nothing]))

        self.options.append(Option("Quitter",[jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))

        