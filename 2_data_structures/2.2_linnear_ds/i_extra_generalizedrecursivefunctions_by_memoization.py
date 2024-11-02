# Generalized Recursive Functions - Kattis

# Runtime: 0.97 s
# It's considerably slower than dp solution

from typing import List, Tuple

class Memoized:
    def __init__(self, func):
        self._func = func
        self._cache = {}
    
    def __call__(self, *args, **kwargs):
        key = (args[0], args[1])
        if key not in self._cache:
            self._cache[key] = self._func(*args, **kwargs)
        return self._cache[key]
    
    def clean(self):
        self._cache = {}

def solve(x, y, a_b_pairs: List[Tuple], c, d):
    if x <= 0 or y <= 0:
        return d
    acc = 0
    for a, b in a_b_pairs:
        acc += solve(x-a, y-b, a_b_pairs, c, d)
    return acc + c

num_cases = int(input())
result = []
solve = Memoized(solve)

for _ in range(num_cases):
    *a_b_pairs, c, d = [*map(int, input().split())]
    if len(a_b_pairs) > 0:
        a_b_pairs = [(a, b) for a, b in zip(a_b_pairs[::2], a_b_pairs[1::2])] # pairing
    x_y_pairs = [*map(int, input().split())]
    x_y_pairs = [(x, y) for x, y in zip(x_y_pairs[::2], x_y_pairs[1::2])] # pairing
    answers = []
    for x, y in x_y_pairs:        
        ans = solve(x, y, a_b_pairs, c, d)
        answers.append(str(ans))
    result.append("\n".join(answers))
    solve.clean()
print("\n\n".join(result))