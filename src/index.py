from time import perf_counter
from board import Board, PIECES
from random_player import RandomPlayer
from human_player import HumanPlayer
from AI_player import AIPlayer
from AI_player_01 import AIPlayerV1
from AI_player_02 import AIPlayerV2

SIZE = 13
ROW = 5
board = Board(SIZE, ROW)

human_00 = HumanPlayer()
human_01 = HumanPlayer()
computer_00 = RandomPlayer()
computer_01 = AIPlayerV1(3, board)
computer_02 = AIPlayerV2(5, board)
computer_03 = AIPlayer(7, 2, board)

players = [computer_02, computer_03]
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