
# 랜덤 손화살표를 추적하는 소년 ( 동영상 참고 )
# ‘hand_arrow.png’ 이미지 사용 – 수업 실습 자료에 포함
# 랜덤 위치에 손이 표시됨.(1점)
# 소년은 손을 따라감.(3점)
# 손에 도착하면, 다시 손이 자동으로 랜덤 위치로 이동함.(1점)
# 캐릭터의 바라보는 방향(좌우)을 이동 방향과 일치시켜야 함.(1점)

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 800

open_canvas(TUK_WIDTH, TUK_WIDTH)
tuk_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')


running = True
frame = 0
x, y = TUK_WIDTH // 2 , TUK_HEIGHT // 2

def exit_key():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# character.clip_draw(frame*100, 0, 100, 100, x, 130, 200, 200)


while running:
    exit_key()
    if not running:
        break
    
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw( frame * 100, 100 * 1, 100, 100, x, y )



    update_canvas()
    frame = ( frame + 1 ) % 8
    delay(0.05)

close_canvas()