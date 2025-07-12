# mon_super_jeu/bateau.py

from constantes import MARCHANDISES


class Bateau:
    """Représente un bateau avec sa soute et ses caractéristiques."""

    def __init__(self, nom, capacite, vitesse, lieu):
        self.nom = nom
        self.capacite = capacite
        self.vitesse = vitesse
        self.lieu = lieu
        self.cargaison = dict()

    def obtenir_nom(self):
        return self.nom

    def obtenir_lieu(self):
        return self.lieu

    def obtenir_volume_utilise(self):
        """Calcule le volume total utilisé par les marchandises dans la soute."""
        volume = 0
        for nom, quantite in self.cargaison.items():
            volume += MARCHANDISES[nom]["volume"] * quantite
        return volume

    def ajouter_cargaison(self, nom_marchandise, quantite):
        """Ajoute une quantité d'une marchandise à la soute."""
        if nom_marchandise in self.cargaison:
            self.cargaison[nom_marchandise] += quantite
        else:
            self.cargaison[nom_marchandise] = quantite

    def retirer_cargaison(self, nom_marchandise, quantite):
        """Retire une quantité d'une marchandise de la soute."""
        if nom_marchandise in self.cargaison:
            self.cargaison[nom_marchandise] -= quantite
            if self.cargaison[nom_marchandise] <= 0:
                del self.cargaison[nom_marchandise]