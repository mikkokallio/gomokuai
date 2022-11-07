import random
import copy

class AIPlayerV1:
    def __init__ (self, depth, board, color, other):
        self.depth = depth
        self.board = board
        self.color = color
        self.opponent = other
    
    def get_possible_moves(self, state):
        moves = []
        for y in range(self.board.get_size()):
            for x in range(self.board.get_size()):
                if state[y][x] == '.':
                    # 0... size
                    prio = abs(self.board.size/2-y) + abs(self.board.size/2-x)
                    # TODO: keep tracks of "center of mass"
                    moves.append((prio, y, x))
        return sorted(moves)

    def get_move(self, board):
        state = board.state
        moves = self.get_possible_moves(state)
        best_move, best_value = None, -999999
        for move in moves:
            child = copy.deepcopy(state)
            child[move[1]][move[2]] = self.color
            #print(child)
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
        if self.board.is_winning_move(node, move[1], move[2], self.opponent):
            return -1
        if sum([row.count('.') for row in node]) == 0 or depth == 0:
            return 0
        v = -999999
        for newmove in self.get_possible_moves(node):
            child = copy.deepcopy(node)
            child[newmove[1]][newmove[2]] = self.color
            v = max(v, self.min_value(child, newmove, depth-1, alpha, beta))
            alpha = max(alpha, v)
            if alpha >= beta:
                return v
        return v

    def min_value(self, node, move, depth, alpha, beta):
        #print(node, move, depth)
        if self.board.is_winning_move(node, move[1], move[2], self.color): 
            return 1
        if sum([row.count('.') for row in node]) == 0 or depth == 0:
            return 0
        v = +999999
        for newmove in self.get_possible_moves(node):
            child = copy.deepcopy(node)
            child[newmove[1]][newmove[2]] = self.opponent
            v = min(v, self.max_value(child, newmove, depth-1, alpha, beta))
            #[print(row) for row in child]
            #print(v)
            beta = min(beta, v)
            if alpha >= beta:
                return v
        return v
