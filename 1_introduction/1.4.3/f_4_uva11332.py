# Summing Digits - UVa 11332

from sys import stdin
while True:
    s = float("Inf")
    n = stdin.readline().strip()
    if n == "0":
        break
    while s >= 10:
        s = sum(int(i) for i in n)
        n = str(s)
    print(s)
    