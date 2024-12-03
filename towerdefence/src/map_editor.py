import os
import random
import pygame
import json

from statics import *
from sprite_utils import *

dirname = os.path.dirname(__file__)

map_size = 10

# Tile indexes
FREE_TILE = (0, 8)
ROAD_TILE = (9, 14)
WALL_TILE = (15, 16)
BASE_TILE = (17, 20)
GOB_BASE_TILE = (21, 24)

class MapEditor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Map Editor")

        self.display = pygame.display.set_mode((TILE_SIZE*12, TILE_SIZE*12), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.map = [[0]*map_size for _ in range(map_size)]
        self.map_pos = (TILE_SIZE, TILE_SIZE)
        self.current_img = None
        self.img_i = 0
        self.path_nodes = []
        
        self.sprites_list = []

        self.tiles_sheet = pygame.image.load(
            os.path.join(dirname, "assets", "td_tiles_h.png")
        )

        self.sprites_list = self.create_sprite_list(self.tiles_sheet, IMG_SIZE, IMG_SIZE)


    def start_editor(self):
        draw_grid = True
        draw_path = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    map_index = self.get_map_tile_by_mouse_coord(self.map, mouse_pos)
                    if map_index != (None, None):
                        self.map[map_index[0]][map_index[1]] = self.img_i
                        self.update_path()

                if pygame.mouse.get_pressed()[2]:
                    mouse_pos = pygame.mouse.get_pos()
                    map_index = self.get_map_tile_by_mouse_coord(self.map, mouse_pos)
                    if map_index != (None, None):
                        self.map[map_index[0]][map_index[1]] = None
                        self.update_path()

                if pygame.mouse.get_pressed()[1]:
                    print("Path")
                    mouse_pos = pygame.mouse.get_pos()
                    map_index = self.get_map_tile_by_mouse_coord(self.map, mouse_pos)
                    if map_index != (None, None):
                        pass

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
                        draw_grid = not draw_grid
                        print("Draw grid:", draw_grid)

                    if event.key == pygame.K_r:
                        self.randomize_map_free_tiles(self.map)

                    if event.key == pygame.K_s:
                        self.save_map(self.map)

                    if event.key == pygame.K_l:
                        self.map = self.load_map()
                        self.update_path()

                    if event.key == pygame.K_p:
                        draw_path = not draw_path
                        print("Draw path:", draw_path)
            
            self.display.fill((30, 30, 30))

            #Show sprite preview
            img = self.sprites_list[self.img_i]
            
            self.current_img = img

            img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
            
            self.draw_map(self.map)
            self.display.blit(img, (0, 0))

            if draw_grid:
                self.draw_grid()

            #Draw path
            if draw_path:
                if len(self.path_nodes) > 1:
                    pygame.draw.lines(self.display, "red", False, self.path_nodes)

            pygame.display.flip()

            self.clock.tick(60)

    def update_path(self):
        self.path_nodes = []
        path = self.generate_path(self.map)
        
        if path:
            path = self.optimize_path(path)
        
            for node in path:
                self.path_nodes.append(self.get_tile_center_coords_by(node))

    def generate_path(self, map):
        path = []
        gob_base = None
        gob_base_count = 0
        home_base_count = 0

        # find goblin base and home base
        for i, row in enumerate(map):
            for j, col in enumerate(row):
                if self.check_tile(col) == GOB_BASE_TILE:
                    gob_base = ((i, j), col)
                    gob_base_count += 1
                elif self.check_tile(col) == BASE_TILE:
                    home_base_count += 1

        # current pos: 0 = map index, 1 = tile_id
        if gob_base_count == 1 and home_base_count == 1:
            path_done = False
            current_pos = gob_base
            prev_tile_direction = None

            while not path_done:
                orientation = self.check_orientation(self.check_tile(current_pos[1]), current_pos[1])
                
                if not orientation:
                    return []
                
                if self.check_tile(current_pos[1]) == BASE_TILE:
                    path_done = True
                
                path.append(current_pos[0])

                current_tile_direction = [0, 0]
                
                for i, next in enumerate(orientation):
                    if i == 0 and next:
                        current_tile_direction[0] -= 1
                    elif i == 1 and next:
                        current_tile_direction[0] += 1
                    elif i == 2 and next:
                        current_tile_direction[1] -= 1
                    elif i == 3 and next:
                        current_tile_direction[1] += 1

                if not prev_tile_direction:
                    prev_tile_direction = current_tile_direction

                else:
                    sum_x = current_tile_direction[0] + prev_tile_direction[0]
                    sum_y = current_tile_direction[1] + prev_tile_direction[1]
                    current_tile_direction = [sum_x, sum_y]
                    prev_tile_direction = current_tile_direction

                next_index = (current_pos[0][0] + current_tile_direction[1], current_pos[0][1] + current_tile_direction[0])
                current_pos = (next_index, map[next_index[0]][next_index[1]])

        return path

    def optimize_path(self, path):
        optimized_path = []
        if path:
            prev = None
            optimized_path.append(path[0])
        
            for i in range(0, len(path) - 1):
                if not prev:
                    prev = path[i]
                    continue
                if prev[0] != path[i+1][0] and prev[1] != path[i+1][1]:
                    optimized_path.append(path[i])

                prev = path[i]

            optimized_path.append(path[-1])
            return optimized_path
        else:
            return None


    def check_tile(self, tile_id):
        if tile_id:
            if tile_id >= ROAD_TILE[0] and tile_id <= ROAD_TILE[1]:
                return ROAD_TILE
            elif tile_id >= BASE_TILE[0] and tile_id <= BASE_TILE[1]:
                return BASE_TILE
            elif tile_id >= GOB_BASE_TILE[0] and tile_id <= GOB_BASE_TILE[1]:
                return GOB_BASE_TILE
        return None


    def check_orientation(self, tile, tile_id):
        if not tile:
            return None
        # tuple: (up, down, left, right)
        orientation = None

        tile_orientation = tile_id - tile[0]

        if tile == ROAD_TILE:
            if tile_orientation == 0:
                orientation = (False, False, True, True)
            elif tile_orientation == 1:
                orientation = (True, True, False, False)
            elif tile_orientation == 2:
                orientation = (True, False, False, True)
            elif tile_orientation == 3:
                orientation = (True, False, True, False)
            elif tile_orientation == 4:
                orientation = (False, True, True, False)
            elif tile_orientation == 5:
                orientation = (False, True, False, True)
        
        else:
            if tile_orientation == 0:
                orientation = (True, False, False, False)
            elif tile_orientation == 1:
                orientation = (False, False, True, False)
            elif tile_orientation == 2:
                orientation = (False, True, False, False)
            elif tile_orientation == 3:
                orientation = (False, False, False, True)

        return orientation
                

    def get_map_tile_by_mouse_coord(self, map_tiles, pos):
        pos_x = pos[0]
        pos_y = pos[1]
        for i in range(0, len(map_tiles)):
            y_tile = (i+1)*TILE_SIZE
            for j in range(0, len(map_tiles)):
                x_tile = (j+1)*TILE_SIZE
                if pos_x >= x_tile and pos_x <= x_tile + TILE_SIZE:
                    if pos_y >= y_tile and pos_y <= y_tile + TILE_SIZE:
                        return (i, j)
        return (None, None)
    
    # NEEDS OFFSET
    def get_tile_center_coords_by(self, coords):
        tile_x = TILE_SIZE + coords[1]*TILE_SIZE
        tile_y = TILE_SIZE + coords[0]*TILE_SIZE

        tile_center_x = tile_x - (TILE_SIZE//2)
        tile_center_y = tile_y - (TILE_SIZE//2)

        return (tile_center_x+TILE_SIZE, tile_center_y+TILE_SIZE)



    # tile = (tile_type, tile_sheet_index)
    def set_map_tile(self, tile_type_and_index, map_tiles, ij):
        if ij == (None, None):
            map_tiles[ij[0]][ij[1]] = tile_type_and_index


    def draw_map(self, map):
        for i, row in enumerate(map):
            for j, col in enumerate(row):
                if col != None:
                    img = self.sprites_list[col]
                    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                    self.display.blit(img, (j*TILE_SIZE+TILE_SIZE, i*TILE_SIZE+TILE_SIZE))

    
    def randomize_map_free_tiles(self, map):
        print("Randomize free tiles")
        for i, row in enumerate(map):
            for j, col in enumerate(row):
                if col >= FREE_TILE[0] and col <= FREE_TILE[1]:
                    map[i][j] = random.randint(FREE_TILE[0], FREE_TILE[1])


    def draw_grid(self):
        for x in range(TILE_SIZE, self.display.get_width() - TILE_SIZE, TILE_SIZE):
            for y in range(TILE_SIZE, self.display.get_height() - TILE_SIZE, TILE_SIZE):
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.display, (255, 255, 255), rect, 1)


    def create_sprite_list(self, sheet, width, height):
        sprites = []
        for i in range(0, sheet.get_width()//width):
            image = pygame.Surface((width, height))
            image.blit(sheet, (0, 0), (width*i, 0, width, height))
            
            sprites.append(image)

        return sprites
    

    def save_map(self, map):
        with open("test_map.txt", "w") as f:
            f.write(json.dumps(map))
        print("map saved")
    

    def load_map(self):
        out_map = []
        with open("test_map.txt", "r") as f:

            for row in json.load(f):
                new_row = []
                for col in row:
                    new_row.append(col)

                out_map.append(new_row)

        return out_map