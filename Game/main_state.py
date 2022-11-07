from pico2d import *
import game_framework
import game_world

from character import Character
from background import Background
# from enemy import Enemy

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
            # object.handle_events(event, character.animation)




character = None
# throw = None
back = None
# enemies = None
def enter():
    global character, back
    character = Character()
    # enemies = Enemy()
    back = Background()
    game_world.add_object(character, 1)
    game_world.add_object(back, 0)
    # game_world.add_object(enemies, 1)
    # running = True

def exit():
    game_world.clear()
    # global enemies, character, back
    # del enemies
    # del character
    # del back
    # running = False

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # character.update()
    # for enemy in enemies:
    #     enemy.update()
    # if throw != None:
    #     throw.update()
    # if object.throw_r or object.throw_l:
    #     object.update(character.x, character.y)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    # back.draw()
    # character.draw()
    # if throw != None:
    #     throw.draw()
    # # if object.throw_r or object.throw_l:
    # #     object.draw()
    # for enemy in enemies:
    #     enemy.draw()
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