# Pivot


# Solution that use sorting algorithm.
# Time complexity: O(n*log(n))

# n = int(input())
# arr = [*map(int, input().split())]
# sorted_arr = sorted(arr)
# count = 0
# curr_max = float("-Inf")
# for i in range(len(arr)):
#     if arr[i] == sorted_arr[i] and arr[i] > curr_max:
#         count += 1
#     curr_max = max(curr_max, arr[i])

# print(count)

#----------------------------------------------------------

# Solution that use static min/max query
# Time complexity: O(n)
from sys import stdin
n = int(stdin.readline())
arr = [int(x) for x in stdin.readline().split()]
max_static_arr = [0]*len(arr) # array for static max query
curr_max = float("-Inf")
for i in range(len(arr)):
    if arr[i] > curr_max:
        curr_max = arr[i]
    max_static_arr[i] = curr_max

min_static_arr = [0]*len(arr) # array for static min query
curr_min = float("Inf")
for i in range(1, len(arr)+1):
    if arr[-i] < curr_min:
        curr_min = arr[-i]
    min_static_arr[-i] = curr_min

count = 0
if arr[0] < min_static_arr[1]:
    count += 1
if arr[-1] > max_static_arr[-2]:
    count += 1

for i in range(1, len(arr)-1):
    if arr[i] > max_static_arr[i-1] and arr[i] < min_static_arr[i+1]:
        count += 1

print(count)