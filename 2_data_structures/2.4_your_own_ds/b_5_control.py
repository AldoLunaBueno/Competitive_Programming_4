# Association for Control Over Minds
# RUNTIME: 0.67 s
#
# We have a number of distinct and individual ingredients.
# A cauldron is a set of these ingredients.
# The union-find structure is revealed when we think of cauldrons like disjoint sets.
# An ingredient can't be in two cauldrons at the same time,
# and once a cauldron is formed it can't be separated.
# A cauldron can only transfer its contents to another cauldron,
# so a cauldron receiving ingredients from several cauldrons 
# is our multi-union operation.
# For simplicity, we consider that each ingredient is from the begining
# in a cauldron of one element (we don't count these cauldrons).
#
# The restriction of this muli-union operation is the concept of recipe.
# A cauldron has exactly the ingredients of the recipe, no more, no less.
# For our multi-union operation, this implies that, if a ingredient of a cauldron
# is found in the recipe, all other ingredients of the cauldron must be found
# to concoct the cauldron.
# So our restriction in the end is this: (why?)
#       sum(size of found cauldrons) == len(recipe)
#
# The final result is the number of cauldrons concocted

from collections import defaultdict
from typing import Tuple
import sys

def UnionFind():
    parent = {}
    size = defaultdict(lambda: 1)

    def find(node):
        tmp = node
        while node in parent:
            node = parent[node]
        if tmp != node:
            parent[tmp] = node # path compression
        return node

    def multi_union(nodes: Tuple[int]):
        # problem specific restriction
        found_roots = list(set(find(node) for node in nodes))
        found_sizes = [size[node] for node in found_roots]
        size_sum = sum(found_sizes)
        if size_sum != len(nodes):
            return False
        
        # multi-union
        root, _ = max(zip(found_roots, found_sizes), key = lambda root_n_size: root_n_size[1])
        for node in nodes:
            parent[node] = root
        del parent[root]
        size[root] = size_sum
        return True
    
    UnionFind.multi_union = multi_union
    return UnionFind

uf = UnionFind()
count = 0
inputs = sys.stdin.readlines()
for line in inputs[1:]:
    m, *recipe_ingredients = map(int, line.split())
    concot_done = uf.multi_union(recipe_ingredients)
    if concot_done:
        count += 1
print(count)
