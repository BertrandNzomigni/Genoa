# mon_super_jeu/bateau.py

from constantes import MARCHANDISES
import position
import mission

from entite import Entite
class Bateau(Entite):
    """Représente un bateau avec sa soute et ses caractéristiques."""

    def __init__(self, nom, capacite, vitesse, lieu,type_bateau,monde):
        super().__init__(lieu)
        self.nom = nom
        self.capacite = capacite
        self.vitesse = vitesse
        self.cargaison = dict()
        self.type_bateau = type_bateau
        self.mission = None
        monde.nouveau_bateau(self)
        self.passagers = list()
        self.mission_active = False
        self.verifier_invariants()

    def obtenir_nom(self):
        return self.nom
    def obtenir_type(self):
        return self.type_bateau
    def __str__(self):return self.nom

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
        self.verifier_invariants()

    def retirer_cargaison(self, nom_marchandise, quantite):
        """Retire une quantité d'une marchandise de la soute."""
        if nom_marchandise in self.cargaison:
            self.cargaison[nom_marchandise] -= quantite
            if self.cargaison[nom_marchandise] <= 0:
                del self.cargaison[nom_marchandise]
        self.verifier_invariants()

    def obtenir_vitesse(self):
        return self.vitesse

    def obtenir_capacite(self):
        return self.capacite

    def obtenir_liste_cargaisons(self):
        return self.cargaison.keys()
    
    def obtenir_quantite_cargaison(self,nom_cargaison):
        if nom_cargaison in self.cargaison.keys():
            return self.cargaison[nom_cargaison]
        else:
            return 0
    
    def nouvelle_mission(self,mission):
        self.mission = mission
        self.verifier_invariants()

    def obtenir_mission(self):
        return self.mission

    def a_mission(self):
        return self.mission != None

    def abondonner_mission(self):
        self.mission = None
        self.verifier_invariants()

    def avancer(self):
        super().avancer()
        for passager in self.passagers:
            passager.suivre_bateau(self.position)

    def ajouter_passager(self,passager):
        from entite import Entite
        assert isinstance(passager,Entite), "Le passager n'est pas une entité."
        self.passagers.append(passager)
        self.verifier_invariants()
    
    def retirer_passager(self,passager):
        from entite import Entite
        assert isinstance(passager,Entite), "Le passager n'est pas une entité."
        assert passager in self.passagers, "Le passager n'était pas dans le bateau."
        self.passagers.remove(passager)
        self.verifier_invariants()
    
    def verifier_invariants(self):
        super().verifier_invariants()
        assert self.obtenir_volume_utilise() <= self.capacite, "Le volume utilisé dépasse la capacité du bateau."
        for passager in self.passagers:
            assert passager.obtenir_lieu() == self.position.obtenir_lieu_actuel(), "Un passager n'est pas dans le même lieu que le bateau."
        if self.a_mission():
            assert self.mission.est_valide(), "La mission du bateau n'est pas valide."

    def demarrer_mission(self):
        self.en_mission = True