Dokumentaatio

Huom: kaikki dokumentit palautetaan joko GitHubin tukemassa markdown-muodossa, katso tuetut formaatit täältä tai .pdf-muodossa! Sijoita dokumentit omaan hakemistoonsa projektin juureen.

Koodin lisäksi tehtävänä on neljä dokumenttia: määrittelydokumentti, toteutusdokumentti, käyttöohje ja testausdokumentti. Dokumenttien merkitys kurssilla on kuitenkin vähäisempi; olennainen asia on toimiva ja tehokas koodi.

Huomaa että jokaisen dokumentin pituus on n. 1-2 A4, poislukien kuvat ja taulukot (todellinen pituus voi olla siis merkittävästi suurempi).

Vaaditut dokumentit:
Määrittelydokumentti
Mitä ohjelmointikieltä käytät? Kerro myös mitä muita kieliä hallitset siinä määrin, että pystyt tarvittaessa vertaisarvioimaan niillä tehtyjä projekteja.
Mitä algoritmeja ja tietorakenteita toteutat työssäsi?
Mitä ongelmaa ratkaiset ja miksi valitsit kyseiset algoritmit/tietorakenteet?
Mitä syötteitä ohjelma saa ja miten näitä käytetään?
Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)
Lähteet
Kurssin hallintaan liittyvistä syistä määrittelydokumentissä tulee mainita opinto-ohjelma johon kuulut. Esimerkiksi tietojenkäsittelytieteen kandidaatti (TKT) tai bachelor’s in science (bSc)
Määrittelydokumentissa tulee myös mainita projektin dokumentaatiossa käytetty kieli (todennäköisesti sama kuin määrittelydokumentin kieli). Projektin koodin, kommenttien ja dokumenttien teksti on valitulla kielellä. Tyypillisesti suomi tai englanti. Tämä vaatimus liittyy projektin puolen välin paikkeilla järjestettäviin koodikatselmointeihin. Tavoitteena on että projektien sisäiset kielivalinnat ovat johdonmukaisia.
Toteutusdokumentti
Ohjelman yleisrakenne
Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)
Suorituskyky- ja O-analyysivertailu (mikäli työ vertailupainotteinen)
Työn mahdolliset puutteet ja parannusehdotukset
Lähteet
Testausdokumentti
Yksikkötestauksen kattavuusraportti.
Mitä on testattu, miten tämä tehtiin?
Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
Miten testit voidaan toistaa?
Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
Testaus on ideaalitapauksessa suoritettava ohjelma. Tällöin testi on helposti toistettavissa, mikä helpottaa toteutuksen tekoa jo varhaisessa vaiheessa. Ainakin yksikkötestit tulee suorittaa ohjelmallisesti, ja niiden kattavuus tulee raportoida automaattisella välineellä. Yksikkötesteillä tulee testata kaikki paitsi käyttöliittymä, suorituskykytestit ja mahdollisesti tiedostojen luku ja kirjoittaminen riippuen projektista.

Mieti mitä oman sovelluksesi toiminnan oikeellisuus tarkoittaa. Reitinhakualgoritmin tulee löytää lyhin reitti, ja reitin ja sen etsinnän etenemisen pitää olla sen kaltainen kuin on tarkoitus. Labyrintin tai luolaston tulee yleensä olla yhtenäinen. Miinaharavabotti ei saa koskaan osua miinaan silloin, kun ruutua pidetään turvallisena. Pakatun tiedoston koon täytyy olla odotusten mukainen, ja sen tulee purkautua alkuperäiseksi - tai näyttää / kuulostaa oikealta, jos kyseessä on häviöllinen pakkaus. Shakkibotti ei saa tehdä laittomia siirtoja, ja sen on osattava tehdä matti, mikäli se on mahdollista sillä laskentasyvyydellä, jota käytetään. Jos kattava oikeellisuustesti vie liikaa aikaa, kannattaa laittaa yksikkötesteihin vain pari edustavaa testitapausta, ja tehdä lisäksi erillinen testiohjelma.

Suorituskykytestaus vie yleensä niin paljon aikaa, että sitä ei kannata tehdä automaattisilla testeillä ohjelman käynnistyksen yhteydessä. Jos yksikkötestien suorittamiseen menee useita minuutteja, ne tulee helposti ohitettua. Vastaavasti jos suorituskykytestien ajamiseen menee alle minuutti, on aika todennäköistä, että testit eivät ole riittäviä. Kokonaisuus täytyy yleensä testata itse kokeilemalla, raportoidaan mitä on kokeiltu. Testeissä saa käyttää mitä tahansa apukirjastoa. Testikattavuus tulee laskea automaattisesti. Huomaa silti, että kattavuuslaskenta on vain apuväline. On hyvin mahdollista tuottaa 100% kattavuus huonosti testatulle koodille. Tavoitteena on havaita kaikki virheet ohjelman toiminnassa. Kannattaa kirjoittaa mahdollisimman pieniä yksikkötestejä mahdollisimman paljon. Ideana on, että jos koodissa on virhe, tulisi vähintään yhden testin havaita se, ja virheen kohta koodissa tulisi olla mahdollisimman selkeä. Tämä on tärkeää, jotta virheiden korjaaminen on tehokasta.

Käyttöohje
Miten ohjelma suoritetaan, miten eri toiminnallisuuksia käytetään
Minkä muotoisia syötteitä ohjelma hyväksyy
Missä hakemistossa on jar ja ajamiseen tarvittavat testitiedostot.
Työn tekemisessä ja arvostelussa painotetaan laitoksen muita harjoitustöitä vähemmän dokumentointia. Ohjelmakoodin on kuitenkin oltava mahdollisimman selkeää, metodien on oltava lyhyitä, luokkien, muuttujien ja metodien on oltava kuvaavasti nimettyjä ja ohjelman rakenteen muutenkin kaikin puolin selkeä.

Koodin tulee olla kirjoitettu mahdollisimman selkeästi ja ymmärrettävästi. Kommentoi koodiasi kattavasti, mutta napakasti. Jokainen luokka, metodi ja attribuutti ei välttämättä kaipaa kommenttia, mutta kaikki olennainen ja vähemmän kuin itsestään selvä on oltava selostettu kommenteissa. Sisällytä metodien kommentteihin niiden parametrien ja paluuarvon merkitykset. Metodien sisäinen kommentointi ei ideaalitapauksessa pitäisi olla tarpeen, sillä metodien tulee olla kuvaavasti nimettyjä, kompakteja ja yksinkertaisia, helposti hahmotettavia kokonaisuuksia. Mikäli metodin toimintaa kuitenkin on vaikea hahmottaa pelkän koodin ja metodin yleiskommentin perusteella, voidaan sen koodia kommentoida sisäisestikin.

JavaDoc-kommentointia käytetään kaikissa töissä, jotka toteutetaan Javalla. NetBeans toteuttaa pyydettäessä luokille ja metodeille JavaDoc-kommenttien pohjat. Mikäli teet työsi jollakin muulla kielellä, sovi käytetystä kommentoitityylistä ohjaajan kanssa. Luokkakaaviot saat lisättyä JavaDoc:iisi suoraan käyttämällä YWorks-nimistä työkalua, joka generoi suoraan NetBeans-projektista kaaviot.
