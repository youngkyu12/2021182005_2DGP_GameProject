from pico2d import *

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600
class Background:
    background_1024x600 = None
    # background_1280x720 = None
    hart = None
    font_item = None
    font_score = None
    ItemBox = None
    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if Background.background_1024x600 == None:
            Background.background_1024x600 = load_image('Background_finalexam_1024x600.png')
        # if Background.background_1280x720 == None:
        #     Background.background_1280x720 = load_image('Background_finalexam_1280x720.png')
        if Background.hart == None:
            Background.hart = load_image('Hart.png')
        if Background.font_item == None:
            Background.font_item = load_font('ENCR10B.TTF', 21)
        if Background.font_score == None:
            Background.font_score = load_font('ENCR10B.TTF', 15)
        if Background.ItemBox == None:
            Background.ItemBox = load_image('ItemBox.png')

    def update(self):
        pass
    def draw(self):
        self.background_1024x600.draw(Width // 2, bg_Height // 2 + 120)
        # self.background_1280x720.draw(Width // 2, Height // 2)
        self.hart.draw(21, Height - 21)
        self.hart.draw(21 + 42 + 1, Height - 21)
        self.hart.draw(64 + 42 + 1, Height - 21)
        self.font_score.draw(Width - 130, Height - 10, "TargetScore", (0, 0, 0))
        self.font_score.draw(Width - 130, Height - 40, "MyScore", (0, 0, 0))
        self.font_item.draw(Width - bg_Width - 130, Height - bg_Height - 10 - 16, "Item", (0, 0, 0))
        self.ItemBox.draw(Width - bg_Width - 130 + 90, Height - bg_Height - 32)

