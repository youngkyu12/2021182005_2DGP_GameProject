from pico2d import *
import game_world
import game_framework
import main_state
from random import randint



# 변수 이름을 의미를 파악하기 힘든 숫자를 쓰지 않기

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600


PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
BUG_SPEED_KMPH = 5.0   # Km / Hour
BUG_SPEED_MPM = (BUG_SPEED_KMPH * 1000.0 / 60.0)
BUG_SPEED_MPS = (BUG_SPEED_MPM / 60.0)
BUG_SPEED_PPS = (BUG_SPEED_MPS * PIXEL_PER_METER)

class Enemy_bug:
    def __init__(self):
        self.x, self.y = randint(16, Width - 16), Height - 16
        self.Bug = load_image("Bug_Enemy32x32.png")
        self.t = 0

    def update(self):
        self.y -= BUG_SPEED_PPS * game_framework.frame_time
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
        if group == 'character:enemy_bug' or group == 'floor:enemy_bug':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

SOJU_SPEED_KMPH = 8.0   # Km / Hour
SOJU_SPEED_MPM = (SOJU_SPEED_KMPH * 1000.0 / 60.0)
SOJU_SPEED_MPS = (SOJU_SPEED_MPM / 60.0)
SOJU_SPEED_PPS = (SOJU_SPEED_MPS * PIXEL_PER_METER)

class Enemy_soju:
    def __init__(self):
        self.x, self.y = randint(16, Width - 16), Height - 16
        self.Soju = load_image("Soju_Enemy32x32.png")

    def update(self):
        self.y -= SOJU_SPEED_PPS * game_framework.frame_time
        if self.y < Height - bg_Height + 16 - 20:
            game_world.remove_object(self)

    def draw(self):
        self.Soju.draw(self.x, self.y)
        # self.Soju.opacify(int(255*255.0)) # 임시 알파값 적용 (투명하게)
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'character:enemy_soju' or group == 'floor:enemy_soju':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


