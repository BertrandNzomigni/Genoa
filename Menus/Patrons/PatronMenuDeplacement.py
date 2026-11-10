from Menus.Option import Option
from .Patron import Patron

class PatronOptionsMenuDeplacement(Patron):
    def __init__(self,jeu,joueur):
        super().__init__(jeu)
        self.joueur = joueur
        
    def creer_options(self):
        super().creer_options()

        if not self.joueur.si_voyage_actuellement():
            destinations = self.joueur.lieu_voisins()
            for destination in destinations:
                self.introduire_nom_option(destination.obtenir_nom())
                self.ajouter_une_fonction(self.joueur.commencer_voyage,destination)
                self.ajouter_une_fonction(self.jeu.quitter_menu_actif)
                self.envoyer_option()
        else:
            self.introduire_nom_option("Faire demi-tour")
            self.ajouter_une_fonction(self.joueur.faire_demi_tour)
            self.ajouter_une_fonction(self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_principal())
            self.envoyer_option()
        
        self.ajouter_quitter()
    def afficher(self):
        if not self.joueur.si_voyage_actuellement():
            print(f"Liste des destinations accesibles depuis {self.joueur.lieu.obtenir_nom()}.")