# Implementation report

This document describes the project's structure and other properties.

## Program structure

When run, the application sets up a game board and two players, and then has the players take turns to place stones until one of them wins. The following are the main parts of the program:

* `index.py`: This is the entry point to the program; it starts the app.
* `app.py`: This class runs the main game loop, giving turns to players and keeping track of game progress.
* `board.py`: This class represents the game board. It keeps the state of stones placed on the board and can check whether a move is legal, remembers in which order moves were made, etc.
* `ai_player.py`: This class represents a parametrizable AI bot that can play the game. Its parameters determine how "intelligent" it is -- in other words, how many turns it can study ahead of time, how many move options it considers for each turn, and so forth.
* `proximity_list.py`: The AI player uses this class to keep track of what coordinates (y,x) on the board are available and within a reasonable distance from existing stones.
* `human_player.py`: A user interface for manually testing the AI players' tactics.
* `config.py`: This file contains only constants the affect how the board and the players behave during the game.

## Performance analysis

* Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)
* Suorituskyky- ja O-analyysivertailu (mikäli työ vertailupainotteinen)

## Known flaws and possible improvements

I read about many different ways to improve the AI, but didn't have time to try everything. Some other ideas how the project could be further developed are listed below.

* Improved heuristics algorithm. Python is the main problem here, but it might be possible to improve performance by moving part of calculations to be handled by Python's libraries written in C. Maybe use arrays instead of lists. Or bitwise operations.
* The heuristics algo doesn't consider blocking the ends of a broken four (e.g. -XX-X-), always blocking with O in the middle. In the vast majority of cases it's the smart thing to do, but there are potentially positions where blocking at the line's end would make sense. Similarly when double threats occur, the AI considers blocking only at the intersection where the two lines would meet if completed.
* Trying iterative deepening instead of the current deepening method (although it does too improve performance).
* Storing results from previous round's minimax and reusing those instead of starting at the root ply each time.
* Quiescent minimaxing performed during the opponent's turn. However this is not so useful when two AI's play on the same machine. Would be more useful against a human opponent or AI on a different machine so they wouldn't be sharing the same compute.
* Improve the use of transposition tables--currently they don't improve AI skill significantly. Hash table could be partitioned e.g. by turn number for faster searching.
* The repo has a pipeline that runs tests and has a corresponding "pipeline passing" icon, but there could also be similar automation for coverage and code quality.

## Sources

*
*
*
