from pico2d import *

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600
class Background:
    background = None
    hart = None
    font_item = None
    font_score = None
    ItemBox = None
    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if Background.background == None:
            Background.background = load_image('Background_finalexam_1024x600.png')
        if Background.hart == None:
            Background.hart = load_image('Hart.png')
        if Background.font_item == None:
            Background.font_item = load_font('ENCR10B.TTF', 21)
        if Background.font_score == None:
            Background.font_score = load_font('ENCR10B.TTF', 15)
        if Background.ItemBox == None:
            Background.ItemBox = load_image('ItemBox.png')

    def draw(self):
        self.hart.draw(21, 720 - 21)
        self.hart.draw(21 + 42 + 1, 720 - 21)
        self.hart.draw(64 + 42 + 1, 720 - 21)
        self.background.draw(Width // 2, bg_Height // 2 + 120)
        self.font_score.draw(1280 - 130, 720 - 10, "TargetScore", (0, 0, 0))
        self.font_score.draw(1280 - 130, 720 - 40, "MyScore", (0, 0, 0))
        self.font_item.draw(1280 - 1024 - 130, 720 - 600 - 10 - 16, "Item", (0, 0, 0))
        self.ItemBox.draw(1280 - 1024 - 130 + 90, 720 - 600 - 32)

