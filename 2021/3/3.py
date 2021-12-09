N = [x.strip() for x in open('in', 'r').readlines()]
width = len(N[0])
V = [[0 for _ in range(width)] for _ in range(2)]
gamma = ''
epsilon = ''

for n in N:
    for i, b in enumerate(n):
        V[1 if b =='1' else 0][i] += 1

for i in range(width):
    if V[0][i] > V[1][i]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(int(gamma, 2) * int(epsilon, 2))


oxygen = N[:]
co2 = N[:]
for i in range(width):
    if len(oxygen) > 1:
        ox_0 = len([x for x in oxygen if x[i] == '0'])
        ox_1 = len([x for x in oxygen if x[i] == '1'])
        if ox_1 >= ox_0:
            oxygen = [x for x in oxygen if x[i] == '1']
        else:
            oxygen = [x for x in oxygen if x[i] == '0']
    if len(co2) > 1:
        co2_0 = len([x for x in co2 if x[i] == '0'])
        co2_1 = len([x for x in co2 if x[i] == '1'])
        if co2_1 >= co2_0:
            co2 = [x for x in co2 if x[i] == '0']
        else:
            co2 = [x for x in co2 if x[i] == '1']
print(int(oxygen[0], 2) * int(co2[0], 2))