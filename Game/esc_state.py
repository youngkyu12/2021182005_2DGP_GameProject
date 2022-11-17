import main_state
import game_framework
from pico2d import *
from character import *

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
num = 0

def enter():
    print('esc_state enter')
    global esc_image, pause_font, continue_font, exit_font, retry_font
    esc_image = load_image('esc_image.png')
    pause_font = load_font('ENCR10B.TTF', 30)
    continue_font = load_font('ENCR10B.TTF', 21)
    exit_font = load_font('ENCR10B.TTF', 21)
    retry_font = load_font('ENCR10B.TTF', 21)

def exit():
    print('esc_state exit')
    global esc_image
    del esc_image


def update():
    pass

def draw():
    global num
    clear_canvas()
    main_state.draw_world()
    esc_image.draw(Width // 2, Height // 2)
    pause_font.draw(Width // 2 - 50, Height // 2 + 70, "Pause", (255, 0, 0))
    continue_font.draw(Width // 2 - 50, Height // 2 + 20, "Continue", (0, 0, 0))
    retry_font.draw(Width // 2 - 50, Height // 2 - 30, "Retry", (0, 0, 0))
    exit_font.draw(Width // 2 - 50, Height // 2 - 80, "Exit", (0, 0, 0))
    draw_rectangle(*Box[num])
    update_canvas()

def handle_events():
    global num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            main_state.character.add_event(RU)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            main_state.character.add_event(RD)
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            main_state.character.add_event(LU)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            main_state.character.add_event(LD)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            num -= 1
            if num < 0:
                num += 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            num += 1
            if num > 2:
                num -= 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            if num == 0:
                game_framework.pop_state()
                pass
            elif num == 1:
                game_world.clear()
                main_state.character = None
                main_state.back = None
                main_state.enemies1 = []
                main_state.enemies2 = []
                main_state.task1 = []
                main_state.task2 = []
                game_world.clear()
                main_state.enter()
                game_framework.pop_state()
                pass
            elif num == 2:
                game_framework.quit()
                pass

def pause():
    print('esc_state pause')
    pass

def resume():
    print('esc_state resume')
    pass



