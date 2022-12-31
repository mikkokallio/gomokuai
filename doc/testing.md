# Testing document

This document describes the different testing types used in this project.

## Unit testing

The project uses pytest and coverage, which can be run with the commands below.

`pytest src`

`coverage run --branch -m pytest src` and then `coverage report -m`

### Branch coverage

All main functionality in the project is unit tested. The following report was generated on December 30th 2022 with the above commands:
```
Name                    Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------
src\ai_player.py          136      5     76      6    94%   39->42, 107->94, 124, 130, 156->163, 160-162
src\app.py                 77     12     34      2    82%   39->30, 47, 87-100
src\board.py               53      0     34      1    99%   56->54
src\config.py              16      0      0      0   100%
src\human_player.py         5      0      2      0   100%
src\proximity_list.py      18      0     10      0   100%
-------------------------------------------------------------------
TOTAL                     305     17    156      9    93%
```

## Code quality

Code quality is tested with the command `pylint src`. Overall, code quality is very good (as of December 30th 2022):

```
------------------------------------------------------------------
Your code has been rated at 9.51/10 (previous run: 9.06/10, +0.45)
```

## Performance testing

Optimizing gomoku AI's performance means finding a balance between the speed (measured in average milliseconds / turn) and skill of the AI (percentage of winning vs losing vs draws).

### Speed

The program measures both players' time expenditure as well as the total length of each game. By changing each AI bot's parameters, it's easy to test how they affect performance. It's possible to collect speed results from the app's output and using `tools/analyze.py` to get insights, as has been done in the Test results section below. See user instructions for further details on how to get output suitable for analysis.

### Skill

Besides speed, the other part of the performance testing is determining how good the AI is at playing gomoku. Benchmarking can be done e.g. against other versions of the AI, using a different set of parameters. For example, if one player has depth 9, it should quite easily defeat another player with depth 5, of course taking into account the first player advantage when comparing win percentages. The tooling included in the project can analyze from game outputs how well different bots do over e.g. 100 or 1000 games.

### Test results

The app supports outputting game results as `.csv`, so it's possible to store them in a file. (For example, running `python src/index.py Eric Robert -a -r 10 -c >> tools/test.csv` gets you results from a total of 20 matches, where Eric plays 10 matches as black and the other 10 as white.) With enough game data stored, it's possible to get insights with the data. The script `tools/analyze.py` put game results in a pandas data frame so it's easy to make calculations. The following performance tests leverage that script.

#### Test: Compare depth values and pass-through deepening

In this [study](https://github.com/mikkokallio/tiralabra/blob/main/tools/study1.csv), four bots each fought 10 matches against each foe in both colors, for a total of 10 x 2 x 4! = 120 matches. Only two parameters were varied: max depth and pass-through deepening, which effectively increases max depth whenever a node has only one child (i.e. no branching occurs). The bots were configured as shown below, and they had the following win statistic and time used per round:

* Eric: depth 3 with PTD; 9 wins, 26 draws, 25 losses, avg time: 0.45 s
* Philip: depth 5 without PTD; 17 wins, 18 draws, 25 losses, avg time: 0.35 s
* Jane: depth 5 with PTD; 35 wins, 14 draws, 11 losses, avg time: 0.72 s
* Emma: depth 7 without PTD; 16 wins, 28 draws, 16 losses, avg time: 0.81 s

Going from depth 5 to 7 without PTD (Philip vs Emma) surprisingly didn't increase wins, but it did decrease losses significantly. Going from depth 3 to 5 with PTD (Eric vs Jane) made a huge difference, increasing successes. Meanwhile, enabling PTD with depth 5 (Philip vs Jane) doubled the length of each turn, but it also greatly improved the bot's odds of winning. It's worth noting PTD makes Jane significantly better than Emma, but Jane's time/round is still less than that of Emma.

Conclusions: Not surprisingly, increases in depth increase the bot's skill but decrease speed, so it's a trade-off. PTD also increases skill and decreases speed, but the ratio is much more favorable than that of increasing depth. In other words, it is a good idea to enable PTD.

#### Test: Compare branching factor

Since we've established that PTD is a good idea, we'll use it consistently in the next set of matches. In this [study](https://github.com/mikkokallio/tiralabra/blob/main/tools/study2.csv), the idea is to test how much constraints on branching affect speed and skill. The bots have two parameters related to branching: reach and branching. To limit the number of possible moves, only squares near existing stones are considered. Reach determines how many steps away from an existing stone a new stone can be placed. Brnaching, on the other hand, determines the maximum number of different moves evaluated at each depth. The number of positions evaluated is equal to branching to the power of max depth. Alpha-beta pruning removes some branches, but it alone is not necessarily enough, so setting a hard limit may be useful. Note: The bot adds +10 branches at the root level. This is because multiprocessing is always on, so at the root level, branching is handled quite effectively.

* Eric: depth 3 with reach 2 and branching 3; 11 wins, 2 draws, 46 losses, avg time: 0.37 s
* Robert: depth 3 with reach 13 and branching 13; 20 wins, 7 draws, 42 losses, avg time: 2.64 s
* Jane: depth 5 with reach 2 and branching 3; 31 wins, 2 draws, 27 losses, avg time: 0.63 s
* Anna: depth 5 with reach 3 and branching 7; 50 wins, 3 draws, 7 losses, avg time: 6.14 s

From the results, it's obvious that bots with higher reach and branching (Robert and Anna) do better than their more constrained counterparts. However, the average time per round was multiplied greatly. What's more, Jane still clearly beats Robert despite the difference in branching limits and is much faster, too.

Conclusions: Reach and branching increase a bot's skill, but at a heavy cost. Increasing depth seems to be a better way to increase skill.

#### Test: Transposition tables

This time there are two depth 5 (Jane, Donald) and two depth 7 bots (George, Maisie) that are otherwise identical except Donald and Maisie have access to data from hundreds of previous games, spesifically first 10 moves and the results (black win, white win, draw) of those games.

* Jane: depth 5, no tables; 15 wins, 5 draws, 40 losses, 0.94 s
* Donald, depth 5, uses tables; 28 wins, 5 draws, 27 losses, 1,82 s
* George: depth 7, no tables; 33 wins, 7 draws, 20 losses, 2.82 s
* Maisie, depth 7, uses tables; 31 wins, 9 draws, 20 losses, 3.73 s

This is curious: Donald plays clearly better than Jane, but George and Maisie are pretty equal. The sample is small, but perhaps the predictive power of greater depth (combined with deepening) is overlapping with the use of tables.

#### Test: Multiprocessing

The bots default to using multiprocessing, and so, the code doesn't currently support using parameters to not to use multiple cores, if available. However, changing manually in the code the line `with ProcessPoolExecutor(max_workers=None) as ex:` to only have `max_workers=1` does the thing. Initial testing with a fast, deterministic bot showed a decrease in computing times of 45% for black player and 30% for white player. In all other ways, the AIs played the games exactly the same way.

It was discussed in the demo session that the minimax algorithm doesn't leverage parallel computation very well, but I think a reduction of 30-45% is significant.

Next, I tested the effects of multiprocessing by running `python src/index.py Jane Janelle -a  -r 10 -c` twice -- again once with 1 worker and another time without a limit. One of these bots uses some randomness in scoring moves, so matches don't end always the same way. The results are the following (with a sample of 20 matches with a single worker vs 20 matches with no limit on cores): Black player's time was cut by 25% and white's only by 1% when using all cores. On a repeated test with same parameters, the results were a 17% reduction for black player and a 21% reduction for white player. The data is recorded in [1](https://github.com/mikkokallio/tiralabra/blob/main/tools/study5.csv), [2](https://github.com/mikkokallio/tiralabra/blob/main/tools/study5b.csv), [3](https://github.com/mikkokallio/tiralabra/blob/main/tools/study5c.csv), and [4](https://github.com/mikkokallio/tiralabra/blob/main/tools/study5d.csv).

Conclusion: The amount of reduction seems to vary, but with this small sample it is still evident that some reduction (1%, 17%, 21%, 25%, 30%, or 45%) happens each time.
