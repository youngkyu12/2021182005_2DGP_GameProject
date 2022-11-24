import main_state
import game_framework
import game_world
import esc_state
from pico2d import *

from character import Character
from background import Shop_Background
from item import *

Width, Height = 1280, 720

character = None
image = None
item_task_clear = None
item_hart_plus = None
item_shield = None

def enter():
    global image, character, item_task_clear, item_hart_plus, item_shield
    character = Character()
    image = Shop_Background()
    item_task_clear = Item_task_clear()
    item_hart_plus = Item_hart_plus()
    item_shield = Item_shield()
    game_world.add_object(character, 1)
    game_world.add_object(image, 0)
    game_world.add_object(item_task_clear, 0)
    game_world.add_object(item_hart_plus, 0)
    game_world.add_object(item_shield, 0)

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(esc_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            game_framework.change_state(main_state)
        else:
            character.handle_events(event)


def pause():
    pass

def resume():
    pass

def test_self():
    import shop_state
    import os

    path = os.getcwd() + "\Resource"
    os.chdir(path)
    hide_cursor()

    open_canvas(Width, Height)
    game_framework.run(shop_state)
    close_canvas()

if __name__ == '__main__':
    test_self()


