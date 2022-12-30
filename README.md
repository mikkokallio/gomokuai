# Gomoku AI project

![GHA workflow badge](https://github.com/mikkokallio/tiralabra/workflows/pipe/badge.svg)

The goal of this project was to build an AI capable of playing Gomoku, a game similar to tic-tac-toe. The project was made for the "tiralabra" course in period 2 of 2022.

![Gomoku board](https://github.com/mikkokallio/tiralabra/blob/main/doc/images/board.png "Opening moves")


## Game rules

The AI players must follow the following rules:

* The game board size is 15 x 15.
* Two players take turns to place stones on the board.
* The first 3 moves are restricted: 1st is at the center of the board, 2nd is within the center 5 x 5 positions, and 3rd is outside the center 5 x 5.
* The player to get 5 stones in a row wins. These may be positioned horizontally, vertically, or diagonally.
* However, overlines (6 or more stones in a row) don't count as a win.
* If there is no winner after 60 turns, the game ends as a draw.

## AI optimization methods implemented

- minimax with alpha-beta pruning
- limiting search space to x squares from closest stone
- ordering moves with threat space analysis
- when forced moves occur, eliminate all other moves
- limiting branching factor by hard limit
- multiprocessing at the root of the tree
- pass-through deepening
- transposition tables

## User instructions

See the [user instructions](https://github.com/mikkokallio/tiralabra/blob/main/doc/instructions.md) document for detailed instructions on installing and running the project.

## Weekly reports

* [Week 1](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-1.md)
* [Week 2](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-2.md)
* [Week 3](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-3.md)
* [Week 4](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-4.md)
* [Week 5](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-5.md)
* [Week 6](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-6.md)

## Other documentation

* [Project specification](https://github.com/mikkokallio/tiralabra/blob/main/doc/specification.md)
* [Testing document](https://github.com/mikkokallio/tiralabra/blob/main/doc/testing.md)
* [Implementation report](https://github.com/mikkokallio/tiralabra/blob/main/doc/implementation.md)
