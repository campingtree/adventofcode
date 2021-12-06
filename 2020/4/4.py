lines = open('in', 'r').read().split('\n\n')

s1 = 0
s2 = 0

def vcolor(c):
    return ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c) <= ord('f')

def vpart(k: str, v : str) -> bool:
    if k == 'byr':
        return v.isnumeric() and 1920 <= int(v) <= 2002
    elif k == 'iyr':
        return v.isnumeric() and 2010 <= int(v) <= 2020
    elif k == 'eyr':
        return v.isnumeric() and 2020 <= int(v) <= 2030
    elif k == 'hgt':
        if v[-2:] == 'cm':
            return v[:-2].isnumeric() and 150 <= int(v[:-2]) <= 193
        elif v[-2:] == 'in':
            return v[:-2].isnumeric() and 59 <= int(v[:-2]) <= 76
        return False
    elif k == 'hcl':
        return v[0] == '#' and all(vcolor(x) for x in v[1:])
    elif k == 'ecl':
        return v in 'amb blu brn gry grn hzl oth'.split()
    elif k == 'pid':
        return v.isnumeric() and len(v) == 9
    elif k == 'cid':
        return True
    return False

for p in lines:
    parts = {}
    for x in p.split():
        a, b = x.split(':')
        parts[a] = b
    if len(parts) == 8 or (len(parts) == 7 and 'cid' not in parts):
        s1 += 1
        if all(vpart(x, y) for x, y in parts.items()):
            s2 += 1

print(s1)
print(s2)
