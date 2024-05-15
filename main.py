
# Import and initialize the pygame library
import pygame
import sys
import time

import EventHandler
from settings import *
from EventHandler import Event1
from introduction import Introduction




class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("TASH GAME")
        self.clock = pygame.time.Clock()
        self.introduction = Introduction()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #dt = self.clock.tick(FPS) / 1000


            self.introduction.setup()

        else:
            print('youre doing great')
            pygame.quit()
            sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()