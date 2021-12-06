import re
from pprint import pprint

data = open('in').read().split('\n\n')
pattern = re.compile(r'([a-z ]+?)\: (\d+)\-(\d+) or (\d+)\-(\d+)')

fields = {}
for x in data[0].split('\n'):
    p = pattern.match(x).groups()
    r1 = range(int(p[1]), int(p[2])+1)
    r2 = range(int(p[3]), int(p[4])+1)
    fields[p[0]] = [r1, r2]

my_ticket = [int(x) for x in data[1].split('\n')[-1].split(',')]
nearby_tickets = [list(map(int, x.split(','))) for x in data[2].split('\n')[1:]]

def p1():
    err = 0
    to_del = []
    for i, t in enumerate(nearby_tickets):
        for n in t:
            flag = False
            for ranges in fields.values():
                if n in ranges[0] or n in ranges[1]:
                    flag = True
                    break
            if not flag:
                err += n
                to_del.append(i)
    vnearby_tickets = [x[1] for x in filter(lambda x: x[0] not in to_del, enumerate(nearby_tickets))]
    return err, vnearby_tickets

err, vnearby_tickets = p1()
print(err)

vnearby_tickets.append(my_ticket)
def p2():
    linelen = len(vnearby_tickets[0])
    answer = {}
    MAP = {}
    s = 1
    for k, f in fields.items():
        for i in range(linelen):
            flag = True
            for j in range(len(vnearby_tickets)):
                if vnearby_tickets[j][i] not in f[0] and vnearby_tickets[j][i] not in f[1]:
                    flag = False
                    break
            if flag:
                if k not in answer:
                    answer[k] = []
                answer[k].append(i)
    for k, v in dict(sorted(answer.items(), key=lambda k: len(k[1]))).items():
        assert len(v) == 1
        i = v[0]
        for k2 in answer:
            if i in answer[k2]:
                answer[k2].remove(i)
        MAP[k] = my_ticket[i]
        if k.startswith('departure'):
            s *= my_ticket[i]
    return MAP, s

MAP, s = p2()
# pprint(MAP)
print(s)
