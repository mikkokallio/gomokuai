# tiralabra
Tiralabra-harjoitustyö 2022 p2

![GHA workflow badge](https://github.com/mikkokallio/tiralabra/workflows/pipe/badge.svg)

## Usage

The project has been designed to be used with poetry.

After cloning the project, install dependencies with `poetry install`.

Then you can make two bots fight one another by running e.g. `poetry run python src/index.py Andrew Anna`

For testing purposes, it may be more practical to sometimes just view the result of a game without all of the output. You can use `poetry run python src/index.py -c Norma Donald`

You can use the `-a` switch to run the game twice -- the second time with the roles switched, e.g. `poetry run python src/index.py Robert Andrew -a`

With the `-r` switch you can also run multiple matches with the same players, e.g. `poetry run python src/index.py Maisie Andrew -a -c -r 2`

When combined with the `-a` switch, the total number of games is twice the number of repeats.

## Weekly reports

* [Week 1](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-1.md)
* [Week 2](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-2.md)
* [Week 3](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-3.md)
* [Week 4](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-4.md)
* [Week 5](https://github.com/mikkokallio/tiralabra/blob/main/doc/weekly-report-5.md)
* TBA
* TBA

## Other documentation

* [Project specification](https://github.com/mikkokallio/tiralabra/blob/main/doc/specification.md)
* [Testing document](https://github.com/mikkokallio/tiralabra/blob/main/doc/testing.md)
* [Implementation report](https://github.com/mikkokallio/tiralabra/blob/main/doc/implementation.md)
* TBA
