import sys
import time
import math
import random
import pygame
import settings
from pygame.locals import *

import grassdata

# set up pygame

class Grass:

    def __init__(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), pygame.RESIZABLE)

        self.attempt()
        self.clock = pygame.time.Clock()

        # set up the grass manager and enable shadows
        self.gm = grassdata.GrassManager('grass', tile_size=13, stiffness=600, max_unique=5, place_range=[0, 1])
        self.gm.enable_ground_shadows(shadow_radius=4, shadow_color=(0, 0, 1), shadow_shift=(1, 2))
        self.scroll = [0, 0]
        self.t = 0
        self.start = time.time()
    def attempt(self):
        self.display = pygame.Surface((settings.GRASS_W, settings.GRASS_H))

    def run(self):
    # fill in the base square
        self.display.fill(settings.BACKGROUND_C)

        for y in range(37):
            y += 5
            for x in range(25):
                x += 5
                v = random.random()
                if v > 0.1:
                    self.gm.place_tile((x-5, y-10), int(v * 7), [0, 1, 2, 3, 4, 5])

        self.rot_function = lambda x, y: int(math.sin(self.t / 60 + x / 100) * 15)
        # demo loop

    def run2(self):
            self.attempt()
        #while True:
            # calc dt
            dt = time.time() - self.start
            self.start = time.time()

            # fill background

            self.display.fill(settings.BACKGROUND_C)

            # create an anonymous function that will apply a wind pattern to the grass when passed to the grass manager's update render function
            # this function uses the X offset of the grass, the master time of the application, and a sine function to create the pattern.


            # run the update/render for the grass
            self.gm.update_render(self.display, dt, offset=self.scroll, rot_function=self.rot_function)

            # increment master time
            self.t += dt * 45

            # render
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            #pygame.display.update()
            self.clock.tick(1000)

