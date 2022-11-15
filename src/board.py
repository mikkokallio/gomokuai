PIECES = {False: 'X', True: 'O'}
EMPTY = '.'
ROW = 5
DIRECTIONS = [(1, 0), (0, 1), (1, 1), (-1, 1)]

class Board:
    def __init__ (self, size):
        self.size = size
        self.state = [[EMPTY for _ in range(size)] for _ in range(size)]
        self.moves = []
        # TODO: Add info about turn black/white, turn number, other stats?

    def print(self):
        '''Output board state with position numbering'''
        print('  ' + ''.join([f'{x:02d}'[0] for x in range(self.size)]))
        print('  ' + ''.join([f'{x:02d}'[1] for x in range(self.size)]))
        for y, row in enumerate(self.state):
            print(f'{y:02d}' + ''.join(row))
        print('')

    def get_size(self):
        '''Number of squares per board's size'''
        return self.size

    def add_piece(self, y, x, color):
        '''Places a new stone on the board if the move is legal and checks if the player wins'''
        if self.is_legal_move(y, x, color):
            self.state[y][x] = color
            self.moves.append((y, x, color))
        else:
            raise ValueError
        return self.is_winning_move(self.state, y, x, color)

    def is_legal_move(self, y, x, color):
        '''Checks the legality of a move'''
        if y < 0 or y >= self.size or x < 0 or x >= self.size:
            return False
        if color not in [PIECES[False], PIECES[True]]:
            return False
        if self.state[y][x] != EMPTY:
            return False
        return True

    def is_winning_move(self, state, y, x, color):
        '''Checks if a move completes a row of exactly 5 stones'''
        for dir in DIRECTIONS:
            count = 1
            for sign in [-1, +1]:
                yy, xx = y, x
                for _ in range(ROW):
                    yy += sign * dir[0]
                    xx += sign * dir[1]
                    if yy < 0 or xx < 0 or yy >= self.size or xx >= self.size:
                        break
                    if state[yy][xx] == color:
                        count +=1
                    else:
                        break
            if count == ROW:
                return True
        return False
