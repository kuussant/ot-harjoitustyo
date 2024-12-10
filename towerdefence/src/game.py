import os
import pygame
import statics as s

from stage import Stage
from game_ui import Game_UI

import wave_data
DIRNAME = os.path.dirname(__file__)
MAP_FILE = os.path.join(DIRNAME, "maps", "map1.json")


class Game:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(
            (s.DISPLAY_WIDTH + s.UI_PANEL, s.DISPLAY_HEIGHT))
        self.stage = Stage(MAP_FILE, wave_data.SPAWN_DATA)
        self.clock = pygame.time.Clock()
        self.ui = Game_UI()
        self.ui_buttons = self.ui.get_buttons()

    def start_game(self):
        time_elapsed = 0

        while True:
            if self._handle_events() == False:
                break

            self.render()

            if self.stage.wave_has_started() and not self.stage.game_won():
                if pygame.time.get_ticks() - time_elapsed > self.stage.get_wave_spawn_rate():
                    self.stage.handle_wave()
                    time_elapsed = pygame.time.get_ticks()

            elif self.stage.game_won():
                print("game won")

            self.stage.update()

            self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                self.stage.add_defender((x, y))

                # self.ui_buttons.update(event.type)

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                defender = self.stage.check_defender((x, y))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.stage.generate_spawns()

            if event.type == pygame.QUIT:
                return False

    def render(self):
        self.display.fill((0, 0, 0))
        self.stage.draw(self.display)
        self.ui.draw(self.display, f"Money: {self.stage.money}")
        pygame.display.flip()
