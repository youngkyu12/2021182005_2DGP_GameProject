from pico2d import *
import game_world
from random import randint

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Enemy1:
    def __init__(self):
        self.x, self.y = randint(1280 - 128 - 1024 + 16, 1280 - 128 - 16), 720 - 16
        self.Bug = load_image("Bug_Enemy32x32.png")

    def update(self):
        self.y -= 1
        if self.y < 720 - 600 + 16:
            game_world.remove_object(self)
    def draw(self):
        self.Bug.draw(self.x, self.y)

class Enemy2:
    def __init__(self):
        self.x, self.y = randint(1280 - 128 - 1024 + 16, 1280 - 128 - 16), 720 - 16
        self.Soju = load_image("Soju_Enemy32x32.png")

    def update(self):
        self.y -= 1
        if self.y < 720 - 600 + 16:
            game_world.remove_object(self)

    def draw(self):
        self.Soju.draw(self.x, self.y)
