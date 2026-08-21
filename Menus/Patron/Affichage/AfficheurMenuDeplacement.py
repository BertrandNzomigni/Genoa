from .Afficheur import Afficheur
from Jeu.Joueur import Joueur

class AfficheurMenuDeplacement(Afficheur):
    def __init__(self,joueur : Joueur):
        super().__init__()
        self.joueur = joueur
    def afficher(self):
        if not self.joueur.si_voyage_actuellement():
            print(f"Liste des destinations accesibles depuis {self.joueur.lieu.obtenir_nom()}.")