class Option:
    def __init__(self,texte,*fonctions):
        self._texte = texte
        self._fonctions = fonctions
    @property
    def texte(self):
        return self._texte
    @property
    def fonctions(self):
        return self._fonctions

    def executer(self):
        for fonction in self._fonctions:
            fonction[0](*fonction[1:])