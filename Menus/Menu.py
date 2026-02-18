class Menu:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
        self.options = dict()
    def charger_options(self):
        pass
    def executer(self):
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
            print(f"{i}) {self.options[i][0]}")

    def ajouter_options(self,texte,*groupes):
        self.options[len(self.options) + 1] = [texte,*groupes]
    def lire(self):
        try:
            entree = int(input())
            if entree in self.options.keys():  
                option = self.options[entree] # Forme option : [Texte,[Fonction,Arg1,Arg2,etc ....],[Fonction,Arg1,Arg2,etc ....]]
                i = 1
                while i < len(option):
                    groupe = option[i] # Forme groupe : [Fonction,Arg1,Arg2,etc ....]
                    x = 1
                    args = list()
                    while x < len(groupe):
                       args.append(groupe[x])
                       x += 1
                    groupe[0](*args)
                    i += 1
                    
        except ValueError:
            print("Entrée non valide. Veuillez entrer un nombre.")