import pygame
from statics import *
from utils.map_utils import *

class Map:
    def __init__(self, map_data, sprite_list):
        self.map = map_data["map"]
        self.sprite_list = sprite_list
        self.path = map_data["path"]

    def set_tile(self, map_index, tile_id):
        self.map_data[map_index[0]][map_index[1]] = tile_id

    def get_path(self):
        return self.path
    
    def draw(self, display):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if col != None:
                    img = self.sprite_list[col]
                    display.blit(img, (j*TILE_SIZE+TILE_SIZE, i*TILE_SIZE+TILE_SIZE))