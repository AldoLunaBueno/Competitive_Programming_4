# Almost Union-Find
# RUNTIME: 	0.41 s
#
# Reasoning:
#
# The extra operation called move challenges a typical union-find structure
# in one specific way:
# If we move a non-leaf node A to B, where A and B aren't together, just by letting A points B,
# A's children now are part of B set, which is nonsense (we want to move just A).
#
# Our solution solves this issue by removing the premise in the first place:
# there isn't any non-leaf node to move, never!
# This is achieved by a clever extension of the "parent" array,
# where the non-leaf nodes are never accessed from the outside
# because they are in the same array, but after all the accessible nodes.
# The accessible nodes point from the beginning to these non-leaf nodes
# (so accessible nodes are leaves and non-leaf nodes are roots 
# from the beginning).
#
# Here, for example, A and B are the only accessible nodes (n=2), 
# but they point to RA and RB (the real roots):
#       parent = [0, A, B, RA, RB]
# If we do A union B, we really do RA union RB.
#
# There is not much more because everything else works as before. And size and sum are easy to implement.
# Be careful with my 30 minutes bug: the input file may contain several test cases.
#
# The idea were found at https://codeforces.com/blog/entry/130521

import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(2*n+1)) # this does the MOVE trick!
        self.parent[1:n+1] = self.parent[n+1:2*n+1] # and this: i = n+i
        self.size = [1]*(2*n+1)
        self.arr_sum = list(range(-n, n+1))
    
    def find(self, a):
        tmp = a
        while a != self.parent[a]:
            a = self.parent[a]
        self.parent[tmp] = a # path compression
        return a
    
    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if self.parent[a_root] == self.parent[b_root]:
            return
        if self.size[a_root] < self.size[b_root]:
            a_root, b_root = b_root, a_root # union by size
        # change size and sum before changing the structure
        self.size[a_root] += self.size[b_root]
        self.arr_sum[a_root] += self.arr_sum[b_root]
        self.parent[b_root] = a_root # changes the structure
    
    def move(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if self.parent[a_root] == self.parent[b_root]:
            return
        # change size and sum before changing the structure
        self.size[a_root] -= 1
        self.size[b_root] += 1
        self.arr_sum[a_root] -= a
        self.arr_sum[b_root] += a
        self.parent[a] = b_root # changes the structure

input = sys.stdin.readlines()
i = 0
while i < len(input):
    n, q = map(int, input[i].split())
    uf = UnionFind(n)
    for j in range(i+1, i+1+q):
        op, *args = map(int, input[j].split())
        match op:
            case 1: # union
                uf.union(*args)
            case 2: # move
                uf.move(*args)
            case 3: # size
                root = uf.find(*args)
                print(uf.size[root], uf.arr_sum[root])
    i += q+1