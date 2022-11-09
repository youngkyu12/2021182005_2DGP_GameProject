from pico2d import *
Width, Height = 1280, 720
import game_world
class Throw:
    image = None
    def __init__(self, x = Width // 2, y = Height // 2, action = 3):
        if Throw.image == None:
            Throw.image = load_image('target_1_32x32.png')
        self.x, self.y = 0, 0
        self.cx = x
        self.cy = y
        self.action = action
        self.t = 0
        self.xl, self.yl = 1280 - 1024 - 128 - 20, 720 - 600 + 100
        self.xr, self.yr = 1280 - 128 + 20, 720 - 600 + 100
        self.i = 0


    def update(self):
        self.t = self.i / 100
        if self.action == 0 or self.action == 2 or self.action == 5:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.cx + (-4 * self.t ** 2 + 4 * self.t) * (self.cx -((self.cx - self.xl) // 2)) + (2 * self.t ** 2 - self.t) * self.xl
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.cy + (-4 * self.t ** 2 + 4 * self.t) * (self.cy + 100) + (2 * self.t ** 2 - self.t) * self.yl
        elif self.action == 1 or self.action == 3 or self.action == 4:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.cx + (-4 * self.t ** 2 + 4 * self.t) * (self.cx + ((self.xr - self.cx) // 2)) + (2 * self.t ** 2 - self.t) * self.xr
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.cy + (-4 * self.t ** 2 + 4 * self.t) * (self.cy + 100) + (2 * self.t ** 2 - self.t) * self.yr

        self.i += 4
        if self.i > 100:
            self.i = 0

        if self.x < 1280 - 1024 - 128 or self.x > 1280 - 128:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self. y)
