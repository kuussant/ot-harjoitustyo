import os
import pygame
import statics as s

DIRNAME = os.path.dirname(__file__)


def load():
    IMAGE_SHEETS = {}
    SOUNDS = {}
    FONTS = {}

    texture_path = "assets/textures"
    sound_path = "assets/sounds"

    # Texture paths
    map_tiles_path = os.path.join(
        DIRNAME, "..", texture_path, "td_tiles_h.png")
    defender_pvt_path = os.path.join(
        DIRNAME, "..", texture_path, "td_defender_pvt.png")
    goblin_grunt_path = os.path.join(
        DIRNAME, "..", texture_path, "td_goblin.png")
    goblin_brute_path = os.path.join(
        DIRNAME, "..", texture_path, "td_goblin_brute.png")
    bolt_path = os.path.join(
        DIRNAME, "..", texture_path, "td_bolt.png")
    
    # UI paths
    buttons_small_path = os.path.join(DIRNAME, "..", texture_path, "td_buttons_small.png")
    buttons_wide_path = os.path.join(DIRNAME, "..", texture_path, "td_buttons_wide.png")

    # Sound paths
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

    bow_sound = os.path.join(DIRNAME, "..", sound_path, "bow_sound.wav")

    button_sound1 = os.path.join(DIRNAME, "..", sound_path, "button1.wav")
    button_sound2 = os.path.join(DIRNAME, "..", sound_path, "button2.wav")

    # defenders and enemies
    IMAGE_SHEETS[s.MAP_TILES] = _create_sprite_list(
        map_tiles_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS[s.DEFENDER_PVT] = _create_sprite_list(
        defender_pvt_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS[s.DEFENDER_SGT] = _create_sprite_list(
        defender_pvt_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS[s.GOBLIN_GRUNT] = _create_sprite_list(
        goblin_grunt_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS[s.GOBLIN_BRUTE] = _create_sprite_list(
        goblin_brute_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS[s.BOLT] = _create_sprite_list(
        bolt_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    
    # UI buttons
    IMAGE_SHEETS["buttons_small"] = _create_sprite_list(buttons_small_path, s.IMG_SIZE, s.IMG_SIZE, scale=s.IMG_SCALE)
    IMAGE_SHEETS["buttons_wide"] = _create_sprite_list(buttons_wide_path, s.IMG_SIZE*2, s.IMG_SIZE, scale=s.IMG_SCALE)

    # Game sounds
    SOUNDS["hit_sound"] = pygame.mixer.Sound(hit_sound)

    SOUNDS["goblin_death1"] = pygame.mixer.Sound(goblin_death1)
    SOUNDS["goblin_death2"] = pygame.mixer.Sound(goblin_death2)
    SOUNDS["goblin_death3"] = pygame.mixer.Sound(goblin_death3)
    SOUNDS["goblin_death4"] = pygame.mixer.Sound(goblin_death4)

    SOUNDS["coin_sound1"] = pygame.mixer.Sound(coin_sound1)
    SOUNDS["coin_sound2"] = pygame.mixer.Sound(coin_sound2)
    SOUNDS["coin_sound3"] = pygame.mixer.Sound(coin_sound3)

    SOUNDS["bow_sound"] = pygame.mixer.Sound(bow_sound)

    # UI sounds
    SOUNDS["button_sound1"] = pygame.mixer.Sound(button_sound1)
    SOUNDS["button_sound2"] = pygame.mixer.Sound(button_sound2)

    FONTS["game_font"] = os.path.join(DIRNAME, "..", "assets/Micro5-Regular.ttf")

    return IMAGE_SHEETS, SOUNDS, FONTS


def _create_sprite_list(file_path, width, height, scale, color=(0, 0, 0)):
    sheet = pygame.image.load(file_path)
    sprite_count = sheet.get_width()//width
    sprites = []

    for i in range(0, sprite_count):
        image = pygame.Surface((width, height))
        image.blit(sheet, (0, 0), (width*i, 0, width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)
        sprites.append(image)

    return sprites
