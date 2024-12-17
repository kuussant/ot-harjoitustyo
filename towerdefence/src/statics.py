# Asset image size
IMG_SIZE = 32
IMG_SCALE = 2

# Game tile size
TILE_SIZE = IMG_SIZE*IMG_SCALE

DISPLAY_WIDTH = TILE_SIZE*12
DISPLAY_HEIGHT = TILE_SIZE*12
UI_PANEL = 300

MAP_OFFSET = (TILE_SIZE, TILE_SIZE)

# Tile type indexes
FREE_TILE = (0, 8)
ROAD_TILE = (9, 14)
WALL_TILE = (15, 16)
BASE_TILE = (17, 20)
GOB_BASE_TILE = (21, 24)

# Asset names
NO_TYPE = "no_type"
MAP_TILES = "map_tiles"
DEFENDER_PVT = "defender_pvt"
DEFENDER_SGT = "defender_sgt"
GOBLIN_GRUNT = "goblin_grunt"
GOBLIN_BRUTE = "goblin_brute"
BOLT = "bolt"
