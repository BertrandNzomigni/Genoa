from .Afficheur import Afficheur


class AfficheurMenuPrincipal(Afficheur):
    def __init__(self,joueur,temps):
        super().__init__()
        self.joueur = joueur
        self.temps = temps
    def afficher(self):
        print(f"Jour : {self.temps.obtenir_valeur()}")
        print(f"Vous avez actuellement {self.joueur.obtenir_florins()} florins.")
        if self.joueur.si_voyage_actuellement():
            print(f"Vous naviguez vers {self.joueur.obtenir_destination()}")
            print(f"{self.joueur.lieu} est derrière vous.")
            print(f"La distance restante est de {self.joueur.obtenir_distance_voyage()} kilomètres.")
        else:
            print(f"Vous êtes situé à {self.joueur.lieu}.")
            print("Vous n'êtes pas en cours de déplacement.")