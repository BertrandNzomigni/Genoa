class Menu:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
        self.options = dict()
    def charger_options(self):
        pass
    def executer(self):
        self.options.clear()
        self.charger_options()
        self.afficher()
        self.lire()
    def afficher(self):
        self.afficher_corps()
        self.afficher_options()
    def afficher_corps(self):
        pass
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