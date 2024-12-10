## Sovelluslogiikka

```mermaid
classDiagram
      Game "1" <-- "1" Stage
      Stage "1" <-- "*" Defender
      Stage "1" <-- "*" Enemy
      Stage "1" <-- "1" Map
      Defender "1" <-- "*" Bullet
      Stage "1" <-- "*" Bullet
      class Stage {
          enemies
          defenders
          bullets
          map
      }
      class Defender{
          damage
          attack_range
      }
      class Enemy{
          hp
          movement_speed
          path_nodes
      }
      class Bullet{
          damage
          pos
          direction
      }
      class Map{
          map_tiles
      }
```

Pelin looppi pyörii luokassa [Game](https://github.com/kuussant/ot-harjoitustyo/blob/main/towerdefence/src/game.py), joka luo pelin logiikan sisältävän olion [Stage](https://github.com/kuussant/ot-harjoitustyo/blob/main/towerdefence/src/stage.py). Pelin puolustajia [Defender](https://github.com/kuussant/ot-harjoitustyo/blob/main/towerdefence/src/sprites/defender.py) asetellaan pelikartan ruudukoihin, jos pelaajalla riittää rahaa. Kun pelaaja on valmis, painaa tämä välilyöntiä, jolloin ensimmäinen kierros voi alkaa. Kierroksen aikana vihollisia [Enemy](https://github.com/kuussant/ot-harjoitustyo/blob/main/towerdefence/src/sprites/enemy.py)
alkaa spawnata. Kun vihollinen lähestyy puolustajia, ampuu puolustajat luoteja [Bullet](https://github.com/kuussant/ot-harjoitustyo/blob/main/towerdefence/src/sprites/bullet.py)
vihollista kohti. Jos luodit osuvat, vähentävät nämä vihollisen hp-arvoa kunnes vihollinen kuolee. Jokaisesta viholliskuolemasta pelaaja ansaitsee rahaa. Kun kaikki viholliset ovat kuolleet, voi pelaaja aloittaa uuden kierroksen.

## Sekvenssikaavio
```mermaid
 sequenceDiagram
    create participant game
    main->>game: Game()
    create participant stage
    activate game
    game->>stage: Stage()
    create participant defender
    stage->>defender: Defender()

    game->>stage: handle_wave()
    create participant enemy
    stage->>enemy: Enemy()
    activate enemy
    stage->>enemy: update()
    stage->>defender: update(enemy_group, bullet_group)
    create participant bullet
    defender->>bullet: Bullet()
    activate bullet
    bullet->>stage: 
    stage->>bullet: bullet.damage
    bullet->>stage: 3
    deactivate bullet
    stage->>enemy: deal_damage(3)
    enemy->>stage: 10
    deactivate enemy
    game->>stage: game_won()
    stage->>game: True
    deactivate game
```
Ohjelman looppi alkaa käynnistämällä index.py tiedoston missä luodaan Game-olio. Game olio luo Stage-olion joka sisältää pelin logiikan. Game-loopissa pelaaja voi asetella puolustajia (Defender). 

Kun pelaaja on valmis, painaa tämä välilyöntiä jolloin kierros alkaa. Kierroksen aikana kartalle alkaa ilmestyä vihollisia (Enemy). Jokaisen Stage-luokassa tapahtuvan updaten aikana liikutetaan vihollisia ja tarkistetaan onko vihollinen tarpeeksi lähellä puolustajaa. Kun vihollinen on tarpeeksi lähellä puolustajaa, ampuu puolustaja luodin (Bullet), joka palautetaan Stage-luokkaan. 

Jos luoti osuu viholliseen, tarkistetaan paljonko se tekee vahinkoa, ja sen jälkeen vahingoitetaan osunutta vihollista. Vihollinen ottaa vahinkoa luodin verran (3), joka riittää tappamaan vihollisen, jonka jälkeen tämä palauttaa palkinnoksi rahasumman (10) pelaajalle.

Kun viimeinen vihollinen on tapettu, kysyy Game luokalta stage onko peli päättyntyt, johon Stage palauttaa arvon True, jolloin peli vihdoin päättyy.
