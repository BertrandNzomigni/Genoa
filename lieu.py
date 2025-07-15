# mon_super_jeu/lieu.py
# Classes Lieu, Port, et Mer

import banque


class Lieu:
    """Classe générique pour un endroit sur la carte."""
    def __init__(self,nom):
        self.nom = nom
        self.voisins = list()
        self.dict_distance=dict()
        self.bateaux = list()

    def ajouter_voisin(self, voisin, distance):
        self.voisins.append(voisin)
        self.dict_distance[voisin]=distance
        voisin.recevoir_voisin(self,distance)
        self.verifier_invariants()
    def recevoir_voisin(self,voisin,distance):
        self.voisins.append(voisin)
        self.dict_distance[voisin]=distance
        self.verifier_invariants()

    def obtenir_voisins(self):
        return self.voisins

    def obtenir_distance(self,voisin):
        assert self.dict_distance[voisin] > 0, f"La distance vers {voisin} doit être strictement positive."
        return self.dict_distance[voisin]

    def ajouter_bateau(self, bateau):
        self.bateaux.append(bateau)
        self.verifier_invariants()

    def obtenir_bateaux(self):
        return self.bateaux

    def obtenir_nom(self):return self.nom
    def __str__(self):return self.nom

    def __eq__(self, other):
        return isinstance(other, Lieu) and self.nom == other.nom

    def __hash__(self):
        return hash(self.nom)
    
    def verifier_invariants(self):
        for voisin in self.voisins:
            assert voisin in self.dict_distance, f"Le voisin {voisin} n'a pas de distance associée."
            assert self.dict_distance[voisin] == voisin.obtenir_distance(self), f"La distance de {self} à {voisin} n'est pas identique à la distance de {voisin} à {self}."
        for bateau in self.bateaux:
            assert bateau is not None, "Un bateau dans la liste est None."

class Port(Lieu):
    """Untype d elieu ou le commerce est possible."""
    def __init__(self,nom,prix_locaux_marchandises):
        from constantes import BATEAUX
        super().__init__(nom)
        self.prix_locaux_marchandises = prix_locaux_marchandises
        self.prix_locaux_bateaux = dict()
        for bateau in BATEAUX.keys():
            self.prix_locaux_bateaux[bateau] = BATEAUX[bateau]["Prix de base"]

        nom_banque = f"Banca di {nom}"
        taux_base = 0.001  # 0.1%
        if nom == "Venise":
            nom_banque = "Credito Veneziano"
            taux_base = 0.0012  # La banque de Venise est un peu plus généreuse

        self.banque = banque.Banque(nom=nom_banque, taux_interet=taux_base)
        self.verifier_invariants()

    def obtenir_prix_bateau(self,type_bateau):
        return self.prix_locaux_bateaux[type_bateau]
    def obtenir_prix_marchandises(self,nom_marchandise):
        return self.prix_locaux_marchandises[nom_marchandise]
    def verifier_invariants(self):
        from constantes import MARCHANDISES
        super().verifier_invariants()
        for marchandise in MARCHANDISES.keys():
            assert marchandise in self.prix_locaux_marchandises.keys(), f"Le prix de {marchandise} n'est pas défini à {self.nom}"

class Mer(Lieu):
    """Un type de lieu qui peut etre traversé qu'en bateau."""
    def __init__(self,nom):
        super().__init__(nom)
        super().verifier_invariants()
