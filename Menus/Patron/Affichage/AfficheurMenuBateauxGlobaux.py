from .Afficheur import Afficheur

class AfficheurMenuBateauGlobaux(Afficheur):
    def __init__(self,monde,joueur):
        super().__init__()
        self.monde = monde
        self.joueur = joueur
    def afficher(self):
        print("Liste des bateaux")
        for bateau in self.joueur.obtenir_bateaux():
            print(f"{bateau.obtenir_nom()} : {bateau.obtenir_lieu().obtenir_nom()}")