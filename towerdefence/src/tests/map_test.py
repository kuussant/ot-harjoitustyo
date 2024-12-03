import os
import unittest
import pygame

from utils.sprite_utils import *
from utils.editor_utils import *
from statics import *

from sprites.map import Map

class MapTest(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((800, 600))

        tiles_sheet = pygame.image.load(TILE_SHEET)
        tiles_list = create_sprite_list(tiles_sheet, IMG_SIZE, IMG_SIZE, 2)
        self.map = Map(load_map(os.path.join(DIRNAME, "maps", "test_map.json")), tiles_list)

    def test_map_route_is_correct(self):
        test = [[160, 160], [160, 480], [352, 480], [352, 288], [544, 288]]
        self.assertEqual(self.map.get_path(), test)