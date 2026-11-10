class Marche:
    def __init__(self):
        self._biens_disponibles = ["Thé","Blé"]
        self.prix = {"Thé" : 10 , "Blé" : 1}
        
    def biens_disponibles(self):
        return self._biens_disponibles

    def obtenir_prix(self,marchandise):
        return self.prix[marchandise]
