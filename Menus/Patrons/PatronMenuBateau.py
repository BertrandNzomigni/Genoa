from .Patron import Patron


class PatronMenuBateau(Patron):
    def __init__(self,jeu,joueur,bateau):
        super().__init__(jeu)
        self.joueur = joueur
        self.bateau = bateau

    def creer_options(self):
        super().creer_options()
        
        if self.joueur.bateau_dirige == None:
            self.ajouter_option("Diriger le bateau",self.joueur.rejoint_bateau,self.bateau)
        elif self.joueur.bateau_dirige == self.bateau:
            self.ajouter_option("Quitter le bateau",self.joueur.quitte_bateau)
        self.ajouter_quitter()


    def afficher(self):
        print("Menu de :",self.bateau.obtenir_nom())
    