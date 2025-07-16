import unittest
from bateau import Bateau
from mission import Mission

class TestBateau(unittest.TestCase):
    def test_mission(self):
        bateau_test =  Bateau()
        bateau_test.mission =  Mission()

if __name__ == '__main__':
    unittest.main()