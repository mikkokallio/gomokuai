# what data structure to use for board?
# - ease of visualization
# - ease of evaluation


# when checking if there's 5 in row: ONLY check around where the new piece landed! input should be piece coordinates and color.

import random

SIZE = 15
board = [['.' for _ in range(SIZE)] for _ in range(SIZE)]

def check_legal(board, y, x, color):
    if board[y][x] != '.':
        return False
    return True

def check_win2(board, y, x, color):
    # only horizontal wins initially!
    count = 1 # how many found horizontal row
    for x1 in range(x-1, max(-1, x-6), -1):
        if board[y][x1] == color:
            count +=1
        else:
            break
    for x1 in range(x+1, min(SIZE, x+6)):
        if board[y][x1] == color:
            count +=1
        else:
            break
    if count == 5:
        return True
    count = 1 # how many found vertical row
    for y1 in range(y-1, max(-1, y-6), -1):
        if board[y1][x] == color:
            count +=1
        else:
            break
    for y1 in range(y+1, min(SIZE, y+6)):
        if board[y1][x] == color:
            count +=1
        else:
            break
    if count == 5:
        return True
    return False

def check_win(board, y, x, color):
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    for dir in directions:
        count = 1
        for sign in [-1, +1]:
            yy, xx = y, x
            for _ in range(5):
                yy += sign * dir[0]
                xx += sign * dir[1]
                if yy < 0 or xx < 0 or yy >= SIZE or xx >= SIZE:
                    break
                if board[yy][xx] == color:
                    count +=1
                else:
                    break
        if count == 5:
            return True
    return False

def print_board(board):
    [print(''.join(row)) for row in board]

for a in range(100):
    y = random.randint(0, SIZE-1)
    x = random.randint(0, SIZE-1)
    if not check_legal(board, y, x, 'X'):
        continue
    print(y, x)
    board[y][x] = 'X'
    print_board(board)
    count = check_win(board, y, x, 'X')
    print(count)
    if count:
        break
