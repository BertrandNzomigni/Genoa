from menus import *
from constantes import *

class MenuGestionBateau(Menu):
    def __init__(self, monde, jeu, bateau,joueur):
        super().__init__(monde, jeu)
        self.bateau = bateau
        self.joueur = joueur
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        i = 1
        if self.joueur.obtenir_bateau_dirige() == self.bateau:
            self.options[i]= ["Quitter le commandement",[self.joueur.quitter_bateau,self.bateau]]
        else:
            self.options[i]= ["Prendre le commandement",[self.joueur.rejoindre_bateau,self.bateau]]
        i += 1
        self.options[i] = ["Envoyer en mission",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_missions(self.bateau)]]
        i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_bateaux_port()]]
    def afficher_corps(self):
        print("---Menu de gestion---")
        print(f"Nom du bateau : {self.bateau}")
        print(f"Type : {self.bateau.obtenir_type()}")