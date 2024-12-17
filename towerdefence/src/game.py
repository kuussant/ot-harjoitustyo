import os
import sys
import pygame
import statics as s

import utils.asset_utils as assets
from stage import Stage
import game_ui as ui

import wave_data
DIRNAME = os.path.dirname(__file__)
MAP_FILE = os.path.join(DIRNAME, "maps", "map1.json")


from confirmation_screen import ConfirmationScreen

class Game:
    def __init__(self, display):
        self.assets = assets.load()
        self.display = display
        self.stage = Stage(self.assets, MAP_FILE, wave_data.SPAWN_DATA)
        self.clock = pygame.time.Clock()
        self.ui = ui.Game_UI(self.assets)
        self.game_running = True

        self.confirm_screen_open = False
        confirm_text = "Leave stage?"
        self.confirm_screen = ConfirmationScreen(self.assets, self.display, confirm_text)

        # Needs to be moved to a better place
        self.time_elapsed = 0
        self.time_delta = 0

    def start_game(self):
        while self.game_running:
            self.ui.disable = self.confirm_screen_open
            if self._handle_events() == False:
                break

            
            if self.stage.wave_has_started() and not self.stage.game_won():
                # Needs to be moved to a better place
                if pygame.time.get_ticks() - self.time_elapsed > self.stage.get_wave_spawn_rate():
                    self.stage.handle_wave()
                    self.time_elapsed = pygame.time.get_ticks()

            elif self.stage.game_won():
                print("game won")

            
            self.stage.update()
            self.ui.update()

            state = self.confirm_screen.update()

            if self.confirm_screen_open:
                self._quit_confirmation(state)

            self.clock.tick(60)                
            self.render()

    def _handle_events(self):
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if not self.stage.game_won():
                    selected_defender = self.ui.get_selected_defender()

                    if selected_defender is None:
                        button_type = self.handle_button(self.ui.update())
                        self.ui.set_selected_defender(button_type)
                    elif self.stage.add_defender(selected_defender, (x, y)):
                        self.ui.set_selected_defender(None)

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                if not self.stage.game_won():
                    self.ui.set_selected_defender(None)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def handle_button(self, button_type):
        type = None
        match button_type:
            case ui.QUIT_STAGE_BUTTON:
                # Needs to be moved to a better place
                self.time_delta = pygame.time.get_ticks() - self.time_elapsed
                self.confirm_screen_open = True
            case ui.START_WAVE_BUTTON:
                self.stage.generate_spawns()
            case None:
                pass
            case _:
                type = button_type
        
        return type

    def _quit_confirmation(self, state):
        if state is not None:
            self.game_running = state
            self.confirm_screen_open = False
            # Needs to be moved to a better place
            self.time_elapsed = pygame.time.get_ticks() - self.time_delta

    def render(self):
        self.display.fill((150, 150, 255))
        
        self.stage.draw(self.display)
        self.ui.set_money(self.stage.money)
        self.ui.set_waves(self.stage.wave, self.stage.waves)
        self.ui.draw(self.display)

        if self.confirm_screen_open:
            self.confirm_screen.draw(self.display)

        pygame.display.flip()
