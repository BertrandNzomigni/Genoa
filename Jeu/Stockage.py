from Jeu.Economie.Marchandise import Marchandise

class Stockage:
    def __init__(self,volume_disponible):
        self.volume_disponible = volume_disponible
        self.marchandises = dict()
    def recevoir_marchandise(self,marchandise):
        if marchandise.nom not in self.marchandises.keys:
            self.marchandises[marchandise.nom] = marchandise
        else:
            self.marchandises[marchandise.nom] = self.marchandises[marchandise.nom].fusionner(marchandise)
        self.volume_disponible -= marchandise.obtenir_volume()

    def retirer_marchandise(self,nom,quantite):

        if nom not in self.marchandises.keys():
            raise Exception("Cette marchandise n'est pas présente dans le stockage.")

        if quantite < 0:
            raise Exception("Impossible de retirer la marchandise : La quantité est négative.")
        if self.marchandises[nom].obtenir_quantite() < quantite:
            raise Exception("Impossible de retirer la marchandise : La quantité demandé est supérieure à la quantité dans le stockage.")

        if self.marchandises[nom].obtenir_quantite() == quantite:
            marchandise = self.marchandises[nom]
            self.volume_disponible += marchandise.obtenir_volume()
            del self.marchandises[nom]
            return marchandise
        else:
            marchandise = Marchandise(nom,quantite)
            self.marchandises[nom].retirer_quantite(quantite)
            self.volume_disponible += marchandise.obtenir_volume()
            return marchandise
