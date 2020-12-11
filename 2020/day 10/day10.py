lines = [int(x) for x in open('input.txt').read().splitlines()]

lines.sort()
lines.insert(0, 0)
lines.append(lines[-1] + 3) 
l = len(lines)
diffs = {1: 0, 3: 0}
# print(lines)

for i in range(1, l):
    dif = lines[i] - lines[i-1]
    if dif == 1:
        diffs[1] += 1
    elif dif == 3:
        diffs[3] += 1

DA = {}
def dp(i):
    if i == l-1:
        return 1
    elif i in DA:
        return DA[i]
    ans = 0
    for j in range(i+1, min(i+5, l)):
        if lines[j] - lines[i] <= 3:
            ans += dp(j)
    DA[i] = ans
    return ans

print(diffs[1] * diffs[3])
print(dp(0))
