import statics

SEED = 123456

SPAWN_DATA = [
    {
        "spawn_rate": 1000,
        "enemies":
        {
            "goblin_grunt": 10,
            "goblin_brute": 0
        }
    },
    {
        "spawn_rate": 400,
        "enemies":
        {
            "goblin_grunt": 30,
            "goblin_brute": 0
        }
    },
    {
        "spawn_rate": 200,
        "enemies":
        {
            "goblin_grunt": 30,
            "goblin_brute": 0
        }
    },
    {
        "spawn_rate": 400,
        "enemies":
        {
            "goblin_grunt": 20,
            "goblin_brute": 10
        }
    },
    {
        "spawn_rate": 300,
        "enemies":
        {
            "goblin_grunt": 20,
            "goblin_brute": 20
        }
    },
    {
        "spawn_rate": 200,
        "enemies":
        {
            "goblin_grunt": 0,
            "goblin_brute": 100
        }
    }
]

ENEMY_DATA = {
    "NaN": {
        "hp": 6,
        "speed": 3,
        "value": 10
    },

    statics.GOBLIN_GRUNT: {
        "hp": 3,
        "speed": 2,
        "value": 10
    },

    statics.GOBLIN_BRUTE: {
        "hp": 15,
        "speed": 1.5,
        "value": 20
    }
}
