from pico2d import *

import background
import game_world
from random import randint
from background import *
Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm

class Task:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image

    def update(self):
        self.y -= self.speed * game_framework.frame_time

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

    def pause(self):
        pass

    def resume(self):
        pass


# 상속 관계를 만들자
class Ppt(Task):
    PPT_SPEED_KMPH = 8.0  # Km / Hour
    PPT_SPEED_MPM = (PPT_SPEED_KMPH * 1000.0 / 60.0)
    PPT_SPEED_MPS = (PPT_SPEED_MPM / 60.0)
    PPT_SPEED_PPS = (PPT_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        super().__init__(randint(16, Width - 16),
                         Height - 16,
                         Ppt.PPT_SPEED_PPS,
                         load_image("target_1_32x32.png"))

    def handle_collision(self, other, group):
        if group == 'character:task_ppt':
            backpack.insert(0, 'ppt')
            game_world.remove_object(self)

        if group == 'floor:task_ppt':
            game_world.remove_object(self)

class Report(Task):
    REPORT_SPEED_KMPH = 5.0  # Km / Hour
    REPORT_SPEED_MPM = (REPORT_SPEED_KMPH * 1000.0 / 60.0)
    REPORT_SPEED_MPS = (REPORT_SPEED_MPM / 60.0)
    REPORT_SPEED_PPS = (REPORT_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        super().__init__(randint(16, Width - 16),
                         Height - 16,
                         Ppt.PPT_SPEED_PPS,
                         load_image("target_2_32x32.png"))

    def handle_collision(self, other, group):
        if group == 'character:task_report':
            backpack.insert(0, 'report')
            game_world.remove_object(self)

        if group == 'floor:task_report':
            game_world.remove_object(self)

