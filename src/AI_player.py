import copy
from concurrent.futures import ProcessPoolExecutor
from board import PIECES, DIRECTIONS

class AIPlayer:
    def __init__ (self, depth, reach, limit_moves, board):
        self.depth = depth
        self.reach = reach
        self.limit_moves = limit_moves
        self.board = board
        self.player_two = None
        n = self.board.size
        self.proximity_map = [[0 for _ in range(n)] for _ in range(n)]
        self.proximity_map[int(n/2)][int(n/2)] = 1 # center square always available!

    def get_move(self, board, player_two):
        '''Asks AI to compute an optimal move, given board state'''
        defenses = []
        self.player_two = player_two
        state = board.state
        if len(self.board.moves) > 0:
            y, x, _ = self.board.moves[-1]
            self.update_proximity_map(y, x)
            threat, defenses = self.evaluate_threat(self.board.state, y, x, PIECES[not player_two], PIECES[player_two])
            #print('Threat: ', threat, 'Defend in positions: ', defenses)
        moves = self.get_possible_moves(state, defenses, True)[:self.limit_moves+8]
        if len(moves) == 1:
            y, x = moves[0][1:3]
        else:
            best_move, best_value = None, -999999
            with ProcessPoolExecutor() as ex:
                for move, value in zip(moves, ex.map(self.async_search_branch, moves)):
                    #print(value)
                    if best_move is None or value > best_value:
                        best_value = value
                        best_move = move
            y, x = best_move[1:3]
            self.update_proximity_map(y, x)
            #print('Best: ',best_value)
        return (y, x)

    def async_search_branch(self, move):
        '''Search game tree's first level in parallel'''
        child = copy.deepcopy(self.board.state)
        child[move[1]][move[2]] = PIECES[self.player_two]
        return self.minimax(child, move, self.depth, -999999, 999999, False)

    def update_proximity_map(self, y, x):
        '''Updates heatmap that determines which moves are considered'''
        n = self.board.size
        r = self.reach
        for yy in range(max(0, y-r), min(y+(r+1), n)):
            for xx in range(max(0, x-r), min(x+(r+1), n)):
                self.proximity_map[yy][xx] += 1

    def get_possible_moves(self, state, moves, max_node):
        '''Get a list of possible moves, given board state'''
        eval_moves = []
        if len(moves) == 0:
            n = self.board.get_size()
            moves = [(y, x) for x in range(n) for y in range(n) if state[y][x] == '.' and self.proximity_map[y][x] >= 1]
        for y, x in moves:
            own, defenses = self.evaluate_threat(state, y, x, PIECES[max_node * self.player_two], PIECES[not max_node * self.player_two])
            foe, _ = self.evaluate_threat(state, y, x, PIECES[not max_node * self.player_two], PIECES[max_node * self.player_two])
            if own >= 50:
                return [(0, y, x, own, [])]
            eval_moves.append((-(2 * own + foe), y, x, own, defenses))
        return sorted(eval_moves)

    def evaluate_threat(self, state, y, x, color, foe_color):
        '''Check if move creates a threat and score the new state'''
        threats, defenses = 0, []
        for dir in DIRECTIONS:
            count, open, gap, openings = 1, 0, 0, []
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
                            if len(openings) > 1:
                                openings.reverse() # blocking gaps is often more effective than open ends
                        count += 1
                        prev = color
                    elif state[yy][xx] == '.':
                        if prev == '.':
                            open += 1.5
                            break
                        else:
                            openings.append((yy, xx))
                            prev = '.'
            if count == 2 and open + gap >= 2.5:
                threats += 0.05
                threats += 0.01 * (open + gap)
            elif count == 3 and (open == 3 and gap == 0):
                threats += 2.50
                defenses.extend(openings)
            elif count == 3 and (open == 2.5 and gap == 0):
                threats += 2.25
                defenses.extend(openings)
            elif count == 3 and (open >= 2 and gap == 1):
                threats += 2.00
                defenses.extend(openings)
            elif count == 3 and (gap == 2) or (open == 2 and gap == 0):
                threats += 0.25
            elif count == 3 and (open + gap >= 2):
                threats += 0.25
            elif count == 4 and open >= 2 and gap == 0:
                threats += 5.00
                defenses.extend(openings)
            elif count == 4 and open + gap >= 1:
                threats += 2.75
                defenses.extend(openings)
            elif count == 5 and gap == 0:
                return (50, [])

            # TODO: 2x --xx--

        return (threats, defenses)

    def minimax(self, node, move, depth, a, b, max_node):
        '''Perform minimaxing with a-b pruning'''
        if self.board.is_winning_move(node, move[1], move[2], PIECES[not max_node * self.player_two]):
            return -1 if max_node else 1
        if depth == 0:
            threats, _ = self.evaluate_threat(node, move[1], move[2], PIECES[not max_node * self.player_two], PIECES[max_node * self.player_two])
            threats /= 10
            return -threats if max_node else threats
        v = -999999 if max_node else 999999
        for newmove in self.get_possible_moves(node, move[4], max_node)[:self.limit_moves]:
            child = copy.deepcopy(node)
            child[newmove[1]][newmove[2]] = PIECES[max_node * self.player_two]
            recurse = self.minimax(child, newmove, depth-1, a, b, not max_node)
            v = max(v, recurse) if max_node else min(v, recurse)
            if max_node:
                a = max(a, v)
            else:
                b = min(b, v)
            if a >= b:
                return v
        return v
