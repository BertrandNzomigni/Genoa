from Jeu.Lieu.Port import Port
from Menus.Option import Option
from .Patron import Patron

class PatronOptionsMenuPrincipal(Patron):
    def __init__(self,temps,monde,jeu):
        super().__init__()
        self.temps = temps
        self.monde = monde
        self.jeu = jeu

    def creer_options(self):
        super().creer_options()

        self.options.append(Option("Jour suivant",[self.temps.avancer]))
        self.options.append(Option("Sélectionner une nouvelle destination",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_deplacement()]))
        self.options.append(Option("Voir l'ensemble de vos bateaux",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateaux_global()]))

        if type(self.monde.obtenir_joueur().obtenir_lieu()) is Port:
            self.options.append(Option("Voir vos bateaux dans le port",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateaux()]))
        
        self.options.append(Option("Quitter le jeu",[self.jeu.quitter]))

        return self.options
