from .Afficheur import Afficheur

class AfficheurMenuBateaux(Afficheur):
    def __init__(self,lieu_joueur):
        super().__init__()
        self.lieu_joueur = lieu_joueur
    def afficher(self):
        print(f"Liste des bateaux à {self.lieu_joueur.obtenir_nom()} :")