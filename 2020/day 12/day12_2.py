ins = [(x[0], int(x[1:])) for x in open('input.txt', 'r').read().splitlines()]

x = 0; y = 0
wx = 10; wy = 1

def move(d, a):
    global wx, wy
    if d == 'N':
        wy += a
    elif d == 'S':
        wy -= a
    elif d == 'W':
        wx -= a
    elif d == 'E':
        wx += a

for i in ins:
    move(i[0], i[1])
    if i[0] == 'L':
        for _ in range(i[1]//90):
            wx, wy = -wy, wx
    elif i[0] == 'R':
        for _ in range(i[1]//90):
            wx, wy = wy, -wx
    elif i[0] == 'F':
        x += i[1]*wx
        y += i[1]*wy

# print(x, y)
print(abs(x) + abs(y))
