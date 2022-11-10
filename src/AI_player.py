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

    def get_possible_moves(self, state, depth):
        moves = []
        for y in range(self.board.get_size()):
            for x in range(self.board.get_size()):
                # TODO: Use either .get_size() or .size consistently!
                if state[y][x] == '.' and self.proximity_map[y][x] >= 1:
                    own = self.evaluate_move(state, y, x, PIECES[self.player_two], PIECES[not self.player_two])
                    foe = self.evaluate_move(state, y, x, PIECES[not self.player_two], PIECES[self.player_two])
                    prio = -(1.1 * own + foe)
                    moves.append((prio, y, x))
        return sorted(moves)

    def evaluate_move(self, state, y, x, color, foe_color):
        '''Check if move completes 2s, 3s, 4s, or 5s'''
        points = 0
        open_3 = 0
        half_open_4 = 0
        for dir in DIRECTIONS:
            count, open, prev, gap = 1, 2, None, 0
            for sign in [-1, +1]:
                yy, xx = y, x
                prev = None
                for _ in range(1, 5):
                    yy += sign * dir[0]
                    xx += sign * dir[1]
                    if yy < 0 or xx < 0 or yy >= self.board.size or xx >= self.board.size or state[yy][xx] == foe_color:
                        if prev != '.':
                            open -= 1
                        else:
                            open -= 0.35 # Only one spot left!
                        break
                    if state[yy][xx] == color:
                        if prev == '.':
                            gap += 1
                            open -= 0.25
                        count += 1
                        prev = color
                    elif state[yy][xx] == '.':
                        if prev == '.':
                            break
                        prev = '.'
            open = max(0, open)
            if count == 2 and open == 2:
                points += 1 * open
            if count == 3:
                points += 10 * open
                if open == 2 and gap == 0:
                    open_3 += 1
            # TODO: rules for 4 -- ?
            # TODO: rules for double 3 open & double 4 (semi-)open
            if count == 4 and gap <= 2:
                points += 100 * open
                if open == 1 and gap == 0:
                    half_open_4 += 1
            if count == 5 and gap == 0:
                points += 1000
        if open_3 >= 2 or open_3 >= 1 and half_open_4 >= 1:
            points += 100
            #print(f'OUCH! {y} {x}')
            #[print(row) for row in state]

        return points

    def update_proximity_map(self, y, x):
        n = self.board.size
        r = self.reach
        for yy in range(max(0, y-r), min(y+(r+1), n)):
            for xx in range(max(0, x-r), min(x+(r+1), n)):
                self.proximity_map[yy][xx] += 1

    def get_async_branch(self, move):
        child = copy.deepcopy(self.board.state)
        child[move[1]][move[2]] = PIECES[self.player_two]
        return self.minimax(child, move, self.depth, -999999, 999999, False)
    
    def get_move(self, board, player_two):
        if len(self.board.moves) > 0:            
            y, x, _ = self.board.moves[-1]
            self.update_proximity_map(y, x)
        self.player_two = player_two
        state = board.state
        moves = self.get_possible_moves(state, self.depth)[:self.limit_moves+2]
        print(moves)
        best_move, best_value = None, -999999
        with ProcessPoolExecutor() as ex:
            for move, value in zip(moves, ex.map(self.get_async_branch, moves)):
                if best_move is None or value > best_value:
                    best_value = value
                    best_move = move
        y, x = best_move[1:]
        self.update_proximity_map(y, x)
        #[print(row) for row in self.proximity_map]
        print(best_value)
        return (y, x)

    def minimax(self, node, move, depth, a, b, maxing):
        if self.board.is_winning_move(node, move[1], move[2], PIECES[not maxing * self.player_two]):
            return -1 if maxing else 1
        if sum([row.count('.') for row in node]) == 0 or depth == 0:
            return 0
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
