import pygame
from defender import Defender

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1000, 800))
        self.font = pygame.font.SysFont("Arial", 20)

        self.money = 100

        self.defender_img = pygame.image.load("src/assets/robot.png")
        self.defenders = []

        self.clock = pygame.time.Clock()


    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if self.money >= Defender.cost:
                        self.defenders.append(Defender(self.defender_img, 10, 5, x, y))
                        self.money -= Defender.cost

            self.display.fill((0, 0, 0))
            self.draw_defenders()

            text = self.font.render("Money: " + str(self.money), True, (255, 255, 255))
            self.display.blit(text, (30, 0))

            pygame.display.flip()

            self.clock.tick(60)


    def add_defender(self, sprite):
        self.defenders.append(sprite)


    def draw_defenders(self):
        for defender in self.defenders:
            self.display.blit(defender.get_img(), defender.get_pos())

