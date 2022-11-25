import sys
from app import App
from config import AI_PLAYERS


def main():
    '''Starts the app'''
    names = sys.argv[-2:]
    if len(names) < 2 or any([name not in AI_PLAYERS for name in names]):
        print("Supply two names from the following list:")
        print(list(AI_PLAYERS.keys()))
        sys.exit()

    app = App(names)
    app.run()

if __name__ == '__main__':
    main()
    