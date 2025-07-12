# mon_super_jeu/jeu.py
# La classe qui orchestre le jeu.

from monde import Monde
from constructeur_menu import ConstructeurMenu
from constantes import clear_screen


class Jeu:
    """Classe principale qui gère la boucle de jeu."""

    def __init__(self):
        self.monde = Monde()
        self.constructeur_menu = ConstructeurMenu(self.monde, self)
        self.menu_actif = self.constructeur_menu.construire_menu_principal()
        self.actif = True

    def obtenir_constructeur_menu(self):
        return self.constructeur_menu

    def changer_menu_actif(self, menu):
        self.menu_actif = menu

    def demarrer(self):
        while self.actif:
            clear_screen()
            self.menu_actif.executer()

    def quitter(self):
        print("Merci d'avoir joué !")
        self.actif = False