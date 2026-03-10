class Prix:
    def __init__(self):
        self.prix = {
            "poisson": 10,
            "coton": 20,
            "sucre": 15,
            "tabac": 25,
            "epices": 30
        }
    def obtenir_prix(self, marchandise):
        return self.prix.get(marchandise, 0)