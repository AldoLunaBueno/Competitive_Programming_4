# Statistics - Kattis

from typing import List

def solve(line: List):
    min_value = min(line)
    max_value = max(line)
    range_value = max_value - min_value
    return min_value, max_value, range_value

i = 1
while True:
    try:
        line = input()
    except EOFError:
        break
    line = [int(x) for x in line.strip().split(" ")]
    
    mn, mx, rg = solve(line[1:])
    print(f"Case {i}: {mn} {mx} {rg}")
    i += 1


