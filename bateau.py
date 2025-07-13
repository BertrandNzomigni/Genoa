# mon_super_jeu/bateau.py

from constantes import MARCHANDISES
import position


class Bateau:
    """Représente un bateau avec sa soute et ses caractéristiques."""

    def __init__(self, nom, capacite, vitesse, lieu,type_bateau,monde):
        self.nom = nom
        self.capacite = capacite
        self.vitesse = vitesse
        self.position = position.Position(lieu)
        self.cargaison = dict()
        self.type_bateau = type_bateau
        monde.nouveau_bateau(self)

    def obtenir_nom(self):
        return self.nom
    def obtenir_type(self):
        return self.type_bateau
    def __str__(self):return self.nom

    def obtenir_lieu(self):
        return self.position.obtenir_depart()

    def obtenir_position(self):
        return self.position

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

    def a_destination(self):
        return self.position.a_destination()
    def obtenir_vitesse(self):
        return self.vitesse
    def avancer(self):
        self.position.avancer(self.vitesse)
    def changer_destination(self,dest):
        self.position.changer_destination(dest)
    def obtenir_capacite(self):
        return self.capacite