class Bateau:
    def __init__(self,nom,capacite,vitesse,lieu):
        self.nom = nom
        self.capacite = capacite
        self.vitesse = vitesse
        self.lieu = lieu
        self.voyage_actuel = None
    def obtenir_nom(self):
        return self.nom
    def obtenir_lieu(self):
        return self.lieu
    def obtenir_vitesse(self):
        return self.vitesse
    
    def finir_voyage(self):
        if not self.si_voyage_actuellement():
            raise("Le navire ne peut pas finir un voyage : Il ne voyage pas.")
        if self.voyage_actuel.obtenir_distance() > 0:
            raise("Le navire ne peut pas finir le voyage : Il est toujours en cours.")
        self.lieu.retirer_bateau(self)
        self.lieu = self.voyage_actuel.obtenir_destination()
        self.lieu.ajouter_bateau(self)
        self.voyage_actuel = None

    def si_voyage_actuellement(self):
        return self.voyage_actuel is not None

    def participer_voyage(self,voyage):
        if self.si_voyage_actuellement():
            raise Exception("Ce bateau ne peut pas participer à ce voyage : Il voyage déjà.")
        else:
            self.voyage_actuel = voyage