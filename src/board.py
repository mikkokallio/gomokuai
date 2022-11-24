from config import PIECES, EMPTY, DIRECTIONS, ROW

class Board:
    def __init__ (self, size):
        self.size = size
        self.state = [[EMPTY for _ in range(size)] for _ in range(size)]
        self.moves = []

    def __str__(self):
        '''Output board state with position numbering'''
        output = '  ' + ''.join([f'{x:02d}'[0] for x in range(self.size)]) + '\n'
        output +='  ' + ''.join([f'{x:02d}'[1] for x in range(self.size)]) + '\n'
        for y, row in enumerate(self.state):
            output+=f'{y:02d}' + ''.join(row) + '\n'
        output+=''
        return output

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
        for line in DIRECTIONS:
            count = 1
            for sign in [-1, +1]:
                y_pos, x_pos = y, x
                for _ in range(ROW):
                    y_pos += sign * line[0]
                    x_pos += sign * line[1]
                    if y_pos < 0 or x_pos < 0 or y_pos >= self.size or x_pos >= self.size:
                        break
                    if state[y_pos][x_pos] == color:
                        count +=1
                    else:
                        break
            if count == ROW:
                return True
        return False
