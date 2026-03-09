class Menu:
    def __init__(self,patron,afficheur):
        self.options = dict()
        self.patron = patron
        self.afficheur = afficheur
    def executer(self):
        self.options.clear()
        self.ajouter_plusieurs_options(self.patron.creer_options())
        self.afficheur.afficher()
        self.afficher_options()
        self.lire()

    def afficher_options(self):
        for i in range(1,len(self.options)+1):
            print(f"{i}) {self.options[i].texte}")

    def ajouter_options(self,option):
        self.options[len(self.options) + 1] = option

    def ajouter_plusieurs_options(self,options):
        for option in options:
            self.ajouter_options(option)
    def lire(self):
        try:
            entree = int(input())
            if entree in self.options.keys():  
                self.options[entree].executer() # Forme option : [Texte,[Fonction,Arg1,Arg2,etc ....],[Fonction,Arg1,Arg2,etc ....]]
                    
        except ValueError:
            print("Entrée non valide. Veuillez entrer un nombre.")