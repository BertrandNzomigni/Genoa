from tkinter import Tk

class Fenetre(Tk):
    def __init__(self,titre = None):
        super().__init__()
        if titre is not None:
            self.changer_titre(titre)
    def changer_titre(self,titre):
        self.title(titre)
    def demarrer(self):
        self.mainloop()