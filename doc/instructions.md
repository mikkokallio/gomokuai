# User instructions

The project has been designed to be used with poetry.

After cloning the project, install dependencies with `poetry install`.

Then you can make two bots fight one another by running e.g. `poetry run python src/index.py Andrew Anna`

For testing purposes, it may be more practical to sometimes just view the result of a game without all of the output. You can use `poetry run python src/index.py -c Norma Donald`

You can use the `-a` switch to run the game twice -- the second time with the roles switched, e.g. `poetry run python src/index.py Robert Andrew -a`

With the `-r` switch you can also run multiple matches with the same players, e.g. `poetry run python src/index.py Maisie Andrew -a -c -r 2`

When combined with the `-a` switch, the total number of games is twice the number of repeats.
TBA!

Huomaa että jokaisen dokumentin pituus on n. 1-2 A4, poislukien kuvat ja taulukot (todellinen pituus voi olla siis merkittävästi suurempi).

* Miten ohjelma suoritetaan, miten eri toiminnallisuuksia käytetään
* Minkä muotoisia syötteitä ohjelma hyväksyy
* Missä hakemistossa on jar ja ajamiseen tarvittavat testitiedostot.
* Työn tekemisessä ja arvostelussa painotetaan laitoksen muita harjoitustöitä vähemmän dokumentointia. Ohjelmakoodin on kuitenkin oltava mahdollisimman selkeää, metodien on oltava lyhyitä, luokkien, muuttujien ja metodien on oltava kuvaavasti nimettyjä ja ohjelman rakenteen muutenkin kaikin puolin selkeä.

Koodin tulee olla kirjoitettu mahdollisimman selkeästi ja ymmärrettävästi. Kommentoi koodiasi kattavasti, mutta napakasti. Jokainen luokka, metodi ja attribuutti ei välttämättä kaipaa kommenttia, mutta kaikki olennainen ja vähemmän kuin itsestään selvä on oltava selostettu kommenteissa. Sisällytä metodien kommentteihin niiden parametrien ja paluuarvon merkitykset. Metodien sisäinen kommentointi ei ideaalitapauksessa pitäisi olla tarpeen, sillä metodien tulee olla kuvaavasti nimettyjä, kompakteja ja yksinkertaisia, helposti hahmotettavia kokonaisuuksia. Mikäli metodin toimintaa kuitenkin on vaikea hahmottaa pelkän koodin ja metodin yleiskommentin perusteella, voidaan sen koodia kommentoida sisäisestikin.

JavaDoc-kommentointia käytetään kaikissa töissä, jotka toteutetaan Javalla. NetBeans toteuttaa pyydettäessä luokille ja metodeille JavaDoc-kommenttien pohjat. Mikäli teet työsi jollakin muulla kielellä, sovi käytetystä kommentoitityylistä ohjaajan kanssa. Luokkakaaviot saat lisättyä JavaDoc:iisi suoraan käyttämällä YWorks-nimistä työkalua, joka generoi suoraan NetBeans-projektista kaaviot.
