from time import perf_counter
import csv
from board import Board
from human_player import HumanPlayer
from ai_player import AIPlayer
from config import CENTER, SIZE, PIECES, BLACK, EMPTY, TABLES_FILE, OPENING_CONSTRAINTS, AI_PLAYERS
states = set()

class App:
    def __init__(self, names):
        self.board = Board(SIZE)
        self.names = names
        self.players = [
            AIPlayer(AI_PLAYERS[names[0]], self.board),
            AIPlayer(AI_PLAYERS[names[1]], self.board)
            ]
        self.winner = EMPTY
        self.clocks = [0.0, 0.0]
        self.silent = False

    def run(self):
        '''Run game loop'''
        end = '\t' if self.silent else '\n'
        print(f'{self.names[0]} vs {self.names[1]}', end=end)

        player_turn = BLACK

        for turn in range(SIZE**2 - 165):
            if not self.silent: print(self.board)
            try:
                win = self.play_turn(self.board, self.players, turn, player_turn, self.clocks)
                if win:
                    if not self.silent: print(self.board)
                    print(f'{self.names[player_turn]} ({PIECES[player_turn]}) wins on turn {turn}!', end=end)
                    print(f'X time: {self.clocks[0]} O time: {self.clocks[1]}')
                    winner = PIECES[player_turn]
                    break
                player_turn = not player_turn
                if turn <= 10:
                    states.add(''.join([''.join(row) for row in self.board.state]))
            except ValueError as error:
                print('Invalid move!')
                print(error)

        if winner == EMPTY:
            print('Draw!')

        self.store_route(states, winner)

    def get_constraint(self, min_dist, max_dist):
        '''For initial moves, get list of allowed moves'''
        moves = []
        for y in range(CENTER-max_dist, CENTER+max_dist+1):
            for x in range(CENTER-max_dist, CENTER+max_dist+1):
                lim_1, lim_2 = CENTER-min_dist, CENTER+min_dist
                if not (y > lim_1 and y < lim_2 and x > lim_1 and x < lim_2):
                    moves.append((y, x))
        return moves

    def play_turn(self, board, players, turn, player_turn, clocks):
        clock_start = perf_counter()
        if turn < len(OPENING_CONSTRAINTS):
            if not self.silent:
                print(f'Place {PIECES[player_turn]} between {OPENING_CONSTRAINTS[turn]} steps from the center')
            y, x = players[int(player_turn)].get_move(board, player_turn, self.get_constraint(*OPENING_CONSTRAINTS[turn]))
        else:
            y, x = players[int(player_turn)].get_move(board, player_turn, None)
        turn_time = perf_counter() - clock_start
        clocks[player_turn] += turn_time
        return board.add_piece(y, x, color=PIECES[player_turn])

    def store_route(self, states, winner):
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
