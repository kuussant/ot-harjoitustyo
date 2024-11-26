import pygame
from pygame.math import Vector2

class Bullet(pygame.sprite.Sprite):
    def __init__(self, damage, speed, pos, direction, radius):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (self.radius, self.radius), self.radius)
        self.damage = damage
        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)
        self.speed = speed
        self.direction = direction

    def update(self, targets):
        self.move(targets)


    def move(self, targets):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos

        for target in targets:
            
            #Still needs to disappear when flying outside the screen
            
            if (target.pos - self.pos).length() <= 20:
                target.deal_damage(self.damage)
                self.kill()
