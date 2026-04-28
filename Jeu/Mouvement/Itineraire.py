# Connait l'itinéraire d'une entité
# Change l'itinéraire d'une entité
class Itineraire:
    def __init__(self,acteur):
        self.destination = None
        self.depart = None
        self.distance_destination = 0
        self.acteur = acteur
    def obtenir_destination(self):
        """
        Renvoie la prochaine destination de l'entité.
        Returns:
            Position: La destination de l'entité.
        """
        return self.destination
    def finir_voyage(self):
        """
        Après l'appel de cette méthode, l'entité n'a plus de prochaine destination et de position derrière elle.
        """
        self.destination = None
        self.depart = None
    def obtenir_depart(self):
        """
        Renvoie la position derrière l'entité.
        Returns:
            Position: La position derrière l'entité
        """
        return self.depart
    def obtenir_distance(self):
        """
        Renvoie la distance entre l'entité et sa prochaine destination.
        Returns:
            float: La distance entre l'entité et sa prochaine destination.
        """
        return self.distance_destination
    def changer_distance(self,distance):
        """
        Change la distance entre l'entité et sa prochaine destination.
        Args:
            distance (float): La nouvelle distance
        """
        self.distance_destination = distance
    def aller_destination(self,dest):
        """
        Commence un nouveau voyage. Change la prochaine destination de l'entité. La position derrière l'entité est sa position initiale.
        La distance entre l'entité et sa prochaine destination devient la distance entre la position initiale de l'entité et sa prochaine destination.

        Args:
            dest (Position): La nouvelle prochaine destination de l'entité
        """
        self.destination = dest
        self.depart = self.acteur.position.lieu
        self.distance_destination = self.destination.obtenir_distance(self.depart)
    def a_atteint_destination(self):
        """
        Vérifie si la distance entre l'entité et sa prochaine destination est nulle.
        Returns:
            boolean : La distance entre l'entité et sa prochaine destination est nulle.
        """
        return self.distance_destination == 0
    def a_destination(self):
        """
        Vérifie si l'entité a une prochaine destination.
        Returns:
            boolean : L'entité a une prochaine destination.
        """
        return self.destination != None
    def faire_demi_tour(self):
        """
        La position derrière l'entité devient sa prochaine destination. \n
        La prochaine destination de l'entité devient la position derrière lui. \n
        La distance entre l'entité et sa prochaine destination devient la distance qu'il a parcouru depuis l'ancienne position derrière lui. \n
        Si la distance entre l'entité et sa prochaine destination est nulle, alors l'entité n'a plus de prochaine destination et de position derrière elle.
        """
        x = self.destination
        self.destination = self.depart
        self.depart = x
        self.distance_destination = self.destination.obtenir_distance(self.depart) - self.distance_destination
        if self.distance_destination == 0:
            self.finir_voyage()