A1 = dict()
A2 = dict()

for line in open('in', 'r'):
    start, end = line.split('->')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    x1 = int(x1.strip())
    y1 = int(y1.strip())
    x2 = int(x2.strip())
    y2 = int(y2.strip())

    dx = x2-x1
    dy = y2-y1

    for i in range(1 + max(abs(dx),abs(dy))):
        x = x1 + (1 if dx > 0 else (-1 if dx < 0 else 0))*i
        y = y1 + (1 if dy > 0 else (-1 if dy < 0 else 0))*i
        # vertical || horizontal
        if dx == 0 or dy == 0:
            if not A1.get((x, y)):
                A1[(x, y)] = 1
            else:
                A1[(x, y)] += 1
        # diagonal
        if not A2.get((x, y)):
            A2[(x, y)] = 1
        else:
            A2[(x, y)] += 1

print(len([i for i in A1 if A1[i] > 1]))
print(len([i for i in A2 if A2[i] > 1]))