import pygame

from statics import *
from utils.editor_utils import *
from utils.sprite_utils import *

from sprites.defender import Defender
from sprites.enemy import Enemy
from sprites.map import Map

class Stage:
    def __init__(self, map_file):
        self.map = Map(load_map(map_file), (TILE_SIZE, TILE_SIZE))
        self.path_nodes = self.map.get_path()

        self.all_sprites = pygame.sprite.Group()

        self.defender_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.tile_group = pygame.sprite.Group()

        self.tile_group = self.map.load_map()
        self.all_sprites.add(self.tile_group)

    def add_enemy(self):
        new_enemy = Enemy("goblin_grunt", self.path_nodes)
        self.enemy_group.add(new_enemy)
        self.all_sprites.add(new_enemy)


    def add_defender(self, pos):
        new_defender = Defender(3, 500, 1, pos)
        self.defender_group.add(new_defender)
        self.all_sprites.add(new_defender)
        print(self.check_if_tile_free(pos))


    def update(self):
        self.enemy_group.update()
        self.bullet_group.update(self.enemy_group)
        self.defender_group.update(self.enemy_group, self.bullet_group, self.all_sprites)
        # self.tile_group.update()


    def draw(self, display):
        self.all_sprites.draw(display)
        self.tile_group.update(display)
    
    def check_if_tile_free(self, pos):
        tile_index = get_map_tile_by_mouse_coord(self.map.get_map(), pos, self.map.get_pos())

        if tile_index is not None:
            tile_id = self.map.get_map()[tile_index[0]][tile_index[1]]

            if get_tile_type(tile_id) == FREE_TILE:
                return True

            else:
                return False
        else:
            return False
