import os
import pygame
import utils.text_utils as tu
from defender_data import DEFENDER_DATA
from statics import DISPLAY_WIDTH, DISPLAY_HEIGHT, TILE_SIZE, UI_PANEL
from sprites.button import Button

DIRNAME = os.path.dirname(__file__)

BUY_BUTTONS = "buy"
MISC_BUTTONS = "misc"
START_WAVE_BUTTON = "start_wave"
QUIT_STAGE_BUTTON = "quit"

class Game_UI:
    def __init__(self, assets):
        self.money = 0
        self.wave = 1
        self.waves = 1
        self.ui_panel_center = DISPLAY_WIDTH+((UI_PANEL//2))-32
        self.assets = assets
        self.font_file = assets[2]["game_font"]
        self.defender_types = [defender_type for defender_type in DEFENDER_DATA.keys()]
        self.buttons = {BUY_BUTTONS: {}, MISC_BUTTONS: {}}
        self.create_buttons()

        self.disable = False
        self.selected_defender = None

    def create_buttons(self):
        # create defender buttons
        row_length = 2

        for i, defender_type in enumerate(self.defender_types):
            current_row = (i)//row_length + 1
            button_bg = self.assets[0]["buttons_small"][0]
            button_fg = self.assets[0][defender_type][0]
            pos = (self.ui_panel_center-48+((i % row_length)*96), 96*current_row)
            self.buttons[BUY_BUTTONS][defender_type] = self._create_button(button_bg, button_fg, pos)

        button_bg = self.assets[0]["buttons_wide"][1]
        button_fg = tu.create_text_surface(self.font_file, "Start Wave", 30)
        pos = (self.ui_panel_center-32, DISPLAY_HEIGHT-100)
        self.buttons[MISC_BUTTONS][START_WAVE_BUTTON] = self._create_button(button_bg, button_fg, pos)

        button_bg = self.assets[0]["buttons_small"][2]
        button_fg = tu.create_text_surface(self.font_file, "Quit", 40)
        pos = (self.ui_panel_center+72, DISPLAY_HEIGHT-100)
        self.buttons[MISC_BUTTONS][QUIT_STAGE_BUTTON] = self._create_button(button_bg, button_fg, pos)

    def _create_button(self, button_bg, button_fg, pos):
        return Button(self.assets[1], button_bg, button_fg, pos)

    def draw(self, display):
        text = f"Money: {self.money}"
        text_surf = tu.create_text_surface(self.font_file, text, 40)
        display.blit(text_surf, text_surf.get_rect(center=(self.ui_panel_center, 32)))

        # draw defender buttons and prices
        for defender_type in self.defender_types:
            button = self.buttons[BUY_BUTTONS][defender_type]

            # draw price
            price = DEFENDER_DATA[defender_type]["cost"]
            text_surf = tu.create_text_surface(self.assets[2]["game_font"], str(price), 30)
            rect = text_surf.get_rect(center=(button.pos[0], button.pos[1]+48))
            display.blit(text_surf, rect)

        for category, button_type in self.buttons.items():
            for id, button in button_type.items():
                if self.disable or category == BUY_BUTTONS and DEFENDER_DATA[id]["cost"] > self.money:
                    button.set_disabled(True)
                else:
                    button.set_disabled(False)
                button.draw(display)
        
        if self.selected_defender is not None:
            self._display_selected_defender(display, self.selected_defender)

    def refresh(self):
        for button in self.buttons.values():
            button.refresh()

    def update(self):
        pressed = None
        for id in self.buttons.values():
            for type, button in id.items():
                if button.update():
                    pressed = type
        return pressed

    def set_money(self, amount):
        self.money = amount

    def set_waves(self, wave, waves):
        self.wave = wave
        self.waves = waves

    def set_selected_defender(self, value):
        self.selected_defender = value

    def get_selected_defender(self):
        return self.selected_defender

    def _display_selected_defender(self, display, defender_type):
        pos = pygame.mouse.get_pos()
        defender_image = self.assets[0][defender_type][0]
        rect = defender_image.get_rect(bottomright=pos)
        display.blit(defender_image, rect.center)