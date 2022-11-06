import random
import copy

class AIPlayer:
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
                    moves.append((y, x))
        return moves

    def get_move(self, board):
        state = board.state
        moves = self.get_possible_moves(state)
        best_move, best_value = None, -999999
        for move in moves:
            child = copy.deepcopy(state)
            child[move[0]][move[1]] = self.color
            #print(child)
            value = self.min_value(child, move, self.depth, -999999, 999999)
            #print(value)
            if best_move is None or value > best_value:
                best_value = value
                best_move = move
        #print(best_value)
        # if board.is_legal_move(y, x, color):
        return best_move
            
    def max_value(self, node, move, depth, alpha, beta):
        #print(node, move, depth)
        if self.board.is_winning_move(node, move[0], move[1], self.opponent):
            return -1
        if sum([row.count('.') for row in node]) == 0 or depth == 0:
            return 0
        v = -999999
        for newmove in self.get_possible_moves(node):
            child = copy.deepcopy(node)
            child[newmove[0]][newmove[1]] = self.color
            v = max(v, self.min_value(child, newmove, depth-1, alpha, beta))
            alpha = max(alpha, v)
            if alpha >= beta:
                return v
        return v

    def min_value(self, node, move, depth, alpha, beta):
        #print(node, move, depth)
        if self.board.is_winning_move(node, move[0], move[1], self.color): 
            return 1
        if sum([row.count('.') for row in node]) == 0 or depth == 0:
            return 0
        v = +999999
        for newmove in self.get_possible_moves(node):
            child = copy.deepcopy(node)
            child[newmove[0]][newmove[1]] = self.opponent
            v = min(v, self.max_value(child, newmove, depth-1, alpha, beta))
            #[print(row) for row in child]
            #print(v)
            beta = min(beta, v)
            if alpha >= beta:
                return v
        return v
