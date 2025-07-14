import copy
import mission
class MissionSchema:
    def __init__(self,mission=None):
        if mission:
            self.arrets = copy.deepcopy(mission.obtenir_arrets())
            self.nombre_max_cycles = mission.obtenir_nombre_max_cycles()
        else:
            self.arrets = list()
            self.nombre_max_cycles = 1
    def ajouter_arret(self,arret,indice):
        assert isinstance(arret,mission.Arret), "Seulement des arrêts peuvent être ajouté à une mission."
        if indice == -1:
            indice = len(self.arrets)
        lieu_arret = arret.obtenir_lieu()
        self.arrets.insert(indice,arret)
    def obtenir_nombre_arrets(self):
        return len(self.arrets)
    def obtenir_arrets(self):
        return self.arrets
    def supprimer_arret(self,arret):
        self.arrets.remove(arret)
    def verifier(self):
        for indice in range(len(self.arrets)-1):
            if not self.arrets[indice].obtenir_lieu() != self.arrets[indice+1].obtenir_lieu():
                return False
        if len(self.arrets) > 1:
            if not self.arrets[0].obtenir_lieu() != self.arrets[-1].obtenir_lieu():
                return False
        else:
            return False
        return True

    def definir_nombre_max_cycles(self,nombre):
        self.nombre_max_cycles =  nombre
    
    def obtenir_nombre_max_cycles(self):
        return self.nombre_max_cycles
