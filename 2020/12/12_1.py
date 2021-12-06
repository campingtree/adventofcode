ins = [(x[0], int(x[1:])) for x in open('in', 'r').read().splitlines()]

x = 0
y = 0
directions = ('E', 'N', 'W', 'S')
dire = 0

def move(d, a):
    global x, y
    if d == 'N':
        y += a
    elif d == 'S':
        y -= a
    elif d == 'W':
        x -= a
    elif d == 'E':
        x += a

for i in ins:
    move(i[0], i[1])
    if i[0] == 'L':
        dire = (dire + i[1] // 90) % 4
    elif i[0] == 'R':
        dire = (dire - (i[1] // 90)) % 4
    elif i[0] == 'F':
        move(directions[dire], i[1])
    # print(i, x, y, directions[dire])

# print(x, y)
print(abs(x) + abs(y))
