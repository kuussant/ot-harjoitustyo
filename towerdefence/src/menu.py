import os
import sys
import pygame
import utils.asset_utils as assets
import utils.text_utils as tu
from game import Game
from sprites.button import Button
from statics import IMG_SIZE, IMG_SCALE, DISPLAY_WIDTH, DISPLAY_HEIGHT, UI_PANEL

DIRNAME = os.path.dirname(__file__)

class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Towerdefence")
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH + UI_PANEL, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()

        self.assets = assets.load()
        self.buttons_small = self.assets[0]["buttons_small"]
        self.buttons_wide = self.assets[0]["buttons_wide"]
        self.font_file = self.assets[2]["game_font"]

        screen_center = self.screen.get_rect().center

        self.play_button = Button(
                self.assets[1], 
                self.buttons_wide[1],
                tu.create_text_surface(self.font_file, "Play", 40), 
                (screen_center[0], screen_center[1]-IMG_SIZE*1.5)
            )
        self.exit_button = Button(
                self.assets[1], 
                self.buttons_wide[2], 
                tu.create_text_surface(self.font_file, "Exit", 40),
                (screen_center[0], screen_center[1]+IMG_SIZE*1.5)
            )
        
        self.begin_game = False

    def start(self):
        while not self.begin_game:
            self._handle_events()
    
            self.screen.fill((150, 150, 255))

            self.play_button.draw(self.screen)
            self.exit_button.draw(self.screen)

            self.play_button.update()
            self.exit_button.update()
            pygame.display.update()
            
            self.clock.tick(60)
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._exit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.update():
                    self._start_game()
                    pass

                if self.exit_button.update():
                    self._exit_game()

    def _start_game(self):
        game = Game(self.screen)
        game.start_game()
    
    def _exit_game(self):
        pygame.quit()
        sys.exit()