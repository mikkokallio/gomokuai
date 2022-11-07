from time import perf_counter
from board import Board, PIECES
from random_player import RandomPlayer
from human_player import HumanPlayer
from AI_player import AIPlayer
from AI_player01 import AIPlayerV1

SIZE = 9
ROW = 5
board = Board(SIZE, ROW)

human_00 = HumanPlayer()
human_01 = HumanPlayer()
computer_00 = RandomPlayer()
computer_01 = AIPlayer(3, board)
computer_02 = AIPlayer(3, board)

players = [computer_01, computer_02]
white_turn = False

start_time = perf_counter()

for a in range(SIZE**2):
    y, x = players[int(white_turn)].get_move(board, white_turn)
    win = board.add_piece(y, x, color=PIECES[white_turn])
    board.print()
    print('')
    if win:
        print(f'{ROW} in a row!', white_turn)
        break
    white_turn = not white_turn

print(perf_counter() - start_time)