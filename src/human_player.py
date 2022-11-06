#import random

class HumanPlayer:
    def __init__ (self, black=True, board=None):
        pass
    
    def get_move(self, board, color):
        while True:
            try:
                coords = input('Give y and x: ')
                y, x = [int(n) for n in coords.split(' ')]
            except:
                print('Invalid coordinates. Type e.g. 9 8')
            if board.is_legal_move(y, x, color):
                return (y, x)
