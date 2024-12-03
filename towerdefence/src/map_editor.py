import os
import pygame

from statics import *
from utils.sprite_utils import *
from utils.editor_utils import *

DIRNAME = os.path.dirname(__file__)

MAP_SIZE = 10

MAP_NAME = os.path.join(DIRNAME, "maps", "map1.json")

class MapEditor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Map Editor")

        self.display = pygame.display.set_mode((TILE_SIZE*12, TILE_SIZE*12), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.map = [[0]*MAP_SIZE for _ in range(MAP_SIZE)]
        self.map_pos = (TILE_SIZE, TILE_SIZE)
        self.current_img = None
        self.img_i = 0
        self.path_nodes = []

        self.tiles_sheet = pygame.image.load(TILE_SHEET)
        self.sprites_list = create_sprite_list(self.tiles_sheet, IMG_SIZE, IMG_SIZE, 2)


    def start_editor(self):
        show_grid = True
        show_path = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if pygame.mouse.get_pressed()[0]:
                    map_index = self.get_map_index_by_mouse(pygame.mouse.get_pos())
                    self.set_tile(map_index, self.img_i)

                if pygame.mouse.get_pressed()[2]:
                    map_index = self.get_map_index_by_mouse(pygame.mouse.get_pos())
                    self.set_tile(map_index, None)

                # Scroll selected image sprite sheet
                if event.type == pygame.MOUSEWHEEL:
                    max_i = len(self.sprites_list) - 1
                    self.img_i += event.y

                    if self.img_i > max_i:
                        self.img_i = 0

                    if self.img_i < 0:
                        self.img_i = max_i

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        show_grid = not show_grid
                        print("Draw grid:", show_grid)

                    if event.key == pygame.K_r:
                        randomize_map_free_tiles(self.map)

                    if event.key == pygame.K_s:
                        save_map(self.map, self.path_nodes, MAP_NAME)

                    if event.key == pygame.K_l:
                        map_dict = load_map(MAP_NAME)
                        if map_dict:
                            self.map = map_dict["map"]
                            self.path_nodes = map_dict["path"]

                    if event.key == pygame.K_p:
                        show_path = not show_path
                        print("Draw path:", show_path)
            
            self.display.fill((30, 30, 30))

            #Show sprite preview
            self.current_img = self.sprites_list[self.img_i]
            
            draw_map(self.display, self.sprites_list, self.map)
            self.display.blit(self.current_img, (0, 0))

            if show_grid:
                draw_grid(self.display)

            #Draw path
            if show_path:
                if len(self.path_nodes) > 1:
                    pygame.draw.lines(self.display, "green", False, self.path_nodes, width=2)

            pygame.display.flip()

            self.clock.tick(60)


    def get_map_index_by_mouse(self, mouse_pos):
        mouse_pos = pygame.mouse.get_pos()
        return get_map_tile_by_mouse_coord(self.map, mouse_pos, MAP_OFFSET)


    def set_tile(self, map_index, value):
        if map_index != (None, None):
            self.map[map_index[0]][map_index[1]] = value
            self.path_nodes = update_path(self.map, MAP_OFFSET)