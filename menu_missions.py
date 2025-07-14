import constantes
import menus
import mission
from mission_schema import MissionSchema
import bateau
class MenuMissions(menus.Menu):
    def __init__(self,monde,jeu,bateau,mission):
        super().__init__(monde, jeu)
        self.bateau = bateau
        if mission:
            assert isinstance(mission,MissionSchema), f"{mission} n'est pas un schéma de mission."
            self.mission_schema = mission
        else:
            self.mission_schema = MissionSchema()
    def charger_options(self):
        i = 1
        self.options[i] = ["Ajouter un arrét",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_ajout_arret(self.mission_schema,self.bateau)]]
        i += 1
        if len(self.mission_schema.obtenir_arrets()) > 0:
            self.options[i] = ["Supprimer un arrêt",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_suppression_arret(self.mission_schema,self.bateau)]]
            i += 1
            self.options[i] = ["Modifier un arrêt",[self.jeu.changer_menu_actif,self.constructeur_menu.construire_menu_modification_arrets(self.mission_schema,self.bateau)]]
            i += 1
            self.options[i] =  ["Changer le nombre de cycles",[self.changer_cycle]]
            i += 1
        self.options[i] = ["Retour", [self.verification_et_sortie]]

    def changer_cycle(self):
        correct = False
        while not correct:
            try:
                cycle = int(input("Donner le nouveau nombre de cycle :"))
                correct = True
            except:
                print("Veuillez saisir un nombre.")
        self.mission_schema.definir_nombre_max_cycles(cycle)

    def afficher_corps(self):
        
        print("--- Mission ---")
        if len(self.mission_schema.obtenir_arrets()) > 0:
            print(f"La mission sera finie au bout de {self.mission_schema.obtenir_nombre_max_cycles()} cycles.")

        print("--- Arrêts ---")
        if len(self.mission_schema.obtenir_arrets()) == 0:
            print("Ce bateau n'a pas d'arrêts.")
        else:
            for arret in self.mission_schema.obtenir_arrets():
                print(f"Arrét à {arret.obtenir_nom_lieu()}")
    def verification_et_sortie(self):      
        if len(self.mission_schema.obtenir_arrets()) > 0:
            correct = self.mission_schema.verifier()
            if correct:
                self.bateau.nouvelle_mission(mission.Mission(self.mission_schema))
                self.jeu.changer_menu_actif(self.constructeur_menu.construire_menu_gestion_bateaux(self.bateau))
            else:
                input("Attention, la mission est incorrecte")
        else:
            self.jeu.changer_menu_actif(self.constructeur_menu.construire_menu_gestion_bateaux(self.bateau))
            
            

class MenuAjoutArret(menus.Menu):
    def __init__(self,monde,jeu,_bateau,_mission):
        super().__init__(monde, jeu)
        assert isinstance(_bateau,bateau.Bateau)
        assert isinstance(_mission,MissionSchema)
        self.bateau = _bateau
        self.mission = _mission
    def charger_options(self):
        i = 1
        for port in self.monde.obtenir_ports():
            self.options[i] = [f"Ajouter un arrêt à {port.obtenir_nom()}",[self.mission.ajouter_arret,mission.Arret(port,self.bateau),-1],[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.mission,self.bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.mission,self.bateau)]]
        
class MenuSuppresionArret(menus.Menu):
    def __init__(self,monde,jeu,_mission,bateau):
        super().__init__(monde, jeu)
        assert isinstance(_mission,MissionSchema), f"{_mission} n'est pas un schéma de mission."
        self.mission = _mission
        self.bateau = bateau
    def charger_options(self):
        i = 1
        for arret in self.mission.obtenir_arrets():
            self.options[i] = [f"Supprimer l'arrêt à {arret.obtenir_nom_lieu()}",[self.mission.supprimer_arret,arret],[self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.mission,self.bateau)]]
            i += 1
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.mission,self.bateau)]]

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
        self.options[i] = ["Retour", [self.jeu.changer_menu_actif, self.constructeur_menu.construire_menu_missions(self.mission,self.bateau)]]
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
