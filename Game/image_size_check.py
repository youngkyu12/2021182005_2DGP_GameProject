from pico2d import *
import os

path = os.getcwd() + "\Resource"
os.chdir(path)


Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600
open_canvas(Width, Height)
hide_lattice()

image = load_image("Bug_enemy.png")
background = load_image("Background_finalexam_1024x600.png")

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()


while True:
    clear_canvas()
    background.draw(Width // 2, bg_Height // 2 + 120)
    image.draw(Width // 2, Height // 2)
    update_canvas()
    handle_events()

