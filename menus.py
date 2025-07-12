# mon_super_jeu/menus.py

from constantes import *
from lieu import Port


class Menu:
    """Classe de base pour tous les menus du jeu."""

    def __init__(self, monde, jeu):
        self.monde = monde
        self.jeu = jeu
        self.options = dict()

    def charger_options(self):
        pass

    def afficher_corps(self):
        pass

    def executer(self):
        self.charger_options()
        self.afficher()
        self.lire()

    def afficher(self):
        self.afficher_corps()
        self.afficher_options()

    def afficher_options(self):
        print("\n--- Options ---")
        for i in sorted(self.options.keys()):
            print(f"{i}) {self.options[i][0]}")

    def lire(self):
        try:
            entree = int(input("\nVotre choix : "))
            if entree in self.options.keys():
                option = self.options[entree]
                i = 1
                while i < len(option):
                    groupe = option[i]
                    args = list(groupe[1:])
                    groupe[0](*args)
                    i += 1
        except (ValueError, KeyError):
            print("Entrée non valide. Veuillez entrer un nombre correspondant à une option.")
            input("Appuyez sur Entrée pour continuer...")


class MenuPrincipal(Menu):
    def __init__(self, monde, jeu, temps):
        super().__init__(monde, jeu)
        self.temps = temps

    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        joueur = self.monde.obtenir_joueur()
        i = 1
        self.options[i] = ["Jour suivant", [self.temps.avancer]];
        i += 1
        self.options[i] = ["Sélectionner une nouvelle destination",
                           [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_deplacement()]];
        i += 1
        self.options[i] = ["Voir l'ensemble de vos bateaux",
                           [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_bateaux_global()]];
        i += 1
        if isinstance(joueur.obtenir_lieu(), Port):
            self.options[i] = ["Gérer vos bateaux dans ce port",
                               [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_bateaux_port()]];
            i += 1
            if joueur.obtenir_bateau_dirige() is not None and isinstance(joueur.obtenir_lieu(), Port):
                self.options[i] = ["Accéder au marché", [self.jeu.changer_menu_actif,
                                                         constructeur_menu.construire_menu_marche(
                                                             joueur.obtenir_bateau_dirige())]];
                i += 1
        self.options[i] = ["Quitter le jeu", [self.jeu.quitter]]

    def afficher_corps(self):
        j = self.monde.obtenir_joueur()
        print(f"Jour : {self.monde.obtenir_temps().obtenir_valeur()}\nFlorins : {j.obtenir_florins()} florins.")
        if j.obtenir_bateau_dirige():
            print(f"Vous commandez le bateau : {j.obtenir_bateau_dirige().obtenir_nom()}")
        else:
            print("Vous ne commandez aucun bateau.")
        print("-" * 20)
        if j.obtenir_itineraire().a_destination():
            print(f"Vous naviguez vers {j.obtenir_itineraire().obtenir_destination()}.")
            print(f"La distance restante est de {j.obtenir_itineraire().obtenir_distance() * 10} kilomètres.")
        else:
            print(f"Vous êtes actuellement à {j.obtenir_lieu()}.")


class MenuDeplacement(Menu):
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        joueur = self.monde.obtenir_joueur()
        self.pas_en_chemin = not joueur.obtenir_itineraire().a_destination()
        if self.pas_en_chemin:
            i = 1
            for destination in joueur.obtenir_lieu().obtenir_lieu().obtenir_voisins():
                self.options[i] = [destination.obtenir_nom(),
                                   [joueur.obtenir_coordinateur().aller_destination, destination],
                                   [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_principal()]];
                i += 1
            self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_principal()]]
        else:
            self.options[1] = ["Faire demi-tour", [joueur.obtenir_coordinateur().faire_demi_tour],
                               [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_principal()]]
            self.options[2] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_principal()]]

    def afficher_corps(self):
        if self.pas_en_chemin:
            print(f"Où souhaitez-vous aller depuis {self.monde.obtenir_joueur().obtenir_lieu().obtenir_nom()} ?")
        else:
            print("Vous êtes déjà en voyage.")


class MenuBateauxPort(Menu):
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        joueur = self.monde.obtenir_joueur()
        i = 1
        for bateau in joueur.obtenir_bateaux_a_lieu(joueur.obtenir_lieu()):
            action_text, action_func = (
            "Quitter le commandement", joueur.quitter_bateau) if joueur.obtenir_bateau_dirige() == bateau else (
            "Prendre le commandement", joueur.rejoindre_bateau)
            self.options[i] = [
                f"{bateau.obtenir_nom()} (Capacité: {bateau.obtenir_volume_utilise()}/{bateau.capacite}) - {action_text}",
                [action_func, bateau], [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_principal()]];
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_principal()]]

    def afficher_corps(self): print(f"Vos bateaux à {self.monde.obtenir_joueur().obtenir_lieu().obtenir_nom()} :")


class MenuBateauxGlobal(Menu):
    def __init__(self, joueur, monde, jeu):
        super().__init__(monde, jeu)
        self.joueur = joueur

    def charger_options(self):
        self.options[1] = ["Retour", [self.jeu.changer_menu_actif,
                                      self.jeu.obtenir_constructeur_menu().construire_menu_principal()]]

    def afficher_corps(self):
        print("--- Flotte complète ---")
        if not self.joueur.obtenir_bateaux(): print("Vous ne possédez aucun bateau.")
        for bateau in self.joueur.obtenir_bateaux():
            print(
                f"- {bateau.obtenir_nom()} à {bateau.obtenir_lieu().obtenir_nom()} (Capacité: {bateau.obtenir_volume_utilise()}/{bateau.capacite})")


class MenuMarche(Menu):
    def __init__(self, monde, jeu, bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau

    def charger_options(self):
        cm = self.jeu.obtenir_constructeur_menu()
        self.options[1] = ["Acheter des marchandises",
                           [self.jeu.changer_menu_actif, cm.construire_menu_achat(self.bateau)]]
        self.options[2] = ["Vendre des marchandises",
                           [self.jeu.changer_menu_actif, cm.construire_menu_vente(self.bateau)]]
        self.options[3] = ["Retour au menu principal", [self.jeu.changer_menu_actif, cm.construire_menu_principal()]]

    def afficher_corps(self):
        port = self.monde.obtenir_joueur().obtenir_lieu()
        print(f"Bienvenue au marché de {port.obtenir_nom()}.")
        print(
            f"Bateau : {self.bateau.obtenir_nom()} (Capacité restante: {self.bateau.capacite - self.bateau.obtenir_volume_utilise()})")
        print(f"Vos florins : {self.monde.obtenir_joueur().obtenir_florins()}")


class MenuAchat(Menu):
    def __init__(self, monde, jeu, bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau
        self.port = self.monde.obtenir_joueur().obtenir_lieu()

    def charger_options(self):
        cm = self.jeu.obtenir_constructeur_menu()
        i = 1
        for nom, prix in self.port.prix_locaux.items():
            vol = MARCHANDISES[nom]["volume"]
            self.options[i] = [f"{nom} ({prix} florins, volume: {vol})", [self.acheter, nom]];
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, cm.construire_menu_marche(self.bateau)]]

    def afficher_corps(self):
        print(f"--- Acheter des marchandises à {self.port.obtenir_nom()} ---")
        print(
            f"Capacité restante du {self.bateau.obtenir_nom()}: {self.bateau.capacite - self.bateau.obtenir_volume_utilise()}")
        print(f"Vos florins: {self.monde.obtenir_joueur().obtenir_florins()}")

    def acheter(self, nom_marchandise):
        try:
            qte = int(input(f"Quelle quantité de {nom_marchandise} acheter ? "))
            if qte <= 0: return
            cout_total = qte * self.port.prix_locaux[nom_marchandise]
            vol_total = qte * MARCHANDISES[nom_marchandise]["volume"]
            joueur = self.monde.obtenir_joueur()
            if joueur.obtenir_florins() < cout_total:
                print("Vous n'avez pas assez de florins.")
            elif self.bateau.capacite - self.bateau.obtenir_volume_utilise() < vol_total:
                print("Pas assez de place dans la soute.")
            else:
                joueur.payer(cout_total)
                self.bateau.ajouter_cargaison(nom_marchandise, qte)
                print(f"{qte} unité(s) de {nom_marchandise} achetée(s) pour {cout_total} florins.")
        except ValueError:
            print("Veuillez entrer un nombre.")
        input("Appuyez sur Entrée pour continuer...")
        self.jeu.changer_menu_actif(self.jeu.obtenir_constructeur_menu().construire_menu_achat(self.bateau))


class MenuVente(Menu):
    def __init__(self, monde, jeu, bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau
        self.port = self.monde.obtenir_joueur().obtenir_lieu()

    def charger_options(self):
        cm = self.jeu.obtenir_constructeur_menu()
        i = 1
        if not self.bateau.cargaison: self.options[i] = ["Retour", [self.jeu.changer_menu_actif,
                                                                    cm.construire_menu_marche(self.bateau)]]; return
        for nom, qte in self.bateau.cargaison.items():
            prix = self.port.prix_locaux.get(nom, 0)
            self.options[i] = [f"{nom} (Quantité: {qte}, Prix de vente: {prix})", [self.vendre, nom]];
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, cm.construire_menu_marche(self.bateau)]]

    def afficher_corps(self):
        print(f"--- Vendre des marchandises depuis {self.bateau.obtenir_nom()} à {self.port.obtenir_nom()} ---")
        if not self.bateau.cargaison: print("La soute est vide.")

    def vendre(self, nom_marchandise):
        try:
            qte_max = self.bateau.cargaison[nom_marchandise]
            qte = int(input(f"Quelle quantité de {nom_marchandise} vendre (max {qte_max}) ? "))
            if qte <= 0: return
            if qte > qte_max: qte = qte_max
            gain = qte * self.port.prix_locaux.get(nom_marchandise, 0)
            self.bateau.retirer_cargaison(nom_marchandise, qte)
            self.monde.obtenir_joueur().gagner(gain)
            print(f"{qte} unité(s) de {nom_marchandise} vendue(s) pour {gain} florins.")
        except ValueError:
            print("Veuillez entrer un nombre.")
        input("Appuyez sur Entrée pour continuer...")
        self.jeu.changer_menu_actif(self.jeu.obtenir_constructeur_menu().construire_menu_vente(self.bateau))

class MenuAchatBateaux(Menu):
    def __init__(self, monde, jeu, joueur,port):
        super().__init__(monde, jeu)
        self.joueur = joueur
    def charger_options(self):
        i = 1
        for bateau in BATEAUX.keys():
            self.options[i] = [f"{i}) {bateau} : {port.prix_locaux_bateaux[bateau]}",nothing]
    def afficher_corps(self):
        print(f"--- Acheter un navire à {self.port.obtenir_nom()} ---")

