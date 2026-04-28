from Jeu.Position import Position

class Bateau:
    def __init__(self,nom,capacite,vitesse,lieu):
        self.nom = nom
        self.capacite = capacite
        self._vitesse = vitesse
        self.position = Position(lieu)
    def obtenir_nom(self):
        return self.nom
    def obtenir_position(self):
        return self.position
    
    def changer_lieu(self,lieu):
        self.position.lieu.retirer_bateau(self)
        self.position.lieu = lieu
        lieu.ajouter_bateau(self)
    
    @property
    def vitesse(self):
        return self._vitesse