import unittest
import pygame
import utils.asset_utils
import statics

from sprites.enemy import Enemy
from pygame.math import Vector2

class TestEnemy(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((100, 100))
        self.assets = utils.asset_utils.load()
        self.path_nodes = [(0, 0), (100, 100)]
        self.enemy = Enemy(self.assets, statics.GOBLIN_GRUNT, self.path_nodes)

        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)

        self.clock = pygame.time.Clock()

    def test_enemy_takes_the_correct_amount_of_damage(self):
        self.enemy.deal_damage(2)

        self.assertEqual(self.enemy.hp, 1)

    def test_can_not_deal_negative_damage_to_enemy(self):
        self.enemy.deal_damage(-5)

        self.assertEqual(self.enemy.hp, 3)

    def test_enemy_dies_when_health_drops_to_zero_or_below(self):
        self.enemy.deal_damage(3)

        self.assertEqual(self.enemy.hp, 0)

    def test_enemy_moves_to_the_correct_path_node(self):
        time_elapsed = 0

        # Give enough time for enemy to get to the last node
        while time_elapsed <= 3000:
            self.enemy_group.update()
            time_elapsed += self.clock.tick(60)

        distance = (Vector2(100, 100) - self.enemy.pos).length()

        self.assertAlmostEqual(distance, 0, delta=2)

    # The reached_end_node attribute is true when an enemy gets removed form the group

    def test_enemy_is_removed_from_group_when_it_reaches_the_end_node(self):
        time_elapsed = 0

        # Give enough time for enemy to get to the last node
        while time_elapsed <= 3000:
            self.enemy_group.update()
            time_elapsed += self.clock.tick(60)

        self.assertTrue(self.enemy._reached_end())

    def test_enemy_is_not_removed_from_group_when_not_at_end_node(self):
        time_elapsed = 0

        # Don't give enough time for enemy to get to the last node
        while time_elapsed <= 100:
            self.enemy_group.update()
            time_elapsed += self.clock.tick(60)

        self.assertTrue(not self.enemy._reached_end())
