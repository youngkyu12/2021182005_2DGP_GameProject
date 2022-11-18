from pico2d import *
import game_framework
import game_world
import esc_state
import shop_state

from character import Character
from background import Background
from enemy import *
from task import *


Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(esc_state)
        else:
            character.handle_events(event)


character = None
back = None
enemies1 = []
enemies2 = []
task1 = []
task2 = []
def init():
    global character, back, enemies1, enemies2, task1, task2
    character = None
    back = None
    enemies1 = []
    enemies2 = []
    task1 = []
    task2 = []


def enter():
    global character, back, enemies1, enemies2, task1, task2
    character = Character()
    enemies1.append(Enemy1())
    enemies2.append(Enemy2())
    task1.append(Task1())
    task2.append(Task2())
    game_framework.World_time = 5.0
    # game_framework.World_time = 1.0   # test
    back = Background()
    game_world.add_object(character, 1)
    game_world.add_object(back, 0)
    obj()
    collide_data()

def collide_data():
    game_world.add_collision_pairs(character, enemies1, 'character:enemy1')
    game_world.add_collision_pairs(character, enemies2, 'character:enemy2')
    game_world.add_collision_pairs(character, task1, 'character:task1')
    game_world.add_collision_pairs(character, task2, 'character:task2')
    game_world.add_collision_pairs(back, enemies1, 'floor:enemy1')
    game_world.add_collision_pairs(back, enemies2, 'floor:enemy2')
    game_world.add_collision_pairs(back, task1, 'floor:task1')
    game_world.add_collision_pairs(back, task2, 'floor:task2')


def obj():
    game_world.add_objects(enemies1, 1)
    game_world.add_objects(enemies2, 1)
    game_world.add_objects(task1, 1)
    game_world.add_objects(task2, 1)


def exit():
    print('main_state exit')
    game_world.clear()

def update():
    # global enemies1, one
    for game_object in game_world.all_objects():
        game_object.update()
    if game_framework.World_time < 0.0:
        game_framework.change_state(shop_state)
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION')
            a.handle_collision(b, group)
            b.handle_collision(a, group)
    # for game_object in game_world.all_add_object():
    #     if time:
    #
    # if enemies1[0].y == 600:
    #     enemies1.append(Enemy1())
    #     game_world.add_object(enemies1[1], 1)

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def pause():
    for game_object in game_world.all_objects():
        game_object.pause()
    pass

def resume():
    for game_object in game_world.all_objects():
        game_object.resume()
    pass

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True



# test
def test_self():
    import main_state
    import os

    path = os.getcwd() + "\Resource"
    os.chdir(path)
    hide_cursor()

    open_canvas(Width, Height)
    game_framework.run(main_state)
    close_canvas()

if __name__ == '__main__':
    test_self()