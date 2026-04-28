class Position:
    def __init__(self,lieu):
        self._lieu = lieu
        self.entites_attachees = list()

    @property
    def lieu(self):
        return self._lieu
    
    @lieu.setter
    def lieu(self,x):
        self._lieu = x
        for entite in self.entites_attachees:
            entite.changer_lieu(x)

    def attacher_entite(self,p):
        self.entites_attachees.append(p)

    def retirer_entite(self,p):
        self.entites_attachees.remove(p)