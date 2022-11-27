from pico2d import *
import game_world
from random import randint

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
PPT_SPEED_KMPH = 8.0   # Km / Hour
PPT_SPEED_MPM = (PPT_SPEED_KMPH * 1000.0 / 60.0)
PPT_SPEED_MPS = (PPT_SPEED_MPM / 60.0)
PPT_SPEED_PPS = (PPT_SPEED_MPS * PIXEL_PER_METER)


# 상속 관계를 만들자
class Task_ppt:
    def __init__(self):
        self.x, self.y = randint(16, Width - 16), Height - 16
        self.task_ppt = load_image("target_1_32x32.png")

    def update(self):
        self.y -= 1
        if self.y < Height - bg_Height + 16 - 20:
            game_world.remove_object(self)

    def draw(self):
        self.task_ppt.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'character:task_ppt' or group == 'floor:task_ppt':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


REPORT_SPEED_KMPH = 5.0   # Km / Hour
REPORT_SPEED_MPM = (REPORT_SPEED_KMPH * 1000.0 / 60.0)
REPORT_SPEED_MPS = (REPORT_SPEED_MPM / 60.0)
REPORT_SPEED_PPS = (REPORT_SPEED_MPS * PIXEL_PER_METER)

class Task_report:
    def __init__(self):
        self.x, self.y = randint(16, Width - 16), Height - 16
        self.task_report = load_image("target_2_32x32.png")

    def update(self):
        self.y -= 1
        if self.y < Height - bg_Height + 16 - 20:
            game_world.remove_object(self)

    def draw(self):
        self.task_report.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'character:task_report' or group == 'floor:task_report':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16
