# Déplace une entité en fonction de son itinéraire
class Deplaceur:
    def __init__(self,itineraire,acteur):
        self.itineraire = itineraire
        self.acteur = acteur
    def avancer(self):
        if self.itineraire.obtenir_distance() == 1:
            self.acteur.changer_lieu(self.itineraire.obtenir_destination())
            self.itineraire.changer_destination(None)
            self.itineraire.changer_depart(None)
        self.itineraire.changer_distance(self.itineraire.obtenir_distance() - 1)
    def changer_lieu(self,lieu):
        self.acteur.changer_lieu(lieu)