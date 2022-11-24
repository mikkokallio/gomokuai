from time import perf_counter
import csv
from board import Board
from human_player import HumanPlayer
from ai_player import AIPlayer
from config import CENTER, SIZE, PIECES, BLACK, EMPTY, TABLES_FILE, OPENING_CONSTRAINTS
states = set()

def main():
    '''Set up board and run game loop'''
    board = Board(SIZE)
    black = {'depth': 9, 'reach': 2, 'branching': 3, 'deepen': True, 'tables': None, 'random': True}
    white = {'depth': 9, 'reach': 2, 'branching': 3, 'deepen': True, 'tables': TABLES_FILE, 'random': False}
    players = [AIPlayer(black, board), AIPlayer(white, board)]
    #players = [AIPlayer(white, board), HumanPlayer()]
    player_turn = BLACK
    winner = EMPTY
    clocks = [0.0, 0.0]

    for turn in range(SIZE**2 - 165):
        #board.print()
        try:
            win = play_turn(board, players, turn, player_turn, clocks)
            if win:
                #board.print()
                print(f'{PIECES[player_turn]} wins on turn {turn}! Clocks: X {clocks[0]} O {clocks[1]}')
                #print('X time:', clocks[0], 'O time:', clocks[1])
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

    store_route(states, winner)

def get_constraint(min_dist, max_dist):
    '''For initial moves, get list of allowed moves'''
    moves = []
    for y in range(CENTER-max_dist, CENTER+max_dist+1):
        for x in range(CENTER-max_dist, CENTER+max_dist+1):
            lim_1, lim_2 = CENTER-min_dist, CENTER+min_dist
            if not (y > lim_1 and y < lim_2 and x > lim_1 and x < lim_2):
                moves.append((y, x))
    return moves

def play_turn(board, players, turn, player_turn, clocks):
    clock_start = perf_counter()
    if turn < len(OPENING_CONSTRAINTS):
        #print(f'Place {PIECES[player_turn]} between {OPENING_CONSTRAINTS[turn]} steps from the center')
        y, x = players[int(player_turn)].get_move(board, player_turn, get_constraint(*OPENING_CONSTRAINTS[turn]))
    else:
        y, x = players[int(player_turn)].get_move(board, player_turn, None)
    turn_time = perf_counter() - clock_start
    clocks[player_turn] += turn_time
    return board.add_piece(y, x, color=PIECES[player_turn])

def store_route(states, winner):
    with open(TABLES_FILE, encoding='utf8', newline='\n') as file:
        reader = csv.reader(file)
        next(reader)
        results = dict(reader)

    for state in states:
        if state in results:
            results[state] += winner
        else:
            results[state] = EMPTY + winner

    with open(TABLES_FILE, 'w', encoding='utf8') as file:
        for result in results.keys():
            file.write(f'{result},{results[result].strip()}\n')


if __name__ == '__main__':
    main()
