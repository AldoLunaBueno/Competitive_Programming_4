# Ladice
# RUNTIME: 0.36 s

import sys
def UnionFind(n: int):
    parent = [*range(n+1)]
    size = [1]*(n+1)
    item_count = [0]*(n+1)

    def union(a, b):
        a_root = find(a)
        b_root = find(b)
        if a_root == b_root:
            if item_count[a_root] >= size[a_root]:
                return False
            item_count[a_root] += 1
            return True
        
        if size[a_root] < size[b_root]:
            a_root, b_root = b_root, a_root # union by size

        if item_count[a_root] + item_count[b_root] >= size[a_root] + size[b_root]:
            return False
        item_count[a_root] += 1 + item_count[b_root]
        size[a_root] += size[b_root]
        parent[b_root] = a_root
        return True    

    def find(a):
        tmp = a
        while a != parent[a]:
            a = parent[a]
        parent[tmp] = a # path compression
        return a
    
    UnionFind.union = union
    return UnionFind

input = sys.stdin.readlines()
q, n = map(int, input[0].split())
uf = UnionFind(n)
output = []

for line in input[1:]:
    a, b = map(int, line.split())
    result = uf.union(a, b)
    output.append(result)

print(*["LADICA" if out else "SMECE" for out in output], sep="\n")

# import sys

# def union(parent, size, item_count, a, b):
#     a_root = find(parent, a)
#     b_root = find(parent, b)
#     if a_root == b_root:
#         if item_count[a_root] >= size[a_root]:
#             return False
#         item_count[a_root] += 1
#         return True
    
#     if size[a_root] < size[b_root]:
#         a_root, b_root = b_root, a_root # union by size

#     if item_count[a_root] + item_count[b_root] >= size[a_root] + size[b_root]:
#         return False
#     item_count[a_root] += 1 + item_count[b_root]
#     size[a_root] += size[b_root]
#     parent[b_root] = a_root
#     return True    

# def find(parent, a):
#     tmp = a
#     while a != parent[a]:
#         a = parent[a]
#     parent[tmp] = a # path compression
#     return a

# input = sys.stdin.readlines()
# q, n = map(int, input[0].split())
# parent = [*range(n+1)]
# size = [1]*(n+1)
# item_count = [0]*(n+1)
# output = []

# for line in input[1:]:
#     a, b = map(int, line.split())
#     result = union(parent, size, item_count, a, b)
#     output.append(result)

# print(*["LADICA" if out else "SMECE" for out in output], sep="\n")