import constantes
import menus
class MenuMissions(menus.Menu):
    def __init__(self,monde,jeu,bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        i = 1
        self.options[i] = ["Définir un arrét",[constantes.nothing]]
        i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_gestion_bateaux(self.bateau)]]
    def afficher_corps(self):
        print("--- Missions ---")

    
