from introduction import Introduction
from home import Home
import settings
class Event:
    def __init__(self):
        self.homes = True
        self.intro = settings.intro
        self.introduction = Introduction()
        self.home = Home()

    def introductions(self):
        if settings.intro:
            self.introduction.setup()

        elif settings.home:
            self.home.start()

    def home(self):
       # print('progress')
        self.homes = True
        self.home.start()

