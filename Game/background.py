from pico2d import *
import main_state
import game_framework
import server

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600


backpack = []
life = [False, False, False]
task = []
gauge = 0.0
gauge_speed = 4.0
money = 0
shield_switch = False
task_clear_switch = False
item_backpack = []
#출돌처리 이후 상호작용 클래스 만들어보자

class Background:
    # background_1024x600 = None
    background = None
    floor = None
    hart = None
    hart_minus = None
    font_item = None
    font_time = None
    item_box = None
    money = None
    font_task = None
    task_box = None
    task_gauge = None
    gauge_mask = None
    report = None
    ppt = None
    font_money = None

    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        # if Background.background_1024x600 == None:
        #     Background.background_1024x600 = load_image('Background_finalexam_1024x600.png')
        if Background.background == None:
            Background.background = load_image('Cherry_Blossom_image.png')
        if Background.floor == None:
            Background.floor = load_image('Cherry_Blossom_floor_1280x100.png')
        if Background.hart == None:
            Background.hart = load_image('Hart.png')
        if Background.hart_minus == None:
            Background.hart_minus = load_image('Hart_Minus.png')
        if Background.font_item == None:
            Background.font_item = load_font('ENCR10B.TTF', 21)
        if Background.font_time == None:
            Background.font_time = load_font('ENCR10B.TTF', 25)
        if Background.item_box == None:
            Background.item_box = load_image('ItemBox.png')
        if Background.money == None:
            Background.money = load_image('Knowledge_image_32x32.png')
        if Background.task_box == None:
            Background.task_box = load_image('ItemBox_32x32.png')
        if Background.task_gauge == None:
            Background.task_gauge = load_image('gauge_bar.png')
        if Background.gauge_mask == None:
            Background.gauge_mask = load_image('gauge_mask.png')
        if Background.ppt == None:
            Background.ppt = load_image("target_1_32x32.png")
        if Background.report == None:
            Background.report = load_image("target_2_32x32.png")
        if Background.font_money == None:
            Background.font_money = load_font('ENCR10B.TTF', 21)

        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 1280
        self.h = 720
        self.window_left = 0
        self.window_bottom = 0

    def draw(self):
        self.background.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0)

        # self.background.draw(Width // 2, Height // 2)
        self.floor.draw(Width // 2, Height - bg_Height - 70)
        self.hart.draw(21, Height - 21)
        self.hart.draw(21 + 42 + 1, Height - 21)
        self.hart.draw(64 + 42 + 1, Height - 21)
        self.money.draw(16, Height - 21 - 64)
        self.font_money.draw(16 + 30, Height - 21 - 64, f'{money}', (0, 0, 255))
        self.font_time.draw(Width // 2 - 30, Height - 20, "Timer", (0, 255, 0))
        self.font_time.draw(Width // 2 + 50, Height - 20, f"{game_framework.World_time:.0f}", (0, 255, 0))
        self.font_item.draw(15, Height - bg_Height - 70, "Item", (0, 0, 0))
        self.item_box.draw(115, Height - bg_Height - 70)
        self.task_gauge.draw(Width - 250 + int(gauge), Height - 600 - 60)
        self.gauge_mask.draw(Width - 250, Height - 600 - 60)
        self.task_box.draw(Width - 196, Height - 600 - 60)
        if task:
            if task[0] == 'report':
                self.report.draw(Width - 196, Height - 600 - 60)
            if task[0] == 'ppt':
                self.ppt.draw(Width - 196, Height - 600 - 60)
        draw_rectangle(Width - 170, Height - 600 - 44, Width - 10, Height - 600 - 76)

        if life[0]:
            self.hart_minus.draw(21, Height - 21)
        if life[1]:
            self.hart_minus.draw(21 + 42 + 1, Height - 21)
        if life[2]:
            self.hart_minus.draw(64 + 42 + 1, Height - 21)

    def update(self):
        self.window_left = clamp(0,
                                 int(server.character.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.character.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)

        global task, backpack, gauge, gauge_speed, money
        gauge = game_framework.task_time * gauge_speed
        if backpack and not task:
            task.append(backpack.pop(-1))
        if gauge > 160.0 and task:
            game_framework.task_time = 0.0
            if task:
                if task[0] == 'report':
                    money += 100
                if task[0] == 'ppt':
                    money += 200
            task.pop()

    def get_bb(self):
        return 0, 0, 1600 - 1, 100

    def handle_collision(self, other, group):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

class Shop_Background:
    shop_image = None
    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if Shop_Background.shop_image == None:
            Shop_Background.shop_image = load_image("shop_image.png")

        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = Shop_Background.shop_image.w
        self.h = Shop_Background.shop_image.h
        self.window_left, self.window_bottom = 0, 0

    def update(self):
        self.window_left = clamp(0,
                                 int(server.character.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.character.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)

    def draw(self):
        self.shop_image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0)



    def pause(self):
        pass

    def resume(self):
        pass

class Esc_Background:
    esc_image = None
    pause_font = None
    continue_font = None
    exit_font = None
    retry_font = None

    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if Esc_Background.esc_image == None:
            Esc_Background.esc_image = load_image("esc_image.png")
        if Esc_Background.pause_font == None:
            Esc_Background.pause_font = load_font('ENCR10B.TTF', 30)
        if Esc_Background.continue_font == None:
            Esc_Background.continue_font = load_font('ENCR10B.TTF', 21)
        if Esc_Background.exit_font == None:
            Esc_Background.exit_font = load_font('ENCR10B.TTF', 21)
        if Esc_Background.retry_font == None:
            Esc_Background.retry_font = load_font('ENCR10B.TTF', 21)

    def update(self):
        pass

    def draw(self):
        self.esc_image.draw(Width // 2, Height // 2)
        self.pause_font.draw(Width // 2 - 50, Height // 2 + 70, "Pause", (255, 0, 0))
        self.continue_font.draw(Width // 2 - 50, Height // 2 + 20, "Continue", (0, 0, 0))
        self.retry_font.draw(Width // 2 - 50, Height // 2 - 30, "Retry", (0, 0, 0))
        self.exit_font.draw(Width // 2 - 50, Height // 2 - 80, "Exit", (0, 0, 0))

    def pause(self):
        pass

    def resume(self):
        pass
class Exam_background(Background):
    # background_1024x600 = None
    background = None
    floor = None
    gauge_mask = None
    warning = None
    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        super().__init__()
        if Exam_background.background == None:
            Exam_background.background = load_image('hell_1680x720.png')
        if Exam_background.floor == None:
            Exam_background.floor = load_image('hell_floor_1280x100.png')
        if Exam_background.gauge_mask == None:
            Exam_background.gauge_mask = load_image('gauge_mask_hell.png')
        if Exam_background.warning == None:
            Exam_background.warning = load_image('DeadLine_Warning.png')

        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = Exam_background.background.w
        self.h = Exam_background.background.h
        self.window_left, self.window_bottom = 0, 0

    def draw(self):
        self.background.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0)

        self.floor.draw(self.w // 2 - self.window_left // 2, self.window_bottom + 50)
        self.hart.draw(21, Height - 21)
        self.hart.draw(21 + 42 + 1, Height - 21)
        self.hart.draw(64 + 42 + 1, Height - 21)
        self.money.draw(16, Height - 21 - 64)
        self.font_money.draw(16 + 30, Height - 21 - 64, f'{money}', (0, 0, 255))
        self.font_time.draw(Width // 2 - 30, Height - 20, "Timer", (0, 255, 0))
        self.font_time.draw(Width // 2 + 50, Height - 20, f"{game_framework.World_time:.0f}", (0, 255, 0))
        self.font_item.draw(15, Height - bg_Height - 70, "Item", (0, 0, 0))
        self.item_box.draw(115, Height - bg_Height - 70)
        self.task_gauge.draw(Width - 250 + int(gauge), Height - 600 - 60)
        self.gauge_mask.draw(Width - 250, Height - 600 - 60)
        self.task_box.draw(Width - 196, Height - 600 - 60)
        if task:
            if task[0] == 'report':
                self.report.draw(Width - 196, Height - 600 - 60)
            if task[0] == 'ppt':
                self.ppt.draw(Width - 196, Height - 600 - 60)
        draw_rectangle(Width - 170, Height - 600 - 44, Width - 10, Height - 600 - 76)

        if life[0]:
            self.hart_minus.draw(21, Height - 21)
        if life[1]:
            self.hart_minus.draw(21 + 42 + 1, Height - 21)
        if life[2]:
            self.hart_minus.draw(64 + 42 + 1, Height - 21)

    def update(self):
        self.window_left = clamp(0,
                                 int(server.character.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.character.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)
        global task, backpack, gauge, gauge_speed, money
        gauge = game_framework.task_time * gauge_speed
        if backpack and not task:
            task.append(backpack.pop(-1))
        if gauge > 160.0 and task:
            game_framework.task_time = 0.0
            if task:
                if task[0] == 'report':
                    money += 100
                if task[0] == 'ppt':
                    money += 200
            task.pop()


    def get_bb(self):
        return 0, 0, 1600 - 1, 100
    def handle_collision(self, other, group):
        super().handle_collision(other, group)

    def pause(self):
        super().pause()

    def resume(self):
        super().resume()

class End_background:
    a_end = None
    b_end = None
    c_end = None
    f_end = None

    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if End_background.a_end == None:
            End_background.a_end = load_image('A_end.png')
        if End_background.b_end == None:
            End_background.b_end = load_image('B_end.png')
        if End_background.c_end == None:
            End_background.c_end = load_image('C_end.png')
        if End_background.f_end == None:
            End_background.f_end = load_image('F_end.png')
        self.x, self.y = Width // 2, Height // 2

    def update(self):
        pass

    def draw(self):
        if main_state.stage[3]:
            self.a_end.draw(self.x, self.y)
        elif main_state.stage[2]:
            self.b_end.draw(self.x, self.y)
        elif main_state.stage[1]:
            self.c_end.draw(self.x, self.y)
        elif main_state.stage[0]:
            self.f_end.draw(self.x, self.y)

    def pause(self):
        pass

    def resume(self):
        pass
