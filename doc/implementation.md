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

As mentioned in the specification document, the time complexity of minimax is `O(b^m)`, where `b` is the number of legal moves and `m` is the maximum depth of the tree. Below is further analysis on how this works in practice with gomoku, and how the different AI optimization techniques help reduce the branching factor.
* Gomoku without constraints on moves has initially 15 x 15 = 225 legal moves, and their number lessens by one each turn. So in theory, there are 225! = 1,23 * 10^433 positions, though some of those cannot occur because the game would end whenever there are 5 stones in a row. Even so, the number is too great to calculate the whole game tree.
* The variant used in this project has some constraints for the first three moves: First stone has only 1 option for position, and 2nd and 3rd stones have 24 options each. The game engine also rules that games end in a draw if neither player has won after 60 turns. Even with these modifications, there are still 24^2 * (222! - 165!) = 6,45 * 10^428 possible board positions, not accounting for positions eliminated by wins.
* Because of board symmetry, it'd be possible to divide these figures by 8 (rotated 4 ways and mirrored), but it's not helping much.
* Therefore, in practice an AI must use a calculation depth, only checking nodes in the tree that are n moves away from current board position.
* Especially for initial moves, this means nearly all nodes at max depth are neither wins or losses, returning 0. Therefore, a heuristic must be used to evaluate positions and put them in an order that helps searching the most promising branches first. This makes it possible to use alpha-beta pruning, where entire branches can be eliminated if it has been determined in another branch that it's not possible to get a better result.
* Of course, the heuristic adds another loop. The heuristic I've implemented studies only new threats created by adding one stone (rather than scanning the whole board), and for this, it requires looking at 5 + a few extra squares in 4 directions for about 20-30 squares per evaluation. That's actually a more or less "constant" factor rather than affected by `b` or `m`, so the time complexity doesn't change. It's still `O(b^m)`.
* So in the end, optimizing the AI is a balancing act of figuring out how to reduce `b` without sacrificing too much AI skill so that `m` can be increased. I tried to keep the game duration of a single game preferably under one minute, but tested also with games of a few minutes in length. The following methods were used and these are the observations base on performance testing:
  - It is not useful to search moves where stones are placed very far from existing stones. Through testing, I determined that max 2 squares away is the sweet spot. While looking at moves 3, 4, etc. squares away, AI skill did increase, but the gains were diminishing. More concretely put, looking at moves 3+ squares away slowed down the AI so much that depth had to be smaller to compensate, and testing indicated that depth had a much bigger effect on AI skill than "reach". With reach 2, branching factor went down from ~200 possible moves to about 20, i.e. a 90% decrease in branching. Of course, many of those would have been eliminated by a-b pruning (or the hard limit, see below), but now it wasn't necessary to evaluate the positions first, saving some time.
  - Branching is also narrowed by a hard limit. At first ply it is 10 + n and at further plies it was n, which depended on the selected AI bot. The reason for having a larger max number of branches at first ply is that multiprocessing is used to share work between computer cores at the first ply. All of this overlaps with a-b pruning to some extent, and according to performance tests, the increase in speed from multiprocessing is only about 25%, on average. The effects or hard limiting were also performance-tested, and much like "reach" mentioned above, there's a sweet spot for max branching, where speed gains (and thus possibility to increase depth) matter much more.
  - Threat-space analysis in the heuristic algorithm greatly enhanced the AI's skill at evaluating board positions, but it also made it possible to eliminate many moves, thus reducing branching factor. For example, in any node where there is an active threat (made by either player), it can be assumed that the other player's moves are limited to blocking the threat. If they don't do so, they lose immediately or a few rounds later, no exceptions. Therefore, in many situations, it's only necessary to keep only one or two branches (the moves that block the threat).
  - It was also shown in performance testing that keeping initial depth lower but selectively deepening greatly increased AI skill without decreasing speed significantly. This was not actual iterative deepening, however.

Overall, through the combined effect of methods described above, it was possible to to keep branching factor at 1-3 for the most part, which in turn made it possible to use greater max depths. Most testing was done at depth 3-9, though 11 and 13 were also tested. Game lengths vary from a few seconds (with e.g. depth 3) to a few minutes (with e.g. depth 11). Regarding AI skill, the AI became tough to play against quite early on in the project, and its further iterations were increasingly difficult to play against (and were able to beat earlier versions of the AI consistently.) My skill as a player also grew during the project, and it's still possible to beat the AI, but requires planning many, many moves ahead.

## Known flaws and possible improvements

I read about many different ways to improve the AI, but didn't have time to try everything. Some other ideas how the project could be further developed are listed below.

* Improving heuristics algorithm. Python is the main problem here, but it might be possible to improve performance by moving part of calculations to be handled by Python's libraries written in C. Maybe use arrays instead of lists. Or bitwise operations.
* The heuristics algo doesn't consider blocking the ends of a broken four (e.g. -XX-X-), always blocking with O in the middle. In the vast majority of cases it's the smart thing to do, but there are potentially positions where blocking at the line's end would make sense. Similarly when double threats occur, the AI considers blocking only at the intersection where the two lines would meet if completed.
* Trying iterative deepening instead of the current deepening method (although it does too improve performance).
* Storing results from previous round's minimax and reusing those instead of starting at the root ply each time.
* Quiescent minimaxing performed during the opponent's turn. However this is not so useful when two AI's play on the same machine. Would be more useful against a human opponent or AI on a different machine so they wouldn't be sharing the same compute.
* Improve the use of transposition tables--currently they don't improve AI skill significantly. Hash table could be partitioned e.g. by turn number for faster searching.
* The repo has a pipeline that runs tests and has a corresponding "pipeline passing" icon, but there could also be similar automation for coverage and code quality.

## Sources

* https://en.wikipedia.org/wiki/Gomoku -- describes game rules and many of the most common variants.
* [Go-Moku and Threat-Space Search](https://www.bing.com/ck/a?!&&p=ca281f984ef1b35aJmltdHM9MTY3MjM1ODQwMCZpZ3VpZD0yZmQzZjU2MS02MjVlLTYxNWEtMzAyMS1lNTUyNjNiNTYwNGUmaW5zaWQ9NTIwMQ&ptn=3&hsh=3&fclid=2fd3f561-625e-615a-3021-e55263b5604e&psq=threat+space+analysis+gomoku&u=a1aHR0cHM6Ly93d3cucmVzZWFyY2hnYXRlLm5ldC9wdWJsaWNhdGlvbi8yMjUyNDQ3X0dvLU1va3VfYW5kX1RocmVhdC1TcGFjZV9TZWFyY2g&ntb=1) -- This article explains how gomoku was "solved" (at least in theory) decades ago, using threat-spaces.
* Various stack overflow and other boards searches for ideas on using different techniques, e.g. multiprocessing.
