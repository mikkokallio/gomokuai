import sys
import argparse
from app import App
from config import AI_PLAYERS


def main():
    '''Starts the app'''
    parser = argparse.ArgumentParser(description='Runs gomoku for two AI players',
                                     epilog=f'Player names must be from the following list:\n{list(AI_PLAYERS.keys())}')
    parser.add_argument('-a', '--alternate', action='store_true', help='plays the game twice with players switching colors')
    parser.add_argument('-r', '--repeat', type=int, metavar='n', default=1, help='repeats the game n times')
    parser.add_argument('-c', '--csv', action='store_true', help='hides normal output and instead prints only game result as a comma-separated string')
    parser.add_argument('-s', '--store', action='store_true', help='saves information about played games')
    parser.add_argument('player1', choices=AI_PLAYERS)
    parser.add_argument('player2', choices=AI_PLAYERS)
    args = parser.parse_args()
    for _ in range(args.repeat):
        app = App([args.player1, args.player2], 60, args.csv, args.store)
        app.run()
        if args.alternate:
            app = App([args.player2, args.player1], 60, args.csv, args.store)
            app.run()

if __name__ == '__main__':
    main()
    