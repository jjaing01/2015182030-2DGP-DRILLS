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


def move_point(p):
    global frame
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * dir, 100, 100, p[0], p[1])
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
charx, chary = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 1

while running:
    handle_events()

close_canvas()
