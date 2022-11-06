import random

class RandomPlayer:
    def __init__ (self, board, color):
        self.color = color
    
    def get_move(self, board):
        while True:
            # TODO: implement get_size?
            y = random.randint(0, board.size-1)
            x = random.randint(0, board.size-1)
            if board.is_legal_move(y, x, color):
                return (y, x)
