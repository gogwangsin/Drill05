
# 랜덤 손화살표를 추적하는 소년 ( 동영상 참고 )
# ‘hand_arrow.png’ 이미지 사용 – 수업 실습 자료에 포함
# 랜덤 위치에 손이 표시됨.(1점)
# 소년은 손을 따라감.(3점)
# 손에 도착하면, 다시 손이 자동으로 랜덤 위치로 이동함.(1점)
# 캐릭터의 바라보는 방향(좌우)을 이동 방향과 일치시켜야 함.(1점)

from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 800, 800

open_canvas(TUK_WIDTH, TUK_WIDTH)
tuk_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
def exit_key():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

frame = 0
x, y = TUK_WIDTH // 2 , TUK_HEIGHT // 2
x_dir = 1
def character_draw():
    if x_dir < 0:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, y)
    else:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

# 화면 상 랜덤 위치 화살 초기화
x2, y2 = random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1) 
def arrow_draw():
    arrow.draw(x2,y2)

def Rendering():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow_draw()
    character_draw()
    update_canvas()


while running:
    exit_key()
    if not running:
        break
    Rendering()
    
    frame = ( frame + 1 ) % 8
    # x += x_dir * 8 
    delay(0.05)

close_canvas()