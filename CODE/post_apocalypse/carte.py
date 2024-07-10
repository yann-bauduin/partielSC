from .ressource.py import Ressource
from .zombie.py import Zombie

class Carte:
    def __init__(self, taille):
        self.taille = taille
        self.ressources = []
        self.zombies = []

    def ajouter_ressource(self, ressource):
        self.ressources.append(ressource)

    def ajouter_zombie(self, zombie):
        self.zombies.append(zombie)

    def deplacer_zombies(self):
        for zombie in self.zombies:
            zombie.deplacer_aleatoirement(self.taille)
