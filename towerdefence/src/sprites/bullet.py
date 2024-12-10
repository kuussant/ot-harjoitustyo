import pygame
from pygame.math import Vector2
import sound


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
    def __init__(self, assets, damage, pos, direction):
        """A constructor for creating a bullet.
    
        Args:
            assets: Contains the global assets that the bullet needs, like image.
            damage: The damage dealt by the bullet.
            pos: The starting position of the bullet.
            direction: The flying direction of the bullet.
        """
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
        """Updates the bullets flying path.
    
        """
        self.move()

    def move(self):
        """Moves the bullet between starting position and direction. Gets removed after flying a certain distance.
    
        """
        velocity = self.direction * 10
        self.distance_travelled = (self.pos - velocity).length()
        self.pos += velocity
        self.rect.center = self.pos

        if self.distance_travelled >= self.max_travel_dist:
            self.kill()
