from Menus.Option import Option


class PatronOptionsMenuDeplacement:
    def __init__(self,jeu,joueur):
        self._options = list()

        constructeur_menu = jeu.obtenir_constructeur_menu()

        if not joueur.a_destination():
            destinations = joueur.obtenir_lieu().obtenir_voisins()
            for destination in destinations:
                self._options.append(Option(destination.obtenir_nom(),[joueur.obtenir_coordinateur().aller_destination,destination],[jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))
        else:
            self._options.append(Option("Faire demi-tour",[joueur.obtenir_coordinateur().faire_demi_tour],[jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))
        self._options.append(Option("Quitter",[jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))

    @property
    def options(self):
        return self._options