import random
import pygame
import json
import statics as s


def update_path(map, map_pos):
    path_nodes = []
    path = generate_path(map)

    if path:
        path = optimize_path(path)

        for node in path:
            path_nodes.append(get_tile_center_by_index(node, map_pos))

    return path_nodes


def generate_path(map):
    path = []
    gob_base = None
    gob_base_count = 0
    home_base_count = 0

    # find goblin base and home base
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if get_tile_type(col) == s.GOB_BASE_TILE:
                gob_base = ((i, j), col)
                gob_base_count += 1
            elif get_tile_type(col) == s.BASE_TILE:
                home_base_count += 1

    # current pos: 0 = map index, 1 = tile_id
    if gob_base_count == 1 and home_base_count == 1:
        path_done = False
        current_pos = gob_base
        prev_tile_direction = None

        while not path_done:
            orientation = check_path_tile_orientation(
                get_tile_type(current_pos[1]), current_pos[1])

            if not orientation:
                return []

            if get_tile_type(current_pos[1]) == s.BASE_TILE:
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

            next_index = (current_pos[0][0] + current_tile_direction[1],
                          current_pos[0][1] + current_tile_direction[0])
            current_pos = (next_index, map[next_index[0]][next_index[1]])

    return path


def optimize_path(path):
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


def get_tile_type(tile_id):
    if tile_id is not None:
        if s.FREE_TILE[0] <= tile_id <= s.FREE_TILE[1]:
            return s.FREE_TILE
        elif s.ROAD_TILE[0] <= tile_id <= s.ROAD_TILE[1]:
            return s.ROAD_TILE
        elif s.WALL_TILE[0] <= tile_id <= s.WALL_TILE[1]:
            return s.WALL_TILE
        elif s.BASE_TILE[0] <= tile_id <= s.BASE_TILE[1]:
            return s.BASE_TILE
        elif s.GOB_BASE_TILE[0] <= tile_id <= s.GOB_BASE_TILE[1]:
            return s.GOB_BASE_TILE
    return None


def check_path_tile_orientation(tile, tile_id):
    if not tile:
        return None

    # tuple: (up, down, left, right)
    orientation = None

    tile_orientation = tile_id - tile[0]

    if tile == s.ROAD_TILE:
        match tile_orientation:
            case 0:
                orientation = (False, False, True, True)
            case 1:
                orientation = (True, True, False, False)
            case 2:
                orientation = (True, False, False, True)
            case 3:
                orientation = (True, False, True, False)
            case 4:
                orientation = (False, True, True, False)
            case 5:
                orientation = (False, True, False, True)

    elif tile == s.GOB_BASE_TILE or tile == s.BASE_TILE:
        match tile_orientation:
            case 0:
                orientation = (True, False, False, False)
            case 1:
                orientation = (False, False, True, False)
            case 2:
                orientation = (False, True, False, False)
            case 3:
                orientation = (False, False, False, True)

    return orientation


def get_map_tile_by_mouse_coord(map_tiles, pos, offset):
    pos_x = pos[0]
    pos_y = pos[1]
    for i in range(0, len(map_tiles)):
        y_tile = (i+1)*s.TILE_SIZE
        for j in range(0, len(map_tiles)):
            x_tile = (j+1)*s.TILE_SIZE
            if pos_x >= x_tile and pos_x <= x_tile + offset[0]:
                if pos_y >= y_tile and pos_y <= y_tile + offset[1]:
                    return (i, j)

    return None

# NEEDS OFFSET


def get_tile_center_by_index(pos, offset):
    tile_x = s.TILE_SIZE + pos[1]*s.TILE_SIZE
    tile_y = s.TILE_SIZE + pos[0]*s.TILE_SIZE

    tile_center_x = tile_x - (s.TILE_SIZE//2)
    tile_center_y = tile_y - (s.TILE_SIZE//2)

    return (tile_center_x+offset[0], tile_center_y+offset[1])


# tile = (tile_type, tile_sheet_index)
def set_map_tile(tile_type_and_index, map_tiles, ij):
    if ij == (None, None):
        map_tiles[ij[0]][ij[1]] = tile_type_and_index


def draw_map(display, sprites_list, map):
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col is not None:
                img = sprites_list[col]
                display.blit(img, (j*s.TILE_SIZE+s.TILE_SIZE,
                             i*s.TILE_SIZE+s.TILE_SIZE))


def randomize_map_free_tiles(map):
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col >= s.FREE_TILE[0] and col <= s.FREE_TILE[1]:
                map[i][j] = random.randint(s.FREE_TILE[0], s.FREE_TILE[1])


def draw_grid(display):
    for x in range(s.TILE_SIZE, display.get_width() - s.TILE_SIZE, s.TILE_SIZE):
        for y in range(s.TILE_SIZE, display.get_height() - s.TILE_SIZE, s.TILE_SIZE):
            rect = pygame.Rect(x, y, s.TILE_SIZE, s.TILE_SIZE)
            pygame.draw.rect(display, (255, 255, 255), rect, 1)


def save_map(map, path, map_name):
    try:
        with open(map_name, "w") as f:
            map_dict = {"map": map, "path": path}
            json_object = json.dumps(map_dict, indent=4)
            f.write(json_object)
        return True
    except:
        print("Could not save map", map_name)
        return False


def load_map(map_name):
    out_map = None
    try:
        with open(map_name, "r") as f:
            out_map = json.load(f)
        return out_map
    except:
        print("No map", map_name)
        return None
