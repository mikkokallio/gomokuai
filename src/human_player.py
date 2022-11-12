class HumanPlayer:
    def get_move(self, board, player_two):
        '''Prompt human player to give coordinates for next move'''
        coords = input('Give y and x: ')
        y, x = [int(n) for n in coords.split(' ')]
        return (y, x)
