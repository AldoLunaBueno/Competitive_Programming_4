# Pipe Rotation

# Pipes:
# (A) Nothing
# (B) Straight pipe (pipes leaving through two opposite edges)
# (C) Elbow-shaped pipe (pipes leaving through two adjacent edges)
# (D) Four-way pipe (pipes leaving through all four edges)

# Interesting problem. Solved with a flag and a flag vector.

POSSIBLE = "Possible"
IMPOSSIBLE = "Impossible"

ROWS, COLS = map(int, input().split())
BOARD = [input() for _ in range(ROWS)]

def solve():
    left_even = True # Is the number of C tubes seen so far from left to right in the row even?
    top_even = [True] * COLS # Is the number of C tubes seen so far from top to bottom in the column even?
    for i in range(ROWS):
        for j in range(COLS):        
            pipe = BOARD[i][j]
            if (left_even and top_even[j]) and pipe in ("A","C"):
                pass
            elif (not left_even and not top_even[j]) and pipe in ("C","D"):
                pass
            elif (not left_even or not top_even[j]) and pipe in ("B","C"):
                pass
            else:
                return IMPOSSIBLE
            
            if pipe == "C": # for the next iteration
                left_even = not left_even # ... of the inner loop
                top_even[j] = not top_even[j] # ... of the outer loop
        if not left_even:
            return IMPOSSIBLE
    if not all(top_even):
        return IMPOSSIBLE
    return POSSIBLE

print(solve())

        
        