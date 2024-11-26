import pygame
from pygame.math import Vector2
import os

dirname = os.path.dirname(__file__)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp = 10, damage = 10, movement_speed = 1, path_nodes = []):
        super().__init__()
        self.hp = hp
        self.damage = damage
        self.movement_speed = movement_speed

        self.path_nodes = path_nodes
        self.node_count = len(path_nodes)
        self.next_node = 1
        self.reached_end_node = False
        self.is_alive = True

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.pos = Vector2(self.path_nodes[0])
        self.rect = self.image.get_rect(center=self.pos)


    def deal_damage(self, damage):
        if damage >= 0:
            self.hp -= damage
            if self.hp <= 0:
                self.is_alive = False


    def move(self):
        if self.next_node < self.node_count:
            target = Vector2(self.path_nodes[self.next_node])
            distance = (target - self.pos).length()

            if distance < 2 * self.movement_speed:
                self.next_node += 1
            normalized = (target - self.pos).normalize()

            self.pos += normalized * self.movement_speed
            self.rect.center = self.pos

        else:
            self.reached_end_node = True
        

    def has_died(self):
        return not self.is_alive


    def reached_end(self):
        return self.reached_end_node
        

    def update(self):
        self.move()
        if self.reached_end() or self.has_died():
            self.kill()