import constantes
import copy

class Mission:
    def __init__(self,schema):
        self.arrets = copy.deepcopy(schema.obtenir_arrets())
        self.nombre_max_cycles = schema.obtenir_nombre_max_cycles()
        self.indice_prochain_arret = 1
        self.nombre_cycles = 0
        self.verifier_invariants()
    def ajouter_arret(self,arret,indice):
        assert isinstance(arret,Arret), "Seulement des arrêts peuvent être ajouté à une mission."
        if indice == -1:
            indice = len(self.arrets)
        lieu_arret = arret.obtenir_lieu()
        self.arrets.insert(indice,arret)
        self.verifier_invariants()
    def obtenir_nombre_arrets(self):
        return len(self.arrets)
    def obtenir_arrets(self):
        return self.arrets
    def supprimer_arret(self,arret):
        self.arrets.remove(arret)
        self.verifier_invariants()

    def definir_nombre_max_cycles(self,nombre):
        self.nombre_max_cycles =  nombre
        self.verifier_invariants()
    
    def obtenir_nombre_max_cycles(self):
        return self.nombre_max_cycles

    def verifier_invariants(self):
        for indice in range(len(self.arrets)-1):
            assert self.arrets[indice].obtenir_lieu() != self.arrets[indice+1].obtenir_lieu(), "Chaque arrêt doit avoir un lieu différent du suivant."
        if len(self.arrets) > 1:
            assert self.arrets[0].obtenir_lieu() != self.arrets[-1].obtenir_lieu(), "Chaque arrêt doit avoir un lieu différent du suivant."
        assert len(self.arrets) > 1, "Une mission doit avoir au moins deux arrêts."
        assert self.nombre_max_cycles >= self.nombre_cycles, "Le nombre de cycle ne doit pas dépasser le nombre maximum de cycle."
        assert self.nombre_max_cycles > 0, "Le nombre maximum de cycle doit être positif."

class Arret:
    def __init__(self,lieu,bateau,arret_base=None):
        self.lieu = lieu
        self.marchandises_depart = dict()
        if arret_base:
            self.marchandises_depart = arret_base.marchandises_depart
        else:
            for marchandise in constantes.MARCHANDISES.keys():
                self.marchandises_depart[marchandise] = 0
        self.bateau = bateau
        self.verifier_invariants()
    def obtenir_lieu(self):
        return self.lieu
    def obtenir_nom_lieu(self):
        return self.lieu.obtenir_nom()
    def modifier_quantite_marchandise(self,nom_marchandise,quantite):
        assert quantite >= 0, "La quantité de marchandise doit être nulle ou positive."
        self.marchandises_depart[nom_marchandise] = quantite
        self.verifier_invariants()
    def obtenir_quantite_marchandise(self,nom_marchandise):
        return self.marchandises_depart[nom_marchandise]
    def verifier_invariants(self):
        quantite = 0
        for marchandise in self.marchandises_depart.keys():
            quantite += self.marchandises_depart[marchandise]
        assert quantite <= self.bateau.obtenir_capacite(), "Le volume total de marchandises en partant d'un arrét ne doit pas être supérieure à la capacité du bateau."
    def obtenir_bateau(self):
        return self.bateau
    def volume_total(self):
        quantite = 0
        for marchandise in constantes.MARCHANDISES.keys():
            quantite += self.obtenir_quantite_marchandise(marchandise) * constantes.MARCHANDISES[marchandise]["volume"]
        return quantite