from sys import stdin
n = int(input())
experiments = map(int, stdin.readline().split())
MODULO = 10**9+7
def solve():
    num_bacteria = 1
    for e in experiments:
        num_bacteria *= 2
        if num_bacteria < e:
            return "error"
        num_bacteria -= e
    return num_bacteria % MODULO

print(solve())

