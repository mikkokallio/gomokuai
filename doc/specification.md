# Project specification

* I'm a student in tietojenkäsittelytieteen kandidaattiohjelma (TKT).
* I'll write all project documentation in English.
* I'll write the project in Python. I can also peer review projects written in Java, Javascript, or C#.
* The intent of the project is to develop a Gomoku AI that can beat beginner human players without using unreasonably long times to compute optimal moves. Gomoku is similar to tic tac toe (ristinolla) with a 15x15 board and some additional rules such as overlines (rows of 6 or more do not win the game). Standard Gomoku has been solved, with Black player able to force a win if playing optimally. For this reason, I'm considering some variant to determine first placements in such a way that Black player doesn't have a huge advantage. One such variant is Swap2, but it may add unnecessary complexity to developing the AI.
* The AI is based on the minimax algorithm with alpha-beta pruning. According to course materials, in this type of games (unlike e.g. chess), heuristic assessment of game state is not an effective way to calculate optimal moves. Instead, maximizing depth is the way to go. Therefore, it is necessary to come up with different ways to prioritize moves. Course material suggests e.g. favoring attack / defence. One way to prioritize should be favoring placements that are close to existing pieces because isolated pieces don't develop into wins very quickly.
* The time complexity of minimax is O(b^m), where b is the number of legal moves and m is the maximum depth of the tree. With such time complexity, computing optimal moves gets unwieldy very quickly, so effective use of pruning is essential to keep branching at minimum. In very simple terms, the goal is to decrease b as much as possible so that it's possible to increase m as much as possible.
* The program has the following main components:
  - The main game loop that maintains game state and gives players turns to place pieces on the board.
  - A rules engine that can check which moves are legal, and check if a player has won.
  - Several player modules for different purposes. When the main game loop is started, the user can determine which of the following modules are used as Black and White players:
    - For testing purposes, an automated player that places pieces randomly.
    - For humans, a text interface for inputing e.g. `3 5` to place a piece at x=3, y=5
    - The AI, which uses the techniques mentioned above to place pieces as optimally as possible within certain constraints (e.g. max depth).

* The following are some sources that explain how the game is played and some related to AI:
  - https://en.wikipedia.org/wiki/Gomoku
  - https://gomocup.org/
