class HumanPlayer:
    def get_move(self):
        '''Prompt human player to give coordinates for next move'''
        coords = input('Give y and x: ')
        y, x = [int(n) for n in coords.split(' ')]
        return (y, x)
