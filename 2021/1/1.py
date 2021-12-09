a1 = 0
a2 = 0
MS = [int(x) for x in open('in', 'r')]

for i in range(len(MS)):
    if i >= 1 and MS[i] > MS[i-1]:
        a1 += 1
    if i >= 3 and MS[i]+MS[i-1]+MS[i-2] > MS[i-1]+MS[i-2]+MS[i-3]:
        a2 += 1

print(a1)
print(a2)