import constantes
import menus
import mission
class MenuMissions(menus.Menu):
    def __init__(self,monde,jeu,bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau


    def charger_options(self):
        self.constructeur_menu = self.jeu.obtenir_constructeur_menu()
        i = 1
        self.options[i] = ["Définir un arrét",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_ajout_arret(self.bateau)]]
        i += 1
        if self.bateau.a_mission():
            self.options[i] = ["Supprimer un arrêt",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_suppresion_arret(self.bateau.obtenir_mission(),self.bateau)]]
            i += 1
            self.options[i] = ["Modifier un arrêt",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_modification_arrets(self.bateau.obtenir_mission(),self.bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.verification_et_sortie]]


    def afficher_corps(self):
        print("--- Arrêts ---")
        for arret in self.bateau.obtenir_arrets():
            print(f"Arrét à {arret.obtenir_nom_lieu()}")
        if len(self.bateau.obtenir_arrets()) == 0:
            print("Ce bateau n'a pas d'arrêts.")
    def verification_et_sortie(self):
        correct = True
        if self.bateau.a_mission():
            correct = self.bateau.obtenir_mission().verifier()
        if correct:
            if self.bateau.a_mission():
                self.bateau.obtenir_mission().verifier_invariants()
            self.jeu.changer_menu_actif(self.constructeur_menu.construire_menu_gestion_bateaux(self.bateau))
        else:
            input("Attention, la mission est incorrecte")
            

class MenuAjoutArret(menus.Menu):
    def __init__(self,monde,jeu,bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        i = 1
        for port in self.monde.obtenir_ports():
            self.options[i] = [f"Ajouter un arrêt à {port.obtenir_nom()}",[self.bateau.ajouter_arret,mission.Arret(port)],[self.jeu.changer_menu_actif, constructeur_menu.construire_menu_missions(self.bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_missions(self.bateau)]]
        
class MenuSuppresionArret(menus.Menu):
    def __init__(self,monde,jeu,_mission,bateau):
        super().__init__(monde, jeu)
        assert isinstance(_mission,mission.Mission), f"{_mission} n'est pas une mission."
        self.mission = _mission
        self.bateau = bateau
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        i = 1
        for arret in self.mission.obtenir_arrets():
            self.options[i] = [f"Supprimer l'arrêt à {arret.obtenir_nom_lieu()}",[self.bateau.supprimer_arret,arret],[self.jeu.changer_menu_actif, constructeur_menu.construire_menu_missions(self.bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_missions(self.bateau)]]

class MenuModificationArrets(menus.Menu):
    def __init__(self,monde,jeu,mission,bateau):
        super().__init__(monde, jeu)
        self.mission = mission
        self.bateau = bateau
    def charger_options(self):
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        i = 1
        for arret in self.mission.obtenir_arrets():
            self.options[i] = [f"Modifier l'arrêt à {arret.obtenir_nom_lieu()}",[constantes.nothing]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, constructeur_menu.construire_menu_missions(self.bateau)]]
    def afficher_corps(self):
        print("--- Modifier un arrêt ---")