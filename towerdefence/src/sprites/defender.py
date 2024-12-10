import os
import random

import pygame
from pygame.math import Vector2
from sprites.bullet import Bullet

DIRNAME = os.path.dirname(__file__)


class Defender(pygame.sprite.Sprite):
    """Defender class. Defenders defend the home base from enemies.

    Attributes:
        assets: The global game assets. The class needs textures from the assets.
        damage: The damage the defender deals to enemies.
        attack_range: The range where the defender automatically attacks an enemy, once they get close.
        attack_speed: The attack interval of the defender.
        pos: The display coordinate position of the attacker.
        update_time: A helper variable for calculating the attack interval.
        image: The image of the defender.
        rect: A rectangle object for rendering the Defender.
        pos: The display coordinate position of the attacker.
    """
    def __init__(self, assets, damage, attack_range, attack_speed, pos):
        """Defender constructor where Defender is created.

        Args:
            assets: The global game assets. The class needs textures from the assets.
            damage: The damage the defender deals to enemies.
            attack_range: The range where the defender automatically attacks an enemy, once they get close.
            attack_speed: The attack interval of the defender.
            pos: The display coordinate position of the attacker.
        """
        super().__init__()
        self.assets = assets
        self.damage = damage
        self.range = attack_range
        self.attack_speed = attack_speed * 1000
        self.update_time = 0

        # Needs refactoring
        self.image = pygame.image.load(
            os.path.join(DIRNAME, "..", "assets/textures", "robot.png")
        )

        self.image = pygame.transform.scale(
            self.image, (self.image.get_width()/1.5, self.image.get_height()/1.5))

        self.rect = self.image.get_rect()

        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, target_group, bullet_group, all_sprites):
        """Updates the defender during the game. Mainly checks if enemies are within range.

        Args:
            target_group: Sprite group for enemies that Defender needs for target acquisition.
            bullet_group: Sprite group for bullets, where Defender adds bullets for rendering.
            all_sprites: Sprite for all game sprites that's needed for rendering.
        """
        self.shoot(target_group, bullet_group, all_sprites)

    def check_defender(self):
        self.kill()

    def shoot(self, target_group, bullet_group, all_sprites):
        """A method that needs to be updated constantly. Allows Defender to shoot bullets.
        
        Args:
            target_group: Sprite group for enemies passed down from the update method that Defender needs for target acquisition.
            bullet_group: Sprite group for bullets passed down from the update method where Defender adds bullets for rendering.
            all_sprites: Sprite group for all game sprites passed down from the update method that's needed for rendering.
        """
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
                bullet = Bullet(self.assets, self.damage, self.pos, direction)
                bullet_group.add(bullet)
                all_sprites.add(bullet)
        return
