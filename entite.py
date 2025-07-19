class Entite:
    def __init__(self, position_initiale):
        from position import Position
        self.position = Position(position_initiale)
        self._itineraire = None  # Liste de lieux à suivre

    from itineraire import Itineraire
    def definir_itineraire(self, itineraire):
        """Assigne un nouvel itinéraire à l'entité et démarre le premier déplacement."""
        assert not itineraire.est_vide(), "L’itinéraire doit contenir au moins une étape."
        
        lieu_actuel = self.position.obtenir_lieu_actuel()
        premiere_etape = itineraire.obtenir_prochaine_etape()
        assert premiere_etape == lieu_actuel or premiere_etape in lieu_actuel.obtenir_voisins(), \
            "Le début de l’itinéraire doit être le lieu actuel ou un voisin direct."

        self._itineraire = itineraire

    def avancer(self):
        """
        Fait avancer l'entité selon sa vitesse,
        potentiellement sur plusieurs étapes de l'itinéraire.
        """
        assert self._itineraire is not None, "Aucun itinéraire défini."
        assert not self._itineraire.est_termine(), "L'itinéraire est terminé."

        vitesse_restante = self.obtenir_vitesse()

        # Tant qu'il reste de la vitesse et qu'il y a des étapes à parcourir
        while vitesse_restante > 0 and not self._itineraire.est_termine():

            # 1) Si on n'est pas déjà en mouvement, on lance le prochain segment
            if not self.position.est_en_transit():
                prochain = self._itineraire.obtenir_prochaine_etape()
                assert prochain is not None, "Pas de prochaine étape dans l'itinéraire."
                assert prochain is not self.position.obtenir_lieu_actuel(), \
                    "La prochaine étape doit être différente du lieu actuel."
                self.position.debuter_deplacement(prochain)

            # 2) On avance sur le segment courant
            distance_faite = self.position.avancer(vitesse_restante)
            vitesse_restante -= distance_faite

            # 3) Si on vient d'atteindre la fin du segment, on passe à l'étape suivante
            if self.position.est_arrive():
                self._itineraire.avancer_etape()

        # 4) Si on est arrivé et que l'itinéraire est terminé, on le supprime
        if self.position.est_arrive() and self._itineraire.est_termine():
            del self._itineraire



    def obtenir_vitesse(self):
        # Vitesse par défaut, à surcharger si besoin
        return 1

    def est_en_transit(self):
        return self.position.est_en_transit()

    def obtenir_position(self):
        return self.position

    def a_une_destination_proche(self):
        return self.position.a_une_destination()

    def obtenir_lieu(self):
        return self.position.obtenir_lieu_actuel()

    def obtenir_voisins_lieu(self):
        return self.position.obtenir_voisins_lieu()

    def obtenir_nom_lieu(self):
        return self.position.obtenir_nom_lieu()

    def changer_destination(self, destination):
        """Construit un itinéraire vers une destination"""
        from constantes import construire_chemin_dijkstra

        depart = self.position.obtenir_lieu_actuel()
        nouvel_itineraire = construire_chemin_dijkstra(depart, destination)
        assert nouvel_itineraire is not None, "Impossible de construire un itinéraire."
        self.definir_itineraire(nouvel_itineraire)
        self.verifier_invariants()


    def itineraire_est_termine(self):
        return self._itineraire.est_termine()

    def a_un_itineraire(self):
        return self._itineraire is not None

    def obtenir_prochaine_etape(self):
        return self._itineraire.obtenir_prochaine_etape()
    
    def obtenir_distance_prochaine_etape(self):
        return self.position.obtenir_distance_restante()

    def verifier_invariants(self):
        from itineraire import Itineraire
        if self._itineraire:
            assert isinstance(self._itineraire, Itineraire), "L'itinéraire doit être une instance de Itineraire."