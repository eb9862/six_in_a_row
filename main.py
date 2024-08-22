import numpy as np
import pygame, sys
from position import get_idx, get_pos

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("six in a row")

board = np.zeros([19, 19])
# sound
##### ~

# img
background = pygame.image.load("six_in_a_row/src/img/Blank_Go_board.png")
background = pygame.transform.scale(background, (800, 800))

# load
stone_black = pygame.image.load("six_in_a_row/src/img/Go_b_no_bg.png")
stone_white = pygame.image.load("six_in_a_row/src/img/Go_w_no_bg.png")

stone_black = pygame.transform.scale(stone_black, (40, 40))
stone_white = pygame.transform.scale(stone_white, (40, 40))

run = True

end = False

turn = 0

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
                turn += 1
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

# 규칙에 상관없이 번갈아가면서 돌 놓기 완료