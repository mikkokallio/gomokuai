SCORES = [  # TODO: dict with count as key then list as value?
    (2, 2.5, 0, 0.05),
    (2, 1.5, 1, 0.05),
    (3, 3, 0, 2.50),
    (3, 2.5, 0, 2.25),
    (3, 2, 1, 2.00),
    (3, 0, 2, 0.25),
    (3, 2, 0, 0.25),
    (3, 1, 1, 0.25),
    (4, 2, 0, 100),
    (4, 1, 0, 2.75),
    (4, 0, 1, 2.75),
    (5, 0, 0, 1000)
]

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
