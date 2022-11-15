import copy
from concurrent.futures import ProcessPoolExecutor
from heatmap import Heatmap
from board import PIECES, DIRECTIONS
from scoring import SCORES, VICTORY, OPEN_FOUR, DOUBLE_THREAT, OWN, THREAT_LEVELS

BIG_NUM = 999999

class AIPlayer:
    def __init__ (self, depth, reach, limit_moves, board):
        self.depth = depth
        self.reach = reach
        self.limit_moves = limit_moves
        self.board = board
        self.player_two = None
        self.heatmap = None

    def get_move(self, board, player_two):
        '''Asks AI to compute an optimal move, given board state'''
        self.player_two = player_two
        state = board.state
        if self.heatmap is None:
            self.heatmap = Heatmap(board.size, self.reach, self.board.moves)
        elif len(self.board.moves) > 0:
            y, x, _ = self.board.moves[-1]
            self.heatmap.update(y, x)
        moves = self.get_possible_moves(state, True)[:self.limit_moves+8]
        print(moves)
        if len(moves) == 1:
            y, x = moves[0][1:3]
        else:
            best_move, best_value = None, -999999
            with ProcessPoolExecutor() as ex:
                for move, value in zip(moves, ex.map(self.async_search_branch, moves)):
                    print(move, value)
                    if best_move is None or value > best_value:
                        best_value, best_move = value, move
            y, x = best_move[1:3]
        self.heatmap.update(y, x)
        return (y, x)

    def async_search_branch(self, move):
        '''Search game tree's first level in parallel'''
        child = copy.deepcopy(self.board.state)
        child[move[1]][move[2]] = PIECES[self.player_two]
        return self.minimax(child, move, self.depth, -BIG_NUM, BIG_NUM, False)

    def get_possible_moves(self, state, max_node):
        '''Get a list of possible moves, given board state'''
        eval_moves = []
        n = self.board.get_size()
        moves = [(y, x) for x in range(n) for y in range(n) if state[y][x] == '.' and self.heatmap.get()[y][x] >= 1]
        high_score = 0

        for y, x in moves:
            own = self.evaluate_threat(state, y, x, PIECES[max_node == self.player_two], PIECES[max_node != self.player_two])
            if own >= VICTORY:
                return [(0, y, x)]
            foe = self.evaluate_threat(state, y, x, PIECES[max_node != self.player_two], PIECES[max_node == self.player_two])
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
        for dir in DIRECTIONS:
            count, open, gap = 1, 0, 0
            for sign in [-1, +1]:
                yy, xx, prev = y, x, None
                for _ in range(1, 7):
                    yy += sign * dir[0]
                    xx += sign * dir[1]
                    if yy < 0 or xx < 0 or yy >= self.board.size or xx >= self.board.size or state[yy][xx] == foe_color:
                        if prev == '.':
                            open += 1
                        break
                    if state[yy][xx] == color:
                        if prev == '.':
                            gap += 1
                        count += 1
                        prev = color
                    elif state[yy][xx] == '.':
                        if prev == '.':
                            open += 1.5
                            break
                        else:
                            prev = '.'
            for score in SCORES:
                if count == score[0] and open >= score[1] and gap == score[2]:
                    threats += score[3]
                    break
            threats += 0.01 * (open + gap) * count
            if threats >= VICTORY:
                return VICTORY
        if threats >= OPEN_FOUR:
            return OPEN_FOUR
        if threats >= 4:
            return DOUBLE_THREAT
        return threats

    def minimax(self, node, move, depth, a, b, max_node):
        '''Perform minimaxing with a-b pruning'''
        if self.board.is_winning_move(node, move[1], move[2], PIECES[max_node != self.player_two]):
            return -1 if max_node else 1
        if depth == 0:
            threats = self.evaluate_threat(node, move[1], move[2], PIECES[max_node != self.player_two], PIECES[max_node == self.player_two]) / 100
            return -threats if max_node else threats
        v = -BIG_NUM if max_node else BIG_NUM
        for newmove in self.get_possible_moves(node, max_node)[:self.limit_moves]:
            child = copy.deepcopy(node)
            child[newmove[1]][newmove[2]] = PIECES[max_node == self.player_two]
            recurse = self.minimax(child, newmove, depth-1, a, b, not max_node)
            v = max(v, recurse) if max_node else min(v, recurse)
            if max_node:
                a = max(a, v)
            else:
                b = min(b, v)
            if a >= b:
                return v
        return v
