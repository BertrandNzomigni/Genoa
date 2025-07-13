import constantes
import menus
import mission
class MenuMissions(menus.Menu):
    def __init__(self,monde,jeu,bateau):
        super().__init__(monde, jeu)
        self.bateau = bateau


    def charger_options(self):
        i = 1
        self.options[i] = ["Ajouter un arrét",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_ajout_arret(self.bateau)]]
        i += 1
        if self.bateau.a_mission():
            self.options[i] = ["Supprimer un arrêt",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_suppression_arret(self.bateau.obtenir_mission(),self.bateau)]]
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
        i = 1
        for port in self.monde.obtenir_ports():
            self.options[i] = [f"Ajouter un arrêt à {port.obtenir_nom()}",[self.bateau.ajouter_arret,mission.Arret(port,self.bateau)],[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.bateau)]]
        
class MenuSuppresionArret(menus.Menu):
    def __init__(self,monde,jeu,_mission,bateau):
        super().__init__(monde, jeu)
        assert isinstance(_mission,mission.Mission), f"{_mission} n'est pas une mission."
        self.mission = _mission
        self.bateau = bateau
    def charger_options(self):
        i = 1
        for arret in self.mission.obtenir_arrets():
            self.options[i] = [f"Supprimer l'arrêt à {arret.obtenir_nom_lieu()}",[self.bateau.supprimer_arret,arret],[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.bateau)]]

class MenuModificationArrets(menus.Menu):
    def __init__(self,monde,jeu,mission,bateau):
        super().__init__(monde, jeu)
        self.mission = mission
        self.bateau = bateau
    def charger_options(self):
        i = 1
        for arret in self.mission.obtenir_arrets():
            self.options[i] = [f"Modifier l'arrêt à {arret.obtenir_nom_lieu()}",[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_modification_arret(arret,self)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.bateau)]]
    def afficher_corps(self):
        print("--- Modifier un arrêt ---")

class MenuModificationArret(menus.Menu):
    def __init__(self,monde,jeu,arret,menu_anterieur):
        super().__init__(monde, jeu)
        assert isinstance(arret,mission.Arret), "L'arrêt doit être une instance de la classe arrêt."
        self.arret = arret
        self.menu_anterieur = menu_anterieur
    def charger_options(self):
        i = 1
        for marchandise in constantes.MARCHANDISES.keys():
            self.options[i] = [f"Le bateau partira avec {self.arret.obtenir_quantite_marchandise(marchandise)} unités de {marchandise} (Volume unitaire : {constantes.MARCHANDISES[marchandise]['volume']}): Modifier quantité",[self.modifier_quantite,marchandise]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.menu_anterieur]]
    def afficher_corps(self):
        print(f"--- Arrêt à {self.arret.obtenir_nom_lieu()} ---")
        print(f"Volume : {self.arret.volume_total()}/{self.arret.obtenir_bateau().obtenir_capacite()}")
    def modifier_quantite(self,nom_marchandise):
        correct = False
        while not correct:
            try:
                quantite = int(input("Donnez une quantité : "))
                if self.verifier_volume(nom_marchandise,quantite):
                    self.arret.modifier_quantite_marchandise(nom_marchandise,quantite)
                    correct = True
                else:
                    input("Le volume total en marchandise est supérieur à la capacité du bateau.")
            except Exception as error:
                print(f"Erreur : {error}")
        return quantite
    def verifier_volume(self,nom_marchandise,quantite):
        quantite2 = 0
        for marchandise in constantes.MARCHANDISES.keys():
            if marchandise != nom_marchandise:
                quantite2 += self.arret.obtenir_quantite_marchandise(marchandise) * constantes.MARCHANDISES[marchandise]["volume"]
            else:
                quantite2 += quantite * constantes.MARCHANDISES[nom_marchandise]["volume"]
        return quantite2 <= self.arret.obtenir_bateau().obtenir_capacite()
