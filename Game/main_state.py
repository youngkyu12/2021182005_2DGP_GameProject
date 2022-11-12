from pico2d import *
import game_framework
import game_world

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
            game_framework.quit()
        else:
            character.handle_events(event)




character = None
back = None
enemies1 = None
enemies2 = None
task1 = None
task2 = None

def enter():
    global character, back, enemies1, enemies2, task1, task2
    character = Character()
    enemies1 = [Enemy1() for i in range(1)]
    enemies2 = [Enemy2() for i in range(1)]
    task1 = [Task1() for i in range(1)]
    task2 = [Task2() for i in range(1)]

    back = Background()
    game_world.add_object(character, 1)
    game_world.add_object(back, 0)
    game_world.add_objects(enemies1, 1)
    game_world.add_objects(enemies2, 1)
    game_world.add_objects(task1, 1)
    game_world.add_objects(task2, 1)

def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
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