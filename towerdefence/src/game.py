import pygame

from statics import *
from stage import Stage

MAP_FILE = os.path.join(DIRNAME, "maps", "map1.json")

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((TILE_SIZE*12, TILE_SIZE*12))
        self.stage = Stage(MAP_FILE)
        self.clock = pygame.time.Clock()
        self.round_start = False
        self.game_won = False

    def start_game(self):
        time_elapsed = 0
        while True:
            if self._handle_events() == False:
                break

            self.render()

            if self.round_start:
                if pygame.time.get_ticks() - time_elapsed > 500:
                    time_elapsed = pygame.time.get_ticks()
                    self.stage.add_enemy()

            self.stage.update()

            if self.game_won:
                print("Game won")

            self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                self.stage.add_defender((x, y))

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                self.round_start = True

            if event.type == pygame.QUIT:
                return False
    
    def render(self):
        self.display.fill((0, 0, 0))
        self.stage.draw(self.display)
        pygame.display.flip()
