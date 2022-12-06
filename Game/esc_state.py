import game_world
import main_state
import game_framework
import shop_state
from pico2d import *
from character import *
import background
import server

esc_image = None
pause_font = None
continue_font = None
retry_font = None
exit_font = None
Key_check = None
Width, Height = 1280, 720

Box = [(Width // 2 - 50, Height // 2 + 30, Width // 2 + 60, Height // 2 + 10),
       (Width // 2 - 50, Height // 2 - 20, Width // 2 + 15, Height // 2 - 40),
       (Width // 2 - 50, Height // 2 - 70, Width // 2, Height // 2 - 90)]
box_num = 0

esc_bg = None

def enter():
    print('esc_state enter')
    global esc_bg
    esc_bg = background.Esc_Background()

def exit():
    print('esc_state exit')
    global esc_bg
    del esc_bg

def update():
    pass

def draw():
    global box_num
    clear_canvas()
    if server.background:
        main_state.draw_world()
    if shop_state.image:
        shop_state.draw_world()
    esc_bg.draw()
    draw_rectangle(*Box[box_num])
    update_canvas()

def handle_events():
    global box_num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            server.character.add_event(RU)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            server.character.add_event(RD)
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            server.character.add_event(LU)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            server.character.add_event(LD)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            box_num -= 1
            if box_num < 0:
                box_num += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            box_num += 1
            if box_num > 2:
                box_num -= 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            if box_num == 0:
                game_framework.pop_state()
                pass
            elif box_num == 1:
                game_world.clear()
                server.character = None
                server.background = None
                server.enemies_bug = []
                server.enemies_soju = []
                server.tasks_ppt = []
                server.tasks_report = []
                background.backpack = []
                background.life = [False, False, False]
                background.task_clear = 10.0
                background.task = []
                background.gauge = 0.0
                background.gauge_speed = 4.0
                main_state.init()
                game_framework.change_state(main_state)
                pass
            elif box_num == 2:
                game_framework.quit()
                pass

def pause():
    # print('esc_state pause')
    pass

def resume():
    # print('esc_state resume')
    pass



