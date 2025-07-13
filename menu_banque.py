import menus

class MenuBanque(menus.Menu):
    def __init__(self, monde, jeu, joueur):
        super().__init__(monde, jeu)
        self.joueur = joueur
        self.banque = self.joueur.obtenir_lieu().banque

    def afficher_corps(self):
        print(f"--- {self.banque.nom} ---")
        print(f"Florins liquides : {self.joueur.florins_liquides}")

        solde = self.banque.obtenir_solde(self.joueur)
        print(f"Solde en compte : {solde:.2f}")

    def charger_options(self):
        self.options[1] = ["Consulter son solde", [self.executer]] # Recharge le menu pour juste afficher
        self.options[2] = ["Déposer des florins", [self.deposer]]
        self.options[3] = ["Retirer des florins", [self.retirer]]
        self.options[4] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_marche()]]

    def deposer(self):
        try:
            montant = int(input("Combien voulez-vous déposer ? "))
            if montant <= 0: return

            # On demande à la banque d'effectuer le dépôt
            erreur = self.banque.deposer(self.joueur, montant)
            if erreur:
                print(erreur)  # Affiche le message d'erreur de la banque
            else:
                print(f"{montant} florins déposés avec succès.")
        except ValueError:
            print("Montant invalide.")
        input("Appuyez sur Entrée pour continuer...")

    def retirer(self):
        try:
            montant = int(input("Combien voulez-vous retirer ? "))
            if montant <= 0: return

            # On demande à la banque d'effectuer le retrait
            erreur = self.banque.retirer(self.joueur, montant)
            if erreur:
                print(erreur) # Affiche le message d'erreur de la banque
            else:
                print(f"{montant} florins retirés avec succès.")
        except ValueError:
            print("Montant invalide.")
        input("Appuyez sur Entrée pour continuer...")