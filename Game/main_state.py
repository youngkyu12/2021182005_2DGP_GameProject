import pico2d.pico2d
from pico2d import *
import game_framework
import game_world
import esc_state
import shop_state
import end_state

from character import Character
from background import *
from enemy import *
from task import *

import server

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600
stage = [True, False, False, False]

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(esc_state)
        else:
            server.character.handle_events(event)


num_bug = 0
num_soju = 0
num_ppt = 0
num_report = 0
exam_switch = False

def init():
    global num_ppt, num_report, num_soju, num_bug
    num_bug = 0
    num_soju = 0
    num_ppt = 0
    num_report = 0

def enter():
    server.background = Background()
    game_world.add_object(server.background, 0)

    server.character = Character()
    game_world.add_object(server.character, 1)

    game_framework.World_time = 30.0
    # game_framework.World_time = 1.0   # test

def obj():
    global num_bug, num_soju, num_ppt, num_report
    if game_framework.bug_time > 1.0:
        server.enemies_bug.append(Bug())
        game_world.add_object(server.enemies_bug[num_bug], 1)
        game_world.add_collision_pairs(server.character, server.enemies_bug[num_bug], 'character:enemy_bug')
        game_world.add_collision_pairs(server.background, server.enemies_bug[num_bug], 'floor:enemy_bug')
        game_framework.bug_time = 0.0
        num_bug += 1

    if game_framework.soju_time > 2.0:
        server.enemies_soju.append(Soju())
        game_world.add_object(server.enemies_soju[num_soju], 1)
        game_world.add_collision_pairs(server.character, server.enemies_soju[num_soju], 'character:enemy_soju')
        game_world.add_collision_pairs(server.background, server.enemies_soju[num_soju], 'floor:enemy_soju')
        game_framework.soju_time = 0.0
        num_soju += 1

    if game_framework.ppt_time > 2.0:
        server.tasks_ppt.append(Ppt())
        game_world.add_object(server.tasks_ppt[num_ppt], 1)
        game_world.add_collision_pairs(server.character, server.tasks_ppt[num_ppt], 'character:task_ppt')
        game_world.add_collision_pairs(server.background, server.tasks_ppt[num_ppt], 'floor:task_ppt')
        game_framework.ppt_time = 0.0
        num_ppt += 1

    if game_framework.report_time > 1.0:
        server.tasks_report.append(Report())
        game_world.add_object(server.tasks_report[num_report], 1)
        game_world.add_collision_pairs(server.character, server.tasks_report[num_report], 'character:task_report')
        game_world.add_collision_pairs(server.background, server.tasks_report[num_report], 'floor:task_report')
        game_framework.report_time = 0.0
        num_report += 1



def exit():
    game_world.clear()

def update():
    global exam_switch
    for game_object in game_world.all_objects():
        game_object.update()

    if game_framework.World_time < 10.0 and not exam_switch:
        game_world.remove_object(server.background)
        server.background = background.Exam_background()
        game_world.add_object(server.background, 0)
        exam_switch = True

    if game_framework.World_time < 0.0:
        exam_switch = False
        if stage[3]:
            game_framework.change_state(end_state)
        game_framework.change_state(shop_state)
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)
    obj()
    if background.life[2]:
        game_framework.change_state(end_state)

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def pause():
    pass

def resume():
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
    # open_canvas(800, 600)
    game_framework.run(main_state)
    close_canvas()

if __name__ == '__main__':
    test_self()