import os

import pygame
from pygame.math import Vector2
from sprites.bullet import Bullet

dirname = os.path.dirname(__file__)

class Defender(pygame.sprite.Sprite):
    cost = 10

    def __init__(self, damage, attack_range, attack_speed, pos):
        super().__init__()
        self.damage = damage
        self.range = attack_range
        self.attack_speed = attack_speed * 1000
        self.update_time = 0

        # Needs refactoring
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.image = pygame.transform.scale(self.image, (self.image.get_width()/1.5, self.image.get_height()/1.5))

        self.rect = self.image.get_rect()

        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)


    def update(self, target_group, bullet_group, all_sprites):
        self.shoot(target_group, bullet_group, all_sprites)


    def shoot(self, target_group, bullet_group, all_sprites):
        if pygame.time.get_ticks() - self.update_time > self.attack_speed:
            self.update_time = pygame.time.get_ticks()
        else:
            return
        
        if target_group:
            closest = 9999
            closest_diff = Vector2(0, 0)

            for target in target_group:
                difference = target.pos - self.pos

                if difference.length() <= closest:
                    closest = difference.length()
                    closest_diff = difference

            if closest_diff.length() <= self.range:
                direction = closest_diff.normalize()
                bullet = Bullet(self.damage, self.pos, direction)
                bullet_group.add(bullet)
                all_sprites.add(bullet)
        return

