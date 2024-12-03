import os

DIRNAME = os.path.dirname(__file__)

TILE_SHEET = os.path.join(DIRNAME, "assets", "td_tiles_h.png")

# Asset image size
IMG_SIZE = 32

# Game tile size
TILE_SIZE = 64

MAP_OFFSET = (TILE_SIZE, TILE_SIZE)

# Tile type indexes
FREE_TILE = (0, 8)
ROAD_TILE = (9, 14)
WALL_TILE = (15, 16)
BASE_TILE = (17, 20)
GOB_BASE_TILE = (21, 24)