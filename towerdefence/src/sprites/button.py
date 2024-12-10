import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, button_type, image, pos):
        super().__init__()
        self.button_type = button_type
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event == pygame.MOUSEBUTTONDOWN:
                print("you pressed button")
