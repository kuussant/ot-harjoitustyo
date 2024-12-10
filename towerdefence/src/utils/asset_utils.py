import os
import pygame
import statics as s

DIRNAME = os.path.dirname(__file__)


def load():
    IMAGE_SHEETS = {}
    SOUNDS = {}

    texture_path = "assets/textures"
    sound_path = "assets/sounds"

    # Textures
    map_tiles_path = os.path.join(
        DIRNAME, "..", texture_path, "td_tiles_h.png")
    defender_pvt = os.path.join(
        DIRNAME, "..", texture_path, "td_tiles_h.png")  # TODO
    goblin_grunt_path = os.path.join(
        DIRNAME, "..", texture_path, "td_goblin.png")
    goblin_brute_path = os.path.join(
        DIRNAME, "..", texture_path, "td_goblin_brute.png")

    # Sounds
    hit_sound = os.path.join(DIRNAME, "..", sound_path, "hit_sound.mp3")
    goblin_death1 = os.path.join(
        DIRNAME, "..", sound_path, "goblin_death1.wav")
    goblin_death2 = os.path.join(
        DIRNAME, "..", sound_path, "goblin_death2.wav")
    goblin_death3 = os.path.join(
        DIRNAME, "..", sound_path, "goblin_death3.wav")
    goblin_death4 = os.path.join(
        DIRNAME, "..", sound_path, "goblin_death4.wav")

    coin_sound1 = os.path.join(DIRNAME, "..", sound_path, "coin_sound1.wav")
    coin_sound2 = os.path.join(DIRNAME, "..", sound_path, "coin_sound2.wav")
    coin_sound3 = os.path.join(DIRNAME, "..", sound_path, "coin_sound3.wav")

    IMAGE_SHEETS[s.MAP_TILES] = _create_sprite_list(
        map_tiles_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS[s.DEFENDER_PVT] = _create_sprite_list(
        defender_pvt, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS[s.GOBLIN_GRUNT] = _create_sprite_list(
        goblin_grunt_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS[s.GOBLIN_BRUTE] = _create_sprite_list(
        goblin_brute_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)

    SOUNDS["hit_sound"] = pygame.mixer.Sound(hit_sound)
    SOUNDS["goblin_death1"] = pygame.mixer.Sound(goblin_death1)
    SOUNDS["goblin_death2"] = pygame.mixer.Sound(goblin_death2)
    SOUNDS["goblin_death3"] = pygame.mixer.Sound(goblin_death3)
    SOUNDS["goblin_death4"] = pygame.mixer.Sound(goblin_death4)

    SOUNDS["coin_sound1"] = pygame.mixer.Sound(coin_sound1)
    SOUNDS["coin_sound2"] = pygame.mixer.Sound(coin_sound2)
    SOUNDS["coin_sound3"] = pygame.mixer.Sound(coin_sound3)

    return IMAGE_SHEETS, SOUNDS


def _create_sprite_list(file_path, width, height, scale, color=(0, 0, 0)):
    sheet = pygame.image.load(file_path).convert_alpha()
    sprite_count = sheet.get_width()//width
    sprites = []

    for i in range(0, sprite_count):
        image = pygame.Surface((width, height))
        image.blit(sheet, (0, 0), (width*i, 0, width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)
        sprites.append(image)

    return sprites
