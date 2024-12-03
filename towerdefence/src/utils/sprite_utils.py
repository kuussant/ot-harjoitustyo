import pygame
from statics import *

def create_sprite_list(sheet, width, height, scale, color=(0, 0, 0)):
    sprite_count = sheet.get_width()//width
    sprites = []

    for i in range(0, sprite_count):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (width*i, 0, width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)
        sprites.append(image)

    return sprites