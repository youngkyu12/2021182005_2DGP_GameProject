from pico2d import *
import game_framework


Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

RD, LD, JD, RU, LU, JU = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): JD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): JU
}




class IDLE:
    def enter():
        print('ENTER IDLE')
        pass

    def exit():
        print('EXIT IDLE')
        pass

    def do():
        pass

    def draw():
        pass

class RUN:
    def enter():
        print('ENTER RUN')

    def exit():
        print('EXIT RUN')

    def do():
        pass

    def draw():
        pass


next_state = {
    IDLE: {RU: RUN, LU: RUN, JU: RUN, RD: RUN, LD: RUN, JD: RUN},
    RUN: {RU: IDLE, LU: IDLE, JU: IDLE, RD: IDLE, LD: IDLE, JD: IDLE}
}


class Character:
    image = None
    def __init__(self):
        self.x, self.y = 1280 - (1026 // 2) - 128 + 41, 720 - 600 + 48
        self.frame = 0
        self.animation = 2
        self.dir_x = 0
        self.dir_y = 0
        if Character.image == None:
            Character.image = load_image("character_anime.png")

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter()
    def update(self):
        self.cur_state.do()

        if self.q:
            event = self.q.pop()
            self.cur_state.exit()
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter()

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
        self.cur_state.draw()

        # Character.image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.q.insert(0, key_event)

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
        # elif event.type == SDL_KEYUP:
        #     if event.key == SDLK_LEFT:
        #         self.dir_x += 1
        #         self.animation = 2
        #     elif event.key == SDLK_RIGHT:
        #         self.dir_x -= 1
        #         self.animation = 3


