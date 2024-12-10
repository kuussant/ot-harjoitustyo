import pygame
import random
from collections import deque

import utils.editor_utils as eu
import utils.asset_utils
import statics as s
import sound

from sprites.defender import Defender
from sprites.enemy import Enemy
from sprites.map import Map


class Stage:
    def __init__(self, map_file, spawn_data):
        self.money = 100
        self.assets = utils.asset_utils.load()
        self.map = Map(self.assets, eu.load_map(
            map_file), (s.TILE_SIZE, s.TILE_SIZE))
        self.path_nodes = self.map.get_path()

        self.waves = spawn_data
        self.wave = 0
        self.spawn_list = deque([])
        self.wave_started = False
        self.stage_won = False

        self.play_area = [[None]*len(self.map.get_map()[0])
                          for _ in range(len(self.map.get_map()))]

        self.all_sprites = pygame.sprite.Group()
        self.defender_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.tile_group = pygame.sprite.Group()

        self.tile_group = self.map.load_map()
        self.all_sprites.add(self.tile_group)

    def _spawn_enemy(self, enemy_type):
        new_enemy = Enemy(self.assets, enemy_type, self.path_nodes)
        self.enemy_group.add(new_enemy)
        self.all_sprites.add(new_enemy)

    def handle_wave(self):
        if self.spawn_list and not self.stage_won:
            next_spawn_type = self.spawn_list.popleft()
            self._spawn_enemy(next_spawn_type)
        elif not self.enemy_group:
            self.wave_started = False

            if self.wave >= len(self.waves) - 1:
                self.stage_won = True
            else:
                self.wave += 1
                print("wave cleared")
            return False
        return True

    def generate_spawns(self):
        if not self.enemy_group:
            self.spawn_list = deque([])
            for key, val in self.waves[self.wave]["enemies"].items():
                self.spawn_list += [key for _ in range(0, val)]

            random.shuffle(self.spawn_list)
            self.wave_started = True

    def get_wave_spawn_rate(self):
        return self.waves[self.wave]["spawn_rate"]

    def wave_has_started(self):
        return self.wave_started

    def game_won(self):
        return self.stage_won

    # Needs defender type
    def add_defender(self, pos):
        tile_index = self.get_free_tile_index_by_pos(pos)

        if tile_index:
            defender = self.play_area[tile_index[0]][tile_index[1]]
            if defender is None:
                if self.money >= 100:
                    tile_center = eu.get_tile_center_by_index(
                        tile_index, self.map.get_pos())

                    new_defender = Defender(
                        self.assets, 3, 100, 1, tile_center)
                    self.play_area[tile_index[0]][tile_index[1]] = new_defender
                    self.defender_group.add(new_defender)
                    self.all_sprites.add(new_defender)
                    self.money -= 100
                    sound.play(self.assets[1]["coin_sound2"], 0.1)
                else:
                    print("Not enough money")
            else:
                print("Space is occupied")

    def check_defender(self, pos):
        tile_index = self.get_free_tile_index_by_pos(pos)

        if tile_index:
            defender = self.play_area[tile_index[0]][tile_index[1]]

            if defender is not None:
                return defender

        return None

    def update(self):
        self.enemy_group.update()
        self.bullet_group.update()
        self.defender_group.update(
            self.enemy_group, self.bullet_group, self.all_sprites)
        self._enemy_and_bullet_collision()

    def draw(self, display):
        self.all_sprites.draw(display)
        self.tile_group.update(display)

    def get_free_tile_index_by_pos(self, pos):
        tile_index = eu.get_map_tile_by_mouse_coord(
            self.map.get_map(), pos, self.map.get_pos())

        if tile_index is not None:
            tile_id = self.map.get_map()[tile_index[0]][tile_index[1]]

            if eu.get_tile_type(tile_id) == s.FREE_TILE:
                return tile_index

            else:
                return None
        else:
            return None

    def _enemy_and_bullet_collision(self):
        collide_group = pygame.sprite.groupcollide(
            self.enemy_group, self.bullet_group, False, True)
        for enemy, bullets in collide_group.items():
            for bullet in bullets:
                money_accumulated = enemy.deal_damage(bullet.damage)
                if money_accumulated > 0:
                    self.money += money_accumulated
                    sound.play(self.assets[1]["coin_sound3"], 0.1)
