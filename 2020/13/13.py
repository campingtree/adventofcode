time, ids = open('in', 'r').read().splitlines()
time = int(time)
ids = [x for x in ids.split(',')]

def p1():
    min_ttw = [0, 1e20]
    for i in filter(lambda x: x.isnumeric(), ids):
        i = int(i)
        ttw = -(time % i) + i
        if ttw < min_ttw[1]:
            min_ttw = [i, ttw]
    return min_ttw

ttw = p1()
print(ttw[0] * ttw[1])

# PART2: need at least python3.8 for built-in inverse mod
X = 1
for el in ids:
    if el.isnumeric():
        X *= int(el)

def chinese():
    x = 0
    for i, el in enumerate(ids):
        if el.isnumeric():
            ai = int(el) - i # adjust for subsequent number being larger
            Xi = X // int(el)
            inv_mod = pow(Xi, -1, mod=int(el))
            x += ai * Xi * inv_mod
    return x % X # because we need the first occurrence of such number

print(chinese())
