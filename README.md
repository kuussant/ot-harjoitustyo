# Tower defence peli (ei vielä nimeä)

Kyseessä on Pygamella toteutettava Tower defense -tyylinen peli jossa pelaajan on tarkoitus puolustaa tukikohtaa suurelta vihollismäärältä. Pelin "looppi" muodostuu kierroksista, joissa pelaajan on sovellettava eri puolustajia (tykkejä, sotilaita yms.) joilla pelaaja puolustaa tukikohtaansa yhä kasvavalta vihollismäärältä. Viholliset seuraavat tiettyä polkua hiljalleen jonossa, jonka juureen pelaajan on pystytettävä puolustuksensa. Polku alkaa jostain kaukaisesta kohdasta karttaa, joka johtaa pelaajan tukikohtaan. Jos yksittäinen vihollinen saavuttaa pelaajan tukikohdan, tekee tämä vahinkoa tukikohtaan, ja jos tukikohdan HP (health points) loppuu, pelaaja häviää.

#### Puolustajat

Pelissä on lukuisia eri puolustajia, esim. tykkejä ja sotilaita yms. joita pelaaja asettelee ympäri pelin karttaa, tien juureen, jota pitkin viholliset liikkuvat. Puolustajat tuhoavat lähellä liikkuvia vihollisjoukkoja automaattisesti. Puolustajien asettaminen ympäri karttaa maksaa rahaa, jota pelaaja tienaa aina voitettuaan kierroksen.

#### Vihollisjoukot

Pelin viholliset koostuvat eri yksiköistä joiden HP-määrä (ja mahdollisesti liikkumisnopeus) vaihtelee. Viholliset liikkuvat tietä pitkin kohti pelaajan tukikohtaa, eivätkä ole uhka itse puolustajille, vaan ainoastaan tukikohdalle.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/kuussant/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä peli komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Pelin voi käynnistää komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Pelaaminen

Pelissä voi toistaiseksi asetella puolustajia hiiren vasemmalla napilla ja vihollisia hiiren oikealla napilla
