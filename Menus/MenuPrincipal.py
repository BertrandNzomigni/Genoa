from Menus.Menu import Menu
from Game.Lieu.Port import Port
from Menus.Option import Option
from Menus.PatronMenuPrincipal import PatronOptionsMenuPrincipal

# Afficher le menu principal
# Traiter les entrées du menu principal
class MenuPrincipal(Menu):
    def __init__(self,monde,jeu,temps):
        Menu.__init__(self,monde,jeu)
        self.temps = temps
    def charger_options(self):
        self.ajouter_plusieurs_options(PatronOptionsMenuPrincipal(self.temps,self.monde,self.jeu).options)
        
    def afficher_corps(self):
        j = self.monde.obtenir_joueur()
        print(f"Jour : {self.monde.obtenir_temps().obtenir_valeur()}")
        print(f"Vous avez actuellement {j.obtenir_florins()} florins.")
        if j.obtenir_itineraire().a_destination():
            print(f"Vous naviguez vers {j.obtenir_itineraire().obtenir_destination()}")
            print(f"{j.obtenir_itineraire().obtenir_depart()} est derrière vous.")
            print(f"La distance restante est de {j.obtenir_itineraire().obtenir_distance()} kilomètres.")
        else:
            print(f"Vous êtes situé à {j.obtenir_lieu()}.")
            print("Vous n'êtes pas en cours de déplacement.")
