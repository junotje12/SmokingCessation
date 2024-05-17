from introduction import Introduction
class Event:
    def __init__(self):
        self.homes = True
        self.intro = False
        self.introduction = Introduction()

    def introductions(self):
        self.intro = True
        self.introduction.setup()


    def home(self):
       # print('progress')
        self.homes = False
