import main_state
import game_framework
from pico2d import *

image = None
Width, Height = 1280, 720

def enter():
    global image
    image = load_image('start_image.png')

def exit():
    global image
    del image

def update():
    pass

def draw():
    clear_canvas()
    image.draw(Width // 2, Height // 2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.change_state(main_state)

def pause():
    pass

def resume():
    pass



