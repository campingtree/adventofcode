import re

lines = open('in').read().splitlines()

G = {}
RG = {}
visited = {}

for l in lines:
    a, b = l.split(' bags contain ')
    in_bags = [(int(x), y) for x, y in re.findall(r'(\d+) ([a-z]+ [a-z]+) bag[s]?[,\.]', b)]
    if in_bags:
        G[a] = in_bags
    for x, y in in_bags:
        if y not in RG:
            RG[y] = []
        RG[y].append((x, a))


def rdfs(graph, x):
    s = 1 # need to count the bag itself
    # print(x)
    if x in visited:
        return visited[x]
    if x not in graph: # no children
        graph[x] = []
    for i, n in graph[x]:
        s += i * rdfs(graph, n)
    visited[x] = s
    return s


rdfs(RG, 'shiny gold')
print(len(visited) - 1)

visited = {}
print(rdfs(G, 'shiny gold') - 1)
