from board import PIECES

class HumanPlayer:
    def get_move(self, board, player_two):
        while True:
            try:
                coords = input('Give y and x: ')
                y, x = [int(n) for n in coords.split(' ')]
                return (y, x)
            except ValueError:
                print('Invalid move!')
