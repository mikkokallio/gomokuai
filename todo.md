Palautus 2-7 TBA

AI:

* AI can do minmax and a-b pruning, but tends to choose "weaker" options, e.g. first branch can force a draw but can't win, next one opponent can force a draw but can lose. Both look like draws, so first one is chosen.
* Bounding box or center of mass or similar to focus efforts on a particular area of the whole
* Incomplete rows should be worth something
* Positions near center are generally worth more because there's more area to expand to