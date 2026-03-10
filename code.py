import os

from Menus.ConstructeurMenu import ConstructeurMenu

from Jeu.Monde import Monde

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Jeu:
    def __init__(self):
        self.monde = Monde()
        self.constructeur_menu = ConstructeurMenu(self.monde,self)
        self.menu_actif = self.constructeur_menu.construire_menu_principal()
        self.actif = True
    def obtenir_constructeur_menu(self):
        return self.constructeur_menu
    def changer_menu_actif(self,menu):
        self.menu_actif = menu
    def demarrer(self):
        while self.actif:
            clear_screen()
            self.menu_actif.executer()
        clear_screen()
    def quitter(self):
        self.actif = False
        
if __name__ == "__main__":
    jeu = Jeu()
    jeu.demarrer()

