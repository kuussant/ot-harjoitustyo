import pygame

class Bullet:
    def __init__(self, damage, x, y, size, color):
        self.damage = damage
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.size)