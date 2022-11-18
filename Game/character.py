from pico2d import *
import game_framework
import game_world
from throw import Throw

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

# Charater Run Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Character Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

RD, LD, RU, LU, SPACE, JU, JD = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): JD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): JU
}

class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir_x = 0
        if event == JD:
            if self.dir_Idle_y == 0:
                self.dir_Idle_y = 1

    def exit(self, event):
        print('EXIT IDLE')
        self.dir_Run_y = self.dir_Idle_y
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
        if self.dir_Idle_y == 0:
            if self.dir_face == 1:
                Character.char_image.clip_draw(int(self.frame) * 82, 5 * 100, 82, 96, self.x, self.y)
            elif self.dir_face != 1:
                Character.char_image.clip_draw(int(self.frame) * 82, 4 * 100, 82, 96, self.x, self.y)
        elif self.dir_Idle_y != 0:
            if self.dir_face == 1:
                Character.char_image.clip_draw(int(self.frame) * 82, 3 * 100, 82, 96, self.x, self.y)
            elif self.dir_face != 1:
                Character.char_image.clip_draw(int(self.frame) * 82, 2 * 100, 82, 96, self.x, self.y)

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1
        elif event == JD:
            if self.dir_Run_y == 0:
                self.dir_Run_y = 1

    def exit(self, event):
        print('EXIT RUN')
        self.dir_face = self.dir_x
        self.dir_Idle_y = self.dir_Run_y
        if event == SPACE:
            pass
            # self.THROW()

    def do(self):
        # if self.dir_Run_y == 0:
        # int(self.frame) = (int(self.frame) + 1) % 5
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        # elif self.dir_Run_y != 0:
        #     int(self.frame) = 0
        # self.x += self.dir_x * 5
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir_Run_y * RUN_SPEED_PPS * game_framework.frame_time
        # self.y += self.dir_Run_y * 5
        self.x = clamp(15, self.x, Width - 15)
        if self.y > Height - bg_Height + 50 + 100 - 20:
            self.dir_Run_y = -1
        if self.y < Height - bg_Height + 49 - 20:
            self.dir_Run_y = 0


    def draw(self):
        if self.dir_Run_y == 0:
            if self.dir_x == -1:
                Character.char_image.clip_draw(int(self.frame) * 82, 0 * 100, 82, 96, self.x, self.y)
            elif self.dir_x == 1:
                Character.char_image.clip_draw(int(self.frame) * 82, 1 * 100, 82, 96, self.x, self.y)
        elif self.dir_Run_y != 0:
            if self.dir_x == -1:
                Character.char_image.clip_draw(int(self.frame) * 82, 2 * 100, 82, 96, self.x, self.y)
            elif self.dir_x == 1:
                Character.char_image.clip_draw(int(self.frame) * 82, 3 * 100, 82, 96, self.x, self.y)

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: IDLE, JD: IDLE, JU: IDLE},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN, JD: RUN, JU: RUN}
}


class Character:
    char_image = None
    object_image = None

    def __init__(self):
        self.x, self.y = Width - (bg_Width // 2) - 128 + 41, Height - bg_Height - 20 + 48
        self.frame = 0
        self.dir_face = 0
        self.dir_x = 0
        self.dir_Idle_y = 0
        self.dir_Run_y = 0
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
        draw_rectangle(*self.get_bb())
        debug_print('PPPP')
        debug_print(f' Dir_x: {self.dir_x}, Dir_Idle_y: {self.dir_Idle_y}, Dir_Run_y: {self.dir_Run_y}')

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def THROW(self):
        print('THROW')
        throw = Throw(self.x, self.y, self.dir_face)
        game_world.add_object(throw, 1)

    def get_bb(self):
        return self.x - 16, self.y - 50, self.x + 16, self.y + 50

    def handle_collision(self, other, group):
        pass

    def pause(self):
        pass

    def resume(self):
        pass