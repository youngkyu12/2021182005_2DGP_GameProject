from pico2d import *
import game_world
Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Throw:
    image = None
    def __init__(self, x, y, dir):
        if Throw.image == None:
            Throw.image = load_image('target_1_32x32.png')
        self.x, self.y = 0, 0
        self.cx = x
        self.cy = y
        self.dir = dir
        self.t = 0
        self.xl, self.yl = Width - bg_Width - 128 - 20, Height - bg_Height + 100
        self.xr, self.yr = Width - 128 + 20, Height - bg_Height + 100
        self.i = 0


    def update(self):
        self.t = self.i / 100
        if self.dir == -1:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.cx + (-4 * self.t ** 2 + 4 * self.t) * (self.cx -((self.cx - self.xl) // 2)) + (2 * self.t ** 2 - self.t) * self.xl
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.cy + (-4 * self.t ** 2 + 4 * self.t) * (self.cy + 100) + (2 * self.t ** 2 - self.t) * self.yl
        elif self.dir == 1:
            self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.cx + (-4 * self.t ** 2 + 4 * self.t) * (self.cx + ((self.xr - self.cx) // 2)) + (2 * self.t ** 2 - self.t) * self.xr
            self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.cy + (-4 * self.t ** 2 + 4 * self.t) * (self.cy + 100) + (2 * self.t ** 2 - self.t) * self.yr

        self.i += 4
        if self.i > 100:
            self.i = 0

        if self.x < Width - bg_Width - 128 or self.x > Width - 128:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self. y)
