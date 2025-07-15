# mon_super_jeu/constantes.py
# Fonctions utiles et constantes (ex: MARCHANDISES)

import os

import heapq

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


import heapq
import itertools
from lieu import Lieu
from itineraire import Itineraire

def construire_chemin_dijkstra(depuis: Lieu, jusqu_a: Lieu) -> Itineraire:
    assert isinstance(depuis, Lieu), f"Le point de départ doit être un objet Lieu, pas {type(depuis)}"
    assert isinstance(jusqu_a, Lieu), f"Le point d'arrivée doit être un objet Lieu, pas {type(jusqu_a)}"
    
    heap = []
    compteur = itertools.count()
    heapq.heappush(heap, (0, next(compteur), depuis, [depuis]))
    visite = set()

    iterations = 0
    while heap:        
        iterations += 1
        if iterations > 10000:
            raise RuntimeError("Trop d'itérations dans Dijkstra, boucle infinie probable.")
        dist_courante, _, noeud_courant, chemin = heapq.heappop(heap)
        if noeud_courant in visite:
            continue
        visite.add(noeud_courant)

        if noeud_courant == jusqu_a:
            # Ne pas enlever le premier lieu si tu veux l’itinéraire complet
            return Itineraire(chemin[1:])
        for voisin in noeud_courant.obtenir_voisins():
            if voisin not in visite:
                dist_voisin = noeud_courant.obtenir_distance(voisin)
                assert dist_voisin > 0, f"Distance non valide entre {noeud_courant} et {voisin}: {dist_voisin}"
                heapq.heappush(heap, (dist_courante + dist_voisin, next(compteur), voisin, chemin + [voisin]))

    raise ValueError(f"Aucun chemin trouvé de {depuis} à {jusqu_a}")



