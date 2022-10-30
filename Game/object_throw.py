from pico2d import *

Width, Height = 1280, 720

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

    def update(self, cx, cy):
        self.t = self.i / 100
        if self.throw_l == True:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * cx + (-4 * self.t ** 2 + 4 * self.t) * (cx -((cx - self.xl) // 2)) + (2 * self.t ** 2 - self.t) * self.xl
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * cy + (-4 * self.t ** 2 + 4 * self.t) * (cy + 100) + (2 * self.t ** 2 - self.t) * self.yl
        elif self.throw_r == True:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * cx + (-4 * self.t ** 2 + 4 * self.t) * (cx + ((self.xr - cx) // 2)) + (2 * self.t ** 2 - self.t) * self.xr
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * cy + (-4 * self.t ** 2 + 4 * self.t) * (cy + 100) + (2 * self.t ** 2 - self.t) * self.yr

        self.i += 4
        if self.i > 100:
            self.i = 0
            self.throw_r = False
            self.throw_l = False

    def draw(self):
        self.image.draw(self.x, self. y)

    def handle_events(self, event, animation):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                if animation == 5 or animation == 2:
                    self.throw_l = True
                elif animation == 4 or animation == 3:
                    self.throw_r = True

