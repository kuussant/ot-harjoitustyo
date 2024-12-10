import os
import pygame
from statics import *
from sprites.button import Button

DIRNAME = os.path.dirname(__file__)


class Game_UI:
    def __init__(self):
        buttons_image = pygame.image.load(os.path.join(
            DIRNAME, "assets/textures", "td_buttons.png"))
        self.buttons = self._get_ui_buttons(buttons_image)
        font_file = os.path.join(DIRNAME, "assets", "Micro5-Regular.ttf")
        self.font = pygame.font.Font(font_file, 50)

        self.button_test = Button("eh", self.buttons[0], (10, 10))
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.button_test)

    def draw(self, display, text_to_show):
        text = self.font.render(str(text_to_show), True, (255, 255, 255))
        text_pos = DISPLAY_WIDTH - TILE_SIZE
        textrect = text.get_rect(
            center=(text_pos+((UI_PANEL+TILE_SIZE)//2), TILE_SIZE//2))
        display.blit(text, textrect)

    def get_buttons(self):
        return self.button_group

    def _get_ui_buttons(self, buttons_image):
        buttons_list = []
        buttons_list.append(self._get_button_by_coords(
            buttons_image, (IMG_SIZE, IMG_SIZE), (0, 0), 2))
        buttons_list.append(self._get_button_by_coords(
            buttons_image, (IMG_SIZE*2, IMG_SIZE), (IMG_SIZE, 0), 2))
        buttons_list.append(self._get_button_by_coords(
            buttons_image, (IMG_SIZE*2, IMG_SIZE), (IMG_SIZE*3, 0), 2))
        return buttons_list

    def _get_button_by_coords(self, buttons_image, width_height, pos, scale):
        image = pygame.Surface(width_height).convert_alpha()
        image.blit(buttons_image, (0, 0),
                   (pos[0], pos[1], width_height[0], width_height[1]))
        image = pygame.transform.scale(
            image, (width_height[0]*scale, width_height[1]*scale))
        image.set_colorkey((0, 0, 0))

        return image
