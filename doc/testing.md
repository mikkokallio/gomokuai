# Testing document

Work in progress.

## Unit testing

The project uses pytest and coverage, which can be run with the commands below. Unit testing is underway but still needs to cover more code.

`poetry run pytest src`

`poetry run coverage run --branch -m pytest src`

`coverage report -m`

### Branch coverage

Name                    Stmts   Miss Branch BrPart  Cover   Missing

-------------------------------------------------------------------

src\ai_player.py          135     40     80      8    68%   26-29, 39-41, 43, 63-65, 70->72, 112->100, 125, 127, 129, 134-161

src\board.py               44      7     30      3    78%   11-15, 33, 35, 46->44

src\human_player.py         5      0      4      0   100%

src\proximity_list.py      18      0     12      0   100%

src\scoring.py             15      0      0      0   100%

-------------------------------------------------------------------

TOTAL                     217     47    126     11    76%

## Performance testing

The program measures both players' time expenditure as well as the total length of each game. By changing each AI bot's parameters, it's easy to test how they affect performance. TBA

"Vastaavasti jos suorituskykytestien ajamiseen menee alle minuutti, on aika todennäköistä, että testit eivät ole riittäviä. Kokonaisuus täytyy yleensä testata itse kokeilemalla, raportoidaan mitä on kokeiltu." Testeissä saa käyttää mitä tahansa apukirjastoa. Testikattavuus tulee laskea automaattisesti. Huomaa silti, että kattavuuslaskenta on vain apuväline. On hyvin mahdollista tuottaa 100% kattavuus huonosti testatulle koodille. Tavoitteena on havaita kaikki virheet ohjelman toiminnassa. Kannattaa kirjoittaa mahdollisimman pieniä yksikkötestejä mahdollisimman paljon. Ideana on, että jos koodissa on virhe, tulisi vähintään yhden testin havaita se, ja virheen kohta koodissa tulisi olla mahdollisimman selkeä. Tämä on tärkeää, jotta virheiden korjaaminen on tehokasta.

## To be processed!

* Huomaa että jokaisen dokumentin pituus on n. 1-2 A4, poislukien kuvat ja taulukot (todellinen pituus voi olla siis merkittävästi suurempi).
* Yksikkötestauksen kattavuusraportti.
* Mitä on testattu, miten tämä tehtiin?
* Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
* Miten testit voidaan toistaa?
* Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.

Testaus on ideaalitapauksessa suoritettava ohjelma. Tällöin testi on helposti toistettavissa, mikä helpottaa toteutuksen tekoa jo varhaisessa vaiheessa. Ainakin yksikkötestit tulee suorittaa ohjelmallisesti, ja niiden kattavuus tulee raportoida automaattisella välineellä. Yksikkötesteillä tulee testata kaikki paitsi käyttöliittymä, suorituskykytestit ja mahdollisesti tiedostojen luku ja kirjoittaminen riippuen projektista.

Mieti mitä oman sovelluksesi toiminnan oikeellisuus tarkoittaa. Reitinhakualgoritmin tulee löytää lyhin reitti, ja reitin ja sen etsinnän etenemisen pitää olla sen kaltainen kuin on tarkoitus. Labyrintin tai luolaston tulee yleensä olla yhtenäinen. Miinaharavabotti ei saa koskaan osua miinaan silloin, kun ruutua pidetään turvallisena. Pakatun tiedoston koon täytyy olla odotusten mukainen, ja sen tulee purkautua alkuperäiseksi - tai näyttää / kuulostaa oikealta, jos kyseessä on häviöllinen pakkaus. Shakkibotti ei saa tehdä laittomia siirtoja, ja sen on osattava tehdä matti, mikäli se on mahdollista sillä laskentasyvyydellä, jota käytetään. Jos kattava oikeellisuustesti vie liikaa aikaa, kannattaa laittaa yksikkötesteihin vain pari edustavaa testitapausta, ja tehdä lisäksi erillinen testiohjelma.

