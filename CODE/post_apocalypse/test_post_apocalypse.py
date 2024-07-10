import unittest
from post_apocalypse.survivant import Survivant
from post_apocalypse.carte import Carte
from post_apocalypse.ressource import Ressource
from post_apocalypse.zombie import Zombie

class TestPostApocalypse(unittest.TestCase):

    def test_survivant_avance(self):
        survivant = Survivant(5, 5, 'nord')
        survivant.avancer()
        self.assertEqual((survivant.x, survivant.y), (5, 4))

    def test_survivant_tourne_gauche(self):
        survivant = Survivant(5, 5, 'nord')
        survivant.tourner_gauche()
        self.assertEqual(survivant.orientation, 'ouest')

    def test_survivant_ramasse_ressource(self):
        carte = Carte(10)
        ressource = Ressource(5, 5, 'nourriture')
        carte.ajouter_ressource(ressource)
        survivant = Survivant(5, 5, 'nord')
        survivant.ramasser_ressource(carte.ressources)
        self.assertIn(ressource, survivant.inventaire)
        self.assertNotIn(ressource, carte.ressources)

    def test_survivant_rencontre_zombie(self):
        zombie = Zombie(5, 5)
        survivant = Survivant(5, 5, 'nord')
        survivant.rencontrer_zombie([zombie])
        self.assertEqual(survivant.sante, 90)

if __name__ == '__main__':
    unittest.main()
