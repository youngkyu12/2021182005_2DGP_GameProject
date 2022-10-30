from pico2d import *
import game_framework

from object_throw import Object
from character import Character
from background import Background
from enemy import Enemy

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            character.handle_events(event)
            object.handle_events(event, character.animation)




character = None
object = None
enemy = None
back = None
def enter():
    global object, enemy, character, back
    object = Object()
    character = Character()
    enemy = Enemy()
    back = Background()
    running = True

def exit():
    global object, enemy, character, back
    del object
    del enemy
    del character
    del back
    running = False

def update():
    character.update()
    if object.throw_r or object.throw_l:
        object.update(character.x, character.y)
    enemy.update()

def draw():
    clear_canvas()
    back.draw()
    character.draw()
    if (object.throw_r == True) or (object.throw_l == True):
        object.draw()
    enemy.draw()
    update_canvas()

def pasue():
    pass

def resume():
    pass

# test
def test_self():
    import main_state
    import os

    path = os.getcwd() + "\Resource"
    os.chdir(path)

    open_canvas(Width, Height)
    game_framework.run(main_state)
    close_canvas()

if __name__ == '__main__':
    test_self()