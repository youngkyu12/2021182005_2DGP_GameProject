from pico2d import *
import game_framework

import character
import background
import object_throw
import enemy

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
    background.handle_events()
    character.handle_events()
    object_throw.handle_events()



def enter():
    background.enter()
    character.enter()
    object_throw.enter()
    enemy.enter()
    running = True

def exit():
    background.exit()
    character.exit()
    object_throw.exit()
    enemy.exit()
    running = False

def update():
    character.update()
    object_throw.update()
    enemy.update()

def draw():
    clear_canvas()
    background.draw()
    character.draw()
    object_throw.draw()
    enemy.draw()
    update_canvas()

def pasue():
    pass

def resume():
    pass