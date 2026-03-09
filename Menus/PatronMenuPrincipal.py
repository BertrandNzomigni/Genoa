from Game.Lieu.Port import Port
from Menus.Option import Option

class PatronOptionsMenuPrincipal:
    def __init__(self,temps,monde,jeu):
        self.temps = temps
        self.monde = monde
        self.jeu = jeu
        self._options = list()

        constructeur_menu = self.jeu.obtenir_constructeur_menu()

        self._options.append(Option("Jour suivant",[self.temps.avancer]))
        self._options.append(Option("Sélectionner une nouvelle destination",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_deplacement()]))
        self._options.append(Option("Voir l'ensemble de vos bateaux",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_bateaux_global()]))

        if type(self.monde.obtenir_joueur().obtenir_lieu()) is Port:
            self._options.append(Option("Voir vos bateaux dans le port",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_bateaux()]))
        
        self._options.append(Option("Quitter le jeu",[self.jeu.quitter]))

    @property
    def options(self):
        return self._options
