class Heatmap:
    def __init__(self, size, reach, moves):
        '''Set up map to control moves and ensure that pre-game moves are included'''
        self.heatmap = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        self.reach = reach
        self.update(int(size/2), int(size/2)) # center of board always available!
        for move in moves:
            self.update(move[0], move[1])

    def get(self):
        '''Get heatmap'''
        return self.heatmap

    def update(self, y, x):
        '''Updates heatmap that determines which moves are considered'''
        for yy in range(max(0, y-self.reach), min(y+(self.reach+1), self.size)):
            for xx in range(max(0, x-self.reach), min(x+(self.reach+1), self.size)):
                self.heatmap[yy][xx] += 1
