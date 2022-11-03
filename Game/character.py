from pico2d import *
import game_framework


Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

RD, LD, JD, RU, LU = range(5)

key_event_table = {
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
        self.frame = 0
        if self.animation == 5:
            self.animation = 2
        elif self.animation == 4:
            self.animation = 3
        pass

    def exit(self):
        print('EXIT IDLE')
        pass

    def do(self):
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


    def exit(self):
        print('EXIT RUN')

    def do(self):
        self.frame = (self.frame + 1) % 5
        self.x += self.dir_x * 5
        self.x = clamp(Width - 128 - bg_Width, self.x, Width - 128)

        pass

    def draw(self):
        Character.char_image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)
        pass

class JUMP:
    def enter(self, event):
        print('ENTER Jump')
        if event == JD:
            self.dir_y += 1
            if self.animation == 5 or self.animation == 2:
                self.animation = 0
            elif self.animation == 4 or self.animation == 3:
                self.animation = 1

    def exit(self):
        print('EXIT Jump')

    def do(self):
        self.y += self.dir_y * 5
        if self.y > 720 - 600 + 48 + 100:
            self.dir_y -= 1
        elif self.y < 720 - 600 + 48:
            self.dir_y = 0
            if self.animation == 0:
                self.animation = 5
            elif self.animation == 1:
                self.animation = 4
        pass

    def draw(self):
        Character.char_image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)

        pass
class THROW:
    def enter(self, event):
        print('ENTER Throw')

    def exit(self):
        print('EXIT Throw')

    def do(self):
        pass

    def draw(self):
        pass

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, JD: JUMP},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, JD: JUMP},
    JUMP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN}

}


class Character:
    char_image = None
    object_image = None
    def __init__(self):
        self.x, self.y = 1280 - (1026 // 2) - 128 + 41, 720 - 600 + 48
        self.throw_x, self.throw_y = Width // 2, Height // 2
        self.frame = 0
        self.animation = 2
        self.dir_x = 0
        self.dir_y = 0
        self.xl, self.yl = 1280 - 1024 - 128, 720 - 600 + 100
        self.xr, self.yr = 1280 - 128, 720 - 600 + 100
        self.throw_l = False
        self.throw_r = False
        self.i = 0
        self.t = 0
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
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

        # self.t = self.i / 100
        # if self.throw_l:
        #     self.throw_x = (2 * self.t ** 2 - 3 * self.t + 1) * self.x + (-4 * self.t ** 2 + 4 * self.t) * (self.x -((self.x - self.xl) // 2)) + (2 * self.t ** 2 - self.t) * self.xl
        #     self.throw_y = (2 * self.t ** 2 - 3 * self.t + 1) * self.y + (-4 * self.t ** 2 + 4 * self.t) * (self.y + 100) + (2 * self.t ** 2 - self.t) * self.yl
        # elif self.throw_r:
        #     self.throw_x = (2 * self.t ** 2 - 3 * self.t + 1) * self.x + (-4 * self.t ** 2 + 4 * self.t) * (self.x + ((self.xr - self.x) // 2)) + (2 * self.t ** 2 - self.t) * self.xr
        #     self.throw_y = (2 * self.t ** 2 - 3 * self.t + 1) * self.y + (-4 * self.t ** 2 + 4 * self.t) * (self.y + 100) + (2 * self.t ** 2 - self.t) * self.yr
        #
        # self.i += 4
        # if self.i > 100:
        #     self.i = 0
        #     self.throw_r = False
        #     self.throw_l = False
        # self.x += self.dir_x * 5
        # self.y += self.dir_y * 5
        # if self.animation == 4 or self.animation == 5:
        #     self.frame = (self.frame + 1) % 5
        # else:
        #     self.frame = 0
        # if self.y > 720 - 600 + 48 + 100:
        #     self.dir_y -= 1
        # elif self.y < 720 - 600 + 48:
        #     self.dir_y = 0
        #     if self.animation == 0:
        #         self.animation = 5
        #     elif self.animation == 1:
        #         self.animation = 4

    def draw(self):
        self.cur_state.draw(self)

        # Character.char_image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)
        # if self.throw_r or self.throw_l:
        #     Character.object_image.draw(self.throw_x, self.throw_y)

    def add_event(self, event):
        self.q.insert(0, event)
    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        # if event.type == SDL_KEYDOWN:
        #     if event.key == SDLK_LEFT:
        #         self.dir_x -= 1
        #         self.animation = 5
        #     elif event.key == SDLK_RIGHT:
        #         self.dir_x += 1
        #         self.animation = 4
        #     elif event.key == SDLK_UP:
        #         if self.animation == 5 or self.animation == 2:
        #             self.animation = 0
        #         elif self.animation == 4 or self.animation == 3:
        #             self.animation = 1
        #         if self.dir_y == 0:
        #             self.dir_y += 1
        #     elif event.key == SDLK_SPACE:
        #         if self.animation == 5 or self.animation == 2:
        #             self.throw_l = True
        #         elif self.animation == 4 or self.animation == 3:
        #             self.throw_r = True
        # elif event.type == SDL_KEYUP:
        #     if event.key == SDLK_LEFT:
        #         self.dir_x += 1
        #         self.animation = 2
        #     elif event.key == SDLK_RIGHT:
        #         self.dir_x -= 1
        #         self.animation = 3


