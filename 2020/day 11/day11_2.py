from pprint import pprint
from copy import deepcopy

lines = open('input.txt', 'r').read().splitlines()

layout = [list(x) for x in lines]
h = len(lines)
w = len(lines[0])
a2 = 0

def check(arr, i, j):
    check = 0
    l = 1; ul = 1; u = 1; ur = 1
    r = 1; dr = 1; d = 1; dl = 1

    while j-l >= 0:
        if arr[i][j-l] == '#':
            check += 1
            break
        elif arr[i][j-l] == 'L':
            break
        l += 1
    while j-ul >= 0 and i-ul >= 0:
        if arr[i-ul][j-ul] == '#':
            check += 1
            break
        elif arr[i-ul][j-ul] == 'L':
            break
        ul += 1
    while i-u >= 0:
        if arr[i-u][j] == '#':
            check +=1
            break
        elif arr[i-u][j] == 'L':
            break
        u += 1
    while j+ur <= w-1 and i-ur >= 0:
        if arr[i-ur][j+ur] == '#':
            check += 1
            break
        elif arr[i-ur][j+ur] == 'L':
            break
        ur += 1
    while j+r <= w-1:
        if arr[i][j+r] == '#':
            check += 1
            break
        elif arr[i][j+r] == 'L':
            break
        r += 1
    while j+dr <= w-1 and i+dr <= h-1:
        if arr[i+dr][j+dr] == '#':
            check += 1
            break
        elif arr[i+dr][j+dr] == 'L':
            break
        dr += 1
    while i+d <= h-1:
        if arr[i+d][j] == '#':
            check += 1
            break
        elif arr[i+d][j] == 'L':
            break
        d += 1
    while j-dl >= 0 and i+dl <= h-1:
        if arr[i+dl][j-dl] == '#':
            check += 1
            break
        elif arr[i+dl][j-dl] == 'L':
            break
        dl += 1
    return check

def sim(_layout, prev_layout = []):
    if prev_layout == _layout:
        return prev_layout

    prev_layout = deepcopy(_layout)
    new_layout = deepcopy(_layout)

    for i in range(h):
        for j in range(w):
            if _layout[i][j] == 'L':
                if check(_layout, i, j) == 0:
                    new_layout[i][j] = '#'
            elif _layout[i][j] == '#':
                if check(_layout, i, j) >= 5: # 4
                    new_layout[i][j] = 'L'
    # pprint(new_layout)
    return sim(new_layout, prev_layout)

for r in sim(layout):
    a2 += r.count('#')
print(a2)
