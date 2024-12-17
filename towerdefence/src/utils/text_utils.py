import pygame

def create_text_surface(font_file, text, size):
    return pygame.font.Font(font_file, size).render(text, False, (255, 255, 255))

def create_text_rect(font_obj, pos):
    return font_obj.get_rect(center=pos)