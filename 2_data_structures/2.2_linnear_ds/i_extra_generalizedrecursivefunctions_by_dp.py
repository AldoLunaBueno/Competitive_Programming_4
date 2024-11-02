# Generalized Recursive Functions - Kattis

# Reasoning
#
# This problem has a recursive solution that can be easily reorder 
# to be solved by dynamic programming (dp).
# The recursive formulation of the function contrains the recursive calls 
# to lower xy pairs (no loops), so the dp solution matrix can begin at (0,0)
# and calculations can be iterated one by one in both dimensions
# until furthest xy pairs are reached.
#
# Runtime: 0.28 s

from typing import List, Tuple

def solve_by_dp(x_y_pairs: List[Tuple], a_b_pairs: List[Tuple], c, d):
    x_max, _ = max(x_y_pairs, key = lambda arr: arr[0])
    _, y_max = max(x_y_pairs, key = lambda arr: arr[1])

    dp = [[0] * (y_max+1) for _ in range(x_max+1)]
    for x in range(x_max+1):
        for y in range(y_max+1):
            if x <= 0 or y <= 0:
                dp[x][y] = d
                continue
            acc = 0
            for a, b in a_b_pairs: # O(1)
                x_, y_ = x-a, y-b
                if x_ <= 0 or y_ <= 0:
                    acc += d
                else:
                    acc += dp[x-a][y-b]
            dp[x][y] = acc + c
    return dp

num_cases = int(input())
result = []

for _ in range(num_cases):
    *a_b_pairs, c, d = [*map(int, input().split())]
    if len(a_b_pairs) > 0:
        a_b_pairs = [(a, b) for a, b in zip(a_b_pairs[::2], a_b_pairs[1::2])] # pairing
    x_y_pairs = [*map(int, input().split())]
    x_y_pairs = [(x, y) for x, y in zip(x_y_pairs[::2], x_y_pairs[1::2])] # pairing
    answers = []
    dp = solve_by_dp(x_y_pairs, a_b_pairs, c, d)
    for x, y in x_y_pairs:        
        ans = dp[x][y]
        answers.append(str(ans))
    result.append("\n".join(answers))
print("\n\n".join(result))
