lines = open('in', 'r').read().splitlines()

s1 = 0
s2 = 0

for l in lines:
    p = l.split()
    n, m = [int(x) for x in p[0].split('-')]
    c = p[1][0]
    if n <= p[2].count(c) and p[2].count(c) <= m:
        s1 += 1
    if p[2][n-1].count(c) + p[2][m-1].count(c) == 1:
        s2 += 1

print(s1)
print(s2)
