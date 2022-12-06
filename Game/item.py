from pico2d import *

import game_framework
import game_world
import main_state
import background
# 변수 이름을 의미를 파악하기 힘든 숫자를 쓰지 않기

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Item_shield:
    def __init__(self):
        self.x, self.y = Width // 2, Height // 2
        self.Shield = load_image("shield_image_32x32.png")
        self.t = 0

    def update(self):
        pass

    def draw(self):
        self.Shield.draw(self.x, self.y)

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'mouse::item_shield':
            # print('shield')
            background.shield_switch = True
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class Item_task_clear:
    def __init__(self):
        self.x, self.y = Width // 2 + 200, Height // 2
        self.task_clear = load_image("task_clear_32x32.png")

    def update(self):
        pass

    def draw(self):
        self.task_clear.draw(self.x, self.y)

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'mouse::item_task_clear':
            # print('task_clear')
            background.task_clear_switch = True
            while background.backpack:
                if background.backpack.pop() == 'report':
                    background.money += 100
                elif background.backpack.pop() == 'ppt':
                    background.money += 200
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class Item_hart_plus:
    def __init__(self):
        self.x, self.y = Width // 2 - 200, Height // 2
        self.hart_plus = load_image("hart_plus_32x32.png")

    def update(self):
        pass

    def draw(self):
        self.hart_plus.draw(self.x, self.y)

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'mouse::item_hart':
            # print('hart')
            for i in range(3):
                if background.life[i]:
                    background.life[i] = False
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class Door:
    def __init__(self):
        self.x, self.y = Width - 128, Height - bg_Height + 64
        self.door = load_image("door.png")

    def update(self):
        pass

    def draw(self):
        self.door.draw(self.x, self.y)

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        if group == 'mouse::door':
            game_framework.change_state(main_state)

    def get_bb(self):
        return self.x - 32, self.y - 32, self.x + 32, self.y + 32

