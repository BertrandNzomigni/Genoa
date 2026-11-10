from Jeu.Lieu.Port import Port
from Menus.Option import Option
from .Patron import Patron

class PatronOptionsMenuPrincipal(Patron):
    def __init__(self,monde,jeu,joueur):
        super().__init__(jeu)
        self.monde = monde
        self.joueur = joueur

    def creer_options(self):
        super().creer_options()

        self.ajouter_option("Jour suivant",self.monde.avancer_temps)

        is_located_in_port = type(self.joueur.obtenir_lieu()) is Port

        if is_located_in_port:
            self.ajouter_option("Aller au marché",self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_marche())

        if self.joueur.dirige_actuellement_un_bateau():
            self.ajouter_option("Sélectionner une nouvelle destination",self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_deplacement())
        self.ajouter_option("Voir l'ensemble de vos bateaux",self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateaux_global())


        if is_located_in_port:
            self.ajouter_option("Voir vos bateaux dans le port",self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateaux())
        
        self.ajouter_option("Quitter le jeu",self.jeu.quitter)
    
    def afficher(self):
        print(f"Jour : {self.monde.obtenir_temps()}")
        print(f"Vous avez actuellement {self.joueur.obtenir_florins()} florins.")
        if self.joueur.si_voyage_actuellement():
            print(f"Vous naviguez vers {self.joueur.obtenir_destination()}")
            print(f"{self.joueur.lieu} est derrière vous.")
            print(f"La distance restante est de {self.joueur.obtenir_distance_voyage()} kilomètres.")
        else:
            print(f"Vous êtes situé à {self.joueur.lieu}.")
            print("Vous n'êtes pas en cours de déplacement.")
