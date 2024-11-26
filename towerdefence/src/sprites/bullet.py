import pygame
from pygame.math import Vector2

class Bullet(pygame.sprite.Sprite):
    def __init__(self, damage, speed, pos, direction, radius):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (self.radius, self.radius), self.radius)

        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)
        
        self.max_travel_dist = 2000
        self.distance_travelled = 0
        self.damage = damage
        self.speed = speed
        self.direction = direction


    def update(self, targets):
        self.move(targets)


    def move(self, targets):
        velocity = self.direction * self.speed

        self.distance_travelled = (self.pos - velocity).length()

        self.pos += velocity

        self.rect.center = self.pos

        if self.distance_travelled >= self.max_travel_dist:
            self.kill()

        for target in targets:
            
            #Hardcoded to disappear off-screen for now

            if (target.pos - self.pos).length() <= 40:
                target.deal_damage(self.damage)
                self.kill()
            