from pico2d import *
import game_world
import game_framework
from background import *
import main_state
from random import randint

# 변수 이름을 의미를 파악하기 힘든 숫자를 쓰지 않기

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm


class Enemy:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed


    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.draw(sx, sy)

    def update(self):
        self.y -= self.speed * game_framework.frame_time

    def pause(self):
        pass

    def resume(self):
        pass

    def get_bb(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        return sx - 16, sy - 16, sx + 16, sy + 16

class Bug(Enemy):
    BUG_SPEED_KMPH = 5.0  # Km / Hour
    BUG_SPEED_MPM = (BUG_SPEED_KMPH * 1000.0 / 60.0)
    BUG_SPEED_MPS = (BUG_SPEED_MPM / 60.0)
    BUG_SPEED_PPS = (BUG_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        super().__init__(randint(16, server.background.w - 16),   # x
                         server.background.h - 16,  # y
                         load_image("Bug_Enemy32x32.png"),     # image
                         Bug.BUG_SPEED_PPS)    # speed

    def handle_collision(self, other, group):
        if group == 'character:enemy_bug':
            if not life[0]:
                life[0] = True
            elif not life[1]:
                life[1] = True
            elif not life[2]:
                life[2] = True
            game_world.remove_object(self)
        if group == 'floor:enemy_bug':
            game_world.remove_object(self)


class Soju(Enemy):
    SOJU_SPEED_KMPH = 8.0  # Km / Hour
    SOJU_SPEED_MPM = (SOJU_SPEED_KMPH * 1000.0 / 60.0)
    SOJU_SPEED_MPS = (SOJU_SPEED_MPM / 60.0)
    SOJU_SPEED_PPS = (SOJU_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        super().__init__(randint(16, server.background.w - 16),   # x
                         server.background.h - 16,  # y
                         load_image("Soju_Enemy32x32.png"),    # image
                         Soju.SOJU_SPEED_PPS)   # speed

    def handle_collision(self, other, group):
        if group == 'character:enemy_soju':
            if not life[0]:
                life[0] = True
            elif not life[1]:
                life[1] = True
            elif not life[2]:
                life[2] = True
            game_world.remove_object(self)
        if group == 'floor:enemy_soju':
            game_world.remove_object(self)
