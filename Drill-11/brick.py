import random
from pico2d import *
import game_world
import game_framework

class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y = random.randint(0, 1600-1), 300
        self.dir = 1
        self.speed = 100

    def get_bb(self):
        # fill here
        return self.x-10, self.y-10, self.x+10, self.y+10

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        if(self.x > 1600 or self.x < 0):
            self.dir = self.dir * -1

        self.x += self.dir * game_framework.frame_time * self.speed


