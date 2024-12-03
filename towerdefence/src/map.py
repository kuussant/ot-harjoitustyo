import pygame
from statics import *
from map_utils import *

class Map:
    def __init__(self, map_data, pos):
        self.map_data = map_data
        self.pos = pos

    def set_tile(self, map_index, tile_id):
        self.map_data[map_index[0]][map_index[1]] = tile_id

    def draw(self, display):
        for i, row in enumerate(map):
            for j, col in enumerate(row):
                if col != (None, None):
                    img = self.sprites_list[col[1]][0]
                    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                    display.blit(img, (j*TILE_SIZE+self.pos, i*TILE_SIZE+self.pos))