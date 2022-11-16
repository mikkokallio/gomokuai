from board import EMPTY


class ProximityList:
    def __init__(self, state, size, reach, moves):
        '''Set up list to control moves and ensure that pre-game moves are included'''
        self.spaces = set()
        self.size = size
        self.reach = reach
        # center of board always available!
        self.update(state, int(size/2), int(size/2), False)
        for move in moves:
            self.update(state, move[0], move[1])

    def get(self):
        '''Get list of available places nearby'''
        return self.spaces

    def update(self, state, y, x, remove=True):
        '''Updates list that determines which moves are considered'''
        for y_pos in range(max(0, y-self.reach), min(y+(self.reach+1), self.size)):
            for x_pos in range(max(0, x-self.reach), min(x+(self.reach+1), self.size)):
                if state is None or state[y_pos][x_pos] == EMPTY:
                    self.spaces.add((y_pos, x_pos))
        if remove and (y, x) in self.spaces:
            self.spaces.remove((y, x))
