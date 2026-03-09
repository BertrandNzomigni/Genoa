from .Patron import Patron
from Menus.Option import Option


def nothing():
    pass

class PatronOptionsMenuBateau(Patron):
    def __init__(self, bateau, monde, jeu):
        super().__init__()
        self.bateau = bateau
        self.monde = monde
        self.jeu = jeu
    
    def creer_options(self):
        super().creer_options()

        lieu_joueur = self.monde.obtenir_joueur().obtenir_lieu()
        for bateau in lieu_joueur.obtenir_bateaux():
            self.options.append(Option(bateau.obtenir_nom(),[nothing]))

        self.options.append(Option("Quitter",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_principal()]))

        return self.options

        