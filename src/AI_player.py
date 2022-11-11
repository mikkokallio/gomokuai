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
        defenses = None
        self.player_two = player_two
        state = board.state
        if len(self.board.moves) > 0:
            y, x, _ = self.board.moves[-1]
            self.update_proximity_map(y, x)
            points, threat, defenses = self.evaluate_threat(self.board.state, y, x, PIECES[not player_two], PIECES[player_two])
            print('Threat: ', threat, 'Defend in positions: ', defenses)
        if len(defenses) == 0:
            moves = self.get_possible_moves(state, self.depth)[:self.limit_moves+8]
        else:
            moves = [(0, defense[0], defense[1]) for defense in defenses]
        print(moves)
        best_move, best_value = None, -999999
        with ProcessPoolExecutor() as ex:
            for move, value in zip(moves, ex.map(self.get_async_branch, moves)):
                print(value)
                if best_move is None or value > best_value:
                    best_value = value
                    best_move = move
        y, x = best_move[1:]
        self.update_proximity_map(y, x)
        print('Best: ',best_value)
        return (y, x)

    def update_proximity_map(self, y, x):
        n = self.board.size
        r = self.reach
        for yy in range(max(0, y-r), min(y+(r+1), n)):
            for xx in range(max(0, x-r), min(x+(r+1), n)):
                self.proximity_map[yy][xx] += 1

    def evaluate_threat(self, state, y, x, color, foe_color):
        '''Check if move completes 2s, 3s, 4s, or 5s'''
        threats = 0
        points, pp = 0, 2
        open_3, half_open_4 = 0, 0
        defenses = []
        for dir in DIRECTIONS:
            openings = []
            count, open, prev, gap = 1, 0, None, 0
            for sign in [-1, +1]:
                yy, xx, prev = y, x, None
                for _ in range(1, 5):
                    yy += sign * dir[0]
                    xx += sign * dir[1]
                    if yy < 0 or xx < 0 or yy >= self.board.size or xx >= self.board.size or state[yy][xx] == foe_color:
                        if prev == '.':
                            open += 1
                            pp -= 1
                        else:
                            pp -= 0.35
                        break
                    if state[yy][xx] == color:
                        if prev == '.':
                            gap += 1
                            pp -= 0.25
                        count += 1
                        prev = color
                    elif state[yy][xx] == '.':
                        if prev == '.':
                            open += 1.5
                            break
                        else:
                            openings.append((yy, xx))
                            prev = '.'
            pp = max(0, pp)
            #print(count, open, gap)
            if count == 2 and open == 2:
                points += 1 * open
            if count == 3:
                points += 10 * open
            if count == 4 and gap <= 2:
                points += 100 * open
            if count == 2 and open + gap >= 2.5:
                threats += 0.05
            elif count == 3 and open + gap in [1.5, 2]:
                threats += 0.25
            elif count == 3 and (open > 2 or open + gap >= 3):
#            elif count == 3 and (open > 2 or open >= 2 and gap == 1): <-- lost!
                threats += 2
                defenses.extend(openings)
            elif count == 4 and open + gap >= 1 and open + gap < 2:
                threats += 2
                defenses.extend(openings)
            elif count == 4 and open >= 2 and gap == 0:
                threats += 5
                defenses.extend(openings)
            elif count == 5 and gap == 0:
                #return (25, None)
                threats += 25
                points += 1000

            # TODO: 2x --xx--

        #if open_3 >= 2 or open_3 >= 1 and half_open_4 >= 1:
        if threats >= 4:
            points += 100
        return (points, threats, defenses)

    def get_possible_moves(self, state, depth):
        moves = []
        for y in range(self.board.get_size()):
            for x in range(self.board.get_size()):
                # TODO: Use either .get_size() or .size consistently!
                if state[y][x] == '.' and self.proximity_map[y][x] >= 1:
                    own, _, _ = self.evaluate_threat(state, y, x, PIECES[self.player_two], PIECES[not self.player_two])
                    #if own >= 1000:
                    #    return [(-99999, y, x)]
                    foe, _, _ = self.evaluate_threat(state, y, x, PIECES[not self.player_two], PIECES[self.player_two])
                    prio1 = -(1.1 * own + foe)
                    prio2 = -(1.4 * own + 0.7 * foe)
                    moves.append((max(prio1, prio2), y, x))
        return sorted(moves)


    def get_async_branch(self, move):
        child = copy.deepcopy(self.board.state)
        child[move[1]][move[2]] = PIECES[self.player_two]
        return self.minimax(child, move, self.depth, -999999, 999999, False)

    def minimax(self, node, move, depth, a, b, maxing):
        if self.board.is_winning_move(node, move[1], move[2], PIECES[not maxing * self.player_two]):
            return -1 if maxing else 1
        if depth == 0:
            #return 0
            _, threats, _ = self.evaluate_threat(node, move[1], move[2], PIECES[not maxing * self.player_two], PIECES[maxing * self.player_two])
            threats /= 10
            return -threats if maxing else threats
        v = -999999 if maxing else 999999
        for newmove in self.get_possible_moves(node, depth)[:self.limit_moves]:
            child = copy.deepcopy(node)
            child[newmove[1]][newmove[2]] = PIECES[maxing * self.player_two]
            recurse = self.minimax(child, newmove, depth-1, a, b, not maxing)
            v = max(v, recurse) if maxing else min(v, recurse)
            if maxing:
                a = max(a, v)
            else:
                b = min(b, v)
            if a >= b:
                return v
        return v
