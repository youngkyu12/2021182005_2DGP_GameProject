from pico2d import *
import game_framework
import game_world
from throw import Throw

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

RD, LD, RU, LU, SPACE = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
}




class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir_x = 0
        self.dir_y = 0
        if self.animation == 5:
            self.animation = 2
        elif self.animation == 4:
            self.animation = 3
        # elif self.animation == 0:
        #     self.animation = 2
        # elif self.animation == 1:
        #     self.animation = 3

    def exit(self, event):
        print('EXIT IDLE')
        if event == SPACE:
            self.THROW()

    def do(self):
        self.frame = 0

        pass

    def draw(self):
        Character.char_image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)
        pass

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir_x += 1
            self.animation = 4
        elif event == LD:
            self.dir_x -= 1
            self.animation = 5
        elif event == RU:
            self.dir_x -= 1
            self.animation = 3
        elif event == LU:
            self.dir_x += 1
            self.animation = 2
        # elif event == JD:
        #     self.dir_y += 1
        #     if self.animation == 5 or self.animation == 2:
        #         self.animation = 0
        #     elif self.animation == 4 or self.animation == 3:
        #         self.animation = 1

    def exit(self, event):
        print('EXIT RUN')
        if event == SPACE:
            self.THROW()

    def do(self):
        # if self.animation == 4 or 5:
        self.frame = (self.frame + 1) % 5
        # elif self.animation == 0 or 1:
        #     self.frame = 0
        self.x += self.dir_x * 5
        self.x = clamp(Width - 128 - bg_Width, self.x, Width - 128)
        # self.y += self.dir_y * 5
        # if self.y > 720 - 600 + 48 + 100:
        #     self.dir_y -= 1
        # elif self.y < 720 - 600:
        #     self.dir_y = 0
        #     if self.animation == 0:
        #         self.animation = 5
        #     elif self.animation == 1:
        #         self.animation = 4


    def draw(self):
        Character.char_image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)
        pass

# class JUMP:
#     def enter(self, event):
#         print('ENTER Jump')
#         if event == JD:
#             self.dir_y += 1
#             if self.animation == 5 or self.animation == 2:
#                 self.animation = 0
#             elif self.animation == 4 or self.animation == 3:
#                 self.animation = 1
#         if event == RD:
#             self.dir_x += 1
#             self.animation = 1
#         elif event == LD:
#             self.dir_x -= 1
#             self.animation = 0
#         elif event == RU:
#             self.dir_x -= 1
#         elif event == LU:
#             self.dir_x += 1
#
#     def exit(self, event):
#         print('EXIT Jump')
#
#     def do(self):
#         self.x += self.dir_x * 5
#         self.x = clamp(Width - 128 - bg_Width, self.x, Width - 128)
#         self.y += self.dir_y * 5
#         if self.y > 720 - 600 + 48 + 100:
#             self.dir_y -= 1
#         elif self.y < 720 - 600 + 48:
#             self.add_event(STOP)
#
#
#         pass
#
#     def draw(self):
#         Character.char_image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)
#
#         pass

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: IDLE},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN}
    # JUMP: {RU: JUMP, LU: JUMP, RD: JUMP, LD: JUMP, STOP: IDLE}
}


class Character:
    char_image = None
    object_image = None
    def __init__(self):
        self.x, self.y = 1280 - (1026 // 2) - 128 + 41, 720 - 600 + 48
        self.frame = 0
        self.animation = 2
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
        throw = Throw(self.x, self.y, self.animation)
        game_world.add_object(throw, 1)

