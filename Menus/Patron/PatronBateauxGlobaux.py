from Menus.Option import Option

class PatronOptionsBateauxGlobaux:
    def __init__(self,jeu):
        self._options = list()
        constructeur_menu = jeu.obtenir_constructeur_menu()
        self.options.append(Option("Quitter",[jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))

    @property
    def options(self):
        return self._options