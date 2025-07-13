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
    def obtenir_nombre_arrets(self):
        return len(self.arrets)
    def obtenir_arrets(self):
        return self.arrets
    def supprimer_arret(self,arret):
        self.arrets.remove(arret)
    def verifier(self):
        for indice in range(len(self.arrets)-1):
            if not self.arrets[indice].obtenir_lieu() != self.arrets[indice+1].obtenir_lieu():
                return False
        if len(self.arrets) > 1:
            if not self.arrets[0].obtenir_lieu() != self.arrets[-1].obtenir_lieu():
                return False
        else:
            return False
        return True

    def verifier_invariants(self):
        for indice in range(len(self.arrets)-1):
            assert self.arrets[indice].obtenir_lieu() != self.arrets[indice+1].obtenir_lieu(), "Chaque arrêt doit avoir un lieu différent du suivant."
        if len(self.arrets) > 1:
            assert self.arrets[0].obtenir_lieu() != self.arrets[-1].obtenir_lieu(), "Chaque arrêt doit avoir un lieu différent du suivant."
        assert len(self.arrets) > 1, "Une mission doit avoir au moins deux arrêts."

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
    def verifier_invariants(self):
        pass
        # Invariant 1 : Le volume total en marchandises ne doit pas dépasser la capacité du bateau.