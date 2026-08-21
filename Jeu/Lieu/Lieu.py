class Lieu:
    def __init__(self,nom):
        self.voisins = list()
        self.dict_distance = dict()
        self.bateaux = list()
        self.nom = nom
    def ajouter_voisin(self,voisin,distance):
        if distance <= 0:
            raise Exception("La distance entre deux lieux ne peut pas être non-positive.")
        else:
            self.voisins.append(voisin)
            self.dict_distance[voisin] = distance
    def obtenir_voisins(self):
        return self.voisins
    def obtenir_distance(self,voisin):
        return self.dict_distance[voisin]
    def ajouter_bateau(self,bateau):
        self.bateaux.append(bateau)
    def retirer_bateau(self,bateau):
        self.bateaux.remove(bateau)
    def obtenir_bateaux(self):
        return self.bateaux
    def __str__(self):
        return self.nom
    def obtenir_nom(self):
        return self.nom