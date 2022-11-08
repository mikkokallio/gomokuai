import random
import copy
from board import PIECES, DIRECTIONS

class AIPlayerV2:
    def __init__ (self, depth, board):
        self.depth = depth
        self.board = board
        self.player_two = None
    
    def get_possible_moves(self, state):
        n = self.board.size
        # TODO: Movemap updated when moves happen rather than creating a new one each time?
        # Requires that engine gives opponent's last move, can be done
        # TODO: Move movemap generation to its own method
        movemap = [[0 for _ in range(n)] for _ in range(n)]
        movemap[int(n/2)][int(n/2)] = 1 # center square always available!
        for y in range(self.board.get_size()):
            for x in range(self.board.get_size()):
                if state[y][x] != '.':
                    for yy in range(max(0, y-1), min(y+2, n)):
                        for xx in range(max(0, x-1), min(x+2, n)):
                            movemap[yy][xx] += 1 # Higher prio if higher number?

        #[print(row) for row in state]
        #[print(row) for row in movemap]
        moves = []
        for y in range(self.board.get_size()):
            for x in range(self.board.get_size()):
                # TODO: Use either .get_size() or .size consistently!
                if state[y][x] == '.' and movemap[y][x] >= 1:
                    # 0... size
                    #prio = abs(self.board.size/2-y) + abs(self.board.size/2-x)
                    #prio = -movemap[y][x]
                    own = self.evaluate_move(state, y, x, PIECES[self.player_two])
                    foe = self.evaluate_move(state, y, x, PIECES[not self.player_two])
                    prio = -(2 * own + foe)
                    moves.append((prio, y, x))
        return sorted(moves)[:10]

    def evaluate_move(self, state, y, x, color):
        '''Check if move completes 2s, 3s, 4s, or 5s'''
        points = 0
        for dir in DIRECTIONS:
            count = 1
            for sign in [-1, +1]:
                yy, xx = y, x
                for _ in range(5):
                    yy += sign * dir[0]
                    xx += sign * dir[1]
                    if yy < 0 or xx < 0 or yy >= self.board.size or xx >= self.board.size:
                        break
                    if state[yy][xx] == color:
                        count +=1
                    else:
                        break
            if count == 2:
                points += 1
            if count == 3:
                points += 10
            if count == 4:
                points += 100
            if count == 5:
                points += 1000
        return points

    def get_move(self, board, player_two):
        self.player_two = player_two
        state = board.state
        moves = self.get_possible_moves(state)
        print(moves)
        best_move, best_value = None, -999999
        for move in moves:
            child = copy.deepcopy(state)
            child[move[1]][move[2]] = PIECES[self.player_two]
            #[print(row) for row in child]
            if self.board.is_winning_move(state, move[1], move[2], PIECES[self.player_two]):
                return move[1:]

            value = self.min_value(child, move, self.depth, -999999, 999999)
            #print(value)
            if best_move is None or value > best_value:
                best_value = value
                best_move = move
        #print(best_value)
        # if board.is_legal_move(y, x, color):
        return best_move[1:]
            
    def max_value(self, node, move, depth, alpha, beta):
        #print(node, move, depth)
        if self.board.is_winning_move(node, move[1], move[2], PIECES[not self.player_two]):
            return -1 - depth # Protect against quick losses
        if sum([row.count('.') for row in node]) == 0:
            return 0
        if depth == 0:
            return 0
        v = -999999
        for newmove in self.get_possible_moves(node):
            child = copy.deepcopy(node)
            child[newmove[1]][newmove[2]] = PIECES[self.player_two]
            v = max(v, self.min_value(child, newmove, depth-1, alpha, beta))
            alpha = max(alpha, v)
            if alpha >= beta:
                return v
        return v

    def min_value(self, node, move, depth, alpha, beta):
        #print(node, move, depth)
        if self.board.is_winning_move(node, move[1], move[2], PIECES[self.player_two]): 
            return 1 + depth # Prefer quick wins
        if sum([row.count('.') for row in node]) == 0:
            return 0
        if depth == 0:
            return 0
        v = +999999
        for newmove in self.get_possible_moves(node):
            child = copy.deepcopy(node)
            child[newmove[1]][newmove[2]] = PIECES[not self.player_two]
            v = min(v, self.max_value(child, newmove, depth-1, alpha, beta))
            #[print(row) for row in child]
            #print(v)
            beta = min(beta, v)
            if alpha >= beta:
                return v
        return v
