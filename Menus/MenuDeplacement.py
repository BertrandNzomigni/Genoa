from Menus.Menu import Menu

from Menus.Option import Option

class MenuDeplacement(Menu):
    def __init__(self,monde,jeu,joueur):
        Menu.__init__(self,monde,jeu)
        self.joueur = joueur
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        self.pas_en_chemin = not self.joueur.a_destination()
        if self.pas_en_chemin :
            destinations = self.joueur.obtenir_lieu().obtenir_voisins()
            for destination in destinations:
                self.ajouter_options(Option(destination.obtenir_nom(),[self.joueur.obtenir_coordinateur().aller_destination,destination],[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))
            self.ajouter_options(Option("Quitter",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))
        else:
            self.ajouter_options(Option("Faire demi-tour",[self.joueur.obtenir_coordinateur().faire_demi_tour],[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))
            self.ajouter_options(Option("Quitter",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]))
    def afficher_corps(self):
        if self.pas_en_chemin :
            print(f"Liste des destinations accesibles depuis {self.joueur.obtenir_lieu().obtenir_nom()}.")
    