# mon_super_jeu/main.py

from jeu import Jeu

# Cette condition vérifie si le fichier est exécuté directement
# (et non importé comme un module)
if __name__ == '__main__':
    partie = Jeu()
    partie.demarrer()