lines = [int(x) for x in open('input.txt', 'r').read().splitlines()]
a1 = 0
a2 = 0

l = len(lines)

for i in range(l):
    for j in range(i + 1, l):
        if (lines[i] + lines[j] == 2020):
            a1 = lines[i] * lines[j]
        for z in range(j + 1, l):
            if (lines[i] + lines[j] + lines[z] == 2020):
                a2 = lines[i] * lines[j] * lines[z]
print(a1)
print(a2)