from Jeu.Mouvement.Voyage import Voyage


# Connait les informations du joueur
class Joueur:
    def __init__(self,lieu_de_depart):
        self.florins = 2000
        self.voyage_actuel = None
        self.lieu = lieu_de_depart
        self.bateaux = list()
        self._bateau_dirige = None

    def obtenir_florins(self):
        return self.florins
    
    def acquerir_bateau(self,bateau):
        self.bateaux.append(bateau)
    def obtenir_bateaux(self):
        return self.bateaux
    def rejoint_bateau(self,bateau):
        self._bateau_dirige = bateau
    def quitte_bateau(self):
        self.position.retirer_entite(self.bateau_dirige)
        self._bateau_dirige = None
        

    def dirige_actuellement_un_bateau(self):
        return self._bateau_dirige is not None


    @property
    def bateau_dirige(self):
        return self._bateau_dirige
    
    @property
    def vitesse(self):
        if self._bateau_dirige:
            return self._bateau_dirige.vitesse
        else:
            return 20

    def obtenir_lieu(self):
        return self.lieu
    
    def lieu_voisins(self):
        return self.lieu.obtenir_voisins()

    def progresser(self):
        if self.si_voyage_actuellement():
            self.voyage_actuel.avancer()
    
    # Gestion voyage
    def commencer_voyage(self,destination):
        if self.si_voyage_actuellement():
            raise Exception("Le joueur ne peut pas commencer un nouveau voyage : Il voyage déjà.")
        elif self.bateau_dirige == None:
            raise Exception("Le joueur ne peut pas commencer un nouveau voyage : Il dirige aucun bateau.")
        else:
            self.voyage_actuel = Voyage(self,self.bateau_dirige,destination,self.lieu)

    def avancer(self):
        if self.si_voyage_actuellement():
            self.voyage_actuel.avancer(self)
        else:
            raise("Le joueur ne peut pas avancer : Aucun voyage est en cours.")
    
    def faire_demi_tour(self):
        if self.si_voyage_actuellement():
            self.voyage_actuel.faire_demi_tour(self)
        else:
            raise("Le joueur ne peut pas faire demi-tour : Aucun voyage est en cours.")

    def si_voyage_actuellement(self):
        return self.voyage_actuel is not None

    def finir_voyage(self):
        if not self.si_voyage_actuellement():
            raise("Le joueur ne peut pas finir un voyage : Il ne voyage pas.")
        self.lieu = self.voyage_actuel.obtenir_destination()
        self.voyage_actuel = None

    def obtenir_distance_voyage(self):
        if self.voyage_actuel:
            return self.voyage_actuel.obtenir_distance()
        else:
            return None

    def obtenir_destination(self):
        if self.voyage_actuel:
            return self.voyage_actuel.obtenir_destination()
        else:
            return None