lines = open('input.txt', 'r').read().split('\n\n')
s1 = 0
s2 = 0

for group in lines:
    people = group.split('\n')
    ans = {}
    for p in people:
        for a in p:
            if a not in ans:
                ans[a] = 0
            ans[a] += 1
    s1 += len(ans)
    for k in ans:
        if ans[k] == len(people):
            s2 += 1

print(s1)
print(s2)
