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
    "Nef" : {"Capacité" : 300, "Vitesse" : 10, "Prix de base": 1000},
    "Galère" : {"Capacité" : 50, "Vitesse" : 20, "Prix de base": 2000},
    "Caraque" : {"Capacité" : 250, "Vitesse" : 20, "Prix de base": 3000},
    "Cocha" : {"Capacité" : 200, "Vitesse" : 10, "Prix de base": 2500},
    "Bateau de test" : {"Capacité" : 10000, "Vitesse" : 1000, "Prix de base": 0}
}

def clear_screen():
    """efface 'ecran de la consoe."""
    os.system('cls' if os.name=='nt' else 'clear')

def nothing():
    """Fonction qui ne fait rien, utilisé comme placeholder."""
    pass


