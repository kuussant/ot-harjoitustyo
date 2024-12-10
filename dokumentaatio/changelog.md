## Viikko 3

- Projektin varsinainen pohja luotu
- Lisätty muutama alustava luokka: Bullet, Defender, Game
    - Vain Game ja Defender tekevät tekevät tällä hetkellä jotain
    - Game huolehtii pelin loopista
    - Defender vastaa puolustajista
- Käyttäjä voi nyt asetella puolustajia "kartalle" (jotka eivät toistaiseksi tee mitään)

## Viikko 4

- Viholliset nyt seuraavat ennaltamäärättyä polkua
    - Vihollisia voi "spawnata" hiiren oikealla näppäimellä
- Puolustajat ampuvat vihollisia luodeilla kunnes ne kuolevat
    - Puolustajia spawnataan hiiren oikealla näppäimellä
 
## Viikko 5

- Uusi map editori lisätty
    - Karttoja voi nyt tehdä map editorilla, jossa voi piirtää uusia karttoja
    - Editori sisältää 25 eri uutta kotitekoista spriteä
    - Editori tarkistaa automaattisesti onko vihollispolku validi, piirtämällä sen näytölle, kun se toimii.
    - Editorin käytöstä lisää [täällä]([https://github.com/kuussant/](https://github.com/kuussant/ot-harjoitustyo/blob/main/README.md))
- Editorilla luotuo kartta lisätty peliin, ja lisäksi uudet vihollis-grafiikat.

## Viikko 6
- Lisätty uudet kotitekoiset vihollisgrafiikat, ja mukaanlukien niiden animaatiot
- Lisätty kaksi uutta vihollistyyppiä: Goblin Grunt ja Goblin Brute
    - Vihollistyypeillä on omat "statsinsa": Eri liikkumisnopeus ja hp-määrä
- Pelissä on nyt toimivat vihollisaallot
    - Vihollisaallon voi käynnistää välilyönnillä
    - Jokainen aalto on erilainen ja sisältää eri määrän eri vihollistyyppejä
- Puolustajia lisätään nyt pelin sisäisiin ruudukkoihin
    - Vain yhden puolustajan voi lisätä yhden ruudun sisälle
- Puolustajat nyt maksavat rahaa, jota voi tienata tappamalla vihollisia
    - Jos raha ei riitä, ei voi ostaa uutta puolustajaa
- Lisätty äänet
