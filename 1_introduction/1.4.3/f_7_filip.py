# Filip - Kattis

from sys import stdin

a, b = stdin.readline().split(" ")
a = int(a[::-1])
b = int(b[::-1])
n = a if a > b else b
print(n)