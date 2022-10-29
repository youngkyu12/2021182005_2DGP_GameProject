import main_state
import game_framework
from pico2d import *

#running = True
image = None
logo_time = 0.0
Width, Height = 1280, 720

def enter():
    global image
    image = load_image('logo_image.png')

def exit():
    global image
    del image

def update():
    global logo_time
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(main_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    clear_canvas()
    image.draw(Width // 2, Height // 2)
    update_canvas()

def handle_events():
    events = get_events()

def pause():
    pass

def resume():
    pass



