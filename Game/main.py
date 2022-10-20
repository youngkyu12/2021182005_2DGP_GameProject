from pico2d import *
import os

path = os.getcwd() + "\Resource"
os.chdir(path)

from character import Character
from background import Background
from object_throw import Object

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

Back = None
character = None
running = None
object = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                close_canvas()
            elif event.key == SDLK_LEFT:
                character.dir_x -= 1
                character.animation = 5
            elif event.key == SDLK_RIGHT:
                character.dir_x += 1
                character.animation = 4
            elif event.key == SDLK_UP:
                if character.animation == 5 or character.animation == 2:
                    character.animation = 0
                elif character.animation == 4 or character.animation == 3:
                    character.animation = 1
                if character.dir_y == 0:
                    character.dir_y += 1
            elif event.key == SDLK_SPACE:
                if character.animation == 5 or character.animation == 2:
                    object.throw_l = True
                elif character.animation == 4 or character.animation == 3:
                    object.throw_r = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                character.dir_x += 1
                character.animation = 2
            elif event.key == SDLK_RIGHT:
                character.dir_x -= 1
                character.animation = 3

def enter():
    global Back, running, character, object
    Back = Background()
    character = Character()
    object = Object()
    running = True

def exit():
    global Back, running, character, object
    del Back
    del character
    del object
    running = False

def update():
    character.update()
    if object.throw_r == True or object.throw_l == True:
       object.update()

def draw():
    clear_canvas()
    Back.draw()
    character.draw()
    if object.throw_r == True or object.throw_l == True:
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
