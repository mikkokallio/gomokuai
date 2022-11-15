from time import perf_counter
from board import Board, PIECES
from human_player import HumanPlayer
from AI_player import AIPlayer
from AI_player_01 import AIPlayerV1
from AI_player_02 import AIPlayerV2
from AI_player_03 import AIPlayerV3

SIZE = 15
ROW = 5

def main():
    '''Set up board and run game loop'''
    board = Board(SIZE, ROW, opening=True)
    #board.add_piece(6, 6, 'X')
    #board.add_piece(6, 8, 'O')
    #board.add_piece(6, 3, 'X')
    white_turn = False

    human_00 = HumanPlayer()
    human_01 = HumanPlayer()
    computer_01 = AIPlayerV1(3, board) # Old version!
    computer_02 = AIPlayerV2(5, board) # Old version!
    computer_03 = AIPlayerV3(7, 2, board, randomness=True) # Old version!
    computer_04 = AIPlayer(depth=11, reach=2, limit_moves=5, board=board)
    computer_05 = AIPlayer(depth=11, reach=2, limit_moves=3, board=board)

    players = [computer_04, computer_05]

    start_time = perf_counter()
    clocks = [0.0, 0.0]

    for turn in range(SIZE**2):
        board.print()
        try:
            clock_start = perf_counter()
            y, x = players[int(white_turn)].get_move(board, white_turn)
            turn_time = perf_counter() - clock_start
            clocks[white_turn] += turn_time
            win = board.add_piece(y, x, color=PIECES[white_turn])

            if win:
                board.print()
                print(f'{PIECES[white_turn]} wins on turn {turn}!')
                print('X time:', clocks[0], 'O time:', clocks[1])
                break
            white_turn = not white_turn
        except ValueError:
            print('Invalid move!')

    print(perf_counter() - start_time)

if __name__ == '__main__':
    main()
