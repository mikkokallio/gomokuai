from time import perf_counter
from board import Board
from random_player import RandomPlayer
from human_player import HumanPlayer
from AI_player import AIPlayer
from AI_player01 import AIPlayerV1

SIZE = 9
ROW = 5
PIECES = {False: 'X', True: 'O'}
board = Board(SIZE, ROW)
#players = [RandomPlayer(), HumanPlayer()]
#players = [HumanPlayer(), AIPlayer(5, board, color=PIECES[0], other=PIECES[1])]
#players = [RandomPlayer(color=PIECES[1]), AIPlayer(5, board, color=PIECES[0], other=PIECES[1])]
#players = [AIPlayerV1(2, board, color=PIECES[0], other=PIECES[1]), 
#           AIPlayer(4, board, color=PIECES[1], other=PIECES[0])]
players = [AIPlayer(4, board, color=PIECES[0], other=PIECES[1]), 
           HumanPlayer(board, PIECES[1])]
white_turn = False

start_time = perf_counter()

for a in range(SIZE**2):
    y, x = players[int(white_turn)].get_move(board)
    win = board.add_piece(y, x, color=PIECES[white_turn])
    board.print()
    print('')
    if win:
        print(f'{SIZE} in a row!', white_turn)
        break
    white_turn = not white_turn

print(perf_counter() - start_time)