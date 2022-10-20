from pico2d import *
import game_framework


Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Character:
    image = None
    def __init__(self):
        self.x, self.y = 1280 - (1026 // 2) - 128 + 41, 720 - 600 + 48
        self.frame = 0
        self.animation = 1
        self.dir_x = 0
        self.dir_y = 0
        if Character.image == None:
            Character.image = load_image("character_anime.png")

    def update(self):
        self.x += self.dir_x * 5
        self.y += self.dir_y * 5
        if self.animation == 4 or self.animation == 5:
            self.frame = (self.frame + 1) % 5
        else:
            self.frame = 0
        if self.y > 720 - 600 + 48 + 100:
            self.dir_y -= 1
        elif self.y < 720 - 600 + 48:
            self.dir_y = 0
            if self.animation == 0:
                self.animation = 5
            elif self.animation == 1:
                self.animation = 4
    def draw(self):
        Character.image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)

