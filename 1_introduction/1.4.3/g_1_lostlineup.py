n = int(input())
line = [int(x) for x in input().strip().split()]
# You, Kattis, are a dirty cat. My 20 min bug was split(" ")
# This crashes when the input line of numbers 
# has several whitespaces between contiguous numbers.
sorting = [0]*(n-1)
for i in range(n-1):
    sorting[line[i]] = i+2

print(1, end=" ")
print(*sorting)