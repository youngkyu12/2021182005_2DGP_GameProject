from pico2d import *
import game_framework
import game_world
from throw import Throw

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

RD, LD, RU, LU, SPACE, JU, JD = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): JD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
}




class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir_x = 0
        self.dir_y = 0
        if self.action == 5:
            self.action = 2
        elif self.action == 4:
            self.action = 3
        # elif self.action == 0:
        #     self.action = 2
        # elif self.action == 1:
        #     self.action = 3

    def exit(self, event):
        print('EXIT IDLE')
        if event == SPACE:
            self.THROW()
        if event == JD:
            if self.action == 2:
                self.action = 0
            elif self.action == 3:
                self.action = 1

    def do(self):
        self.frame = 0

        pass

    def draw(self):
        Character.char_image.clip_draw(self.frame * 82, self.action * 100, 82, 96, self.x, self.y)
        pass

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == JD or self.dir_y == 1 or self.dir_y == -1:
            if event == RD:
                self.dir_x += 1
                self.action = 1
            elif event == LD:
                self.dir_x -= 1
                self.action = 0
            elif event == RU:
                self.dir_x -= 1
            elif event == LU:
                self.dir_x += 1
            self.dir_y = 1
            if self.action == 5 or self.action == 2:
                self.action = 0
            elif self.action == 4 or self.action == 3:
                self.action = 1
        else:
            if event == RD:
                self.dir_x += 1
                self.action = 4
            elif event == LD:
                self.dir_x -= 1
                self.action = 5
            elif event == RU:
                self.dir_x -= 1
                self.action = 3
            elif event == LU:
                self.dir_x += 1
                self.action = 2

    def exit(self, event):
        print('EXIT RUN')
        if event == SPACE:
            self.THROW()

    def do(self):
        if self.action == 4 or self.action == 5:
            self.frame = (self.frame + 1) % 5
        elif self.action == 0 or self.action == 1:
            self.frame = 0
        self.x += self.dir_x * 5
        self.y += self.dir_y * 5
        self.x = clamp(Width - 128 - bg_Width, self.x, Width - 128)
        if self.y > 720 - 600 + 48 + 100:
            self.dir_y = -1
        if self.y < 720 - 600 + 49:
            self.dir_y = 0
            if self.dir_x == 0:
                self.add_event(JU)

    def draw(self):
        Character.char_image.clip_draw(self.frame * 82, self.action * 100, 82, 96, self.x, self.y)
        pass


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: IDLE, JD: RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN, JD: RUN, JU: IDLE}
}


class Character:
    char_image = None
    object_image = None
    def __init__(self):
        self.x, self.y = 1280 - (1026 // 2) - 128 + 41, 720 - 600 + 48
        self.frame = 0
        self.action = 2
        self.dir_x = 0
        self.dir_y = 0
        if Character.char_image == None:
            Character.char_image = load_image("character_anime.png")
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
        debug_print(f' Dir_x: {self.dir_x}, Dir_y: {self.dir_y}')

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def THROW(self):
        print('THROW')
        throw = Throw(self.x, self.y, self.action)
        game_world.add_object(throw, 1)

