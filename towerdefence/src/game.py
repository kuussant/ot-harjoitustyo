import pygame

from statics import *
from utils.editor_utils import *
from utils.sprite_utils import *

from sprites.defender import Defender
from sprites.enemy import Enemy
from map import Map

MAP_NAME = os.path.join(DIRNAME, "maps", "map1.json")

class Game:
    def __init__(self):
        pygame.init()
        self.time_elapsed = 0
        self.display = pygame.display.set_mode((TILE_SIZE*12, TILE_SIZE*12))

        self.all_sprites = pygame.sprite.Group()
        self.defender_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        tiles_sheet = pygame.image.load(TILE_SHEET)
        tiles_list = create_sprite_list(tiles_sheet, IMG_SIZE, IMG_SIZE, 2)
        self.map = Map(load_map(MAP_NAME), tiles_list)

        self.path_nodes = self.map.get_path()

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                # TESTING

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    new_defender = Defender(2, 300, (x, y), self.bullet_group)
                    self.defender_group.add(new_defender)
                    self.all_sprites.add(new_defender)
                    print(self.map.get_path())

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                    new_enemy = Enemy(10, 2, self.path_nodes)
                    self.enemy_group.add(new_enemy)
                    self.all_sprites.add(new_enemy)


            self.display.fill((0, 0, 0))
            
            self.map.draw(self.display)

            self.enemy_group.update()
            self.bullet_group.update(self.enemy_group)

            #Test bullet delays, will move to a better location

            if self.time_elapsed >= 1000:
                self.defender_group.update(self.enemy_group, self.bullet_group)

                self.time_elapsed = 0

            self.all_sprites.draw(self.display)
            self.bullet_group.draw(self.display)

            pygame.display.flip()

            self.time_elapsed += self.clock.tick(60)
