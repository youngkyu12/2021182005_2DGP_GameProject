import pico2d.pico2d
from pico2d import *
import game_framework
import game_world
import esc_state
import shop_state

from character import Character
from background import Background
from enemy import *
from task import *

# 변수에 의미 없는 숫자 넣지 말고 의미를 담는 단어를 사용
# 함수는 소문자, 클래스는 첫글자 대문자

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
enemy_bug = []
enemy_soju = []
task_ppt = []
task_report = []
def init():
    global character, back, enemy_bug, enemy_soju, task_ppt, task_report
    character = None
    back = None
    enemy_bug = []
    enemy_soju = []
    task_ppt = []
    task_report = []


def enter():
    global character, back, enemy_bug, enemy_soju, task_ppt, task_report
    character = Character()
    enemy_bug.append(Enemy_bug())
    enemy_soju.append(Enemy_soju())
    task_ppt.append(Task_ppt())
    task_report.append(Task_report())
    game_framework.World_time = 2.0
    # game_framework.World_time = 1.0   # test
    back = Background()
    game_world.add_object(character, 1)
    game_world.add_object(back, 0)
    obj()
    collide_data()

def collide_data():
    game_world.add_collision_pairs(character, enemy_bug, 'character:enemy_bug')
    game_world.add_collision_pairs(character, enemy_soju, 'character:enemy_soju')
    game_world.add_collision_pairs(character, task_ppt, 'character:task_ppt')
    game_world.add_collision_pairs(character, task_ppt, 'character:task_report')
    game_world.add_collision_pairs(back, enemy_bug, 'floor:enemy_bug')
    game_world.add_collision_pairs(back, enemy_soju, 'floor:enemy_soju')
    game_world.add_collision_pairs(back, task_ppt, 'floor:task_ppt')
    game_world.add_collision_pairs(back, task_report, 'floor:task_report')


def obj():
    game_world.add_objects(enemy_bug, 1)
    game_world.add_objects(enemy_soju, 1)
    game_world.add_objects(task_ppt, 1)
    game_world.add_objects(task_report, 1)


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

    # 연속적인 오브젝트 찍기 이때 시간을 기준으로 찍는 것이 좋을 것 같음 객체를 여기서 찍는게 아니라 Class안에서 찍게 해보자
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