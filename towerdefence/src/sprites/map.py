import pygame
from statics import *
from sprites.tile import Tile


class Map:
    def __init__(self, assets, map_data, pos):
        self.tiles_list = assets[0]["map_tiles"]
        self._map = map_data["map"]
        self._path = map_data["path"]
        self._pos = pos

    def get_pos(self):
        return self._pos

    def get_path(self):
        return self._path

    def get_map(self):
        return self._map

    def load_map(self):
        sprite_group = pygame.sprite.Group()
        for i, row in enumerate(self._map):
            for j, sprite_id in enumerate(row):
                if sprite_id is not None:
                    img = self.tiles_list[sprite_id]
                    tile = Tile(img, (j*TILE_SIZE+self._pos[0], i*TILE_SIZE+self._pos[1]))
                    sprite_group.add(tile)
        return sprite_group
