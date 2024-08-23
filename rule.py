# vertical line check
def check_up(x, y, color, board):
    global cnt_v
    while y >= 0 and board[y][x] == color:
        if board[y][x] == color:
            cnt_v += 1
        y -= 1

def check_down(x, y, color, board):
    global cnt_v
    while y < 19 and board[y][x] == color:
        if board[y][x] == color:
            cnt_v += 1
        y += 1

def check_vertical(idx_x, idx_y, board):
    global cnt_v
    cnt_v = 0
    x , y = idx_x, idx_y
    color = board[y][x]
    check_up(x, y, color, board)
    check_down(x, y, color, board)
    return cnt_v - 1

# horizontal line check
def check_left(x, y, color, board):
    global cnt_h
    while x >= 0 and board[y][x] == color:
        if board[y][x] == color:
            cnt_h += 1
        x -= 1

def check_right(x, y, color, board):
    global cnt_h
    while x < 19 and board[y][x] == color:
        if board[y][x] == color:
            cnt_h += 1
        x += 1

def check_horizontal(idx_x, idx_y, board):
    global cnt_h
    cnt_h = 0
    x , y = idx_x, idx_y
    color = board[y][x]
    check_left(x, y, color, board)
    check_right(x, y, color, board)
    return cnt_h - 1

# diagonal line check
def check_up_right(x, y, color, board):
    global upward
    while x < 19 and y >= 0 and board[y][x] == color:
        if board[y][x] == color:
            upward += 1
        x += 1
        y -= 1

def check_down_left(x, y, color, board):
    global upward
    while x >= 0 and y < 19 and board[y][x] == color:
        if board[y][x] == color:
            upward += 1
        x -= 1
        y += 1

def check_diagonal_upward(idx_x, idx_y, board):
    global upward
    upward = 0
    x , y = idx_x, idx_y
    color = board[y][x]
    check_up_right(x, y, color, board)
    check_down_left(x, y, color, board)
    return upward - 1

def check_up_left(x, y, color, board):
    global downward
    while x >= 0 and y >= 0 and board[y][x] == color:
        if board[y][x] == color:
            downward += 1
        x -= 1
        y -= 1

def check_down_right(x, y, color, board):
    global downward
    while x < 19 and y < 19 and board[y][x] == color:
        if board[y][x] == color:
            downward += 1
        x += 1
        y += 1

def check_diagonal_downward(idx_x, idx_y, board):
    global downward
    downward = 0
    x , y = idx_x, idx_y
    color = board[y][x]
    check_up_left(x, y, color, board)
    check_down_right(x, y, color, board)
    return downward - 1