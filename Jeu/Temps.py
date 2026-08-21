# Sait le tour actuel
# Fait avancer le temps en actualisant le monde
class Temps:
    def __init__(self,monde):
        self.monde = monde
        self.jours = 0
    def avancer(self):
        self.jours += 1
        self.monde.obtenir_joueur().progresser()
    def obtenir_valeur(self):
        return self.jours