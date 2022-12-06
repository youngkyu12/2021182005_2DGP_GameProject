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
mouse_pointer = None
door = None
class Mouse_point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        pass

    def draw(self):
        pass
    def handle_collision(self, other, group):
        pass
    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

def enter():
    global image, character, item_task_clear, item_hart_plus, item_shield, mouse_pointer, door
    door = Door()
    image = Shop_Background()
    item_task_clear = Item_task_clear()
    item_hart_plus = Item_hart_plus()
    item_shield = Item_shield()
    mouse_pointer = Mouse_point()
    game_world.add_object(image, 0)
    game_world.add_object(item_task_clear, 0)
    game_world.add_object(item_hart_plus, 0)
    game_world.add_object(item_shield, 0)
    game_world.add_object(mouse_pointer, 0)
    game_world.add_object(door, 0)
    game_world.add_collision_pairs(mouse_pointer, item_shield, 'mouse::item_shield')
    game_world.add_collision_pairs(mouse_pointer, item_hart_plus, 'mouse::item_hart')
    game_world.add_collision_pairs(mouse_pointer, item_task_clear, 'mouse::item_task_clear')
    game_world.add_collision_pairs(mouse_pointer, door, 'mouse::door')


def exit():
    game_world.clear()
    for i in range(4):
        if not main_state.stage[i]:
            main_state.stage[i] = True

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            # print('COLLISION')
            a.handle_collision(b, group)
            b.handle_collision(a, group)

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
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse_pointer.x, mouse_pointer.y = event.x, Height - 1 - event.y
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(esc_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            game_framework.change_state(main_state)

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

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


