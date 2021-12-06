lines = open('in', 'r').read().splitlines()
l = len(lines)
w = len(lines[0])

def check(r, d=1):
    s = 0
    x = 0
    for i in range(1, l):
        x += r
        x %= w
        if i * d < l:
            if lines[i*d][x] == '#':
                s += 1
    return s

print(check(3))    
print(check(1) * check(3) * check(5) * check(7) * check(1, 2))
