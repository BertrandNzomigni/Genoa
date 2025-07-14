from menus import *
from constantes import *
from mission_schema import MissionSchema
class MenuGestionBateau(Menu):
    def __init__(self, monde, jeu, bateau,joueur):
        super().__init__(monde, jeu)
        self.bateau = bateau
        self.joueur = joueur
    def charger_options(self):
        i = 1
        if self.joueur.obtenir_bateau_dirige() == self.bateau:
            self.options[i]= ["Quitter le commandement",[self.joueur.quitter_bateau,self.bateau]]
        else:
            self.options[i]= ["Prendre le commandement",[self.joueur.rejoindre_bateau,self.bateau]]
        i += 1
        if self.bateau.a_mission():
            mission_schema = MissionSchema(self.bateau.obtenir_mission())
            self.options[i] = ["Envoyer en mission",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_missions(mission_schema,self.bateau)]]
            i += 1
        else:
            self.options[i] = ["Envoyer en mission",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_missions(None,self.bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_bateaux_port()]]
    def afficher_corps(self):
        print("---Menu de gestion---")
        print(f"Nom du bateau : {self.bateau}")
        print(f"Type : {self.bateau.obtenir_type()}")