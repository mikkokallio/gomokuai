from time import perf_counter
import csv
from board import Board
#from human_player import HumanPlayer
from ai_player import AIPlayer
from config import CENTER, SIZE, PIECES, BLACK, WHITE, EMPTY, TABLES_FILE, CONSTRAINTS, AI_PLAYERS


class App:
    def __init__(self, names, rounds, silent, save, colors):
        self.board = Board(SIZE, colors)
        self.names = names
        self.rounds = rounds
        self.players = [
            AIPlayer(AI_PLAYERS[names[0]], self.board),
            AIPlayer(AI_PLAYERS[names[1]], self.board)
            ]
        self.clocks = [0.0, 0.0]
        self.silent = silent
        self.save = save

    def run(self):
        '''Run game loop'''
        if not self.silent:
            print(f'{self.names[0]} vs {self.names[1]}')

        player_turn = BLACK
        winner = None
        states = set()

        for turn in range(self.rounds):
            if not self.silent:
                print(self.board)
            try:
                win = self.play_turn(self.board, self.players, turn, player_turn, self.clocks)
                if win:
                    winner = player_turn
                    break
                player_turn = not player_turn
                if turn <= 10:
                    states.add(''.join([''.join(row) for row in self.board.state]))
            except ValueError as error:
                print('Invalid move!')
                print(error)

        self.declare_winner(winner, turn)
        if self.save:
            self.store_route(states, winner)
        return f'{self.names[BLACK]},{self.names[WHITE]},{self.clocks[BLACK]},{self.clocks[WHITE]},{self.names[winner] if winner is not None else "draw"},{turn}'

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
        '''Play and clock one player's turn'''
        clock_start = perf_counter()
        if turn < len(CONSTRAINTS):
            if not self.silent:
                print(f'Place {PIECES[player_turn]} {CONSTRAINTS[turn]} steps from the center')
            y, x = players[int(player_turn)].get_move(board, player_turn, self.get_constraint(*CONSTRAINTS[turn]))
        else:
            y, x = players[int(player_turn)].get_move(board, player_turn, None)
        turn_time = perf_counter() - clock_start
        clocks[player_turn] += turn_time
        return board.add_piece(y, x, color=PIECES[player_turn])

    def declare_winner(self, winner, turn):
        if not self.silent:
            print(self.board)
            if winner is None:
                print('Draw!')
            else:
                print(f'{self.names[winner]} ({PIECES[winner]}) wins on turn {turn}!')
            print(f'X time: {self.clocks[0]} O time: {self.clocks[1]}')

    def store_route(self, states, winner):
        '''Save data about finished game'''
        with open(TABLES_FILE, encoding='utf8', newline='\n') as file:
            reader = csv.reader(file)
            next(reader)
            results = dict(reader)

        for state in states:
            if state in results:
                results[state] += PIECES[winner]
            else:
                results[state] = EMPTY + PIECES[winner]

        with open(TABLES_FILE, 'w', encoding='utf8') as file:
            for result in results.keys():
                file.write(f'{result},{results[result].strip()}\n')
