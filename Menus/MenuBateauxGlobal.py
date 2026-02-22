from Menus.Menu import Menu

class MenuBateauxGlobal(Menu):
    def __init__(self,joueur,monde,jeu):
        Menu.__init__(self,monde,jeu)
        self.joueur = joueur
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        self.ajouter_options("Quitter",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()])
    def afficher_corps(self):
        print("Liste des bateaux")
        for bateau in self.joueur.obtenir_bateaux():
            print(f"{bateau.obtenir_nom()} : {bateau.obtenir_lieu().obtenir_nom()}")