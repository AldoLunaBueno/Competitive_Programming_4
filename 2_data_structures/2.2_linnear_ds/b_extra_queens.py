# Queens
#
# Interesting problem solved by 1D array minipulation
#
# Reasoning:
#
# Four lists are used: row (r), column (c), positive diagonal (p) 
# and negative diagonal (n).
# Each queen have a key for each of the four list.
# The key is generated using the coordinates x and y like this:
# - r: y
# - c: x
# - p: x+y
# - n: x-y
# If any list has a key already occupied for one queen,
# then the solution is incorrect.
# If it doesn't happened for any queen,
# then the solution is correct.

def solve():
    N = int(input())
    r = [False]*N
    c = [False]*N
    p = [False]*(2*N-1)
    n = [False]*(2*N-1)
    for _ in range(N):
        x, y = map(int, input().split()) # queen (x,y) position
        if r[y] or c[x] or p[x+y] or n[x-y]:
            return "INCORRECT"
        else:
            r[y], c[x], p[x+y], n[x-y] = [True]*4
    return "CORRECT"

print(solve())
