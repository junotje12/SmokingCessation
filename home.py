import pygame
from grass import Grass
import settings
from settings import *
from pygame.locals import *
from pathlib import Path
from timer import Timer
from support import get_path

class Home:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
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

        font_path = get_path('./font/LycheeSoda.ttf')
        self.font1 = pygame.font.Font(font_path, int(settings.SCREEN_WIDTH/8.7))


        self.timer = Timer(settings.duration) # 10 seconds


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
            self.carrot_timer = self.font1.render("Done!",
                                                  False, 'White')
        else:
            self.carrot_timer = self.font1.render(str(int(pygame.time.get_ticks() - self.timer.start_time) / 1000), False, 'White')

        self.text_carrot = self.carrot_timer.get_rect(
            topleft =(20, settings.SCREEN_HEIGHT - 60))

        pygame.draw.rect(self.screen, 'Black',
                         self.text_carrot.inflate(10, 10), 0, 4)
        self.screen.blit(self.carrot_timer, self.text_carrot)
        #print(settings.carrots)
        #pygame.display.update()

    def settings(self):
        print('settings')
        print(settings.usage)
        self.select = False

        pass
    def goals(self):
        print('goals')
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
        print('shop')
        self.select = False
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
            if event.type == KEYDOWN:

                if event.key == K_RIGHT:
                    x = self.currentpos.pop()
                    self.currentpos.insert(0,x)

                if event.key == K_LEFT:
                    y = self.currentpos.pop(0)
                    self.currentpos.insert(len(self.currentpos),y)

                if event.key == K_e:
                    self.select = True

                if event.key == K_ESCAPE:
                    pygame.quit()




