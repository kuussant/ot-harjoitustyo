import json
from statics import *


def save_map(file, map):
    try:
        with open(file, "w") as f:
            f.write(json.dumps(map))
        return True
    except IOError as e:
        print("Failed to save map", e)

    return False


def load_map(file):
    out_map = []
    try:
        with open(file, "r") as f:

            for row in json.load(f):
                new_row = []
                for col in row:
                    col_tuple = (col[0], col[1])
                    new_row.append(col_tuple)

                out_map.append(new_row)
    except IOError as e:
        print("Failed to load map:", e)
        return None

    return out_map
