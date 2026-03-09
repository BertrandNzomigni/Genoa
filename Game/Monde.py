from Game.Lieu.Port import Port
from Game.Lieu.Mer import Mer
from Game.Joueur import Joueur
from Game.Bateau import Bateau
from Game.Temps import Temps

# Connait les entités du monde    
class Monde:
    def __init__(self):
        self.ports = [Port("Gênes"),Port("Venise"),Port("Marseille")]
        self.mers = [Mer("Mer Adriatique"),Mer("Mer Méditerranée")]

        # Connexions
        self.connecter_lieu(self.ports[0],self.mers[0],50)
        self.connecter_lieu(self.ports[1],self.mers[0],50)
        self.connecter_lieu(self.ports[2],self.mers[1],50)
        self.connecter_lieu(self.mers[0],self.mers[1],50)
        # Création bateau
        self.joueur = Joueur(self.ports[0])
        premier_bateau = Bateau("Queen Anne's Revenge",0,10,self.ports[0])
        self.ports[0].ajouter_bateau(premier_bateau)
        self.joueur.acquerir_bateau(premier_bateau)
        self.temps = Temps(self)
    def obtenir_joueur(self):
        return self.joueur
    def obtenir_temps(self):
        return self.temps
    def changer_temps(self,temps):
        self.temps = temps
    def connecter_lieu(self,lieu1,lieu2,distance):
        lieu1.ajouter_voisin(lieu2,distance)
        lieu2.ajouter_voisin(lieu1,distance)
    def avancer_temps(self):
        self.temps.avancer()