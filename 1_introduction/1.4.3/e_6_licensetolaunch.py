# License to Launch - Kattis

n = int(input())
arr = [int(x) for x in input().split(" ")]

min_value_index = 0
for i in range(1, len(arr)):
    if arr[i] < arr[min_value_index]:
        min_value_index = i
print(min_value_index)