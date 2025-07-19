import lieu
class Itineraire:
    def __init__(self, chemin=None):
        # chemin est une liste ordonnée de lieux (objets Lieu)
        self._chemin : list[lieu.Lieu] = chemin if chemin else []
        self.verifier_invariants()

    def ajouter_etape(self, lieu):
        self._chemin.append(lieu)
        self.verifier_invariants()

    def obtenir_prochaine_etape(self):
        if self._chemin:
            return self._chemin[0]
        return None

    def avancer_etape(self):
        if self._chemin:
            self._chemin.pop(0)
        self.verifier_invariants()

    def est_termine(self):
        return len(self._chemin) == 0

    def obtenir_tout_le_chemin(self):
        return list(self._chemin)
    
    def est_vide(self):
        return len(self._chemin) == 0

    def __len__(self):
        return len(self._chemin)
    def __str__(self):
        return " -> ".join(str(lieu) for lieu in self._chemin)

    def verifier_invariants(self):
        i = 0
        while i < len(self._chemin)-1:
            assert self._chemin[i+1] in self._chemin[i].obtenir_voisins(), f"L'étape d'indice {i+1} ne fait pas partie des voisins de l'étape précédente. "
            assert self._chemin[i] in self._chemin[i+1].obtenir_voisins(), f"L'étape d'indice {i} ne fait pas partie des voisins de l'étape suivante. "
            i += 1

