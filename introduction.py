import pygame

import grassdata
from settings import *
from support import get_path
from grass import Grass
import settings
import pygame
from pygame.locals import *
from home import Home

class Introduction:
    def __init__(self):

        font_path = get_path('./font/LycheeSoda.ttf')
        self.intro = True
        self.font1 = pygame.font.Font(font_path, int(SCREEN_WIDTH/8.7))
        self.font2 = pygame.font.Font(font_path, int(SCREEN_WIDTH/16))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.display_surface = pygame.display.get_surface()
        self.home = Home()
        self.grass = Grass()
        self.grass.run()
        self.setup()

    def setup(self):
        # create text surfaces
        if self.intro:

            self.grass.run2()
            self.TASH_text = self.font1.render("Welcome to T.A.S.H", False, 'White')
            self.info_text = self.font2.render('To Assist Smoking Cessation Habits', False, 'White')
            self.continue_text = self.font1.render("CONTINUE", False, 'White')

            self.text_TASH = self.TASH_text.get_rect(
                midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5))

            self.text_info = self.info_text.get_rect(
                midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))

            self.text_continue = self.continue_text.get_rect(
                midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            pygame.draw.rect(self.display_surface, 'Black',
                             self.text_TASH.inflate(10, 10), 0, 4)
            pygame.draw.rect(self.display_surface, 'Black',
                             self.text_info.inflate(10, 10), 0, 4)
            pygame.draw.rect(self.display_surface, 'Black',
                             self.text_continue.inflate(10, 10), 0, 4)

            self.display_surface.blit(self.TASH_text, self.text_TASH)
            self.display_surface.blit(self.info_text, self.text_info)
            self.display_surface.blit(self.continue_text, self.text_continue)
            pygame.display.update()
            self.input()

        else:
            print('hi')
            settings.home = True
            settings.intro = False
            #self.home.start()

    def input(self):

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.text_continue.collidepoint(event.pos):
                    self.intro = False
            if event.type == KEYDOWN:

                if event.key == K_e:
                    print(self.text_continue)
                    self.intro = False


    def update(self):
        self.input()




