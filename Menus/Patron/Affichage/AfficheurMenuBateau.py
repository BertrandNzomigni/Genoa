from .Afficheur import Afficheur

class AfficheurMenuBateau(Afficheur):
    def __init__(self,bateau):
        super().__init__()
        self.bateau = bateau
    def afficher(self):
        print("Menu de :",self.bateau.obtenir_nom())