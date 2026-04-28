from .Afficheur import Afficheur

class AfficheurMenuMarche(Afficheur):
    def __init__(self,joueur):
        super().__init__()
        self.lieu = joueur.position.lieu
        self.joueur = joueur
    def afficher(self):
        print("Marché de",self.lieu.obtenir_nom())