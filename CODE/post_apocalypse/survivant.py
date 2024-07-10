from .carte import Carte
from .zombie import Zombie

class Survivant:
    def __init__(self, x, y, orientation, sante=100):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.sante = sante
        self.inventaire = []

    def avancer(self):
        if self.orientation == 'nord':
            self.y -= 1
        elif self.orientation == 'sud':
            self.y += 1
        elif self.orientation == 'est':
            self.x += 1
        elif self.orientation == 'ouest':
            self.x -= 1

    def tourner_gauche(self):
        orientations = ['nord', 'ouest', 'sud', 'est']
        idx = orientations.index(self.orientation)
        self.orientation = orientations[(idx + 1) % 4]

    def tourner_droite(self):
        orientations = ['nord', 'est', 'sud', 'ouest']
        idx = orientations.index(self.orientation)
        self.orientation = orientations[(idx + 1) % 4]

    def rencontrer_zombie(self, zombies):
        for zombie in zombies:
            if self.x == zombie.x and self.y == zombie.y:
                self.sante -= 10

    def ramasser_ressource(self, ressources):
        for ressource in ressources:
            if self.x == ressource.x and self.y == ressource.y:
                self.inventaire.append(ressource)
                ressources.remove(ressource)
