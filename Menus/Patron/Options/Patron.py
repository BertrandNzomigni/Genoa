class Patron:
    def __init__(self):
        self._options = list()

    @property 
    def options(self):
        return self._options