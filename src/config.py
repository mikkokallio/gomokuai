SCORES = {
    2: [
        (2.5, 0, 0.05),
        (1.5, 1, 0.05),
    ],
    3: [
        (3, 0, 2.50),
        (2.5, 0, 2.25),
        (2, 1, 2.00),
        (0, 2, 0.25),
        (2, 0, 0.25),
        (1, 1, 0.25),
    ],
    4: [
        (2, 0, 100),
        (1, 0, 2.75),
        (0, 1, 2.75),
    ],
    5: [
        (0, 0, 1000),
    ]
}

VICTORY = 1000
OPEN_FOUR = 100
DOUBLE_THREAT = 10
OWN = 2

THREAT_LEVELS = [
    VICTORY,
    OWN * OPEN_FOUR,
    OPEN_FOUR,
    OWN * DOUBLE_THREAT,
    DOUBLE_THREAT]

SIZE = 15
CENTER = int(SIZE/2)
BLACK, WHITE = False, True

PIECES = {False: 'X', True: 'O'}
EMPTY = '.'
ROW = 5
DIRECTIONS = [(1, 0), (0, 1), (1, 1), (-1, 1)]

CONSTRAINTS = [
    (0, 0),
    (1, 2),
    (3, 3)
]

TABLES_FILE = 'games.csv'

AI_PLAYERS = {
    'Tester': {'depth': 3, 'reach': 2, 'branching': 3, 'deepen': False,
               'tables': None, 'random': False},
    'WeakAI': {'depth': 5, 'reach': 2, 'branching': 3, 'deepen': True,
               'tables': None, 'random': True},
    'WeakAI2': {'depth': 5, 'reach': 3, 'branching': 5, 'deepen': True,
               'tables': None, 'random': True},
    'AverageAI': {'depth': 5, 'reach': 2, 'branching': 4, 'deepen': False,
               'tables': None, 'random': True},
    'AverageAI2': {'depth': 5, 'reach': 5, 'branching': 9, 'deepen': False,
               'tables': None, 'random': True},
    'Robert': {'depth': 3, 'reach': 13, 'branching': 13, 'deepen': True,
               'tables': None, 'random': True},
    'Anna': {'depth': 4, 'reach': 3, 'branching': 7, 'deepen': True,
             'tables': TABLES_FILE, 'random': True},
    'Donald': {'depth': 4, 'reach': 3, 'branching': 7, 'deepen': True,
               'tables': None, 'random': True},
    'Maisie': {'depth': 7, 'reach': 2, 'branching': 3, 'deepen': True,
               'tables': TABLES_FILE, 'random': True},
    'Andrew': {'depth': 7, 'reach': 2, 'branching': 3, 'deepen': True,
               'tables': TABLES_FILE, 'random': True},
    'Norma': {'depth': 7, 'reach': 2, 'branching': 3, 'deepen': True,
              'tables': None, 'random': True},
    'Pierre': {'depth': 11, 'reach': 2, 'branching': 3, 'deepen': False,
               'tables': None, 'random': True},
}
