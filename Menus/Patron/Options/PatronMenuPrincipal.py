from Jeu.Lieu.Port import Port
from Menus.Option import Option
from .Patron import Patron

class PatronOptionsMenuPrincipal(Patron):
    def __init__(self,temps,monde,jeu,joueur):
        super().__init__(jeu)
        self.temps = temps
        self.monde = monde
        self.joueur = joueur

    def creer_options(self):
        super().creer_options()

        self.options.append(Option("Jour suivant",[self.temps.avancer]))

        is_located_in_port = type(self.joueur.obtenir_lieu()) is Port

        if is_located_in_port:
            self.options.append(Option("Aller au marché",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_marche()]))

        if self.joueur.dirige_actuellement_un_bateau():
            self.options.append(Option("Sélectionner une nouvelle destination",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_deplacement()]))
        self.options.append(Option("Voir l'ensemble de vos bateaux",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateaux_global()]))

        if is_located_in_port:
            self.options.append(Option("Voir vos bateaux dans le port",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateaux()]))
        
        self.options.append(Option("Quitter le jeu",[self.jeu.quitter]))

        return self.options
