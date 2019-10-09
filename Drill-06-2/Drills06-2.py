from pico2d import*
import random

KPU_WIDTH, KPU_HEIGHT = 800, 600

point = [(random.randint(50, 750), random.randint(50, 550)) for i in range(10)]

global dir

def handle_events():
    # fill here
    global running  # 달리는 것

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
                running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

