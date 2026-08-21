# Connait l'itinéraire d'une entité
# Change l'itinéraire d'une entité

from Jeu.Lieu.Lieu import Lieu

class Voyage:
    def __init__(self,meneur,bateau,destination : Lieu,depart : Lieu):
        self.destination = destination
        self.depart = depart
        self.distance_destination = destination.obtenir_distance(depart)
        self.meneur = meneur
        self.bateau = bateau
        self.participants = {meneur,bateau}

        self.bateau.participer_voyage(self)

    def ajouter_participant(self,participant):
        if participant.si_voyage_actuellement():
            raise Exception("Cette entité ne peut pas participer à ce voyage : Il voyage déjà.")
        else:
            self.participants.add(participant)
    
    def obtenir_destination(self):
        """
        Renvoie la prochaine destination de l'entité.
        Returns:
            Position: La destination de l'entité.
        """
        return self.destination

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

    def avancer(self):
        if self.distance_destination <= self.bateau.obtenir_vitesse():
            self.distance_destination = 0
            self.finir()
        else:
            self.distance_destination -= self.bateau.obtenir_vitesse()
    
    def faire_demi_tour(self,acteur):
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
            self.finir()

    def finir(self):
        if self.distance_destination != 0:
            raise Exception("Le voyage ne peut pas être fini : La distance à la destination n'est pas nulle.")
        else:
            for participant in self.participants:
                participant.finir_voyage()