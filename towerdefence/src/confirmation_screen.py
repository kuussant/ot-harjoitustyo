import os
import pygame
import utils.text_utils as tu
from defender_data import DEFENDER_DATA
from statics import DISPLAY_WIDTH, DISPLAY_HEIGHT, TILE_SIZE, UI_PANEL
from sprites.button import Button

DIRNAME = os.path.dirname(__file__)

class ConfirmationScreen:
    def __init__(self, assets, display, text):
        self.assets = assets
        self.display = display
        self.font_file = assets[2]["game_font"]
        self.text = text
        self.text_surf = tu.create_text_surface(self.font_file, self.text, 50)

        self.disp_center = ((DISPLAY_WIDTH + UI_PANEL) // 2, DISPLAY_HEIGHT // 2)

        self.screen_shadow = pygame.Surface((DISPLAY_WIDTH+UI_PANEL, DISPLAY_HEIGHT)).convert_alpha()
        self.screen_shadow.fill((0, 0, 0, 150))

        pos = (self.disp_center[0]-96, self.disp_center[1])
        yes_text = tu.create_text_surface(self.font_file, "Yes", 40)
        self.confirm_button = Button(assets[1], assets[0]["buttons_wide"][1], yes_text, pos)

        pos = (self.disp_center[0]+96, self.disp_center[1])
        no_text = tu.create_text_surface(self.font_file, "No", 40)
        self.decline_button = Button(assets[1], assets[0]["buttons_wide"][2], no_text, pos)

    def update(self):
        if self.confirm_button.update():
            return False
        elif self.decline_button.update():
            return True
        return None

    def draw(self, display):
        display.blit(self.screen_shadow, (0, 0))

        pos = (self.disp_center[0], self.disp_center[1]-128)
        display.blit(self.text_surf, self.text_surf.get_rect(center=pos))
        
        self.confirm_button.draw(display)
        self.decline_button.draw(display)
