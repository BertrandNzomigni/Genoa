import menus
import constantes
class MenuAchatBateau(menus.Menu):
    def __init__(self,monde,jeu,type_bateau,prix,joueur):
        super().__init__(monde, jeu)
        assert isinstance(type_bateau,str), "Le type de bateau doit être une chaine de caractère."
        self.type_bateau = type_bateau
        self.prix = prix
        self.joueur = joueur
    def charger_options(self):
        self.options[1] = ["Acheter",[self.acheter]]
        self.options[2] = ["Retour",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_achat_bateaux()]]
    def afficher_corps(self):
        bateau = constantes.BATEAUX[self.type_bateau]
        print("--- Achat d'un bateau ---")
        print(f"Type : {self.type_bateau}")
        print(f"Capacité : {bateau['Capacité']}")
        print(f"Vitesse : {bateau['Vitesse']}")
        print(f"Prix : {self.prix}")
    def acheter(self):
        correct = False
        while not correct:
            reponse = input(f"Confirmez vous l'achat de {self.type_bateau} ? (Y/N)").upper()
            retour = self.joueur.peut_acheter_bateau(self.type_bateau)
            if isinstance(retour,str):
                input(retour+" - Appuyez sur une touche pour continuer")
                return
            if reponse == 'Y':
                self.acheter2()
                correct = True
            elif reponse == "N":
                return
            else:
                print("Entrée incorrecte")

    def acheter2(self):
        nom = input("Donnez un nom au bateau : ")
        correct = False
        while not correct:
            reponse = (input(f"Le nom du bateau sera {nom}. Confirmez vous ? (Y/N) :")).upper()
            if reponse == "Y":
                correct = True
            elif reponse == "N":
                return
            else:
                print("Entrée incorrecte")
        self.joueur.acheter_bateau(self.type_bateau,nom)