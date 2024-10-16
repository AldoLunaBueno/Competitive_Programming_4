from sys import stdin
from typing import List, Tuple

from algorithms.brute_force import solve

def main():
    while True:
        n = int(stdin.readline())
        if n == 0:
            break
        xy = []
        for _ in range(2*n):
            _, *pair = [x for x in stdin.readline().split(" ")]
            pair = [int(x) for x in pair]      
            xy.append(pair)
        solve(xy)
    
if __name__ == "__main__":
    main()