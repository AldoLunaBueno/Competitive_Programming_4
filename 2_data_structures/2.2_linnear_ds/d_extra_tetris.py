# Tetris - Kattis

# Reasoning
#
# Each piece have a special set of height pattern for its rotations.
# Just search for this patterns through the column heigth array of the board.
# The patterns are the relative heights (difference) from left to right.

from sys import stdin

pieces = {
    1: [[], [0, 0, 0]], # |
    2: [[0]], # []
    3: [[0, 1], [-1]], # S
    4: [[-1, 0], [1]], # Z
    5: [[0, 0], [-1], [-1, 1], [1]], # _|_
    6: [[0, 0], [-2], [1, 0], [0]], # L
    7: [[0, 0], [0], [0, -1], [2]] # _|
}

c, p = map(int, stdin.readline().split())
heights = [*map(int, stdin.readline().split())]

count = 0
for pattern in pieces[p]:
    if len(pattern) == 0:
        count += len(heights)
        continue
    tail = [None]*len(pattern)
    prev_h = float("Inf")
    for h in heights:
        diff = h - prev_h
        tail = tail[1:] + [diff]
        if tail == pattern:
            count += 1
        prev_h = h
print(count)