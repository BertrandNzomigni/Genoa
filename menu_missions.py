import constantes
import menus
import mission
class MenuMissions(menus.Menu):
    def __init__(self,monde,jeu,bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        i = 1
        self.options[i] = ["Définir un arrét",[self.jeu.changer_menu_actif,constructeur_menu.construre_menu_ajout_arret(self.bateau)]]
        i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_gestion_bateaux(self.bateau,self.bateau.obtenir_mission())]]
    def afficher_corps(self):
        print("--- Arrêts ---")
        for arret in self.bateau.obtenir_arrets():
            print(f"Arrét à {arret.obtenir_nom_lieu()}")

class MenuAjoutArret(menus.Menu):
    def __init__(self,monde,jeu,bateau,mission):
        super().__init__(monde, jeu)
        self.bateau = bateau
        self.mission = mission
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        i = 1
        for port in self.monde.obtenir_ports():
            self.options[i] = [f"Ajouter un arrêt à {port.obtenir_nom()}",[self.bateau.ajouter_arret,mission.Arret(port)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_missions(self.bateau)]]
        


    
