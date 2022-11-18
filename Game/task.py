from pico2d import *
import game_world
from random import randint

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Task1:
    def __init__(self):
        self.x, self.y = randint(16, Width - 16), Height - 16
        self.task1 = load_image("target_1_32x32.png")

    def update(self):
        self.y -= 1
        if self.y < Height - bg_Height + 16 - 20:
            game_world.remove_object(self)

    def draw(self):
        self.task1.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'character:task1' or group == 'floor:task1':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class Task2:
    def __init__(self):
        self.x, self.y = randint(16, Width - 16), Height - 16
        self.task2 = load_image("target_2_32x32.png")

    def update(self):
        self.y -= 1
        if self.y < Height - bg_Height + 16 - 20:
            game_world.remove_object(self)

    def draw(self):
        self.task2.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'character:task2' or group == 'floor:task2':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16
