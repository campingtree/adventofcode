numbers = [int(x) for x in open('in', 'r').read().split(',')]

l = len(numbers)
days = {x[1]: [x[0]+1, -1] for x in enumerate(numbers)}
prev = list(days)[-1]

def update(days, i):
    if not days.get(prev):
            days[prev] = [i, -1]
    else:
        if days[prev][1] != -1:
            days[prev][0] = days[prev][1]
        days[prev][1] = i

for i in range(l+1, 30000000+1):
    d = days.get(prev)
    if d[1] == -1:
        prev = 0
        update(days, i)
    elif d[1] != -1:
        prev = d[1] - d[0]
        update(days, i)

print(prev)