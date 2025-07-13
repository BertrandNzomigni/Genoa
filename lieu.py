# mon_super_jeu/lieu.py
# Classes Lieu, Port, et Mer
import constantes

class Lieu:
    """Classe générique pour un endrooit sur la carte."""
    def __init__(self,nom):
        self.nom = nom
        self.voisins = list()
        self.dict_distance=dict()
        self.bateaux = list()

    def ajouter_voisin(self, voisin, distance):
        self.voisins.append(voisin)
        self.dict_distance[voisin]=distance

    def obtenir_voisins(self):
        return self.voisins

    def obtenir_distance(self,voisin):
        return self.dict_distance[voisin]

    def ajouter_bateau(self, bateau):
        self.bateaux.append(bateau)

    def obtenir_bateaux(self):
        return self.bateaux

    def obtenir_nom(self):return self.nom
    def __str__(self):return self.nom


class Port(Lieu):
    """Untype d elieu ou le commerce est possible."""
    def __init__(self,nom):
        super().__init__(nom)
        self.prix_locaux_marchandises =dict()
        self.prix_locaux_bateaux = dict()
        for bateau in constantes.BATEAUX.keys():
            self.prix_locaux_bateaux[bateau] = constantes.BATEAUX[bateau]["Prix de base"]
    def obtenir_prix_bateau(self,type_bateau):
        return self.prix_locaux_bateaux[type_bateau]

class Mer(Lieu):
    """Untype de lieu qui peut etre traversé qu'en bateau."""
    def __init__(self,nom):
        super().__init__(nom)
