import unittest
from bateau import Bateau
from mission import Mission
from mission import Arret
from mission_schema import MissionSchema
from lieu import Lieu

class TestBateau(unittest.TestCase):
    def test_mission(self):
        # Si le bateau cesse une mission, il n'est pas en cours de mission juste après.
        bateau_test =  Bateau()
        schema = MissionSchema()
        for i in range(4):
            arret = Arret(Lieu(f"Lieu {i}"),bateau_test)
            schema.ajouter_arret(arret)
        bateau_test.mission =  Mission(schema)
        bateau_test.demarrer_mission()
        

if __name__ == '__main__':
    unittest.main()