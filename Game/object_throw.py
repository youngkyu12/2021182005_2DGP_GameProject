from pico2d import *
import os

path = os.getcwd() + "\Resource"
os.chdir(path)

Width, Height = 1280, 720



class Object:
    def __init__(self):
        self.image = load_image('target_1_32x32.png')
        self.x = Width // 2
        self.y = Height // 2
        self.t = 0
        self.x1, self.y1 = 1280 - 512 - 128, Height - 600
        self.x2, self.y2 = 1280 - 128 - 512 - 256, 720 - 600 + 150
        self.x3, self.y3 = 1280 - 1024 - 128, 720 - 600 + 100
        self.i = 0

    def update(self):
        self.t = self.i / 100
        self.x = (2 * self.t ** 2 - 3 * self.t + 1) * self.x1 + (-4 * self.t ** 2 + 4 * self.t) * self.x2 + (2 * self.t ** 2 - self.t) * self.x3
        self.y = (2 * self.t ** 2 - 3 * self.t + 1) * self.y1 + (-4 * self.t ** 2 + 4 * self.t) * self.y2 + (2 * self.t ** 2 - self.t) * self.y3
        self.i += 2
        if self.i > 100:
            self.i = 0
        delay(0.05)

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

object = None
running = None

def enter():
    global object, running
    object = Object()
    running = True

def exit():
    global object, running
    del object
    running = False

def update():
    object.update()


def draw():
    clear_canvas()
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