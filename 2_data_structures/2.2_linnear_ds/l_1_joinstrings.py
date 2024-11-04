# Join Strings

# Runtime: 0.14 s (The best in Python)
#
# Reasoning
#
# Clever solution by chaining indexes. (What DS am I using?)
# Being i the index of the i string...
# next[i] keeps the next string after i
# tail[i] keeps the last string in the sequence begining from i
# So "next" forms the chain of indexes 
# and "tail" let us chain sequences of indexes by connecting tail to head
# so that any concatenation is done in O(1) time.

from sys import stdin
inputs = stdin.read().splitlines()
n = int(inputs[0])
a = 1
next = [0] * (n+1)
tail = [i for i in range(n+1)]
for op in inputs[n+1:]:
    a, b = map(int, op.split())
    if tail[a] == 0:
        next[a] = b
    else:
        next[tail[a]] = b
    tail[a] = tail[b]
ans = []
index = a
for _ in range(n):
    ans.append(inputs[index])
    index = next[index]
print(*ans, sep="")


# Too slow implementation:

# from sys import stdin
# inputs = stdin.read().splitlines()
# n = int(inputs[0])
# a = 1
# for op in inputs[n+1:]:
#     a, b = map(int, op.split())
#     inputs[a] += inputs[b]
#     inputs[b] = ""
# print(inputs[a])