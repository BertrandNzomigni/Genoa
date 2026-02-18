class Lieu:
    def __init__(self):
        self.voisins = list()
        self.dict_distance = dict()
        self.bateaux = list()
    def ajouter_voisin(self,voisin,distance):
        self.voisins.append(voisin)
        self.dict_distance[voisin] = distance
    def obtenir_voisins(self):
        return self.voisins
    def obtenir_distance(self,voisin):
        return self.dict_distance[voisin]
    def ajouter_bateau(self,bateau):
        self.bateaux.append(bateau)
    def obtenir_bateaux(self):
        return self.bateaux