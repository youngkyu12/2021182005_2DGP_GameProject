import main_state
from background import *

class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw



class TestGameState:

    def __init__(self, name):
        self.name = name

    def enter(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def resume(self):
        print("State [%s] Resumed" % self.name)

    def handle_events(self):
        print("State [%s] handle_events" % self.name)

    def update(self):
        print("State [%s] update" % self.name)

    def draw(self):
        print("State [%s] draw" % self.name)



running = None
stack = []



def get_prev_state():
    try:
        return stack[-2]
    except:
        return None

def change_state(state):
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()
    stack.append(state)
    state.enter()



def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()



def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()



def quit():
    global running
    running = False


# pree fill statck with previous states
def fill_states(*states):
    for state in states:
        stack.append(state)

import time
frame_time = 0.0
World_time = 60.0
bug_time = 4.0
soju_time = 4.0
ppt_time = 4.0
report_time = 4.0
task_time = 0.0
deadline_time = 9.0

def run(start_state):
    global running, stack
    running = True

    # prepare previous states if any
    for state in stack:
        state.enter()
        state.pause()

    stack.append(start_state)
    stack[-1].enter()
    current_time = time.time()
    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        global frame_time, World_time, bug_time, soju_time, ppt_time, report_time, task_time, deadline_time
        frame_time = time.time() - current_time
        if stack[-1] == main_state:
            World_time = float(World_time) - frame_time
        bug_time += frame_time
        soju_time += frame_time
        ppt_time += frame_time
        report_time += frame_time
        deadline_time += frame_time
        if task:
            task_time += frame_time * 16.0
        # frame_rate = 1 / frame_time
        current_time += frame_time
        # print(f"Frame Time: {frame_time}, Frame Rate: {frame_rate}")

    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def test_game_framework():
    start_state = TestGameState('StartState')
    run(start_state)



if __name__ == '__main__':
    test_game_framework()