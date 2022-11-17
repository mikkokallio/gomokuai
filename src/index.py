from time import perf_counter
from random import randint
from board import Board, PIECES
from human_player import HumanPlayer
from AI_player import AIPlayer
from AI_player_02 import AIPlayerV2
from AI_player_03 import AIPlayerV3
from AI_player_04 import AIPlayerV4

SIZE = 15
CENTER = int(SIZE/2)
BLACK, WHITE = False, True


def get_constraint(min_dist, max_dist):
    '''For initial moves, get list of allowed moves'''
    moves = []
    for y in range(CENTER-max_dist, CENTER+max_dist+1):
        for x in range(CENTER-max_dist, CENTER+max_dist+1):
            if not (y > CENTER-min_dist and y < CENTER+min_dist and x > CENTER-min_dist and x < CENTER+min_dist):
                moves.append((y, x))
    print('Allowed moves:', moves)
    return moves

def main():
    '''Set up board and run game loop'''
    board = Board(SIZE)

    #human_00 = HumanPlayer()
    #human_01 = HumanPlayer()
    # computer_02 = AIPlayerV2(5, board) # Old version!
    computer_03 = AIPlayerV3(7, 2, board, randomness=True)  # Old version!
    computer_04 = AIPlayerV4(depth=11, reach=2, limit_moves=3, board=board)
    computer_05 = AIPlayer(
        depth=7, reach=2, limit_moves=4, deepen=True, board=board)

    players = [computer_04, computer_05]

    start_time = perf_counter()
    clocks = [0.0, 0.0]

    board.print()
    y, x = players[BLACK].get_move(board, BLACK, get_constraint(0, 0))
    board.add_piece(y, x, PIECES[BLACK])
    board.print()
    y, x = players[WHITE].get_move(board, WHITE, get_constraint(1, 2))
    board.add_piece(y, x, PIECES[WHITE])
    board.print()
    y, x = players[BLACK].get_move(board, BLACK, get_constraint(3, 7))
    board.add_piece(y, x, PIECES[BLACK])
    player_turn = WHITE

    for turn in range(SIZE**2 - len(board.moves)):
        board.print()
        try:
            clock_start = perf_counter()
            y, x = players[int(player_turn)].get_move(board, player_turn, None)
            turn_time = perf_counter() - clock_start
            clocks[player_turn] += turn_time
            win = board.add_piece(y, x, color=PIECES[player_turn])

            if win:
                board.print()
                print(f'{PIECES[player_turn]} wins on turn {turn}!')
                print('X time:', clocks[0], 'O time:', clocks[1])
                break
            player_turn = not player_turn
        except ValueError as e:
            print('Invalid move!')
            print(e)

    print(perf_counter() - start_time)


if __name__ == '__main__':
    main()
