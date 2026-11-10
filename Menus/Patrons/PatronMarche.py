from Menus.Option import Option
from .Patron import Patron

class PatronMarche(Patron):
    def __init__(self,jeu, joueur):
        super().__init__(jeu)
        self.lieu = joueur.lieu
    def creer_options(self):
        super().creer_options()

        for biens in self.lieu.biens_disponibles():
            self.ajouter_option(f" Acheter {biens}",self.constructeur_menu.construire_menu_achat,biens)
            self.ajouter_option(f" Vendre {biens}",self.constructeur_menu.construire_menu_vente,biens)

        self.ajouter_quitter()

    def afficher(self):
        print("Marché de",self.lieu.obtenir_nom())
        print("-----------------------------------")
        for biens in self.lieu.biens_disponibles():
            print(f"{biens} : {self.lieu.obtenir_prix(biens)} florins")
        print("-----------------------------------")

    def ouvrir_menu_achat(self,biens):
        pass

    def ouvrir_menu_vente(self,biens):
            pass
    

