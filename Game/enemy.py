from pico2d import *
import game_framework
from random import randint

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Enemy:
    def __init__(self):
        self.x, self.y = randint(1280 - 128 - 1024 + 32, 1280 - 128 - 32), 720 - 32
        self.Bug = load_image("Bug_Enemy.png")
        # self.soju = load_image()
        self.Bug_num = 1

    def update(self):
        self.y -= 1

    def draw(self):
        if self.y >= 720 - 600:
            self.Bug.draw(self.x, self.y)


enemy = None

def enter():
    global enemy
    enemy = Enemy()

def exit():
    global enemy
    del enemy

def handle_events():
    pass

def update():
    enemy.update()

def draw():
    enemy.draw()
