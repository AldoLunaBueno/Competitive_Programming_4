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

def find(network, a):
    _a = a
    while a != network[a]:
        a = network[a]
    network[_a] = a # path compression
    return a

input = sys.stdin.readlines()
n, q = map(int, input[0].split())
network = [*range(n)]
size = [1]*n
output = []

for line in input[1:]:
    op, a, b = line.split()
    a, b = int(a), int(b)
    if op == "=": # union
        union(network, size, a, b)
    else: # equivalence query
        a_group = find(network, a)
        b_group = find(network, b)
        output.append(a_group==b_group)

print(*["yes" if out else "no" for out in output], sep="\n")