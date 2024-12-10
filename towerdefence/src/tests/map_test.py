import os
import unittest
import pygame

import utils.asset_utils
from utils.editor_utils import *
import utils.editor_utils as eu
from statics import *
from sprites.map import Map

DIRNAME = os.path.dirname(__file__)
MAP_FILE = os.path.join(DIRNAME, "..", "maps", "test_map.json")

class MapTest(unittest.TestCase):
    def setUp(self):
        # pygame.init()
        pygame.display.set_mode((800, 600))
        self.assets = utils.asset_utils.load()
    
        self.map = Map(self.assets, eu.load_map(
            MAP_FILE), (s.TILE_SIZE, s.TILE_SIZE))

    def test_map_route_is_correct(self):
        test = [[160, 160], [160, 480], [352, 480], [352, 288], [544, 288]]
        self.assertEqual(self.map.get_path(), test)

    def test_map_position_is_correct(self):
        self.assertEqual(self.map.get_pos(), (s.TILE_SIZE, s.TILE_SIZE))

    def test_get_map_returns_the_correct_map(self):
        map_test = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 24, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 14, 10, 10, 17, 0, 0],
            [0, 9, 0, 0, 9, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 9, 0, 0, 0, 0, 0],
            [0, 13, 10, 10, 12, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(self.map.get_map(), map_test)

    def test_load_map_returns_correct_sprite_group(self):
        #Testing the contents of a sprite group is difficult
        self.assertEqual(str(self.map.load_map()), "<Group(100 sprites)>")
