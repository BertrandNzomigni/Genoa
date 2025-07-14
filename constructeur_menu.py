# mon_super_jeu/constructeur_menu.py

from menus import *
from menu_gestion_bateau import *
from menu_information_bateau import *
from menu_achat_bateau import *
from menu_missions import *
from menu_banque import MenuBanque
import bateau
import mission_schema

class ConstructeurMenu:
    """Classe 'Factory' pour créer les différents menus du jeu."""

    def __init__(self, monde, jeu):
        self.monde = monde
        self.jeu = jeu
        self.joueur = monde.obtenir_joueur()
        self.bateaux = self.joueur.obtenir_bateaux()

    def construire_menu_principal(self):
        return MenuPrincipal(self.monde, self.jeu, self.monde.obtenir_temps())

    def construire_menu_bateaux_port(self):
        return MenuBateauxPort(self.monde, self.jeu,self.joueur)

    def construire_menu_bateaux_global(self):
        return MenuBateauxGlobal(self.bateaux, self.monde, self.jeu)

    def construire_menu_deplacement(self):
        return MenuDeplacement(self.monde, self.jeu,self.joueur)

    def construire_menu_marche(self):
        return MenuMarche(self.monde, self.jeu, self.joueur.obtenir_bateau_dirige(),self.joueur)

    def construire_menu_achat(self):
        return MenuAchat(self.monde, self.jeu, self.joueur.obtenir_bateau_dirige(),self.joueur)

    def construire_menu_vente(self):
        return MenuVente(self.monde, self.jeu, self.joueur.obtenir_bateau_dirige(),self.joueur)

    def construire_menu_achat_bateaux(self):
        return MenuAchatBateaux(self.monde,self.jeu,self.joueur,self.joueur.obtenir_lieu())

    def construire_menu_gestion_bateaux(self,bateau):
        return MenuGestionBateau(self.monde,self.jeu,bateau,self.joueur)

    def construire_menu_information_bateau(self,bateau):
        return MenuInformationBateau(self.monde,self.jeu,bateau)

    def construire_menu_achat_bateau(self,type_bateau,prix):
        return MenuAchatBateau(self.monde,self.jeu,type_bateau,prix,self.joueur)
    
    def construire_menu_missions(self,mission,bateau):
        return MenuMissions(self.monde,self.jeu,bateau,mission)
    
    def construire_menu_ajout_arret(self,_mission,_bateau):
        assert isinstance(_mission,mission_schema.MissionSchema)
        assert isinstance(_bateau,bateau.Bateau)
        return MenuAjoutArret(self.monde,self.jeu,_bateau,_mission)

    def construire_menu_suppression_arret(self,mission,bateau):
        return MenuSuppresionArret(self.monde,self.jeu,mission,bateau)

    def construire_menu_banque(self):
        return MenuBanque(self.monde, self.jeu, self.joueur)

    def construire_menu_modification_arrets(self,mission,bateau):
        return MenuModificationArrets(self.monde,self.jeu,mission,bateau)

    def construire_menu_modification_arret(self,arret,menu_anterieur):
        return MenuModificationArret(self.monde,self.jeu,arret,menu_anterieur)

