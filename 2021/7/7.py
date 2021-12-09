X = [int(x) for x in open('in', 'r').read().strip().split(',')]

# [PART1]
# Need to find T, such that min(sum_{x for X}{|x-T|}).
# If we change T to T-1 -> costs increases by 1 for each x >= T and
#   decreases by 1 for each x <= T-1.
# If we change T to T+1 -> costs increases by 1 for each x <= T and
#   decreases by 1 for each x >= T+1.
# Delta = |X's to right of T| - |X's to left of T|.
# Best T - median of sorted ascending sorted X.

# [PART2]
# Need to find T, such that min(sum}{x for X}{|x_T|*(|x-T|+1)/2})

X.sort()
T = X[len(X)//2]
M = max(X)
a1 = 0

def binom_2(n):
    # choose 2 from n+1
    # (n+1)!/2!(n+1-2)! = (n+1)n/2
    return (n+1)*n // 2

for x in X:
    a1 += abs(x-T)

upper_bound = 1e10
for med in range(M):
    score = 0
    for x in X:
        delta = abs(x-med)
        score += binom_2(delta)
    if score < upper_bound:
        upper_bound = score

print(a1)
print(upper_bound)