import numpy as np
import pygame
from position import get_idx, get_pos
from rule import check_vertical, check_horizontal, check_diagonal_upward, check_diagonal_downward

pygame.init()

screen = pygame.display.set_mode((800, 800))
#clock = pygame.time.Clock()
pygame.display.set_caption("six in a row")

# sound
##### ~

# img load
background = pygame.image.load("six_in_a_row/src/img/Blank_Go_board.png")
background = pygame.transform.scale(background, (800, 800))

stone_black = pygame.image.load("six_in_a_row/src/img/Go_b_no_bg.png")
stone_white = pygame.image.load("six_in_a_row/src/img/Go_w_no_bg.png")
stone_black = pygame.transform.scale(stone_black, (40, 40))
stone_white = pygame.transform.scale(stone_white, (40, 40))

board = np.zeros([19, 19])

run = True

end = False

turn = 0

t = 0

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
                    print(f"{current_player} win!")
                # 2 stones per turn
                t += 1
                if t == 2 or turn == 0:
                    turn += 1
                    t = 0
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

    pygame.display.update()

pygame.quit()
# 규칙에 상관없이 번갈아가면서 돌 놓기 완료