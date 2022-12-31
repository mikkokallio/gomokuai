# User instructions

The project has been designed to be used with poetry.

## Getting started

1. Install poetry.
2. Clone the project.
3. Install dependencies with `poetry install`.
4. Open virtual environment with `poetry shell`.
5. Make two bots fight one another by running e.g. `python src/index.py Andrew Anna -v`
  - `Àndrew` and `Anna` are AI bot names. Each bot has slightly different level of skill.
  - The `-v` switch adds color to the output.
  - Try running with the `-h` switch to get a list of bot names and other instructions.

## Testing the AI in different ways

For testing purposes, consider the following options:

* It may be more practical to sometimes just view the result of a game without all of the output using the `-c` switch. Try `python src/index.py -c Norma Donald`
* You can use the `-a` switch to run the game twice, the second time with the bots' roles reversed, e.g. `python src/index.py Robert Andrew -a`
* With the `-r` switch you can also run multiple matches with the same players, e.g. `python src/index.py Maisie Andrew -a -c -r 2`
* When `-r` is combined with the `-a` switch, the total number of games is twice the number of repeats.
* You can output the results to a `.csv` file by using `>>` as in `python src/index.py Maisie Andrew -a -c -r 2 >> results.csv`
* The resulting `.csv` files can then be analyzed with `tools/analyze.py`. See the `tools` folder for examples of such files. See also the [testing document](https://github.com/mikkokallio/tiralabra/blob/main/doc/testing.md) for examples of how the analysis tool has been used to do performance testing for different bots and their features.

## Analyzing test data

If data is collected as `.csv` files as described above and saved e.g. in the `tools` folder, it can be analyzed by running e.g. `python tools/analyze.py tools/study2.csv`. This summarizes information about the sample, showing average time (s) per turn as well as wins, losses, and draws while playing as black and white:

```
Robert's statistics
-> black
2.9083791728637562
14 wins, 4 draws, 12 losses {'Jane': 5, 'Anna': 4, 'Eric': 3}
-> white
2.3739910156255295
6 wins, 3 draws, 20 losses {'Anna': 10, 'Jane': 7, 'Eric': 3}

...
```
