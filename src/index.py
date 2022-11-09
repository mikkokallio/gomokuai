from time import perf_counter
from board import Board, PIECES
from human_player import HumanPlayer
from AI_player import AIPlayer
from AI_player_01 import AIPlayerV1
from AI_player_02 import AIPlayerV2
from AI_player_03 import AIPlayerV3

SIZE = 15
ROW = 5
board = Board(SIZE, ROW, opening=True)

human_00 = HumanPlayer()
human_01 = HumanPlayer()
computer_01 = AIPlayerV1(3, board)
computer_02 = AIPlayerV2(5, board)
computer_03 = AIPlayerV3(7, 2, board)
computer_04 = AIPlayer(depth=5, reach=2, limit_moves=3, board=board)

players = [human_00, computer_04]
white_turn = False

start_time = perf_counter()

board.print()
print('')

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