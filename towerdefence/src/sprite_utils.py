import pygame

def create_sprite_sheet(sheet, width, height):
    sprite_count = sheet.get_width()//width
    sprites = []

    for i in range(0, sprite_count):
        image = pygame.Surface((width, height))
        image.blit(sheet, (0, 0), (width*i, 0, width, height))
        sprites.append(image)

    return sprites