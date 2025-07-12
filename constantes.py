# mon_super_jeu/constantes.py
# Fonctions utiles et constantes (ex: MARCHANDISES)

import os

#Définition globale des marchandises disponibles dans le jeu

MARCHANDISES = {
    "Soie": {"volume": 2},
    "Épices": {"volume": 1},
    "Vin": {"volume": 3},
    "Bois": {"volume": 5}
}

BATEAUX = {
    "Nef" : {"Capacité" : 300, "Vitesse" : 10},
    "Galère" : {"Capacité" : 50, "Vitesse" : 20},
    "Caraque" : {"Capacité" : 250, "Vitesse" : 20},
    "Cocha" : {"Capcité" : 200, "Vitesse" : 10}
}

def clear_screen():
    """efface 'ecran de la consoe."""
    os.system('cls' if os.name=='nt' else 'clear')

def nothing():
    """Fonction qui ne fait rien, utilisé comme placeholder."""
    pass


