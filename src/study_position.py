from board import Board
from ai_player import AIPlayer


def main():
    board = Board(size=15)
    config = {'depth': 11, 'reach': 4, 'branching': 7, 'deepen': False, 'tables': None, 'random': False}
    ai = AIPlayer(config, board)

    state = '................................................................................................................X.O..............O...............X...............................................................................'
    state = '......................................................................X.........X..XOO.........O.OXXX.........O.X............O...................................................................................................'
    i = 0
    for y in range(15):
        for x in range(15):
            if state[i] != '.':
                board.add_piece(y, x, state[i])
            i += 1

    print(board)
    print(ai.heatmap)
    res = ai.get_move(board, True, None)
    print(res)

if __name__ == '__main__':
    main()
