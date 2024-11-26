import pygame
from collections import deque

from sprites.defender import Defender
from sprites.enemy import Enemy
from sprites.bullet import Bullet

class Game:

    def __init__(self):
        pygame.init()
        self.time_elapsed = 0
        self.display = pygame.display.set_mode((1000, 800))
        self.font = pygame.font.SysFont("Arial", 20)

        self.money = 100

        self.defenders = []

        self.all_sprites = pygame.sprite.Group()
        self.defender_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.path_nodes = [(100, 0), (100, 700), (500, 700), (500, 200), (900, 200), (900, 800)]

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                # TESTING

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if pygame.mouse.get_pressed()[0]:
                        if self.money >= Defender.cost:
                            new_defender = Defender(10, 2, 300, (x, y), self.bullet_group)
                            self.defender_group.add(new_defender)
                            self.all_sprites.add(new_defender)
                            self.money -= Defender.cost

                    if pygame.mouse.get_pressed()[2]:
                        new_enemy = Enemy(10, 10, 2, self.path_nodes)
                        self.enemy_group.add(new_enemy)
                        self.all_sprites.add(new_enemy)

                    if pygame.mouse.get_pressed()[1]:
                        new_bullet = Bullet(1, 2, (x, y), 5)
                        self.bullet_group.add(new_bullet)
                        self.all_sprites.add(new_bullet)


            self.display.fill((30, 30, 30))

            # Enemy path showed 
            pygame.draw.lines(self.display, "red", False, self.path_nodes)
            
            
            self.enemy_group.update()
            self.bullet_group.update(self.enemy_group)

            #Test bullet delays, will move to a better location

            if self.time_elapsed >= 1000:
                self.defender_group.update(self.enemy_group, self.bullet_group)
                print(self.bullet_group)
                
                self.time_elapsed = 0

            self.all_sprites.draw(self.display)
            self.bullet_group.draw(self.display)

            pygame.display.flip()

            self.time_elapsed += self.clock.tick(60)

