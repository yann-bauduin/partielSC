import random

class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer_aleatoirement(self, taille):
        directions = ['nord', 'sud', 'est', 'ouest']
        direction = random.choice(directions)
        if direction == 'nord' and self.y > 0:
            self.y -= 1
        elif direction == 'sud' and self.y < taille - 1:
            self.y += 1
        elif direction == 'est' and self.x < taille - 1:
            self.x += 1
        elif direction == 'ouest' and self.x > 0:
            self.x -= 1
