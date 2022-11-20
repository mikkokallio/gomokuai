# Testing document

## Branch coverage

Week 2:

Name                  Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------
src\AI_player.py        124     36     72     14    69%   21->26, 28, 43-45, 58->61, 65, 76->74, 87, 90->76, 101-102, 104-105, 107-108, 112, 114-115, 117-118, 120, 128-146
src\board.py             47      7     30      3    79%   14-18, 36, 38, 51->49
src\human_player.py       5      0      4      0   100%
src\scoring.py            0      0      0      0   100%
-----------------------------------------------------------------
TOTAL                   176     43    106     17    73%

TBA!

* Huomaa että jokaisen dokumentin pituus on n. 1-2 A4, poislukien kuvat ja taulukot (todellinen pituus voi olla siis merkittävästi suurempi).
* Yksikkötestauksen kattavuusraportti.
* Mitä on testattu, miten tämä tehtiin?
* Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
* Miten testit voidaan toistaa?
* Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.

Testaus on ideaalitapauksessa suoritettava ohjelma. Tällöin testi on helposti toistettavissa, mikä helpottaa toteutuksen tekoa jo varhaisessa vaiheessa. Ainakin yksikkötestit tulee suorittaa ohjelmallisesti, ja niiden kattavuus tulee raportoida automaattisella välineellä. Yksikkötesteillä tulee testata kaikki paitsi käyttöliittymä, suorituskykytestit ja mahdollisesti tiedostojen luku ja kirjoittaminen riippuen projektista.

Mieti mitä oman sovelluksesi toiminnan oikeellisuus tarkoittaa. Reitinhakualgoritmin tulee löytää lyhin reitti, ja reitin ja sen etsinnän etenemisen pitää olla sen kaltainen kuin on tarkoitus. Labyrintin tai luolaston tulee yleensä olla yhtenäinen. Miinaharavabotti ei saa koskaan osua miinaan silloin, kun ruutua pidetään turvallisena. Pakatun tiedoston koon täytyy olla odotusten mukainen, ja sen tulee purkautua alkuperäiseksi - tai näyttää / kuulostaa oikealta, jos kyseessä on häviöllinen pakkaus. Shakkibotti ei saa tehdä laittomia siirtoja, ja sen on osattava tehdä matti, mikäli se on mahdollista sillä laskentasyvyydellä, jota käytetään. Jos kattava oikeellisuustesti vie liikaa aikaa, kannattaa laittaa yksikkötesteihin vain pari edustavaa testitapausta, ja tehdä lisäksi erillinen testiohjelma.

## Unit testing

The project uses pytest and coverage, which can be run with the commands below. Unit testing is underway but still needs to cover more code.

`poetry run pytest src`

`poetry run coverage run --branch -m pytest src`
`coverage report -m`

## Performance testing

The program measures both players' time expenditure as well as the total length of each game. By changing each AI bot's parameters, it's easy to test how they affect performance. TBA

"Vastaavasti jos suorituskykytestien ajamiseen menee alle minuutti, on aika todennäköistä, että testit eivät ole riittäviä. Kokonaisuus täytyy yleensä testata itse kokeilemalla, raportoidaan mitä on kokeiltu." Testeissä saa käyttää mitä tahansa apukirjastoa. Testikattavuus tulee laskea automaattisesti. Huomaa silti, että kattavuuslaskenta on vain apuväline. On hyvin mahdollista tuottaa 100% kattavuus huonosti testatulle koodille. Tavoitteena on havaita kaikki virheet ohjelman toiminnassa. Kannattaa kirjoittaa mahdollisimman pieniä yksikkötestejä mahdollisimman paljon. Ideana on, että jos koodissa on virhe, tulisi vähintään yhden testin havaita se, ja virheen kohta koodissa tulisi olla mahdollisimman selkeä. Tämä on tärkeää, jotta virheiden korjaaminen on tehokasta.
