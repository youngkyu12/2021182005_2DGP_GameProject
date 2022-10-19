from pico2d import *
import os

path = os.getcwd() + "\Resource"
os.chdir(path)


Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600


def handle_events():
    global running
    global x
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

open_canvas(Width, Height)
background = load_image("Background_finalexam_1024x600.png")
character = load_image('Move_Right.png')

running = True
x = 800 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    background.draw(Width // 2, bg_Height // 2 + 120)
    character.clip_draw(frame * 82, 0, 82, 96, x, 180)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 6
    x += dir * 5
    delay(0.05)

close_canvas()

