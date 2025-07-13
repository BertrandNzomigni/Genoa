# Fichier : banque.py

class Compte:
    """Représente le compte d'un joueur dans une banque spécifique."""
    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0.0

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        self.solde -= montant

    def appliquer_interets(self, taux):
        self.solde += self.solde * taux

class Banque:
    """Gère les opérations d'une banque spécifique à un port."""
    def __init__(self, nom, taux_interet):
        self.nom = nom
        self.taux_interet = taux_interet
        self.comptes = dict()  # Dictionnaire pour lier un joueur à son compte

    def obtenir_compte(self, joueur):
        """Récupère le compte d'un joueur, ou en crée un s'il n'existe pas."""
        if joueur not in self.comptes:
            self.comptes[joueur] = Compte(joueur)
        return self.comptes[joueur]

    def obtenir_solde(self, joueur):
        return self.obtenir_compte(joueur).solde

    def deposer(self, joueur, montant):
        if montant > joueur.florins_liquides:
            return "Vous n'avez pas assez de florins liquides."
        joueur.payer(montant)
        self.obtenir_compte(joueur).deposer(montant)
        return None  # Pas d'erreur

    def retirer(self, joueur, montant):
        compte = self.obtenir_compte(joueur)
        if montant > compte.solde:
            return "Fonds insuffisants en banque."
        compte.retirer(montant)
        joueur.gagner(montant)
        return None  # Pas d'erreur

    def calculer_interets_journaliers(self):
        """La banque calcule elle-même les intérêts pour tous ses comptes."""
        for compte in self.comptes.values():
            if compte.solde > 0:
                compte.appliquer_interets(self.taux_interet)