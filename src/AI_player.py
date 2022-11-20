import copy
from concurrent.futures import ProcessPoolExecutor
import random
import csv
from proximity_list import ProximityList
from scoring import SCORES, VICTORY, OPEN_FOUR, DOUBLE_THREAT, OWN, THREAT_LEVELS, PIECES, DIRECTIONS, EMPTY, TABLES_FILE

BIG_NUM = 999999


class AIPlayer:
    def __init__(self, config, board):
        self.depth = config['depth']
        self.deepen = config['deepen']
        self.reach = config['reach']
        self.limit_moves = config['branching']
        self.board = board
        self.size = board.size
        self.white = None
        self.heatmap = None
        self.tables = self.load_tables(config['tables'])
        self.randomized = config['random']

    def load_tables(self, use_table):
        if use_table:
            with open(TABLES_FILE, encoding='utf8', newline='\n') as file:
                reader = csv.reader(file)
                next(reader)
                return dict(reader)
        else:
            return None

    def get_move(self, board, white, constraint):
        '''Asks AI to compute an optimal move, given board state'''
        self.white = white
        state = board.state
        if self.heatmap is None:
            self.heatmap = ProximityList(state, self.size, self.reach, self.board.moves)
        elif len(self.board.moves) > 0:
            y, x, _ = self.board.moves[-1]
            self.heatmap.update(state, y, x)
        if constraint is not None:
            moves = self.get_possible_moves(state, [random.choice(constraint)], True)[:self.limit_moves+10]
        else:
            moves = self.get_possible_moves(state, None, True)[:self.limit_moves+10]
        #print(moves)
        if len(moves) == 1:
            y, x = moves[0][1:3]
        else:
            best_move, best_value = None, -999999
            with ProcessPoolExecutor() as ex:
                for move, value in zip(moves, ex.map(self.async_search_branch, moves)):
                    #print(move, value)
                    if best_move is None or value > best_value:
                        best_value, best_move = value, move
            y, x = best_move[1:3]
        self.heatmap.update(state, y, x)
        #print(y, x)
        return (y, x)

    def async_search_branch(self, move):
        '''Search game tree's first level in parallel'''
        child = copy.deepcopy(self.board.state)
        child[move[1]][move[2]] = PIECES[self.white]
        return self.minimax(child, move, self.depth, -BIG_NUM, BIG_NUM, False)

    def get_possible_moves(self, state, moves, max_node):
        '''Get a list of possible moves, given board state'''
        eval_moves = []
        if moves is None:
            moves = [move for move in self.heatmap.get() if state[move[0]][move[1]] == EMPTY]
        high_score = 0

        for y, x in moves:
            own = self.evaluate_threat(
                state, y, x, PIECES[max_node == self.white], PIECES[max_node != self.white])
            if own >= VICTORY:
                return [(0, y, x)]
            foe = self.evaluate_threat(
                state, y, x, PIECES[max_node != self.white], PIECES[max_node == self.white])
            score = OWN * own + foe
            if score > high_score:
                high_score = score
            eval_moves.append((score, y, x))
        for level in THREAT_LEVELS:
            if high_score >= level:
                threshold = level
                break
            threshold = 0

        return sorted([move for move in eval_moves if move[0] >= threshold], reverse=True)

    def evaluate_threat(self, state, y, x, color, foe_color):
        '''Check if move creates a threat and score the new state'''
        threats = 0
        for line in DIRECTIONS:
            count, ends, gap = 1, 0, 0
            for sign in [-1, +1]:
                y_pos, x_pos, prev = y, x, None
                for _ in range(6):
                    y_pos += sign * line[0]
                    x_pos += sign * line[1]
                    if y_pos < 0 or x_pos < 0 or y_pos >= self.size or x_pos >= self.size or state[y_pos][x_pos] == foe_color:
                        if prev == EMPTY:
                            ends += 1
                        break
                    if state[y_pos][x_pos] == color:
                        if prev == EMPTY:
                            gap += 1
                        count += 1
                        prev = color
                    elif state[y_pos][x_pos] == EMPTY:
                        if prev == EMPTY:
                            ends += 1.5
                            break
                        prev = EMPTY
            for score in SCORES.get(count, []):
                if ends >= score[0] and gap == score[1]:
                    threats += score[2]
                    break
            threats += 0.01 * (ends + gap) * count
            if threats >= VICTORY:
                return VICTORY
        if threats >= OPEN_FOUR:
            return OPEN_FOUR
        if threats >= 4:
            return DOUBLE_THREAT
        if self.randomized:
            threats += (threats/10 * random.random())
        return threats

    def minimax(self, node, move, depth, alfa, beta, max_node):
        '''Perform minimaxing with a-b pruning'''
        if self.board.is_winning_move(node, move[1], move[2], PIECES[max_node != self.white]):
            return -1 if max_node else 1
        if self.tables is not None and len(self.board.moves) + (self.depth - depth) <= 15:
            hashable = ''.join([''.join(row) for row in node])
            result = self.tables.get(hashable, '').strip()
            if result != '':
                value = (result.count(PIECES[self.white == max_node]) - result.count(PIECES[self.white != max_node]))/max(10, len(result))
                if value != 0.0:
                    return value if max_node else -value
        if depth == 0:
            threats = self.evaluate_threat(
                node, move[1], move[2], PIECES[max_node != self.white], PIECES[max_node == self.white]) / 101
            return -threats if max_node else threats
        value = -BIG_NUM if max_node else BIG_NUM
        newmoves = self.get_possible_moves(node, None, max_node)[:self.limit_moves]
        deepen = len(newmoves) == 1 and self.deepen
        for newmove in newmoves:
            child = copy.deepcopy(node)
            child[newmove[1]][newmove[2]] = PIECES[max_node == self.white]
            recurse = self.minimax(child, newmove, depth-1+deepen, alfa, beta, not max_node)
            value = max(value, recurse) if max_node else min(value, recurse)
            if max_node:
                alfa = max(alfa, value)
            else:
                beta = min(beta, value)
            if alfa >= beta:
                return value
        return value
