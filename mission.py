import constantes

class Mission:
    def __init__(self):
        self.arrets = list()
        self.indice_prochain_arret = 1
    def ajouter_arret(self,arret,indice):
        assert isinstance(arret,Arret), "Seulement des arrêts peuvent être ajouté à une mission."
        lieu_arret = arret.obtenir_lieu()
        if len(self.arrets) > 0:
            assert lieu_arret != self.arrets[indice].obtenir_lieu(), "Chaque arrêt doit avoir un lieu différent du suivant."
            assert lieu_arret != self.arrets[indice-1].obtenir_lieu(), "Chaque arrêt doit avoir un lieu différent du précédent."
        self.arrets.insert(indice,arret)
    def obtenir_nombre_arrets(self):
        return len(self.arrets)
    def obtenir_arrets(self):
        return self.arrets

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