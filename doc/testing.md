# Testing document

Work in progress.

## Unit testing

The project uses pytest and coverage, which can be run with the commands below. Unit testing is underway but still needs to cover more code.

`poetry run pytest src`

`poetry run coverage run --branch -m pytest src`

`coverage report -m`

### Branch coverage
```
Name                    Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------
src\ai_player.py          136     31     80      3    76%   39->42, 64-66, 113->101, 130, 135-166
src\app.py                 75     25     36      7    64%   25, 33, 37-38, 40->31, 42-44, 48, 66, 76-81, 85-98
src\board.py               45      1     30      2    96%   36, 47->45
src\config.py              16      0      0      0   100%
src\human_player.py         5      0      4      0   100%
src\proximity_list.py      18      0     12      0   100%
-------------------------------------------------------------------
TOTAL                     295     57    162     12    79%
```

## Performance testing

Optimizing gomoku AI means finding a balance between the speed (measured in average milliseconds / turn) and skill of the AI (percentage of winning vs losing vs draws).

### Speed

The program measures both players' time expenditure as well as the total length of each game. By changing each AI bot's parameters, it's easy to test how they affect performance. TBA. Maybe a script that has the game play 100 matches, calculating the total amount of time used.

Tavoitteena on havaita kaikki virheet ohjelman toiminnassa. Kannattaa kirjoittaa mahdollisimman pieniä yksikkötestejä mahdollisimman paljon. Ideana on, että jos koodissa on virhe, tulisi vähintään yhden testin havaita se, ja virheen kohta koodissa tulisi olla mahdollisimman selkeä. Tämä on tärkeää, jotta virheiden korjaaminen on tehokasta.

### Skill

As part of the performance testing is determining how good the AI is at playing gomoku. Benchmarking can be done e.g. against other versions of the AI, using a different set of parameters. For example, if one player has depth 9, it should quite easily defeat another player with depth 5, of course taking into account the first player advantage when comparing win percentages. Ideally, each player plays both as many games as black and white and the winning % from e.g. 100 games determines which version is better. TBA: script that runs e.g. 100 games and automatically calculates performance.

### Test results

#### Test 1: Compare depth values and pass-through deepening

Four bots each fought 10 matches against each foe in both colors, for a total of 10*2*4!=120 matches. Only two parameters were varied: max depth and pass-through deepening, which effectively increases max depth whenever a node has only one child (i.e. no branching occurs). The bots were configured as shown below, and they had the following win statistic and time used per round:

* Eric: depth 3 with PTD; 9 wins, 26 draws, 25 losses, avg time: 0.45 s
* Philip: depth 5 without PTD; 17 wins, 18 draws, 25 losses, avg time: 0.35 s
* Jane: depth 5 with PTD; 35 wins, 14 draws, 11 losses, avg time: 0.72 s
* Emma: depth 7 without PTD; 16 wins, 28 draws, 16 losses, avg time: 0.81 s

Going from depth 5 to 7 without PTD (Philip vs Emma) surprisingly didn't increase wins, but it did decrease losses significantly. Going from depth 3 to 5 with PTD (Eric vs Jane) made a huge difference, increasing successes. Meanwhile, enabling PTD with depth 5 (Philip vs Jane) doubled the length of each turn, but it also greatly improved the bot's odds of winning. It's worth noting PTD makes Jane significantly better than Emma, but Jane's time/round is still less than that of Emma.

Conclusions: Not surprisingly, increases in depth increase the bot's skill but decrease speed, so it's a trade-off. PTD also increases skill and decreases speed, but the ratio is much more favorable than that of increasing depth. In other words, it is a good idea to enable PTD.

## Test 2: Compare branching factor

TBA

## To be processed!

* Mitä on testattu, miten tämä tehtiin?
* Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
* Miten testit voidaan toistaa?
* Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.

Yksikkötesteillä tulee testata kaikki paitsi käyttöliittymä, suorituskykytestit ja mahdollisesti tiedostojen luku ja kirjoittaminen riippuen projektista.

Mieti mitä oman sovelluksesi toiminnan oikeellisuus tarkoittaa. Reitinhakualgoritmin tulee löytää lyhin reitti, ja reitin ja sen etsinnän etenemisen pitää olla sen kaltainen kuin on tarkoitus. Labyrintin tai luolaston tulee yleensä olla yhtenäinen. Miinaharavabotti ei saa koskaan osua miinaan silloin, kun ruutua pidetään turvallisena. rkautua alkuperäiseksi - tai näyttää / kuulostaa oikealta, jos kyseessä on häviöllinen pakkaus. "Shakkibotti ei saa tehdä laittomia siirtoja, ja sen on osattava tehdä matti, mikäli se on mahdollista sillä laskentasyvyydellä, jota käytetään. Jos kattava oikeellisuustesti vie liikaa aikaa, kannattaa laittaa yksikkötesteihin vain pari edustavaa testitapausta, ja tehdä lisäksi erillinen testiohjelma."

