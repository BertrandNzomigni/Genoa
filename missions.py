import constantes

class Mission:
    def __init__(self):
        self.arrets = list()
        self.indice_prochain_arret = 1

class Arret:
    def __init__(self,lieu):
        self.lieu = lieu
        self.cargaisons_depart = dict()
        for marchandise in constantes.MARCHANDISES.keys():
            self.cargaisons_depart