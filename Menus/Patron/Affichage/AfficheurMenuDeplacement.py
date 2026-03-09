from .Afficheur import Afficheur


class AfficheurMenuDeplacement(Afficheur):
    def __init__(self,joueur):
        super().__init__()
        self.joueur = joueur
    def afficher(self):
        if not self.joueur.a_destination():
            print(f"Liste des destinations accesibles depuis {self.joueur.obtenir_lieu().obtenir_nom()}.")