import os

import pygame
from pygame.math import Vector2
from utils.sprite_utils import *
dirname = os.path.dirname(__file__)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp, movement_speed, path_nodes):
        super().__init__()
        self.hp = hp
        self.movement_speed = movement_speed

        self.path_nodes = path_nodes
        self.next_node = 1
        self.reached_end_node = False

        goblin = pygame.image.load(os.path.join(dirname, "..", "assets", "td_goblin.png"))
        self.sprite_list = create_sprite_list(goblin, IMG_SIZE, IMG_SIZE, 2)

        self.image = self.sprite_list[0]
        # pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

        self.pos = Vector2(self.path_nodes[0])
        self.rect = self.image.get_rect(center=self.pos)

    def deal_damage(self, damage):
        if damage >= 0:
            self.hp -= damage
            if self.hp <= 0:
                self.kill()


    def move(self):
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


    def reached_end(self):
        return self.reached_end_node


    def update(self):
        self.move()
        if self.reached_end():
            self.kill()
