import numpy as np
import pygame
from position import get_idx, get_pos
from rule import check_vertical, check_horizontal, check_diagonal_upward, check_diagonal_downward

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 800))
#clock = pygame.time.Clock()
pygame.display.set_caption("six in a row")

# sound
sound_place_stone = pygame.mixer.Sound("six_in_a_row/src/sound/pop-39222.mp3")
sound_place_stone.set_volume(0.5)
sound_for_winner = pygame.mixer.Sound("six_in_a_row/src/sound/yeah~.mp3")
sound_for_winner.set_volume(0.5)

# img load
background = pygame.image.load("six_in_a_row/src/img/Blank_Go_board.png")
background = pygame.transform.scale(background, (800, 800))

stone_black = pygame.image.load("six_in_a_row/src/img/Go_b_no_bg.png")
stone_white = pygame.image.load("six_in_a_row/src/img/Go_w_no_bg.png")
stone_black = pygame.transform.scale(stone_black, (40, 40))
stone_white = pygame.transform.scale(stone_white, (40, 40))

# font
font = pygame.font.Font(None, 36)

board = np.zeros([19, 19])

run = True

end = False

turn = 0

t = 0

win = False

def place_stone(x, y, color):
    if color == "black":
        stone = stone_black
    else:
        stone = stone_white
    stone_rect = stone.get_rect(center=(x, y))
    screen.blit(stone, stone_rect)

while run:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 왼쪽 마우스 버튼
            mouse_pos = list(pygame.mouse.get_pos())
            idx_x, idx_y = get_idx(mouse_pos[0], mouse_pos[1])
            if idx_x != -1 and idx_y != -1 and board[idx_y][idx_x] == 0: # 중복 돌 놓기 체크
                if turn % 2 == 0: #black
                    board[idx_y][idx_x] = 1
                else:
                    board[idx_y][idx_x] = 2
                # rule, 승리 조건 체크
                v = check_vertical(idx_x, idx_y, board)
                print(f"vertical = {v}")
                h = check_horizontal(idx_x, idx_y, board)
                print(f"horizontal = {h}")
                uw = check_diagonal_upward(idx_x, idx_y, board)
                print(f"upward = {uw}")
                dw = check_diagonal_downward(idx_x, idx_y, board)
                print(f"downward = {dw}")
                if v >= 6 or h >= 6 or uw >= 6 or dw >= 6:
                    if turn % 2 == 0:
                        current_player = "black"
                    else:
                        current_player = "white"
                    win = True
                # 2 stones per turn
                t += 1
                if t == 2 or turn == 0:
                    turn += 1
                    t = 0
                # sound after placing stone
                sound_place_stone.play()
            print(mouse_pos)
    
    for y in range(19):
        for x in range(19):
            if board[y][x] != 0:
                stone_x, stone_y = get_pos(x, y)
                if board[y][x] == 1:
                    color = "black"
                else:
                    color = "white"
                place_stone(stone_x, stone_y, color)
    
    if win == True:
        # 반투명 overlay 생성
        overlay = pygame.Surface((800, 800))
        overlay.set_alpha(128)
        overlay.fill((200, 200, 200))
        screen.blit(overlay, (0, 0))

        # 승리 메시지 생성
        win_text = font.render(f"{current_player} wins!", True, (0, 0, 0))
        text_rect = win_text.get_rect(center=(400, 400))
        screen.blit(win_text, text_rect)
        
        sound_for_winner.play()

        run = False
    
    pygame.display.update()

# 승패 결과 출력 후 창을 닫을때까지 대기
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
