import constantes

class Mission:
    def __init__(self):
        self.arrets = list()
        self.indice_prochain_arret = 1
    def ajouter_arret(self,arret,indice):
        assert isinstance(arret,Arret), "Seulement des arrêts peuvent être ajouté à une mission."
        if indice == -1:
            indice = len(self.arrets)
        lieu_arret = arret.obtenir_lieu()
        self.arrets.insert(indice,arret)
        if indice < len(self.arrets) - 1:
            assert lieu_arret != self.arrets[indice+1].obtenir_lieu(), "Chaque arrêt doit avoir un lieu différent du suivant."
        if indice > 1:
            assert lieu_arret != self.arrets[indice-1].obtenir_lieu(), "Chaque arrêt doit avoir un lieu différent du précédent."
    def obtenir_nombre_arrets(self):
        return len(self.arrets)
    def obtenir_arrets(self):
        return self.arrets
    def supprimer_arret(self,arret):
        self.arrets.remove(arret)

class Arret:
    def __init__(self,lieu,arret_base=None):
        self.lieu = lieu
        self.marchandises_depart = dict()
        if arret_base:
            self.marchandises_depart = arret_base.marchandises_depart
        else:
            for marchandise in constantes.MARCHANDISES.keys():
                self.marchandises_depart[marchandise] = 0
    def obtenir_lieu(self):
        return self.lieu
    def obtenir_nom_lieu(self):
        return self.lieu.obtenir_nom()
    def modifier_quantite_marchandise(self,nom_marchandise,quantite):
        assert quantite > 0, "La quantité de marchandise doit être nulle ou positive."
        self.marchandises_depart[nom_marchandise] = quantite