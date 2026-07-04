from Menus.Option import Option
from .Patron import Patron

class PatronOptionsMenuDeplacement(Patron):
    def __init__(self,jeu,joueur):
        super().__init__(jeu)
        self.joueur = joueur
        
    def creer_options(self):
        super().creer_options()

        if not self.joueur.a_destination():
            destinations = self.joueur.lieu_voisins()
            for destination in destinations:
                self.options.append(Option(destination.obtenir_nom(),[self.joueur.aller_destination,destination],[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_principal()]))
        else:
            self.options.append(Option("Faire demi-tour",[self.joueur.faire_demi_tour],[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_principal()]))
        self.options.append(Option("Quitter",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_principal()]))

        return self.options