from constantes import *
from bateau import Bateau

class Transaction:
    def __init__(self,joueur,lieu):
        self.joueur = joueur
        self.lieu = lieu
        self.erreur = ""
        self.montant = 0
    def verifier_appliquer(self):
        if self.verifier():
            self.appliquer()
            return True
        else:
            return False
    def obtenir_erreur(self):
        return self.erreur
    def obtenir_montant(self):
        return self.montant

class AchatMarchandises(Transaction):
    def __init__(self, joueur,lieu,quantite,nom_marchandise,prix,bateau):
        super().__init__(joueur,lieu)
        self.quantite = quantite
        self.prix = prix
        self.bateau = bateau
        self.nom_marchandise = nom_marchandise

    def verifier(self):
        self.montant = self.quantite * self.prix
        volume_total = self.quantite * MARCHANDISES[self.nom_marchandise]["volume"]
        if self.joueur.obtenir_florins() < self.montant:
            self.erreur = "Pas assez d'argent"
            return False
        elif self.bateau.capacite - self.bateau.obtenir_volume_utilise() < volume_total:
            self.erreur = "Pas assez de place dans la soute."
            return False
        return True

    def appliquer(self):
        self.joueur.payer(self.montant)
        self.bateau.ajouter_cargaison(self.nom_marchandise, self.quantite)

class VenteMarchandises(Transaction):

    def __init__(self, joueur,lieu,quantite,nom_marchandise,prix,bateau):
        super().__init__(joueur,lieu)
        self.quantite = quantite
        self.prix = prix
        self.bateau = bateau
        self.nom_marchandise = nom_marchandise
    def verifier(self):
        quantite_max = self.bateau.cargaison[self.nom_marchandise]
        if quantite_max > self.quantite:
            self.erreur = "Pas assez de marchandises."
            return False
        else:
            return True
    def appliquer(self):
        self.montant = self.quantite * self.prix
        self.bateau.retirer_cargaison(self.nom_marchandise, self.quantite)
        self.joueur.gagner(self.montant)

class AchatBateau(Transaction):
    def __init__(self,joueur,lieu,type_bateau,prix,nom):
        super().__init__(joueur,lieu)
        self.type_bateau = type_bateau
        self.prix = prix
        self.nom =  nom
    def verifier(self):
        if self.joueur.obtenir_florins() < self.montant:
            self.erreur = "Pas assez d'argent"
            return False
        else:
            return True
    def appliquer(self):
        print(self.type_bateau)
        vitesse = BATEAUX[self.type_bateau]["Vitesse"]
        capacite = BATEAUX[self.type_bateau]["Capacité"]
        nouveau_bateau = Bateau(self.nom,capacite,vitesse,self.lieu)
        self.joueur.acquerir_bateau(nouveau_bateau)
        self.lieu.ajouter_bateau(nouveau_bateau)
        self.joueur.payer(self.prix)
        print("Fin test")
