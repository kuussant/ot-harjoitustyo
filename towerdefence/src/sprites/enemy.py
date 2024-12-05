import pygame
from pygame.math import Vector2
from utils.sprite_utils import *
from wave_data import ENEMY_DATA

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, path_nodes):
        super().__init__()
        self.hp = None
        self.movement_speed = None
        self.sprite_list = []
        
        self._load_data(enemy_type)

        self.path_nodes = path_nodes
        self.next_node = 1
        self.reached_end_node = False

        self.image = self.sprite_list[0]
        self.pos = Vector2(self.path_nodes[0])
        self.rect = self.image.get_rect(center=self.pos)


    def deal_damage(self, damage):
        if damage >= 0:
            self.hp -= damage
            if self.hp <= 0:
                self.kill()


    def _move(self):
        if self.next_node < len(self.path_nodes):
            target = Vector2(self.path_nodes[self.next_node])
            distance = (target - self.pos).length()

            if distance < 2 * self.movement_speed:
                self.next_node += 1
            normalized = (target - self.pos).normalize()

            self.pos += normalized * self.movement_speed
            self.rect.center = self.pos

        else:
            self.reached_end_node = True


    def _reached_end(self):
        return self.reached_end_node


    def update(self):
        self._move()
        if self._reached_end():
            self.kill()


    def _load_data(self, enemy_type):
        enemy = ENEMY_DATA[enemy_type]
        self.hp = enemy["hp"]
        self.movement_speed = enemy["speed"]
        enemy_image = pygame.image.load(enemy["image_file"])
        self.sprite_list = create_sprite_list(enemy_image, IMG_SIZE, IMG_SIZE, scale=2)

