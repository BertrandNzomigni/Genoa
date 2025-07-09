import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Afficher le menu principal
# Traiter les entrées du menu principal
class MenuPrincipal:
    def __init__(self,monde,jeu,temps):
        self.monde = monde
        self.jeu = jeu
        self.temps = temps
        self.options = dict()
        self.charger_options()
    def charger_options(self):
        i = 1
        self.options[i] = ("Jour suivant",self.temps.avancer)
        i += 1
        self.options[i] = ("Sélectionner une nouvelle destination",self.jeu.changer_menu_actif,[MenuDeplacement(self.monde,self.jeu)])
        i += 1
        self.options[i] = ("Voir l'ensemble de vos bateaux",self.jeu.changer_menu_actif,[MenuBateauxGlobal(self.monde.obtenir_joueur(),self.monde,self.jeu)])
        i += 1
        if type(self.monde.obtenir_joueur().obtenir_lieu()) is Port:
            self.options[i] = ("Voir vos bateaux dans le port",self.jeu.changer_menu_actif,[MenuBateaux(self.monde,self.jeu)])
            i += 1
        self.options[i] = ("Quitter le jeu",self.jeu.quitter)
    def afficher(self):
        j = self.monde.obtenir_joueur()
        print(f"Jour : {self.monde.obtenir_temps().obtenir_valeur()}")
        print(f"Vous avez actuellement {j.obtenir_florins()} florins.")
        if j.obtenir_itineraire().a_destination():
            print(f"Vous naviguez vers {j.obtenir_itineraire().obtenir_destination()}")
            print(f"{j.obtenir_itineraire().obtenir_depart()} est derrière vous.")
            print(f"La distance restante est de {j.obtenir_itineraire().obtenir_distance()*10} kilomètres.")
        else:
            print(f"Vous êtes situé à {j.obtenir_lieu()}.")
            print("Vous n'êtes pas en cours de déplacement.")
        for i in range(1,len(self.options)+1):
            print(f"{i}) {self.options[i][0]}")
    def lire(self):
        try:
            entree = int(input())
            if entree in self.options.keys():
                if len(self.options[entree]) > 2:
                    self.options[entree][1](*self.options[entree][2])
                else:
                    self.options[entree][1]()
        except ValueError:
            print("Entrée non valide. Veuillez entrer un nombre.")


# Affiche le menu de déplacement
# Déclenche les déplacements en fonction des entrées
class MenuDeplacement:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
        self.options = dict()
        self.charger_options()
    def charger_options(self):
        self.pas_en_chemin = not self.monde.obtenir_joueur().obtenir_itineraire().a_destination()
        if self.pas_en_chemin :
            destinations = self.monde.obtenir_joueur().obtenir_lieu().obtenir_lieu().obtenir_voisins()
            i = 1
            for destination in destinations:
                self.options[i] = destination
                i += 1
    def afficher(self):
        if self.pas_en_chemin :
            print(f"Liste des destinations accesibles depuis {self.monde.obtenir_joueur().obtenir_lieu().obtenir_nom()}.")
            for cle in self.options.keys():
                print(f"{cle}) {self.options[cle].obtenir_nom()}")
            print(f"{len(self.options.keys())+1}) Quitter")
        else:
            print("1) Faire demi-tour")
            print("2) Quitter")
    def lire(self):
        try :
            entree = int(input())
            constructeur_menu = self.jeu.obtenir_constructeur_menu()
            if self.pas_en_chemin:
                if entree in self.options.keys():
                    self.monde.obtenir_joueur().obtenir_coordinateur().aller_destination(self.options[entree])
                    self.jeu.changer_menu_actif(constructeur_menu.construire_menu_principal())
                elif entree == len(self.options.keys())+1:
                    self.jeu.changer_menu_actif(constructeur_menu.construire_menu_principal())
            else:
                if entree == 1:
                    self.monde.obtenir_joueur().obtenir_coordinateur().faire_demi_tour()
                    self.jeu.changer_menu_actif(constructeur_menu.construire_menu_principal())
                elif entree == 2:
                    self.jeu.changer_menu_actif(constructeur_menu.construire_menu_principal())
        except ValueError:
            print("Entrée non valide. Veuillez entrer un nombre.")

class Bateau:
    def __init__(self,nom,capacite,vitesse,lieu):
        self.nom = nom
        self.capacite = capacite
        self.vitesse = vitesse
        self.lieu = lieu
    def obtenir_nom(self):
        return self.nom
    def obtenir_lieu(self):
        return self.lieu

class MenuBateaux:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
        self.options = dict()
        self.charger_options()
    def charger_options(self):
        lieu_joueur = self.monde.obtenir_joueur().obtenir_lieu().obtenir_lieu()
        i = 1
        for bateau in lieu_joueur.obtenir_bateaux():
            self.options[i] = bateau
            i += 1
    def afficher(self):
        print(f"Liste des bateaux à {self.monde.obtenir_joueur().obtenir_lieu().obtenir_nom()} :")
        for i in range(1,len(self.options)+1):
            print(f"{i}) {self.options[i].obtenir_nom()}")
        print(f"{len(self.options)+1}) Quitter")
    def lire(self):
        try :
            entree = int(input())
            constructeur_menu = self.jeu.obtenir_constructeur_menu()
            if entree in self.options.keys():
                pass
            elif entree == len(self.options.keys())+1:
                self.jeu.changer_menu_actif(constructeur_menu.construire_menu_principal())
        except ValueError:
            print("Entrée non valide. Veuillez entrer un nombre.")

class MenuBateauxGlobal:
    def __init__(self,joueur,monde,jeu):
        self.joueur = joueur
        self.monde = monde
        self.jeu = jeu
    def afficher(self):
        print("Liste des bateaux")
        for bateau in self.joueur.obtenir_bateaux():
            print(f"{bateau.obtenir_nom()} : {bateau.obtenir_lieu().obtenir_nom()}")
        print("1) Revenir au menu principal")
    def lire(self):
        entree = input()
        constructeur_menu = self.jeu.obtenir_constructeur_menu()
        if entree == "1":
            self.jeu.changer_menu_actif(constructeur_menu.construire_menu_principal())


# Connait les entités du monde    
class Monde:
    def __init__(self):
        self.ports = [Port("Gênes"),Port("Venise")]
        self.mers = [Mer("Mer Adriatique")]

        # Connexions
        self.connecter_lieu(self.ports[0],self.mers[0],5)
        # Création bateau
        self.joueur = Joueur(self.ports[0])
        premier_bateau = Bateau("Navire de base",0,10,self.ports[0])
        self.ports[0].obtenir_lieu().ajouter_bateau(premier_bateau)
        self.joueur.acquerir_bateau(premier_bateau)
        self.temps = Temps(self)
    def obtenir_joueur(self):
        return self.joueur
    def obtenir_temps(self):
        return self.temps
    def changer_temps(self,temps):
        self.temps = temps
    def connecter_lieu(self,lieu1,lieu2,distance):
        lieu1.obtenir_lieu().ajouter_voisin(lieu2,distance)
        lieu2.obtenir_lieu().ajouter_voisin(lieu1,distance)
    def avancer_temps(self):
        self.temps.avancer()


# Sait le tour actuel
# Fait avancer le temps en actualisant le monde
class Temps:
    def __init__(self,monde):
        self.monde = monde
        self.jours = 0
    def avancer(self):
        self.jours += 1
        self.monde.obtenir_joueur().obtenir_coordinateur().avancer()
    def obtenir_valeur(self):
        return self.jours

# Connait les informations du joueur
class Joueur:
    def __init__(self,lieu_de_depart):
        self.florins = 2000
        self.itineraire = Itineraire(self)
        self.lieu = lieu_de_depart
        self.deplaceur = Deplaceur(self.itineraire,self)
        self.coord = CoordinationMouvement(self,self.deplaceur,self.itineraire)
        self.bateaux = list()
        self.bateau_dirige = None
    def obtenir_florins(self):
        return self.florins
    def obtenir_itineraire(self):
        return self.itineraire
    def obtenir_lieu(self):
        return self.lieu
    def changer_lieu(self,lieu):
        self.lieu = lieu
    def obtenir_coordinateur(self):
        return self.coord
    def acquerir_bateau(self,bateau):
        self.bateaux.append(bateau)
    def obtenir_bateaux(self):
        return self.bateaux
    def rejoint_bateau(self,bateau):
        self.bateau_dirige = bateau
    def quitte_bateau(self):
        self.bateau_dirige = None
        

# Recoit les messages de mouvement
# Traite les messages de mouvement
class CoordinationMouvement:
    def __init__(self,entite,deplaceur,itineraire):
        self.entite = entite
        self.deplaceur = deplaceur
        self.itineraire = itineraire
    def aller_destination(self,dest):
        self.itineraire.aller_destination(dest)
    def faire_demi_tour(self):
        if self.itineraire.obtenir_distance() == 0:
            self.entite.changer_lieu(self.itineraire.obtenir_destination())
        self.itineraire.faire_demi_tour()
    def avancer(self):
        self.deplaceur.avancer()

# Connait l'itinéraire d'une entité
# Change l'itinéraire d'une entité
class Itineraire:
    def __init__(self,acteur):
        self.destination = None
        self.depart = None
        self.distance_destination = 0
        self.acteur = acteur
    def obtenir_destination(self):
        return self.destination
    def changer_destination(self,destination):
        self.destination = destination
    def obtenir_depart(self):
        return self.depart
    def changer_depart(self,depart):
        self.depart = depart
    def obtenir_distance(self):
        return self.distance_destination
    def changer_distance(self,distance):
        self.distance_destination = distance
    def aller_destination(self,dest):
        self.destination = dest
        self.depart = self.acteur.obtenir_lieu()
        self.distance_destination = dest.obtenir_lieu().obtenir_distance(self.acteur.obtenir_lieu())
    def a_atteint_destination(self):
        return self.distance_destination == 0
    def a_destination(self):
        return self.destination != None
    def faire_demi_tour(self):
        x = self.destination
        self.destination = self.depart
        self.depart = x
        self.distance_destination = self.destination.obtenir_lieu().obtenir_distance(self.obtenir_depart()) - self.distance_destination
        if self.distance_destination == 0:
            self.destination = None
            self.depart = None


# Déplace une entité en fonction de son itinéraire
class Deplaceur:
    def __init__(self,itineraire,acteur):
        self.itineraire = itineraire
        self.acteur = acteur
    def avancer(self):
        if self.itineraire.obtenir_distance() == 1:
            self.acteur.changer_lieu(self.itineraire.obtenir_destination())
            self.itineraire.changer_destination(None)
            self.itineraire.changer_depart(None)
        self.itineraire.changer_distance(self.itineraire.obtenir_distance() - 1)
    def changer_lieu(self,lieu):
        self.acteur.changer_lieu(lieu)
            
class Lieu:
    def __init__(self):
        self.voisins = list()
        self.dict_distance = dict()
        self.bateaux = list()
    def ajouter_voisin(self,voisin,distance):
        self.voisins.append(voisin)
        self.dict_distance[voisin] = distance
    def obtenir_voisins(self):
        return self.voisins
    def obtenir_distance(self,voisin):
        return self.dict_distance[voisin]
    def ajouter_bateau(self,bateau):
        self.bateaux.append(bateau)
    def obtenir_bateaux(self):
        return self.bateaux
        
class Port:
    def __init__(self,nom):
        self.nom = nom
        self.lieu = Lieu()
    def obtenir_nom(self):
        return self.nom
    def obtenir_lieu(self):
        return self.lieu
    def __str__(self):
        return self.nom
    
class Mer:
    def __init__(self,nom):
        self.nom = nom
        self.lieu = Lieu()
    def obtenir_nom(self):
        return self.nom
    def obtenir_lieu(self):
        return self.lieu
    def __str__(self):
        return self.nom

class Jeu:
    def __init__(self):
        self.monde = Monde()
        self.constructeur_menu = ConstructeurMenu(self.monde,self)
        self.menu_actif = self.constructeur_menu.construire_menu_principal()
        self.actif = True
    def obtenir_constructeur_menu(self):
        return self.constructeur_menu
    def changer_menu_actif(self,menu):
        self.menu_actif = menu
    def demarrer(self):
        while self.actif:
            clear_screen()
            self.menu_actif.afficher()
            self.menu_actif.lire()
    def quitter(self):
        self.actif = False

class ConstructeurMenu:
    def __init__(self,monde,jeu):
        self.monde = monde
        self.jeu = jeu
    def construire_menu_principal(self):
        return MenuPrincipal(self.monde,self.jeu,self.monde.obtenir_temps())
jeu = Jeu()
jeu.demarrer()
