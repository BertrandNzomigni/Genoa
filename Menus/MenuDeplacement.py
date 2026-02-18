from Menus.Menu import Menu

class MenuDeplacement(Menu):
    def __init__(self,monde,jeu):
        Menu.__init__(self,monde,jeu)
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        self.pas_en_chemin = not self.monde.obtenir_joueur().obtenir_itineraire().a_destination()
        if self.pas_en_chemin :
            destinations = self.monde.obtenir_joueur().obtenir_lieu().obtenir_lieu().obtenir_voisins()
            i = 1
            for destination in destinations:
                self.options[i] = [destination.obtenir_nom(),[self.monde.obtenir_joueur().obtenir_coordinateur().aller_destination,destination],[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]]
                i += 1
            self.options[i] = ["Quitter",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]]
        else:
            self.options[1] = ["Faire demi-tour",[self.monde.obtenir_joueur().obtenir_coordinateur().faire_demi_tour],[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]]
            self.options[2] = ["Quitter",[self.jeu.changer_menu_actif,constructeur_menu.construire_menu_principal()]]
    def afficher_corps(self):
        if self.pas_en_chemin :
            print(f"Liste des destinations accesibles depuis {self.monde.obtenir_joueur().obtenir_lieu().obtenir_nom()}.")
    