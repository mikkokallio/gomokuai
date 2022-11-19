# Weekly report 3

## What did I do this week? How is the program progressing?

Having developed a few increasingly better versions of game AI, I continued with "Iteration 4", which got a better scoring system capable of indicating when a position was already won even if there wasn't yet 5 in a row, or included a threat that had to be countered, leaving the opponent with only 1-3 possible moves to avoid losing (i.e. forced moves). That enabled me to cut away more branches than before, making the AI faster and smarter than the previous versions. I was happy with the new features, so I started working on Iteration 5.

Iteration 5 got two significant upgrades. One was "pass-through deepening", which leverages the aforementioned ability to cut off branches that cannot win. If pass-through deepening is enabled and the AI encounters a node that only has one child, it doesn't decrease the depth parameter when moving to that child node. That way, if multiple "forced moves" are chained, it's possible to dig really deep in the tree without increasing the number of visited nodes too much.

Thw other new feature was the ability to use stored data about previous games to make quicker and better decisions about early turns. I started saving data about which were the 10 first nodes a game traverses and the result of those games (black win, white win, draw). That way, the AI "learns" which routes are likely to end in failure or victory, so it starts preferring the ones that have a higher likelihood of success. I've made the AI play hundreds of games against itself, and it's becoming evident that with access to the "winning routes", the AI stands a much better chance of winning against black--despite the first player advantage--if black can't use the routes data. If black can also use the routes, it regains its advantage.

I also decided that there won't be more named iterations. Rather, "Iteration 5" will now only get new parameters that can be used to de/activate the different features. That way, it's possible to test any combination of features using otherwise identical AI's against each other.

Other tasks included adding constraints to the first three moves. This makes the game a bit more even, though black still has an advantage.

I also continued to improve docs/testing/quality and similar things.

## What am I doing next?

I'll still probably experiment with new features that either make calculating positions faster or further limit branching. But I think I'm gradually getting to the point where I can start focusing more on other aspects of the project, such as getting all documentation to the desired level. Also making the program's structure better and more readable.

## How many hours did I spend?

Probably around 30 hours.
