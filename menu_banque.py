import menus

class MenuBanque(menus.Menu):
    def __init__(self, monde, jeu, joueur):
        super().__init__(monde, jeu)
        self.joueur = joueur

    def afficher_corps(self):
        print("--- Banque de la Cité ---")
        print(f"Florins liquides : {self.joueur.florins_liquides}")
        print(f"Solde en banque : {self.joueur.solde_bancaire}")

    def charger_options(self):
        cm = self.jeu.obtenir_constructeur_menu()
        self.options[1] = ["Consulter son solde", [self.executer]] # Recharge le menu pour juste afficher
        self.options[2] = ["Déposer des florins", [self.deposer]]
        self.options[3] = ["Retirer des florins", [self.retirer]]
        self.options[4] = ["Retour", [self.jeu.changer_menu_actif, cm.construire_menu_marche()]]

    def deposer(self):
        try:
            montant = int(input("Combien voulez-vous déposer ? "))
            if montant <= 0: return
            if montant > self.joueur.florins_liquides:
                print("Vous n'avez pas assez de florins liquides.")
            else:
                self.joueur.florins_liquides -= montant
                self.joueur.solde_bancaire += montant
                print(f"{montant} florins déposés avec succès.")
        except ValueError:
            print("Montant invalide.")
        input("Appuyez sur Entrée pour continuer...")

    def retirer(self):
        try:
            montant = int(input("Combien voulez-vous retirer ? "))
            if montant <= 0: return
            if montant > self.joueur.solde_bancaire:
                print("Vous n'avez pas assez de fonds en banque.")
            else:
                self.joueur.solde_bancaire -= montant
                self.joueur.florins_liquides += montant
                print(f"{montant} florins retirés avec succès.")
        except ValueError:
            print("Montant invalide.")
        input("Appuyez sur Entrée pour continuer...")