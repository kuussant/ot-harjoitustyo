import pygame
from statics import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, display):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            highlight_rect = pygame.Rect(
                self.rect.x, self.rect.y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(display, (255, 255, 255), highlight_rect, 1)
