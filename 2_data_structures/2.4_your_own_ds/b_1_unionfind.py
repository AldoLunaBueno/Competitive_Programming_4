# Union-Find
# RUNTIME: 0.85 s

import sys

def union(network, size, a, b):
    a_group = find(network, a)
    b_group = find(network, b)
    if a_group == b_group:
        return
    # union by size
    if size[a_group] < size[b_group]:
        a_group, b_group = b_group, a_group
    network[b_group] = a_group
    size[a_group] += size[b_group]

# With this recursive find() it's slower! RUNTIME: 0.96 s
# def find(parent, a):
#     if a != parent[a]:
#         parent[a] = find(parent, parent[a])
#     return parent[a]

def find(parent, a):
    tmp = a
    while a != parent[a]:
        a = parent[a]
    parent[tmp] = a # path compression
    return a


input = sys.stdin.readlines()
n, q = map(int, input[0].split())
parent = [*range(n)]
size = [1]*n
output = []

for line in input[1:]:
    op, a, b = line.split()
    a, b = int(a), int(b)
    if op == "=": # union
        union(parent, size, a, b)
    else: # equivalence query
        a_group = find(parent, a)
        b_group = find(parent, b)
        output.append(a_group==b_group)

print(*["yes" if out else "no" for out in output], sep="\n")