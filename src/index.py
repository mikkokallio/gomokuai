from time import perf_counter
import csv
from board import Board
from human_player import HumanPlayer
from AI_player import AIPlayer
from scoring import CENTER, SIZE, PIECES, BLACK, WHITE, EMPTY, OPENING_TURNS
states = set()

def get_constraint(min_dist, max_dist):
    '''For initial moves, get list of allowed moves'''
    moves = []
    for y in range(CENTER-max_dist, CENTER+max_dist+1):
        for x in range(CENTER-max_dist, CENTER+max_dist+1):
            if not (y > CENTER-min_dist and y < CENTER+min_dist and x > CENTER-min_dist and x < CENTER+min_dist):
                moves.append((y, x))
    return moves

def main():
    '''Set up board and run game loop'''
    board = Board(SIZE)

    #human_00 = HumanPlayer()
    #human_01 = HumanPlayer()
    computer_05 = AIPlayer(
        depth=7, reach=2, limit_moves=3, deepen=True, use_table=True, randomized=True, board=board)
    computer_06 = AIPlayer(
        depth=7, reach=2, limit_moves=3, deepen=True, use_table=True, randomized=False, board=board)

    players = [computer_05, computer_06]

    start_time = perf_counter()
    clocks = [0.0, 0.0]

    for turn in OPENING_TURNS:
        #board.print()
        #print(f'Place {PIECES[turn[0]]} at least {turn[1]} and at most {turn[2]} squares from the center')
        y, x = players[turn[0]].get_move(board, turn[0], get_constraint(turn[1], turn[2]))
        board.add_piece(y, x, PIECES[turn[0]])
        states.add(''.join([''.join(row) for row in board.state]))
    player_turn = WHITE
    winner = EMPTY
    board.print()

    for turn in range(SIZE**2 - len(board.moves) - 125):
        #board.print()
        try:
            clock_start = perf_counter()
            y, x = players[int(player_turn)].get_move(board, player_turn, None)
            turn_time = perf_counter() - clock_start
            clocks[player_turn] += turn_time
            win = board.add_piece(y, x, color=PIECES[player_turn])

            if win:
                #board.print()
                print(f'{PIECES[player_turn]} wins on turn {turn}!')
                print('X time:', clocks[0], 'O time:', clocks[1])
                winner = PIECES[player_turn]
                break
            player_turn = not player_turn
            if turn <= 10:
                states.add(''.join([''.join(row) for row in board.state]))
        except ValueError as error:
            print('Invalid move!')
            print(error)

    if winner == EMPTY:
        print('Draw!')
    #print(perf_counter() - start_time)

    with open('games.csv', encoding='utf8', newline='\n') as file:
        reader = csv.reader(file)
        next(reader)
        results = dict(reader)

    for state in states:
        if state in results:
            results[state] += winner
        else:
            results[state] = EMPTY + winner

    with open('games.csv', 'w', encoding='utf8') as file:
        for result in results.keys():
            file.write(f'{result},{results[result].strip()}\n')


if __name__ == '__main__':
    main()
