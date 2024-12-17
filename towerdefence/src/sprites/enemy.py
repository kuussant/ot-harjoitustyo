import math
import random
import sound

import pygame
from pygame.math import Vector2
from wave_data import ENEMY_DATA

# FRAME_DELAY = 100
# ANGLE_OFFSET = 90
# CLOSE_ENOUGH_TO_WAYPOINT = 2

"TODO FIX DOCSTRINGS"

class Enemy(pygame.sprite.Sprite):
    """Enemy class. Enemies attack the home base.

    Attributes:
        assets: The global game assets. The class needs textures from the assets.
        enemy_type: The type of the enemy.
        hp: Enemy health points.
        movement_speed: The speed at which the enemy moves.
        money_value: The monetary reward when the enemy is killed.
        sprite_list: Contains all of the animation frames.
        path_nodes: A list of coordinate nodes that the enemy follows.
        next_node: A node list index dictating the next destination for the enemy.
        reached_end_node: A boolean dictating if the enemy has reached the end node.
        frame_delay: Animation frame delay for the enemy in milliseconds.
        animation_index: The current animation frame index in the sprite sheet.
        update_time: A helper variable to update the time between frames.
        image: The enemy image.
        pos: The current position of the enemy.
        rect: A rectangle object of the enemy, needed in rendering.
    """
    FRAME_DELAY = 100
    ANGLE_OFFSET = 90
    CLOSE_ENOUGH_TO_WAYPOINT = 2

    def __init__(self, assets, type, waypoints):
        """Enemy constructor. Creates a new enemy.

        Args:
            assets: The global game assets. The class needs textures from the assets.
            enemy_type: The type of the enemy.
            path_nodes: A list of coordinate nodes that the enemy follows.
        """
        super().__init__()
        self.assets = assets
        self.hp = None
        self.movement_speed = None
        self.money_value = None
        self.sprite_list = []

        self._load_data(type)

        self.waypoints = waypoints
        self.next_node = 1
        self.reached_end_node = False

        self.animation_index = random.randint(0, len(self.sprite_list)-1)
        self.update_time = 0

        self.image = self.sprite_list[self.animation_index]

        self.pos = Vector2(self.waypoints[0])
        self.rect = self.image.get_rect(center=self.pos)
        self.mask = pygame.mask.from_surface(self.image)

    def deal_damage(self, damage):
        """Damages the enemy by taking hp away according to damage dealt.

        Args:
            damage: The damage dealt to the enemy.
        """
        sound.play(self.assets[1]["hit_sound"], 0.05)
        if damage >= 0:
            self.hp -= damage
            if self.hp <= 0:
                self.kill()
                sound.play(random.choice(self._get_death_sounds()), 0.1)
                return self.money_value
        return 0

    def _move(self):
        """Method for moving the enemy and rotating it towards the direction it is moving.

        """
        if self.next_node < len(self.waypoints):
            target = Vector2(self.waypoints[self.next_node])
            distance = target - self.pos

            if distance.length() < self.CLOSE_ENOUGH_TO_WAYPOINT * self.movement_speed:
                self.next_node += 1
            else:
                direction = distance.normalize()
                self.pos += direction * self.movement_speed
                self.rect.center = self.pos
                self._rotate(direction)
        else:
            self.reached_end_node = True

    def _rotate(self, normalized):
        """Rotates the enemy image towards the movement direction.
        Args:
            normalized: The normalized 2D vector that is needed for image rotation.
        """
        self.angle = math.degrees(math.atan2(-normalized[1], normalized[0]))+self.ANGLE_OFFSET
        self.image = pygame.transform.rotate(
            self.sprite_list[self.animation_index], self.angle)

    def _reached_end(self):
        """Checks if Enemy has reached the end node.
        Returns:
            True if enemy has reached the end node, and False otherwise
        """
        return self.reached_end_node

    def update(self):
        """Updates the enemy behavior per frame. Kills the enemy if it reaches the end node.
        
        """
        self._move()
        self._play_animation()
        if self._reached_end():
            self.kill()

    def _play_animation(self):
        """Plays the enemy animations.
        
        """
        if pygame.time.get_ticks() - self.update_time > self.FRAME_DELAY:
            self.update_time = pygame.time.get_ticks()
            self.animation_index += 1
            if self.animation_index >= len(self.sprite_list):
                self.animation_index = 0

    def _get_death_sounds(self):
        """Get death sounds.
        
        """
        return [
            self.assets[1]["goblin_death1"],
            self.assets[1]["goblin_death2"],
            self.assets[1]["goblin_death3"],
            self.assets[1]["goblin_death4"]
        ]

    def _load_data(self, enemy_type):
        """Loads all of the necessary enemy data based on enemy type.
        
        Args:
            enemy_type: The enemy type who's data is fetched from a dictionary containing enemy data.
        """
        self.sprite_list = self.assets[0][enemy_type]
        enemy = ENEMY_DATA[enemy_type]
        self.hp = enemy["hp"]
        self.movement_speed = enemy["speed"]
        self.money_value = enemy["value"]
