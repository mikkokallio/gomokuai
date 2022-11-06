from board import Board
from random_player import RandomPlayer
from human_player import HumanPlayer
from AI_player import AIPlayer

SIZE = 4
ROW = 3
PIECES = {False: 'X', True: 'O'}
board = Board(SIZE, ROW)
#players = [RandomPlayer(), HumanPlayer()]
players = [RandomPlayer(), AIPlayer(board)]
white_turn = False

for a in range(25):
    y, x = players[int(white_turn)].get_move(board, color=PIECES[white_turn])
    win = board.add_piece(y, x, color=PIECES[white_turn])
    board.print()
    print('')
    if win:
        print('5 in a row!')
        break
    white_turn = not white_turn
