
# Import and initialize the pygame library
import pygame
import sys
import time
import os
#       import RPi.GPIO as GPIO
from settings import *
from EventHandler import Event
from pygame.locals import *

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.OUT)
#GPIO.setup(17, GPIO.OUT)
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)
        self.running = True
        pygame.display.set_caption("TASH GAME")
        self.clock = pygame.time.Clock()
        self.action = Event()


    def run(self):
        while self.running:
            #starttime = time.time()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            #dt = self.clock.tick(FPS) / 1000
            self.action.introductions()
            pygame.display.update()
        else:
            print('youre doing great')
            pygame.quit()
            sys.exit()



if __name__ == '__main__':
    game = Game()
    game.run()