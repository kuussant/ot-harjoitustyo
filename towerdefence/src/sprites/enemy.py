import pygame
import math
import random
import statics as s
import sound
from pygame.math import Vector2
from wave_data import ENEMY_DATA


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
    def __init__(self, assets, enemy_type, path_nodes):
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

        self._load_data(enemy_type)

        self.path_nodes = path_nodes
        self.next_node = 1
        self.reached_end_node = False

        self.frame_delay = 100
        self.animation_index = random.randint(0, len(self.sprite_list)-1)
        self.update_time = 0

        self.image = self.sprite_list[self.animation_index]

        self.pos = Vector2(self.path_nodes[0])
        self.rect = self.image.get_rect(center=self.pos)

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
                sound.play(self._choose_random_death_sound(), 0.1)
                return self.money_value
        return 0

    def _move(self):
        """Method for moving the enemy and rotating it towards the direction it is moving.

        """
        if self.next_node < len(self.path_nodes):
            target = Vector2(self.path_nodes[self.next_node])
            distance = target - self.pos

            if distance.length() < 2 * self.movement_speed:
                self.next_node += 1
            normalized = distance.normalize()

            self.pos += normalized * self.movement_speed
            self.rect.center = self.pos

            self._rotate(normalized)
        else:
            self.reached_end_node = True

    def _rotate(self, normalized):
        """Rotates the enemy image towards the movement direction.
        Args:
            normalized: The normalized 2D vector that is needed for image rotation.
        """
        self.angle = math.degrees(math.atan2(-normalized[1], normalized[0]))+90
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
        if pygame.time.get_ticks() - self.update_time > self.frame_delay:
            self.update_time = pygame.time.get_ticks()
            self.animation_index += 1
            if self.animation_index >= len(self.sprite_list):
                self.animation_index = 0

    def _choose_random_death_sound(self):
        """Chooses a random death sound for Enemy when it's killed.
        
        """
        death_sound = None
        rand = random.randint(1, 3)
        if rand == 0:
            death_sound = self.assets[1]["goblin_death1"]
        elif rand == 1:
            death_sound = self.assets[1]["goblin_death2"]
        elif rand == 2:
            death_sound = self.assets[1]["goblin_death3"]
        elif rand == 3:
            death_sound = self.assets[1]["goblin_death4"]
        return death_sound

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
