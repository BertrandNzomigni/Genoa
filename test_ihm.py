import unittest
from IHM import Fenetre

class TestIHM(unittest.TestCase):
    def test_fenetre(self):
        # Test 1 : Vérifier qu'une fenêtre s'affiche.
        f = Fenetre()
        f.demarrer()
        self.assertEqual(input("Est qu'une fenêtre s'est affiché ? (y/n) : ").upper(),"Y","La fenêtre n'est pas affiché.")

if __name__ == '__main__':
    unittest.main()