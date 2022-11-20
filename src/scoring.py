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

OPENING_CONSTRAINTS = [
    (0, 0),
    (1, 2),
    (3, 4)
]

TABLES_FILE = 'games.csv'
