from collections import Counter, defaultdict

FISH = Counter([int(x) for x in open('in', 'r').read().strip().split(',')])

def solve(n):
    X = FISH
    for day in range(n):
        NEW_FISH = defaultdict(int)
        for x, cnt in X.items():
            if x == 0:
                NEW_FISH[6] += cnt
                NEW_FISH[8] += cnt
            else:
                NEW_FISH[x-1] += cnt
        X = NEW_FISH
    return sum(X.values())

print(solve(80))
print(solve(256))