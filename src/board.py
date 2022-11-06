class Board:
    def __init__ (self, size):
        self.size = size
        self.state = [['.' for _ in range(size)] for _ in range(size)]
        # TODO: Add info about turn black/white, turn number, other stats?

    def print(self):
        for row in self.state:
            print(''.join(row))

    def add_piece(self, y, x, color):
        # TODO: Check legality again?
        self.state[y][x] = color
        return self.is_winning_move(y, x, color)

    def is_legal_move(self, y, x, color):
        if y < 0 or y >= self.size or x < 0 or x >= self.size:
            return False
        #if color not in [0, 1]:
        #    return False
        if self.state[y][x] != '.':
            return False
        return True

    def is_winning_move(self, y, x, color):
        '''Check if new piece forms a row of exactly 5 pieces'''
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        for dir in directions:
            count = 1
            for sign in [-1, +1]:
                yy, xx = y, x
                for _ in range(5):
                    yy += sign * dir[0]
                    xx += sign * dir[1]
                    if yy < 0 or xx < 0 or yy >= self.size or xx >= self.size:
                        break
                    if self.state[yy][xx] == color:
                        count +=1
                    else:
                        break
            if count == 5:
                return True
        return False
