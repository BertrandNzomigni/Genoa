class Transaction:
    def __init__(self,joueur,montant,lieu):
        self.joueur = joueur
        self.montant = montant
        self.lieu = lieu
        self.possible = False
    def verifier_appliquer(self):
        self.possible = self.verifier()
        if self.possible:
            self.appliquer()

class AchatMarchandises(Transaction):
    def __init__(self, joueur,montant,lieu,quantite,prix,bateau):
        super().__init__(joueur, montant,lieu,quantite,prix)
        self.quantite = quantite
        self.prix = prix