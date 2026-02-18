class Bateau:
    def __init__(self,nom,capacite,vitesse,lieu):
        self.nom = nom
        self.capacite = capacite
        self.vitesse = vitesse
        self.lieu = lieu
    def obtenir_nom(self):
        return self.nom
    def obtenir_lieu(self):
        return self.lieu