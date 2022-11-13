# Weekly report 2

## What did I do this week?

Most work went into developing a basic AI and then increasing its "intelligence".

I also added some other things for the most relevant classes (not including old versions of the AI which are no longer developed and only kept for testing purposes):
- Basic doc strings (will be improved over time)
- Unit tests (also to be improved)
- Test coverage tooling

## What progress did I make?

The main task was improving the AI -- to make it faster and also more "intelligent" i.e. winning with a higher likelihood. That's going really well. I develop the AI in iterations, where "graduating" to the next iteration requires that the newer version must play white (i.e. not go first) and still beat the older version. That gets tougher and tougher to do since black has a significant advantage.

I started with a totally random bot that didn't know any rules other than legal placement of stones. Then I created a simple AI ('Iteration 1') that understood the rules, and tested that it could beat the random bot consistently.

I then created another version ('Iteration 2') that applied scoring to board states / moves and was able to plan ahead a few moves but was still quite slow if depth was too great.

The next version ('Iteration 3') had better scoring system, also accounting for broken rows and other more advanced stuff. The scoring proved effective and I was able to limit branching quite a lot without losing too many potentially good moves. At this stage, the AI already became quite frustratingly difficult to play against.

The current one ('Iteration 4') also uses multiprocessing and has a much better system for eliminating bad moves so it can dig deeper into the promising branches. It can beat Iteration 3 quite fast in multiple board setups even though Iteration 3 has first player advantage.

## How is the program progressing?

Besides the AI development, the basic structure of the program is mostly there. I've also parametrized the AI to make it easier to test different configurations.

## What did I learn this week?

The most important learning is regarding how to make a-b pruning more effective. It's also very useful to simply remove branches that don't respond to threats because a few turns later, that player would lose.

## What was unclear or has been challenging?

Expressing some things in code has been an interesting challenge. For example, how to check if a board state is a "threat" that must be countered immediately.

## What am I doing next?

Still improving AI and trying to also polish everything else in the project.

## How many hours did I spend?

Probably around 25 hours.
