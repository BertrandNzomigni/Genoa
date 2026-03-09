# Connait l'itinéraire d'une entité
# Change l'itinéraire d'une entité
class Itineraire:
    def __init__(self,acteur):
        self.destination = None
        self.depart = None
        self.distance_destination = 0
        self.acteur = acteur
    def obtenir_destination(self):
        return self.destination
    def changer_destination(self,destination):
        self.destination = destination
    def obtenir_depart(self):
        return self.depart
    def changer_depart(self,depart):
        self.depart = depart
    def obtenir_distance(self):
        return self.distance_destination
    def changer_distance(self,distance):
        self.distance_destination = distance
    def aller_destination(self,dest):
        self.destination = dest
        self.depart = self.acteur.obtenir_lieu()
        self.distance_destination = dest.obtenir_distance(self.acteur.obtenir_lieu())
    def a_atteint_destination(self):
        return self.distance_destination == 0
    def a_destination(self):
        return self.destination != None
    def faire_demi_tour(self):
        x = self.destination
        self.destination = self.depart
        self.depart = x
        self.distance_destination = self.destination.obtenir_lieu().obtenir_distance(self.obtenir_depart()) - self.distance_destination
        if self.distance_destination == 0:
            self.destination = None
            self.depart = None