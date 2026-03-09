from Menus.Menu import Menu
from Menus.Option import Option

def nothing():
    pass

class MenuBateaux(Menu):
    def __init__(self,monde,jeu):
        Menu.__init__(self,monde,jeu)
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        lieu_joueur = self.monde.obtenir_joueur().obtenir_lieu()
        i = 1
        for bateau in lieu_joueur.obtenir_bateaux():
            self.ajouter_options(Option(bateau.obtenir_nom(),[nothing]))
            i += 1
        self.ajouter_options(Option("Quitter",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))
    def afficher_corps(self):
        print(f"Liste des bateaux à {self.monde.obtenir_joueur().obtenir_lieu().obtenir_nom()} :")