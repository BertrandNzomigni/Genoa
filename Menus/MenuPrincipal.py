from Menus.Menu import Menu
from Game.Lieu.Port import Port
from Menus.Option import Option

# Afficher le menu principal
# Traiter les entrées du menu principal
class MenuPrincipal(Menu):
    def __init__(self,monde,jeu,temps):
        Menu.__init__(self,monde,jeu)
        self.temps = temps
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()

        self.ajouter_options(Option("Jour suivant",[self.temps.avancer]))
        
        self.ajouter_options(Option("Sélectionner une nouvelle destination",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_deplacement()]))

        self.ajouter_options(Option("Voir l'ensemble de vos bateaux",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_bateaux_global()]))

        if type(self.monde.obtenir_joueur().obtenir_lieu()) is Port:
            self.ajouter_options(Option("Voir vos bateaux dans le port",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_bateaux()]))

        self.ajouter_options(Option("Quitter le jeu",[self.jeu.quitter]))
        
    def afficher_corps(self):
        j = self.monde.obtenir_joueur()
        print(f"Jour : {self.monde.obtenir_temps().obtenir_valeur()}")
        print(f"Vous avez actuellement {j.obtenir_florins()} florins.")
        if j.obtenir_itineraire().a_destination():
            print(f"Vous naviguez vers {j.obtenir_itineraire().obtenir_destination()}")
            print(f"{j.obtenir_itineraire().obtenir_depart()} est derrière vous.")
            print(f"La distance restante est de {j.obtenir_itineraire().obtenir_distance()*10} kilomètres.")
        else:
            print(f"Vous êtes situé à {j.obtenir_lieu()}.")
            print("Vous n'êtes pas en cours de déplacement.")
