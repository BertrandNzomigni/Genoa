class Patron:
    def __init__(self,jeu):
        self.jeu = jeu
    def creer_options(self):
        self.options = list()
        self.constructeur_menu = self.jeu.obtenir_constructeur_menu()