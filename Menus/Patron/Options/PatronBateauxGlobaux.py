from Menus.Option import Option
from .Patron import Patron

class PatronOptionsBateauxGlobaux(Patron):
    def __init__(self,jeu):
        super().__init__()
        
        constructeur_menu = jeu.obtenir_constructeur_menu()
        self.options.append(Option("Quitter",[jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))