import random
import copy

class AIPlayer:
    def __init__ (self, depth, board, color, other):
        self.depth = depth
        self.board = board
        self.color = color
        self.opponent = other
    
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
                    for yy in range(max(0, y-1), min(y+2, n-1)):
                        for xx in range(max(0, x-1), min(x+2, n-1)):
                            movemap[yy][xx] += 1 # Higher prio if higher number?

        #[print(row) for row in state]
        #[print(row) for row in movemap]
        moves = []
        for y in range(self.board.get_size()):
            for x in range(self.board.get_size()):
                # TODO: Use either .get_size() or .size consistently!
                # Keep state of a "proximity map"? I.e. when a piece is placed,
                # update map to include positions within x intersections (and exclude occupied positions)
                if state[y][x] == '.' and movemap[y][x] >= 1:
                    # 0... size
                    #prio = abs(self.board.size/2-y) + abs(self.board.size/2-x)
                    prio = -movemap[y][x]
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
            #[print(row) for row in child]
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
            return -1 - depth # Protect against quick losses
        if sum([row.count('.') for row in node]) == 0:
            return 0
        if depth == 0:
            return -random.random()
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
            return 1 + depth # Prefer quick wins
        if sum([row.count('.') for row in node]) == 0:
            return 0
        if depth == 0:
            return random.random()
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
