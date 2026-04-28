class Position:
    def __init__(self,lieu):
        self._lieu = lieu

    @property
    def lieu(self):
        return self._lieu
    
    @lieu.setter
    def lieu(self,x):
        self._lieu = x