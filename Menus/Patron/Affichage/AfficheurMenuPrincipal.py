from .Afficheur import Afficheur


class AfficheurMenuPrincipal(Afficheur):
    def __init__(self,joueur,temps):
        super().__init__()
        self.joueur = joueur
        self.temps = temps
    def afficher(self):
        print(f"Jour : {self.temps.obtenir_valeur()}")
        print(f"Vous avez actuellement {self.joueur.obtenir_florins()} florins.")
        if self.joueur.obtenir_itineraire().a_destination():
            print(f"Vous naviguez vers {self.joueur.obtenir_itineraire().obtenir_destination()}")
            print(f"{self.joueur.obtenir_itineraire().obtenir_depart()} est derrière vous.")
            print(f"La distance restante est de {self.joueur.obtenir_itineraire().obtenir_distance()} kilomètres.")
        else:
            print(f"Vous êtes situé à {self.joueur.obtenir_lieu()}.")
            print("Vous n'êtes pas en cours de déplacement.")