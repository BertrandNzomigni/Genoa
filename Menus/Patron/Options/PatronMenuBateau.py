from Menus.Option import Option

from .Patron import Patron


class PatronMenuBateau(Patron):
    def __init__(self,jeu,joueur,bateau):
        super().__init__(jeu)
        self.joueur = joueur
        self.bateau = bateau

    def creer_options(self):
        super().creer_options()
        
        if self.joueur.bateau_dirige == None:
            self.options.append(Option("Diriger le bateau",[self.joueur.rejoint_bateau,self.bateau]))
        elif self.joueur.bateau_dirige == self.bateau:
            self.options.append(Option("Quitter le bateau",[self.joueur.quitte_bateau]))
        self.options.append(Option("Quitter",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_bateaux()]))
        return self.options
    