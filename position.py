start = 25
end = 775

block = round((end - start) / 18, 2)

def get_idx(x, y):
    origin = x
    for i in range(19):
        c = block * i + 25
        if x > c - 15 and x < c + 15:
            x = i
    if origin == x:
        x = -1
    origin = y
    for i in range(19):
        c = block * i + 25
        if y > c - 15 and y < c + 15:
            y = i
    if origin == y:
        x = -1
    return x, y

def get_pos(idx_x, idx_y):
    return int(block * idx_x + 25), int(block * idx_y + 25)