# Implementation report

This document describes the project's structure and other properties.

## Program structure

TBA
* `index.py`: This is the entry point to the program; it starts the app.
* `app.py`: This class runs the main game loop, giving turns to players and keeping track of game progress.
* `board.py`: This class represents the game board. It keeps the state of stones placed on the board and can check whether a move is legal, remembers in which order moves were made, etc.
* `ai_player.py`: This class represents a parametrizable AI bot that can play the game. Its parameters determine how "intelligent" it is -- in other words, how many turns it can study ahead of time, how many move options it considers for each turn, and so forth.
* `proximity_list.py`: The AI player uses this class to keep track of what coordinates (y,x) on the board are available and within a reasonable distance from existing stones.
* `human_player.py`: A user interface for manually testing the AI players' tactics.
* 

## Performance analysis

* Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)
* Suorituskyky- ja O-analyysivertailu (mikäli työ vertailupainotteinen)

## Known flaws and possible improvements

TBA

## Sources

*
*
*
