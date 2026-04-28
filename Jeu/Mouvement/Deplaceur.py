# Déplace une entité en fonction de son itinéraire
class Deplaceur:
    def __init__(self,itineraire,acteur):
        self.itineraire = itineraire
        self.acteur = acteur
    def avancer(self):
        if self.itineraire.obtenir_distance() <= self.acteur.vitesse and self.itineraire.a_destination():
            self.acteur.position.lieu = self.itineraire.obtenir_destination()
            self.itineraire.finir_voyage()
        self.itineraire.changer_distance(self.itineraire.obtenir_distance() - self.acteur.vitesse)