# User instructions

The project has been designed to be used with poetry.

## Getting started

1. Install poetry.
2. Clone the project.
3. Install dependencies with `poetry install`.
4. Make two bots fight one another by running e.g. `poetry run python src/index.py Andrew Anna`

## Testing the AI in different ways

For testing purposes, consider the following options:

* Running with the `-v` switch adds colors, which may help analyzing board positions.
* It may be more practical to sometimes just view the result of a game without all of the output. You can use `poetry run python src/index.py -c Norma Donald`
* You can use the `-a` switch to run the game twice -- the second time with the roles switched, e.g. `poetry run python src/index.py Robert Andrew -a`
* With the `-r` switch you can also run multiple matches with the same players, e.g. `poetry run python src/index.py Maisie Andrew -a -c -r 2`
* When combined with the `-a` switch, the total number of games is twice the number of repeats.

Run `poetry run python src/index.py -h` to view more instructions.
