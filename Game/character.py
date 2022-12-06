from pico2d import *
import game_framework
import game_world
from throw import Throw

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

import server
import background
# 60프레임 고정시켜보기

# Charater Run Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 20.0   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Character Action Speed
TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

RD, LD, RU, LU, SPACE, JU, JD, DU, DD = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): JD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): JU,
    (SDL_KEYUP, SDLK_DOWN): DU
}

class IDLE:
    def enter(self, event):
        # print('ENTER IDLE')
        self.dir_x = 0
        if event == JD and self.dir_Idle_down == 0:
            if self.dir_Idle_y == 0:
                self.dir_Idle_y = 1
        elif event == DD and self.dir_Idle_y == 0:
            self.dir_Idle_down = 1
        elif event == DU and self.dir_Idle_y == 0:
            self.dir_Idle_down = 0

    def exit(self, event):
        # print('EXIT IDLE')
        self.dir_Run_y = self.dir_Idle_y
        self.dir_Run_down = self.dir_Idle_down
        # print(f'{self.dir_Idle_down}')
        if event == SPACE:
            pass
            # self.THROW()

    def do(self):
        self.frame = 0
        self.y += self.dir_Idle_y * RUN_SPEED_PPS * game_framework.frame_time
        if self.y > Height - bg_Height + 50 + 100 - 20:
            self.dir_Idle_y = -1
        if self.y < Height - bg_Height + 49 - 20:
            self.dir_Idle_y = 0

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        if self.dir_Idle_y == 0 and self.dir_Idle_down == 0:
            if self.dir_face == 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 3 * 100, 100, 99, sx, sy)
            elif self.dir_face != 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 2 * 100, 100, 99, sx, sy)
        elif self.dir_Idle_y != 0 and self.dir_Idle_down == 0:
            if self.dir_face == 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 4 * 100, 100, 99, sx, sy)
            elif self.dir_face != 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 5 * 100, 100, 99, sx, sy)
        elif self.dir_Run_y == 0 and self.dir_Idle_down == 1:
            # 테스트 이미지
            if self.dir_face == 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 0 * 100, 100, 99, sx, sy)
            elif self.dir_face != 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 1 * 100, 100, 99, sx, sy)

class RUN:
    def enter(self, event):
        # print('ENTER RUN')
        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1
        elif event == JD and self.dir_Run_down == 0:
            if self.dir_Run_y == 0:
                self.dir_Run_y = 1
        elif event == DD and self.dir_Run_y == 0:
            self.dir_Run_down = 1
        elif event == DU and self.dir_Run_y == 0:
            self.dir_Run_down = 0

    def exit(self, event):
        self.dir_face = self.dir_x
        self.dir_Idle_y = self.dir_Run_y
        self.dir_Idle_down = self.dir_Run_down

        if event == SPACE:
            pass

    def do(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir_Run_y * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0 + 15, self.x, server.background.w - 1 - 15)


        if self.y > Height - bg_Height + 49 + 100 - 20:
            self.dir_Run_y = -1
        if self.y < Height - bg_Height + 49 - 20:
            self.dir_Run_y = 0


    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        if self.dir_Run_y == 0 and self.dir_Run_down == 0:
            if self.dir_x == -1:
                Character.char_image.clip_draw(int(self.frame) * 100, 6 * 100, 100, 99, sx, sy)
            elif self.dir_x == 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 7 * 100, 100, 99, sx, sy)
        elif self.dir_Run_y == 0 and self.dir_Run_down == 1:
            # 테스트 이미지
            if self.dir_x == -1:
                Character.char_image.clip_draw(int(self.frame) * 100, 1 * 100, 100, 99, sx, sy)
            elif self.dir_x == 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 0 * 100, 100, 99, sx, sy)
        elif self.dir_Run_y != 0 and self.dir_Run_down == 0:
            if self.dir_x == -1:
                Character.char_image.clip_draw(int(self.frame) * 100, 5 * 100, 100, 99, sx, sy)
            elif self.dir_x == 1:
                Character.char_image.clip_draw(int(self.frame) * 100, 4 * 100, 100, 99, sx, sy)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: IDLE, JD: IDLE, JU: IDLE, DD: IDLE, DU: IDLE},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN, JD: RUN, JU: RUN, DD: RUN, DU: RUN}
}


class Character:
    char_image = None
    object_image = None

    def __init__(self):
        self.x, self.y = server.background.w // 2, server.background.h // 2 - 210
        self.frame = 0
        self.dir_face = 0
        self.dir_x = 0
        self.dir_Idle_y = 0
        self.dir_Run_y = 0
        self.dir_Idle_down = 0
        self.dir_Run_down = 0

        if Character.char_image == None:
            Character.char_image = load_image("character_anime_full.png")

        if Character.object_image == None:
            Character.object_image = load_image('target_1_32x32.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(self.cur_state, event)
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f' Dir_x: {self.dir_x}, Dir_Idle_y: {self.dir_Idle_y}, Dir_Run_y: {self.dir_Run_y}')

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def THROW(self):
        throw = Throw(self.x, self.y, self.dir_face)
        game_world.add_object(throw, 1)

    def get_bb(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        if self.cur_state == RUN:
            if self.dir_Run_down != 1:
                return sx - 16, sy - 50, sx + 16, sy + 50
            else:
                return sx - 50, sy - 48, sx + 50, sy - 16
        elif self.cur_state == IDLE:
            if self.dir_Idle_down != 1:
                return sx - 16, sy - 50, sx + 16, sy + 50
            else:
                return sx - 50, sy - 48, sx + 50, sy - 16

    def handle_collision(self, other, group):
        pass

    def pause(self):
        pass

    def resume(self):
        pass