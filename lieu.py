# mon_super_jeu/lieu.py
# Classes Lieu, Port, et Mer


class Lieu:
    """Classe générique pour un endrooit sur la carte."""
    def __init__(self):
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


class Port:
    """Untype d elieu ou le commerce est possible."""
    def __init__(self,nom):
        self.nom=nom
        self.lieu =Lieu()
        self.prix_locaux_marchandises =dict()
        self.prix_locaux_bateaux = dict()

    def obtenir_nom(self):return self.nom
    def obtenir_lieu(self): return self.lieu
    def __str__(self):return self.nom

class Mer:
    """Untype de lieu qui peut etre traversé qu'en bateau."""
    def __init__(self,nom):
        self.nom =nom
        self.lieu =Lieu()

    def obtenir_nom(self): return self.nom
    def obtenir_lieu(self): return self.lieu
    def __str__(self): return self.nom
