from board import PIECES

class HumanPlayer:
    def get_move(self, board, player_two):
        while True:
            try:
                coords = input('Give y and x: ')
                y, x = [int(n) for n in coords.split(' ')]
            except:
                print('Invalid coordinates. Type e.g. 9 8')
            if board.is_legal_move(y, x, PIECES[player_two]):
                return (y, x)
