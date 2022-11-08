PIECES = {False: 'X', True: 'O'}
DIRECTIONS = [(1, 0), (0, 1), (1, 1), (-1, 1)]

class Board:
    def __init__ (self, size, row_len):
        self.size = size
        self.row_len = row_len
        self.state = [['.' for _ in range(size)] for _ in range(size)]
        self.moves = []
        # TODO: Add info about turn black/white, turn number, other stats?

    def print(self):
        print('  ' + ''.join([f'{x:02d}'[0] for x in range(self.size)]))
        print('  ' + ''.join([f'{x:02d}'[1] for x in range(self.size)]))
        for y, row in enumerate(self.state):
            print(f'{y:02d}' + ''.join(row))

    def get_size(self):
        return self.size
    
    def add_piece(self, y, x, color):
        # TODO: Check legality again?
        self.state[y][x] = color
        self.moves.append((y, x, color))
        return self.is_winning_move(self.state, y, x, color)

    def is_legal_move(self, y, x, color):
        if y < 0 or y >= self.size or x < 0 or x >= self.size:
            return False
        if color not in PIECES:
            return False
        if self.state[y][x] != '.':
            return False
        if len(self.moves) == 2:
            pass
        return True

    def is_winning_move(self, state, y, x, color):
        '''Check if new piece forms a row of exactly 5 pieces'''
        for dir in DIRECTIONS:
            count = 1
            for sign in [-1, +1]:
                yy, xx = y, x
                for _ in range(5):
                    yy += sign * dir[0]
                    xx += sign * dir[1]
                    if yy < 0 or xx < 0 or yy >= self.size or xx >= self.size:
                        break
                    if state[yy][xx] == color:
                        count +=1
                    else:
                        break
            if count == self.row_len:
                return True
        return False
