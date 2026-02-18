# Recoit les messages de mouvement
# Traite les messages de mouvement
class CoordinationMouvement:
    def __init__(self,entite,deplaceur,itineraire):
        self.entite = entite
        self.deplaceur = deplaceur
        self.itineraire = itineraire
    def aller_destination(self,dest):
        self.itineraire.aller_destination(dest)
    def faire_demi_tour(self):
        if self.itineraire.obtenir_distance() == 0:
            self.entite.changer_lieu(self.itineraire.obtenir_destination())
        self.itineraire.faire_demi_tour()
    def avancer(self):
        self.deplaceur.avancer()
