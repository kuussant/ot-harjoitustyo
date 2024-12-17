import os
from statics import DEFENDER_PVT, DEFENDER_SGT, BOLT

DEFENDER_DATA = {
    DEFENDER_PVT: {
        "damage": 3,
        "speed": 1,
        "range": 120,
        "cost": 50,
        "projectile": BOLT,
        "projectiles": 1,
        "projectile_speed": 20
    },

    DEFENDER_SGT: {
        "damage": 3,
        "speed": 0.5,
        "range": 120,
        "cost": 100,
        "projectile": BOLT,
        "projectiles": 5,
        "projectile_speed": 7
    }
}
