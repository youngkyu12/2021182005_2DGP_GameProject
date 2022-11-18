from pico2d import *
import game_world
import main_state
from random import randint


Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Enemy1:
    def __init__(self):
        self.x, self.y = randint(16, Width - 16), Height - 16
        self.Bug = load_image("Bug_Enemy32x32.png")
        self.t = 0

    def update(self):
        self.y -= 1
        if self.y < Height - bg_Height + 16 - 20:
            game_world.remove_object(self)


    def draw(self):
        self.Bug.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'character:enemy1' or group == 'floor:enemy1':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class Enemy2:
    def __init__(self):
        self.x, self.y = randint(16, Width - 16), Height - 16
        self.Soju = load_image("Soju_Enemy32x32.png")

    def update(self):
        self.y -= 1
        if self.y < Height - bg_Height + 16 - 20:
            game_world.remove_object(self)

    def draw(self):
        self.Soju.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'character:enemy2' or group == 'floor:enemy2':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16
