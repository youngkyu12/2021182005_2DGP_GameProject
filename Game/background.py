from pico2d import *
import main_state
import game_framework

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600
class Background:
    # background_1024x600 = None
    Cherry_Blossom_1280x720 = None
    Cherry_Blossom_floor = None
    hart = None
    font_item = None
    font_time = None
    ItemBox = None
    coin = None

    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        # if Background.background_1024x600 == None:
        #     Background.background_1024x600 = load_image('Background_finalexam_1024x600.png')
        if Background.Cherry_Blossom_1280x720 == None:
            Background.Cherry_Blossom_1280x720 = load_image('Cherry_Blossom_image.png')
        if Background.Cherry_Blossom_floor == None:
            Background.Cherry_Blossom_floor = load_image('Cherry_Blossom_floor_1280x100.png')
        if Background.hart == None:
            Background.hart = load_image('Hart.png')
        if Background.font_item == None:
            Background.font_item = load_font('ENCR10B.TTF', 21)
        if Background.font_time == None:
            Background.font_time = load_font('ENCR10B.TTF', 25)
        if Background.ItemBox == None:
            Background.ItemBox = load_image('ItemBox.png')
        if Background.coin == None:
            Background.coin = load_image('Knowledge_image_32x32.png')

    def update(self):
        pass

    def draw(self):
        # self.background_1024x600.draw(Width // 2, bg_Height // 2 + 120)
        self.Cherry_Blossom_1280x720.draw(Width // 2, Height // 2)
        self.Cherry_Blossom_floor.draw(Width // 2, Height - bg_Height - 70)
        self.hart.draw(21, Height - 21)
        self.hart.draw(21 + 42 + 1, Height - 21)
        self.hart.draw(64 + 42 + 1, Height - 21)
        self.coin.draw(16, Height - 21 - 64)
        self.font_time.draw(Width // 2 - 30, Height - 10, "Timer", (0, 255, 0))
        self.font_time.draw(Width // 2 + 50, Height - 10, f"{game_framework.World_time:.0f}", (0, 255, 0))
        self.font_item.draw(15, Height - bg_Height - 70, "Item", (0, 0, 0))
        self.ItemBox.draw(115, Height - bg_Height - 70)
        draw_rectangle(*self.get_bb())

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

    def update(self):
        pass

    def draw(self):
        self.shop_image.draw(Width // 2, Height // 2)

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
