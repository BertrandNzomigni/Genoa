from Game.Lieu.Port import Port
from Menus.Option import Option
from .Patron import Patron

class PatronOptionsMenuPrincipal(Patron):
    def __init__(self,temps,monde,jeu):
        super().__init__()

        constructeur_menu = jeu.obtenir_constructeur_menu()

        self._options.append(Option("Jour suivant",[temps.avancer]))
        self._options.append(Option("Sélectionner une nouvelle destination",[jeu.changer_menu_actif,constructeur_menu.construire_menu_deplacement()]))
        self._options.append(Option("Voir l'ensemble de vos bateaux",[jeu.changer_menu_actif,constructeur_menu.construire_menu_bateaux_global()]))

        if type(monde.obtenir_joueur().obtenir_lieu()) is Port:
            self._options.append(Option("Voir vos bateaux dans le port",[jeu.changer_menu_actif,constructeur_menu.construire_menu_bateaux()]))
        
        self._options.append(Option("Quitter le jeu",[jeu.quitter]))
