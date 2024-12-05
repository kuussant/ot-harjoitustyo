import os
from statics import DIRNAME

SPAWN_DATA = [
    {
        "goblin_grunt": 20,
        "goblin_brute": 0
    },
    {
        "goblin_grunt": 30,
        "goblin_brute": 0
    },
    {
        "goblin_grunt": 20,
        "goblin_brute": 10
    },
    {
        "goblin_grunt": 20,
        "goblin_brute": 20
    },
    {
        "goblin_grunt": 30,
        "goblin_brute": 20
    }
]

ENEMY_DATA = {
    "goblin_grunt": {
        "image_file": os.path.join(DIRNAME, "assets", "td_goblin.png"),
        "hp": 3,
        "speed": 2
    },

    "goblin_brute": {
        "image_file": os.path.join(DIRNAME, "assets", "td_goblin.png"),
        "hp": 20,
        "speed": 1
    }
}