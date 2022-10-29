from pico2d import *
import game_framework
import os

path = os.getcwd() + "\Resource"
os.chdir(path)

import logo_state

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

open_canvas(Width, Height)
game_framework.run(logo_state)
close_canvas()
