import pygame
from statics import *
from utils.sprite_utils import *
from sprites.tile import Tile

class Map:
    def __init__(self, map_data, pos):
        self._map = map_data["map"]
        self._path = map_data["path"]
        self._pos = pos

        tiles_image = pygame.image.load(
            os.path.join(DIRNAME, "assets", "td_tiles_h.png")
        )

        self.tiles_list = create_sprite_list(tiles_image, IMG_SIZE, IMG_SIZE, 2)


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