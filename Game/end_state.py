import game_world
import main_state
import game_framework
from pico2d import *
import background
import start_state

Width, Height = 1280, 720
end_background = None

def enter():
    global end_background
    end_background = background.End_background()
    game_world.add_object(end_background, 0)
    pass

def exit():
    game_world.clear()
    pass

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
        elif event.type == SDL_KEYDOWN:
            for i in range(4):
                main_state.stage[i] = False
            main_state.stage[0] = True
            game_framework.change_state(start_state)


def pause():
    pass

def resume():
    pass



