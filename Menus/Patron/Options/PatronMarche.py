from Menus.Option import Option
from .Patron import Patron

class PatronMarche(Patron):
    def __init__(self,jeu):
        super().__init__(jeu)
        
    def creer_options(self):
        super().creer_options()

        self.options.append(Option("Quitter",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_principal()]))
        return self.options