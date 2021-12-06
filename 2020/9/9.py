lines = [int(x) for x in open('in', 'r').read().splitlines()]

preamble = 25
l = len(lines)

def p1():
    a = 0
    for i in range(l):
        if i < preamble:
            continue
        _pass = False
        for j in range(a, i-1):
            for z in range(j+1, i):
                if lines[j] + lines[z] == lines[i]:
                    _pass = True
                    break
        if not _pass:
            return lines[i]
        a += 1

def p2(num):
    a = 0
    b = 1
    s = lines[0]
    while True:
        if s == num:
            return min(lines[a:b]) + max(lines[a:b])
        elif s < num:
            s += lines[b]
            b += 1
        elif s > num:
            s -= lines[a]
            a += 1

a1 = p1()
print(a1)
print(p2(a1))
