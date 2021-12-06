from itertools import product, repeat
from pprint import pprint


data = open('in').read().split('\n')


def p1(cycles=6):
    ON = set()
    NEW_ON = set()
    CHECK = set()

    for y, row in enumerate(data):
        for x, state in enumerate(row):
            if state == '#':
                ON.add((x, y, 0))

    for _ in range(cycles):
        for x, y, z in ON:
            for dx, dy, dz in product((-1, 0, 1), repeat=3):
                # if w+dw == 0:
                CHECK.add((x+dx, y+dy, z+dz))

        for x, y, z in CHECK:
            nbrs = 0
            for dx, dy, dz in product((-1, 0, 1), repeat=3):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                # if dx != 0 or dy != 0 or dz != 0:
                if (x+dx, y+dy, z+dz) in ON:
                    nbrs += 1
            if (x, y, z) in ON and nbrs in (2, 3):
                NEW_ON.add((x, y, z))
            elif (x, y, z) not in ON and nbrs == 3:
                NEW_ON.add((x, y, z))
        ON = NEW_ON

    return len(ON)
        

print(p1())