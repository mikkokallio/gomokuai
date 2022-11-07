import random
from board import PIECES

class RandomPlayer:
    def get_move(self, board, player_two):
        while True:
            # TODO: implement get_size?
            y = random.randint(0, board.size-1)
            x = random.randint(0, board.size-1)
            if board.is_legal_move(y, x, PIECES[player_two]):
                return (y, x)
