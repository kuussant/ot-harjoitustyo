import pygame
from pygame.math import Vector2
import sound


class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, damage, pos, direction):
        super().__init__()
        self.sounds = assets
        self.radius = 5
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        pygame.draw.circle(self.image, (255, 0, 0),
                           (self.radius, self.radius), self.radius)

        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)

        self.max_travel_dist = 2000
        self.distance_travelled = 0
        self.damage = damage
        self.direction = direction

    def update(self):
        self.move()

    def move(self):
        velocity = self.direction * 10
        self.distance_travelled = (self.pos - velocity).length()
        self.pos += velocity
        self.rect.center = self.pos

        if self.distance_travelled >= self.max_travel_dist:
            self.kill()
