from pico2d import *

Width, Height = 1280, 720

import character


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
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * character.Character().x + (-4 * self.t ** 2 + 4 * self.t) * (character.Character().x -((character.Character().x - self.xl) // 2)) + (2 * self.t ** 2 - self.t) * self.xl
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * character.Character().y + (-4 * self.t ** 2 + 4 * self.t) * (character.Character().y + 100) + (2 * self.t ** 2 - self.t) * self.yl
        elif self.throw_r == True:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * character.Character().x + (-4 * self.t ** 2 + 4 * self.t) * (character.Character().x + ((self.xr - character.Character().x) // 2)) + (2 * self.t ** 2 - self.t) * self.xr
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * character.Character().y + (-4 * self.t ** 2 + 4 * self.t) * (character.Character().y + 100) + (2 * self.t ** 2 - self.t) * self.yr

        self.i += 4
        if self.i > 100:
            self.i = 0
            self.throw_r = False
            self.throw_l = False

    def draw(self):
        self.image.draw(self.x, self. y)

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                if character.animation == 5 or character.animation == 2:
                    self.throw_l = True
                elif character.animation == 4 or character.animation == 3:
                    self.throw_r = True

