import os
import pygame
DIRNAME = os.path.dirname(__file__)


def play(sound, volume):
    sound.set_volume(volume)
    pygame.mixer.Sound.play(sound)
    pygame.mixer.music.stop()
