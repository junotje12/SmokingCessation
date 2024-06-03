import pygame
import grassdata
import sys
from settings import *
from support import get_path
from grass import Grass
import settings
import pygame
from pygame.locals import *
from home import Home

class Introduction:
    def __init__(self):
        self.dragging = False

        font_path = get_path('./font/LycheeSoda.ttf')
        self.TASC = pygame.image.load('./Sprites/TASC.png')
        self.amountChosen = False
        self.intro = True
        self.numberwidth = 0.75
        self.font1 = pygame.font.Font(font_path, int(SCREEN_WIDTH/8.7))
        self.font2 = pygame.font.Font(font_path, int(SCREEN_WIDTH/16))
        self.font3 = pygame.font.Font(font_path, int(SCREEN_WIDTH/self.numberwidth))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.display_surface = pygame.display.get_surface()
        self.slider_pos = (SCREEN_WIDTH/2 - 70, SCREEN_HEIGHT -50)

        self.handle_x = self.slider_pos[0]
        self.handle_y = self.slider_pos[1] + 10 // 2
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
                midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))

            self.text_continue = self.continue_text.get_rect(
                midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            #pygame.draw.rect(self.display_surface, 'Black',
             #                self.text_TASH.inflate(10, 10), 0, 4)
            pygame.draw.rect(self.display_surface, 'Black',
                             self.text_info.inflate(10, 10), 0, 4)
            pygame.draw.rect(self.display_surface, 'Black',
                             self.text_continue.inflate(10, 10), 0, 4)

            #self.display_surface.blit(self.TASH_text, self.text_TASH)
            self.display_surface.blit(self.info_text, self.text_info)
            self.display_surface.blit(self.continue_text, self.text_continue)
            self.display_surface.blit(self.TASC,(0,0))
            pygame.display.update()
            self.input()

        else:

            self.setusage()
            settings.home = True
            settings.intro = False
    def setusage(self):

        self.blackwidth = 50
        self.usageXpos = 3.6
        settings.usage = 0
        while self.amountChosen == False:
            self.input()
            self.grass.run2()
            self.nowsmoke = self.font2.render("what amount do you currently smoke", False, 'White')
            self.usage_text = self.font3.render(str(settings.usage), False, 'White')

            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()

            if settings.usage <= 0:
                settings.usage = 0



            if settings.usage >= 10:
                self.blackwidth = SCREEN_WIDTH/2 - 10
                self.usageXpos = 10

            elif settings.usage >= 20:

                self.blackwidth = SCREEN_WIDTH/2
                self.usageXpos = 20
                self.numberwidth = 0.85

            else:
                self.usageXpos = 3.6
                self.blackwidth = SCREEN_WIDTH/10
                self.text_usage = self.continue_text.get_rect(
                    midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.85))
            self.text_nowsmoke = self.nowsmoke.get_rect(
                midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 14))

            pygame.draw.rect(self.display_surface, 'Black',
                             self.text_usage.inflate(self.blackwidth, 200), 0, 4)
            pygame.draw.rect(self.display_surface, 'Black',
                             self.text_nowsmoke.inflate(10, 10), 0, 4)

            pygame.draw.rect(self.display_surface, 'White',
                             self.text_nowsmoke.inflate(10, 10), 4, 4)

            self.display_surface.blit(self.usage_text,(SCREEN_WIDTH/self.usageXpos , SCREEN_HEIGHT/40))
            self.display_surface.blit(self.nowsmoke, self.text_nowsmoke)


# run slider here


            pygame.draw.rect(self.screen, (255,255,255), (*self.slider_pos, SCREEN_WIDTH-100, 10))

            pygame.draw.circle(self.screen, (0,0,0), (self.handle_x, self.handle_y), 15)

            slider_value = int(((self.handle_x - self.slider_pos[0]) / 15)* 5)

            print(slider_value)

            settings.usage = slider_value
            pygame.display.update()

        if settings.usage > 0 and settings.usage <= 5:
            settings.duration = 6000
        elif settings.usage > 5 and settings.usage <= 10:
            settings.duration = 12000
        elif settings.usage > 10:
            settings.duration = 18000


    def input(self):

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.intro:
                    if self.text_continue.collidepoint(event.pos):
                        self.intro = False

                if event.button == 1:  # Left mouse button
                    if (self.handle_x - 15 <= event.pos[0] <= self.handle_x + 15 and
                                    self.handle_y - 15 <= event.pos[1] <= self.handle_y + 15):
                                self.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:  # Left mouse button
                            self.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                        if self.dragging:
                            self.handle_x = event.pos[0]
                            self.handle_x = max(self.slider_pos[0], min(self.handle_x, self.slider_pos[0] + (SCREEN_WIDTH - 100)))

                #if self.text_usage.collidepoint(event.pos):
                        #self.amountChosen = True

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    settings.usage = settings.usage+1

                if event.key == K_DOWN:
                    settings.usage = settings.usage-1

                if event.key == K_e:
                    self.amountChosen = True
                    print(settings.usage)

                if event.key == K_ESCAPE:
                    pygame.quit()
