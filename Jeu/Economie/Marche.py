from Jeu.Joueur import Joueur
from Jeu.Bateau import Bateau
from Jeu.Lieu.Lieu import Lieu
from Jeu.Economie.Marchandise import Marchandise
class Marche:
    def __init__(self,lieu : Lieu):
        self.lieu = lieu
        self.prix = {
            "poisson": 10,
            "coton": 20,
            "sucre": 15,
            "tabac": 25,
            "epices": 30
        }
    def obtenir_prix(self, marchandise):
        return self.prix.get(marchandise, 0)
    def obtenir_tout_prix(self):
        resultat = list()
        for prix in self.prix.keys():
            resultat.append((prix,self.prix[prix]))
        return resultat
    
    def acheter_marchandise(self,bateau : Bateau,marchandise : str,quantite : int,joueur : Joueur):
        if marchandise not in self.prix.keys():
            raise Exception(f"L'achat est impossible : {marchandise} n'est pas échangé dans le marché.")
        if quantite < 0:
            raise Exception(f"L'achat est impossible : La quantité est négative.")
        if joueur.obtenir_florins() < quantite * self.obtenir_prix(marchandise):
            raise Exception(f"La personne n'a pas assez d'argent pour acheter {quantite} de {marchandise}.")
        if bateau.obtenir_lieu() != self.lieu:
            raise Exception(f"L'achat est impossible : Le bateau n'est pas au même lieu que le marché.")
        if joueur.obtenir_lieu() != self.lieu:
            raise Exception(f"L'achat est impossible : La personne n'est pas au même lieu que le marché.")

        marchandise_achete = Marchandise(marchandise,quantite)
        bateau.recevoir_marchandise(marchandise_achete)
        joueur.depenser_florins(quantite * self.obtenir_prix(marchandise))

    def vendre_marchandise(self,bateau : Bateau,marchandise : str,quantite : int,joueur : Joueur):
        if marchandise not in self.prix.keys():
            raise Exception(f"La vente est impossible : {marchandise} n'est pas échangé dans le marché.")
        if quantite < 0:
            raise Exception(f"La vente est impossible : La quantité est négative.")
        if bateau.obtenir_lieu() != self.lieu:
            raise Exception(f"La vente est impossible : Le bateau n'est pas au même lieu que le marché.")
        if joueur.obtenir_lieu() != self.lieu:
            raise Exception(f"La vente est impossible : La personne n'est pas au même lieu que le marché.")

        bateau.retirer_marchandise(marchandise,quantite)
        joueur.recevoir_florins(quantite * self.obtenir_prix(marchandise))

