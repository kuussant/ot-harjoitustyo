import os

import pygame
from pygame.math import Vector2
from sprites.bullet import Bullet

dirname = os.path.dirname(__file__)

class Defender(pygame.sprite.Sprite):
    cost = 10

    def __init__(self, damage, attack_range, pos, bullet_group):
        super().__init__()
        self.damage = damage
        self.range = attack_range
        self.bullet_group = bullet_group

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.rect = self.image.get_rect()

        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)


    def update(self, targets, bullets):
        self.shoot(targets, bullets)


    def shoot(self, targets, bullets):
        if targets:
            closest = 9999
            closest_diff = Vector2(0, 0)

            for target in targets:
                difference = target.pos - self.pos

                if difference.length() <= closest:
                    closest = difference.length()
                    closest_diff = difference

            if closest_diff.length() <= self.range:
                direction = closest_diff.normalize()
                bullets.add(Bullet(self.damage, self.pos, direction))
