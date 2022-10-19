from pico2d import *
import game_framework
import os

path = os.getcwd() + "\Resource"
os.chdir(path)

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
            self.background = load_image('Background_finalexam_1024x600.png')
        if Background.hart == None:
            self.hart = load_image('Hart.png')
        if Background.font_item == None:
            self.font_item = load_font('ENCR10B.TTF', 21)
        if Background.font_score == None:
            self.font_score = load_font('ENCR10B.TTF', 15)
        if Background.ItemBox == None:
            self.ItemBox = load_image('ItemBox.png')

    def draw(self):
        self.hart.draw(21, 720 - 21)
        self.hart.draw(21 + 42 + 1, 720 - 21)
        self.hart.draw(64 + 42 + 1, 720 - 21)
        self.background.draw(Width // 2, bg_Height // 2 + 120)
        self.font_score.draw(1280 - 130, 720 - 10, "TargetScore", (0, 0, 0))
        self.font_score.draw(1280 - 130, 720 - 40, "MyScore", (0, 0, 0))
        self.font_item.draw(1280 - 1024 - 130, 720 - 600 - 10 - 16, "Item", (0, 0, 0))
        self.ItemBox.draw(1280 - 1024 - 130 + 90, 720 - 600 - 32)

class Enmey:
    def __init__(self):
        self.Bug = load_image("Bug_Enemy.png")
        # self.soju = load_image()

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
        if self.x < 1280 - 1024 - 128:
            self.x -= self.dir_x * 5
        elif self.x > 1280 - 128:
            self.x -= self.dir_x * 5

    def draw(self):
        Character.image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)

class Object:
    def __init__(self):
        self.image = load_image('target_1_32x32.png')
        self.x = Width // 2
        self.y = Height // 2
        self.t = 0
        self.xl, self.yl = 1280 - 1024 - 128, 720 - 600 + 100
        self.xr, self.yr = 1280 - 128, 720 - 600 + 100
        self.i = 0
        self.throw_r = False
        self.throw_l = False

    def update(self):
        self.t = self.i / 100
        if self.throw_l == True:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * character.x + (-4 * self.t ** 2 + 4 * self.t) * (character.x -((character.x - self.xl) // 2)) + (2 * self.t ** 2 - self.t) * self.xl
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * character.y + (-4 * self.t ** 2 + 4 * self.t) * (character.y + 100) + (2 * self.t ** 2 - self.t) * self.yl
        elif self.throw_r == True:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * character.x + (-4 * self.t ** 2 + 4 * self.t) * (character.x + ((self.xr - character.x) // 2)) + (2 * self.t ** 2 - self.t) * self.xr
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * character.y + (-4 * self.t ** 2 + 4 * self.t) * (character.y + 100) + (2 * self.t ** 2 - self.t) * self.yr

        self.i += 4
        if self.i > 100:
            self.i = 0
            self.throw_r = False
            self.throw_l = False

    def draw(self):
        self.image.draw(self.x, self. y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                close_canvas()
            elif event.key == SDLK_LEFT:
                character.dir_x -= 1
                character.animation = 5
            elif event.key == SDLK_RIGHT:
                character.dir_x += 1
                character.animation = 4
            elif event.key == SDLK_UP:
                if character.animation == 5 or character.animation == 2:
                    character.animation = 0
                elif character.animation == 4 or character.animation == 3:
                    character.animation = 1
                if character.dir_y == 0:
                    character.dir_y += 1
            elif event.key == SDLK_SPACE:
                if character.animation == 5 or character.animation == 2:
                    object.throw_l = True
                elif character.animation == 4 or character.animation == 3:
                    object.throw_r = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                character.dir_x += 1
                character.animation = 2
            elif event.key == SDLK_RIGHT:
                character.dir_x -= 1
                character.animation = 3


Back = None
character = None
running = None
object = None
def enter():
    global Back, running, character, object
    Back = Background()
    character = Character()
    object = Object()
    running = True

def exit():
    global Back, running, character, object
    del Back
    del character
    del object
    running = False

def update():
    character.update()
    if object.throw_r == True or object.throw_l == True:
       object.update()

def draw():
    clear_canvas()
    Back.draw()
    character.draw()
    if object.throw_r == True or object.throw_l == True:
        object.draw()
    update_canvas()

open_canvas(Width, Height)
hide_lattice()
enter()

while running:
    handle_events()
    update()
    draw()
exit()
