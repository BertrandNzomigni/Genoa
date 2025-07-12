class Transaction:
    def __init__(self,joueur,montant,lieu):
        self.joueur = joueur
        self.montant = montant
        self.lieu = lieu
    def verifier_appliquer(self):
        if self.verifier():
            self.appliquer()
            return True
        else:
            return False

class AchatMarchandises(Transaction):
    def __init__(self, joueur,montant,lieu,quantite,nom_marchandise,prix,bateau):
        super().__init__(joueur, montant,lieu,quantite,prix)
        self.quantite = quantite
        self.prix = prix
        self.bateau = bateau
        self.nom_marchandise = nom_marchandise
        self.erreur = ""
    def verifier(self):
        self.cout_total = self.quantite * self.prix
        volume_total = self.quantite * MARCHANDISES[self.nom_marchandise]["volume"]
        if self.joueur.obtenir_florins() < self.cout_total:
            self.erreur = "Pas assez d'argent"
            return False
        elif self.bateau.capacite - self.bateau.obtenir_volume_utilise() < volume_total:
            self.erreur = "Pas assez de place dans la soute."
            return False
        return True
    def appliquer(self):
        self.joueur.payer(self.cout_total)
        self.bateau.ajouter_cargaison(self.nom_marchandise, self.quantite)