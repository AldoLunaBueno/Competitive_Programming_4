# Digits - Kattis
from sys import stdin

while True:
    s = float("Inf")
    n = stdin.readline().strip()
    if n == "END":
        break
    i = 0
    if n == "1":
        print(1)
        continue
    while s != 1:
        s = len(n)
        n = str(s)
        i += 1
    print(i+1)