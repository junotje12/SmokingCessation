import pygame
import sys
from grass import Grass
import settings
from settings import *
from pygame.locals import *
from pathlib import Path
from timer import Timer
import time
from support import get_path
import Rpi.GPIO as GPIO
from settingScreen import Settings
import random

class Home:
    def __init__(self):
        GPIO.setmode(GPIO.BMC)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(21, GPIO.IN)
        self.shopping = False
        self.bird1 = pygame.image.load('./Sprites/Untitled_Artwork-2.png')
        self.dest1 = (random.randint(-20,100),random.randint(20,100))
        self.bird2 = pygame.image.load('./Sprites/Untitled_Artwork-3.png')
        self.dest2 = (random.randint(-30, 100), random.randint(60, 160))
        self.bird3 = pygame.image.load('./Sprites/Untitled_Artwork-4 2.png')
        self.dest3 = (random.randint(-40, 100), random.randint(140, 300))


        self.cat1 = pygame.image.load('./Sprites/Untitled_Artwork-5.png')
        self.dest4 = (random.randint(-20, 100), random.randint(20, 100))
        self.cat2 = pygame.image.load('./Sprites/Untitled_Artwork-6.png')
        self.dest5 = (random.randint(-30, 100), random.randint(20, 160))
        self.cat3 = pygame.image.load('./Sprites/Untitled_Artwork-7.png')
        self.dest6 = (random.randint(-40, 100), random.randint(20, 300))

        self.bird_amount = 0
        self.cat_amount = 0
        self.bird_bought = False
        self.cat_bought = False
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.worth = True
        self.select = False
        self.grass2 = Grass()
        self.grass2.run()
        self.red = (255, 0, 0)
        self.pos1 = (10, 10, settings.SCREEN_WIDTH/2 - 10, settings.SCREEN_HEIGHT/2 - 10)
        self.pos4 = (settings.SCREEN_WIDTH/2 , 10, settings.SCREEN_WIDTH/2 -10, settings.SCREEN_HEIGHT/2 - 10)
        self.pos3 =  (10, settings.SCREEN_HEIGHT/2 , settings.SCREEN_WIDTH/2 - 10, settings.SCREEN_HEIGHT/2 - 10)
        self.pos2 = (settings.SCREEN_WIDTH/2 , settings.SCREEN_HEIGHT/2, settings.SCREEN_WIDTH/2 - 10, settings.SCREEN_HEIGHT/2 - 10)
        self.currentpos = [self.pos1, self.pos2, self.pos3, self.pos4]
        self.CarrotCollect = False
        self.quit = False
        font_path = get_path('./font/LycheeSoda.ttf')
        self.font1 = pygame.font.Font(font_path, int(settings.SCREEN_WIDTH/8.7))

        self.font2 = pygame.font.Font(font_path, int(settings.SCREEN_WIDTH/14))


        self.timer = Timer(settings.duration) # 10 seconds
        self.buzzertimer = Timer(600)


    def start(self):

        if self.worth:
            print('im working here')

            self.timer.activate()
            settings.GRASS_W = 60
            settings.GRASS_H = 90
            self.worth = False
        #self.screen.fill(settings.BACKGROUND_C)

        self.grass2.run2()
        self.selecter()

        #self.timer.activate()
        self.CarrotCollect = True
        self.timer.update()
        #timer is timer since activation devided by 10 seconds
        if (int(pygame.time.get_ticks() - self.timer.start_time) / 1000) >= settings.duration/600:
            self.buzzertimer.activate()

            if timer.buzzer:
                GPIO.output(17, GPIO.HIGH)

                self.buzzertimer.buzzerupdate()
            else:
                GPIO.output(17, GPIO.LOW)

            self.carrot_timer = self.font1.render("Done!",
                                                  False, 'White')




        else:
            self.carrot_timer = self.font1.render(str(int(pygame.time.get_ticks() - self.timer.start_time) / 1000), False, 'White')

        self.carrot_amount = self.font1.render(str(settings.carrots), False,
                                              'White')

        self.text_carrot = self.carrot_timer.get_rect(
            topleft =(20, settings.SCREEN_HEIGHT - 60))
        self.amount_carrot = self.carrot_timer.get_rect(
            topleft=(settings.SCREEN_WIDTH -50, settings.SCREEN_HEIGHT - 60))

        pygame.draw.rect(self.screen, 'Black',
                         self.text_carrot.inflate(10, 10), 0, 4)

        pygame.draw.rect(self.screen, 'Black',
                         self.amount_carrot.inflate(10, 10), 0, 9)
        self.screen.blit(self.carrot_timer, self.text_carrot)
        self.screen.blit(self.carrot_amount, self.amount_carrot)
        #print(settings.carrots)
        #pygame.display.update()
        if self.bird_amount > 0:
            self.screen.blit(self.bird1, self.dest1)
        if self.bird_amount > 1:

            self.screen.blit(self.bird1, self.dest1)
            self.screen.blit(self.bird2, self.dest2)
        if self.bird_amount >2:

            self.screen.blit(self.bird1, self.dest1)
            self.screen.blit(self.bird2, self.dest2)
            self.screen.blit(self.bird3, self.dest3)


        if self.cat_amount > 0:
            self.screen.blit(self.cat1, self.dest4)
        if self.cat_amount > 1:

            self.screen.blit(self.cat1, self.dest4)
            self.screen.blit(self.cat2, self.dest5)
        if self.cat_amount >2:

            self.screen.blit(self.cat1, self.dest4)
            self.screen.blit(self.cat2, self.dest5)
            self.screen.blit(self.cat3, self.dest6)



    def settings(self):

        self.screen.fill(settings.BACKGROUND_C)
        self.settings_text = self.font2.render("settings", False, 'White')

        self.user_amount_text = self.font2.render(f"starting usage amount: {settings.usage}", False, 'White')

        self.text_user_amount = self.user_amount_text.get_rect(
            topleft=(50, 60))
        self.text_settings = self.settings_text.get_rect(
            topleft=(50, 20))

        pygame.draw.rect(self.screen, 'Black',
                         self.text_user_amount.inflate(10, 10), 0, 4)

        pygame.draw.rect(self.screen, 'Black',
                         self.text_settings.inflate(10, 10), 0, 4)

        self.screen.blit(self.user_amount_text, self.text_user_amount)
        self.screen.blit(self.settings_text, self.text_settings)

        print('settings')
        if self.quit:
            self.screen.fill(settings.BACKGROUND_C)
            self.select = False
            self.quit = False

        print(settings.usage)

        pass
    def goals(self):
        print('goals')
        #GPIO.output(17, GPIO.HIGH)

        self.select = False
        pass
    def smokingInd(self):
        print('Smoking Ind')

        if self.timer.carrot:
            settings.carrots = settings.carrots + 1
            self.timer.activate()
            self.timer.carrot = False

        print(settings.carrots)
        self.timer.update()

        self.select = False
        pass
    def shop(self):

        self.shopping = True
        self.screen.fill(settings.BACKGROUND_C)
        self.shop_text = self.font2.render("shop", False, 'White')

        self.bird_text = self.font2.render("Buy Bird : 1 Carrot", False, 'White')
        self.cat_text = self.font2.render("Buy Cat : 1 Carrot", False, 'White')

        self.text_bird = self.bird_text.get_rect(
            topleft=(50, 60))


        self.text_cat = self.cat_text.get_rect(
            topleft=(50, 100))
        self.text_shop = self.shop_text.get_rect(
            topleft=(50, 20))

        pygame.draw.rect(self.screen, 'Black',
                         self.text_bird.inflate(10, 10), 0, 4)


        pygame.draw.rect(self.screen, 'Black',
                         self.text_cat.inflate(10, 10), 0, 4)

        pygame.draw.rect(self.screen, 'Black',
                         self.text_shop.inflate(10, 10), 0, 4)

        self.screen.blit(self.bird_text, self.text_bird)

        self.screen.blit(self.cat_text, self.text_cat)
        self.screen.blit(self.shop_text, self.text_shop)

        if self.quit:
            self.screen.fill(settings.BACKGROUND_C)
            self.shopping = False
            self.select = False
            self.quit = False



        pass

    def selecter(self):
        pygame.draw.rect(self.screen, self.red, pygame.Rect(self.currentpos[0]),6)
        self.input()

        if self.select and self.currentpos[0] == self.pos1:
            self.settings()

        if self.select and self.currentpos[0] == self.pos2:
            self.goals()

        if self.select and self.currentpos[0] == self.pos3:
            self.smokingInd()

        if self.select and self.currentpos[0] == self.pos4:
            self.shop()


    def input(self):
        for event in pygame.event.get():


            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.shopping:
                    if self.text_bird.collidepoint(event.pos):
                        if settings.carrots > 0:
                            self.bird_bought = True
                            self.bird_amount = self.bird_amount + 1
                            settings.carrots = settings.carrots - 1
                            self.bird_bought = False
                    if self.text_cat.collidepoint(event.pos):
                        if settings.carrots > 0:
                            self.cat_bought = True
                            self.cat_amount = self.cat_amount + 1
                            settings.carrots = settings.carrots - 1
                            self.cat_bought = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:

                if event.key == K_RIGHT:
                    x = self.currentpos.pop()
                    self.currentpos.insert(0,x)

                if event.key == K_LEFT:
                    y = self.currentpos.pop(0)
                    self.currentpos.insert(len(self.currentpos),y)

                if event.key == K_e:
                    self.select = True

                if event.key == K_q:
                    self.quit = True

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()





