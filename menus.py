# mon_super_jeu/menus.py

from constantes import *
from lieu import Port
from transaction import *


class Menu:
    """Classe de base pour tous les menus du jeu."""

    def __init__(self, monde, jeu):
        self.monde = monde
        self.jeu = jeu
        self.constructeur_menu = jeu.obtenir_constructeur_menu()
    def charger_options(self):
        pass

    def afficher_corps(self):
        pass

    def executer(self):
        self.options = dict()
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
        except (ValueError, KeyError) as e:
            print(f"Erreur : {e}")
            print("Entrée non valide. Veuillez entrer un nombre correspondant à une option.")
            input("Appuyez sur Entrée pour continuer...")


class MenuPrincipal(Menu):
    def __init__(self, monde, jeu, temps):
        super().__init__(monde, jeu)
        self.temps = temps

    def charger_options(self):
        joueur = self.monde.obtenir_joueur()
        i = 1
        self.options[i] = ["Jour suivant", [self.monde.avancer_temps,],[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_principal()]]
        i += 1
        if joueur.dirige_bateau():
            self.options[i] = ["Sélectionner une nouvelle destination",
                           [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_deplacement()]];
            i += 1
        self.options[i] = ["Voir l'ensemble de vos bateaux",
                           [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_bateaux_global()]];
        i += 1
        if isinstance(joueur.obtenir_lieu(), Port) and not joueur.est_parti():
            self.options[i] = ["Gérer vos bateaux dans ce port",[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_bateaux_port()]];
            i += 1
            self.options[i] = ["Accéder au marché", [self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_marche()]];
            i += 1
        self.options[i] = ["Quitter le jeu", [self.jeu.quitter]]

    def afficher_corps(self):
        j = self.monde.obtenir_joueur()
        print(f"Jour : {self.temps.obtenir_valeur()}\nFlorins : {j.obtenir_florins()} florins.")
        if j.obtenir_bateau_dirige():
            print(f"Vous commandez le bateau : {j.obtenir_bateau_dirige().obtenir_nom()}")
        else:
            print("Vous ne commandez aucun bateau.")
        print("-" * 20)
        if j.a_destination():
            print(f"Vous naviguez vers {j.obtenir_destination()}.")
            print(f"La distance restante est de {j.obtenir_distance_voyage()} kilomètres.")
        else:
            print(f"Vous êtes actuellement à {j.obtenir_lieu()}.")


class MenuDeplacement(Menu):
    def __init__(self,monde,jeu,joueur):
        super().__init__(monde, jeu)
        self.joueur = joueur
    def charger_options(self):
        self.pas_en_chemin = not self.joueur.a_destination()
        if self.pas_en_chemin:
            i = 1
            for destination in self.joueur.obtenir_voisins_lieu():
                self.options[i] = [destination.obtenir_nom(),
                                   [self.joueur.changer_destination, destination],
                                   [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_principal()]];
                i += 1
            self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_principal()]]
        else:
            self.options[1] = ["Faire demi-tour", [self.joueur.faire_demi_tour],
                               [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_principal()]]
            self.options[2] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_principal()]]

    def afficher_corps(self):
        if self.pas_en_chemin:
            print(f"Où souhaitez-vous aller depuis {self.joueur.obtenir_nom_lieu()} ?")
        else:
            print("Vous êtes déjà en voyage.")


class MenuBateauxPort(Menu):
    def __init__(self,monde,jeu,joueur):
        super().__init__(monde, jeu)
        self.joueur = joueur
    def charger_options(self):
        i = 1
        for bateau in self.joueur.obtenir_bateaux_a_lieu(self.joueur.obtenir_lieu()):
            self.options[i] = [f"{bateau} : Gérer",[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_gestion_bateaux(bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_principal()]]

    def afficher_corps(self): print(f"Vos bateaux à {self.joueur.obtenir_nom_lieu()} :")


class MenuBateauxGlobal(Menu):
    def __init__(self, bateaux, monde, jeu):
        super().__init__(monde, jeu)
        self.bateaux = bateaux

    def charger_options(self):
        i = 1
        for bateau in self.bateaux:
            self.options[i] = [f"Voir plus d'informations à propos de {bateau.obtenir_nom()}.",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_information_bateau(bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif,
                                      self.constructeur_menu.construire_menu_principal()]]

    def afficher_corps(self):
        print("--- Flotte complète ---")
        if not self.bateaux: print("Vous ne possédez aucun bateau.")
        for bateau in self.bateaux:
            print(
                f"- {bateau.obtenir_nom()} à {bateau.obtenir_nom_lieu()} (Capacité: {bateau.obtenir_volume_utilise()}/{bateau.capacite})")


class MenuMarche(Menu):
    def __init__(self, monde, jeu, bateau,joueur):
        super().__init__(monde, jeu)
        self.bateau = bateau
        self.joueur = joueur

    def charger_options(self):
        i = 1
        if self.joueur.obtenir_bateau_dirige() is not None:
            self.options[i] = ["Acheter des marchandises",
                               [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_achat()]]
            i += 1
            self.options[i] = ["Vendre des marchandises",
                               [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_vente()]]
            i += 1

        self.options[i] = ["Acheter un bateau",[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_achat_bateaux()]]
        i += 1
        self.options[i] = ["Accéder à la banque", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_banque()]]
        i += 1
        self.options[i] = ["Retour au menu principal", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_principal()]]

    def afficher_corps(self):
        nom_port = self.joueur.obtenir_nom_lieu()
        print(f"Bienvenue au marché de {nom_port}.")
        print(f"Vos florins : {self.joueur.obtenir_florins()}")


class MenuAchat(Menu):
    def __init__(self, monde, jeu, bateau, joueur):
        super().__init__(monde, jeu)
        self.bateau = bateau
        self.joueur = joueur
        self.port = self.joueur.obtenir_lieu()

    def charger_options(self):
        i = 1
        for nom, prix in self.port.prix_locaux_marchandises.items():
            vol = MARCHANDISES[nom]["volume"]
            self.options[i] = [f"{nom} ({prix} florins, volume: {vol})", [self.acheter, nom]];
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_marche()]]

    def afficher_corps(self):
        print(f"--- Acheter des marchandises à {self.port.obtenir_nom()} ---")
        print(
            f"Capacité restante du {self.bateau.obtenir_nom()}: {self.bateau.capacite - self.bateau.obtenir_volume_utilise()}")
        print(f"Vos florins: {self.joueur.obtenir_florins()}")

    def acheter(self, nom_marchandise):
        try:
            qte = int(input(f"Quelle quantité de {nom_marchandise} acheter ? "))
            if qte <= 0: return

            prix = self.port.prix_locaux_marchandises[nom_marchandise]
            achat = AchatMarchandises(self.joueur,self.port,qte,nom_marchandise,prix,self.bateau)
            reussite = achat.verifier_appliquer()
            if not reussite:
                print(achat.obtenir_erreur())
            else:
                print(f"{qte} unité(s) de {nom_marchandise} achetée(s) pour {achat.obtenir_montant()} florins.")
        except ValueError:
            print("Veuillez entrer un nombre.")
        input("Appuyez sur Entrée pour continuer...")
        self.jeu.changer_menu_actif(self.jeu.obtenir_constructeur_menu().construire_menu_achat())


class MenuVente(Menu):
    def __init__(self, monde, jeu, bateau, joueur):
        super().__init__(monde, jeu)
        self.bateau = bateau
        self.joueur = joueur
        self.port = self.joueur.obtenir_lieu()
        

    def charger_options(self):
        i = 1
        if not self.bateau.cargaison: self.options[i] = ["Retour", [self.jeu.changer_menu_actif,
                                                                    self.constructeur_menu.construire_menu_marche()]]; return
        for nom in self.bateau.obtenir_liste_cargaisons():
            prix = self.port.prix_locaux_marchandises.get(nom, 0)
            qte = self.bateau.obtenir_quantite_cargaison(nom)
            self.options[i] = [f"{nom} (Quantité: {qte}, Prix de vente: {prix})", [self.vendre, nom]];
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_marche()]]

    def afficher_corps(self):
        print(f"--- Vendre des marchandises depuis {self.bateau.obtenir_nom()} à {self.port.obtenir_nom()} ---")
        if not self.bateau.cargaison: print("La soute est vide.")

    def vendre(self, nom_marchandise):
        try:
            qte_max = self.bateau.cargaison[nom_marchandise]
            qte = int(input(f"Quelle quantité de {nom_marchandise} vendre (max {qte_max}) ? "))
            if qte <= 0: return

            prix = self.port.obtenir_prix_marchandises(nom_marchandise)
            vente = VenteMarchandises(self.joueur,self.port,qte,nom_marchandise,prix,self.bateau)
            if not(vente.verifier_appliquer()):
                print(vente.obtenir_erreur())
            else:
                print(f"{qte} unité(s) de {nom_marchandise} vendue(s) pour {vente.obtenir_montant()} florins.")
        except ValueError:
            print("Veuillez entrer un nombre.")
        input("Appuyez sur Entrée pour continuer...")
        self.jeu.changer_menu_actif(self.constructeur_menu.construire_menu_vente())

class MenuAchatBateaux(Menu):
    def __init__(self, monde, jeu, joueur,port):
        super().__init__(monde, jeu)
        self.joueur = joueur
        self.port = port
    def charger_options(self):
        i = 1
        for bateau in BATEAUX.keys():
            self.options[i] = [f"{bateau} : {self.port.obtenir_prix_bateau(bateau)} florins",[self.achat,bateau]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_marche()]]
    def afficher_corps(self):
        print(f"--- Acheter un navire à {self.port.obtenir_nom()} ---")
    def achat(self,type_bateau):
        prix = self.port.prix_locaux_bateaux[type_bateau]
        self.jeu.changer_menu_actif(self.constructeur_menu.construire_menu_achat_bateau(type_bateau,self.port.obtenir_prix_bateau(type_bateau)))

