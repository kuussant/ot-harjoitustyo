import pygame
import math
import sound

from pygame.math import Vector2
from sprites.bullet import Bullet
from defender_data import DEFENDER_DATA


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
    def __init__(self, assets, type, pos):
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
        self.type = type
        self.damage = DEFENDER_DATA[type]["damage"]
        self.range = DEFENDER_DATA[type]["range"]
        self.attack_speed = 1000 // DEFENDER_DATA[type]["speed"] # attacks / second
        self.projectiles = DEFENDER_DATA[type]["projectiles"]
        self.projectile_speed = DEFENDER_DATA[type]["projectile_speed"]
        self.update_time = 0
        self.sprite_list = assets[0][type]
        
        self.frame_delay = self.attack_speed / len(self.sprite_list)
        self.animation_index = 0
        self.update_time = 0
        self.angle = 0
        self.shot = False

        self.image = self.sprite_list[self.animation_index]

        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, target_group, bullet_group, all_sprites):
        """Updates the defender during the game. Mainly checks if enemies are within range.

        Args:
            target_group: Sprite group for enemies that Defender needs for target acquisition.
            bullet_group: Sprite group for bullets, where Defender adds bullets for rendering.
            all_sprites: Sprite for all game sprites that's needed for rendering.
        """
        self._play_animation()
        self.shoot(target_group, bullet_group, all_sprites)
        # self._draw_attack_radius()

    def check_defender(self):
        self.kill()

    def shoot(self, target_group, bullet_group, all_sprites):
        """A method that needs to be updated constantly. Allows Defender to shoot bullets.
        
        Args:
            target_group: Sprite group for enemies passed down from the update method that Defender needs for target acquisition.
            bullet_group: Sprite group for bullets passed down from the update method where Defender adds bullets for rendering.
            all_sprites: Sprite group for all game sprites passed down from the update method that's needed for rendering.
        """
        if target_group and not self.shot:
            closest = 9999
            closest_diff = Vector2(0, 0)

            for target in target_group:
                difference = target.pos - self.pos

                if difference.length() <= closest:
                    closest = difference.length()
                    closest_diff = difference
            
            if closest_diff.length() <= self.range:
                for n in range(self.projectiles//2, -self.projectiles//2, -1):
                    if self.projectiles % 2 == 0 and n <= 0:
                        n -= 1
                    direction = closest_diff.normalize()
                    spread_per_projectile = direction.rotate(10*n)
                    bullet = Bullet(self.assets, self.type, self.pos, spread_per_projectile)
                    bullet_group.add(bullet)
                    all_sprites.add(bullet)
                    self.shot = True

                    self._rotate(direction)

            if self.shot:
                sound.play(self.assets[1]["bow_sound"], 0.03)
        return
    
    def _play_animation(self):
        if pygame.time.get_ticks() - self.update_time > self.frame_delay and self.shot:
            self.update_time = pygame.time.get_ticks()
            self.animation_index += 1
            if self.animation_index >= len(self.sprite_list):
                self.animation_index = 0
                self.shot = False # Reload
            self._set_image(self.animation_index, self.angle)

    def _rotate(self, normalized):
        self.angle = math.degrees(math.atan2(-normalized[1], normalized[0]))+90
        self._set_image(0, self.angle)

    def _set_image(self, image_index, angle):
        self.image = pygame.transform.rotate(self.sprite_list[image_index], angle)
        self.rect = self.image.get_rect(center=self.pos)