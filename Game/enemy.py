from pico2d import *
import game_world
from random import randint


Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Enemy1:
    def __init__(self):
        self.x, self.y = randint(Width - 128 - bg_Width + 16, Width - 128 - 16), Height - 16
        self.Bug = load_image("Bug_Enemy32x32.png")
        self.t = 0

    def update(self):
        self.y -= 1
        if self.y < Height - bg_Height + 16:
            game_world.remove_object(self)


    def draw(self):
        self.Bug.draw(self.x, self.y)

class Enemy2:
    def __init__(self):
        self.x, self.y = randint(Width - 128 - bg_Width + 16, Width - 128 - 16), Height - 16
        self.Soju = load_image("Soju_Enemy32x32.png")

    def update(self):
        self.y -= 1
        if self.y < Height - bg_Height + 16:
            game_world.remove_object(self)

    def draw(self):
        self.Soju.draw(self.x, self.y)
