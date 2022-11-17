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

    def update(self):
        pass
    def draw(self):
        # self.background_1024x600.draw(Width // 2, bg_Height // 2 + 120)
        self.Cherry_Blossom_1280x720.draw(Width // 2, Height // 2)
        self.Cherry_Blossom_floor.draw(Width // 2, Height - bg_Height - 70)
        self.hart.draw(21, Height - 21)
        self.hart.draw(21 + 42 + 1, Height - 21)
        self.hart.draw(64 + 42 + 1, Height - 21)
        self.font_time.draw(Width // 2 - 30, Height - 10, "Timer", (0, 255, 0))
        self.font_time.draw(Width // 2 + 50, Height - 10, f"{game_framework.World_time:.0f}", (0, 255, 0))
        self.font_time.draw(Width - 130, Height - 40, "MyScore", (0, 255, 0))
        self.font_item.draw(15, Height - bg_Height - 70, "Item", (0, 0, 0))
        self.ItemBox.draw(115, Height - bg_Height - 70)

    def pause(self):
        pass

    def resume(self):
        pass
