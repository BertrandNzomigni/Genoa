# mon_super_jeu/temps.py

class Temps:
    """Gère le passage du temps (tours)."""
    def __init__(self, monde):
        self.monde = monde
        self.jours = 0

    def avancer(self):
        self.jours += 1

    def obtenir_valeur(self):
        return self.jours