import game_framework
from pico2d import*

name = "PauseState"
image=None

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    pass