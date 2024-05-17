import pygame
from grass import Grass
import settings
class Home:

    def __init__(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.worth = True
        self.grass2 = Grass()
        self.grass2.run()


    def start(self):
        if self.worth:
            print('im working here')

            settings.GRASS_W = 10
            settings.GRASS_H = 10
            self.worth = False
        #self.screen.fill(settings.BACKGROUND_C)

        self.grass2.run2()
        #pygame.display.update()


