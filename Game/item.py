from pico2d import *
import game_world
import main_state

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
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        # self.hart_plus.opacify(int(255*255.0)) # 임시 투명 적용
        pass

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
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        # self.task_clear.opacify(int(255*255.0)) # 임시 투명 적용
        pass

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
        draw_rectangle(*self.get_bb())

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_collision(self, other, group):
        # self.hart_plus.opacify(int(255*255.0)) # 임시 투명 적용
        pass

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

