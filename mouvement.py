# mon_super_jeu/mouvement.py

from lieu import Mer


class CoordinationMouvement:
    """Coordonne les actions de mouvement."""

    def __init__(self, entite, deplaceur, itineraire):
        self.entite = entite
        self.deplaceur = deplaceur
        self.itineraire = itineraire

    def aller_destination(self, dest):
        if isinstance(dest, Mer) and self.entite.obtenir_bateau_dirige() is None:
            print("\nAction impossible : Vous devez commander un bateau pour aller en mer !")
            input("Appuyez sur Entrée pour continuer...")
            return
        self.itineraire.aller_destination(dest)

    def faire_demi_tour(self):
        if self.itineraire.obtenir_distance() == 0:
            self.entite.changer_lieu(self.itineraire.obtenir_destination())
        self.itineraire.faire_demi_tour()

    def avancer(self):
        if self.itineraire.a_destination():
            self.deplaceur.avancer()
        else:
            print("Vous ne bougez pas.")


class Itineraire:
    """Gère l'itinéraire d'une entité."""

    def __init__(self, acteur):
        self.destination = None
        self.depart = None
        self.distance_destination = 0
        self.acteur = acteur

    def obtenir_destination(self): return self.destination

    def changer_destination(self, destination): self.destination = destination

    def obtenir_depart(self): return self.depart

    def changer_depart(self, depart): self.depart = depart

    def obtenir_distance(self): return self.distance_destination

    def changer_distance(self, distance): self.distance_destination = distance

    def aller_destination(self, dest):
        self.destination = dest
        self.depart = self.acteur.obtenir_lieu()
        self.distance_destination = dest.obtenir_lieu().obtenir_distance(self.acteur.obtenir_lieu())
        print(f"Mise en route vers {dest.obtenir_nom()}.")

    def a_atteint_destination(self):
        return self.distance_destination <= 0

    def a_destination(self):
        return self.destination is not None

    def faire_demi_tour(self):
        x = self.destination
        self.destination = self.depart
        self.depart = x
        self.distance_destination = self.destination.obtenir_lieu().obtenir_distance(
            self.obtenir_depart()) - self.distance_destination
        print("Vous faites demi-tour.")
        if self.distance_destination <= 0:
            self.destination = None
            self.depart = None


class Deplaceur:
    """Gère le déplacement physique d'une entité."""

    def __init__(self, itineraire, acteur):
        self.itineraire = itineraire
        self.acteur = acteur

    def avancer(self):
        vitesse = 1
        bateau_commande = self.acteur.obtenir_bateau_dirige()
        self.acteur.changer_lieu(None)

        if bateau_commande and isinstance(self.acteur.obtenir_lieu(), Mer):
            vitesse = bateau_commande.vitesse
            print(f"Votre {bateau_commande.obtenir_nom()} avance...")

        self.itineraire.changer_distance(self.itineraire.obtenir_distance() - vitesse)

        if self.itineraire.a_atteint_destination():
            lieu_arrivee = self.itineraire.obtenir_destination()
            print(f"Vous êtes arrivé à {lieu_arrivee.obtenir_nom()}.")
            self.acteur.changer_lieu(lieu_arrivee)

            if bateau_commande:
                bateau_commande.lieu = lieu_arrivee

            self.itineraire.changer_destination(None)
            self.itineraire.changer_depart(None)