import menus

class MenuInformationBateau(menus.Menu):
    def __init__(self,monde,jeu,bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau
    def charger_options(self):
        self.options[1] = ["Retour",[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_bateaux_global()]]
    def afficher_corps(self):
        print(f"Nom : {self.bateau.obtenir_nom()}")
        print(f"Type : {self.bateau.obtenir_type()}")
        print(f"Capacité : {self.bateau.obtenir_capacite()}")
        print(f"Volume utilisé : {self.bateau.obtenir_volume_utilise()}")
        print(f"Vitesse : {self.bateau.obtenir_vitesse()}")
    
