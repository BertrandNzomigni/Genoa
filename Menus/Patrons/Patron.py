from Menus.Option import Option

class Patron:
    def __init__(self,jeu):
        self.jeu = jeu
        self.constructeur_menu = self.jeu.obtenir_constructeur_menu()
        self.temp = list()

    def creer_options(self):
        self.options = list()
        
    def ajouter_option(self,texte,fonction,*arguments):
        self.options.append(Option(texte, [fonction] + list(arguments)))

    def obtenir_options(self):
        return self.options

    def ajouter_quitter(self):
        self.ajouter_option("Quitter",self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_principal())

    def introduire_nom_option(self,texte):
        self.nom_temp = texte

    def ajouter_une_fonction(self,fonction,*arguments):
        self.temp.append([fonction] + list(arguments))

    def envoyer_option(self):
        self.options.append(Option(self.nom_temp,*self.temp))

    def afficher(self):
        pass