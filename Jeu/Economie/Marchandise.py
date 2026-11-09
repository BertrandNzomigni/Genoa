class Marchandise:
    ensemble_marchandises = {"poisson","coton","sucre","tabac","epices"}
    info = {"poisson":{"volume":1},"coton":{"volume":1},"sucre":{"tabac":1},"epices":{"volume":1}}

    def __init__(self,nom,quantite = 1):
        if nom not in self.ensemble_marchandises:
            raise Exception(f"'{nom}' n'est pas le nom d'une marchandise.")
        if quantite < 1:
            raise Exception("La quantité doit être supérieure à zéro.")
        self.volume_unitaire = Marchandise.info[nom]["volume"]
        self.quantite = quantite
        self.nom = nom
    def ajouter_quantite(self,quantite):
        if quantite < 0:
            raise Exception("Il est impossible d'ajouter une quantité négative de marchandise.")
        self.quantite += quantite
    def retirer_quantite(self,quantite):
        if quantite < 0:
            raise Exception("Il est impossible de retirer une quantité négative de marchandise.")
        self.quantite -= quantite

    def obtenir_quantite(self):
        return self.quantite

    def obtenir_volume(self):
        return self.quantite * self.volume_unitaire

    def obtenir_nom(self):
        return self.nom

    def fusionner(self,marchandise):
        if self.nom != marchandise.obtenir_nom():
            raise Exception("Impossible de fusionner des marchandises de types différents")
        quantite = self.quantite + marchandise.obtenir_quantite()
        return Marchandise(self.nom,quantite)

epices1 = Marchandise("epices")
epices2 = Marchandise("epices")
epices3 = epices1.fusionner(epices2)

print(epices3.quantite)