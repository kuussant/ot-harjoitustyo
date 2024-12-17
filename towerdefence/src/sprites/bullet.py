import pygame
from pygame.math import Vector2
import math
from defender_data import DEFENDER_DATA

class Bullet(pygame.sprite.Sprite):
    """A class for bullets that are shot (created) by defenders.
    
    Attributes:
        sounds: Bullet sound assets.
        radius: Bullet size.
        image: Bullet image.
        pos: The current position of the bullet.
        rect: Rectangle object of the bullet needed in rendering.
        max_travel_dist: The max travel distance of the bullet in pixels.
        distance_travelled: The distance the bullet has travelled.
        damage: The damage dealt by the bullet.
        direction: The flying direction of the bullet.
    """
    def __init__(self, assets, defender_type, pos, direction):
        """A constructor for creating a bullet.
    
        Args:
            assets: Contains the global assets that the bullet needs, like image.
            damage: The damage dealt by the bullet.
            pos: The starting position of the bullet.
            direction: The flying direction of the bullet.
        """
        super().__init__()
        self.image = assets[0][DEFENDER_DATA[defender_type]["projectile"]][0]

        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.max_lifetime = 2000
        self.start_time = pygame.time.get_ticks()

        self.damage = DEFENDER_DATA[defender_type]["damage"]
        self.speed = DEFENDER_DATA[defender_type]["projectile_speed"]

        self.direction = direction

        self._rotate()

    def update(self):
        """Updates the bullets flying path.
    
        """
        self.move()

    def move(self):
        """Moves the bullet between starting position and direction. Gets removed after flying a certain distance.
    
        """
        velocity = self.direction * self.speed
        self.pos += velocity
        self.rect.center = self.pos

        if pygame.time.get_ticks() - self.start_time >= self.max_lifetime:
            self.kill()

    def _rotate(self):
        angle = math.degrees(math.atan2(-self.direction[1], self.direction[0]))+90
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.pos)
