from .Patron import Patron
from Menus.Option import Option


def nothing():
    pass

class PatronOptionsMenuBateaux(Patron):
    def __init__(self, jeu, joueur):
        super().__init__(jeu)
        self.joueur = joueur
    
    def creer_options(self):
        super().creer_options()

        lieu_joueur = self.joueur.position.lieu
        for bateau in lieu_joueur.obtenir_bateaux():
            self.options.append(Option(bateau.obtenir_nom(),[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateau(bateau)]))

        self.options.append(Option("Quitter",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_principal()]))

        return self.options

        