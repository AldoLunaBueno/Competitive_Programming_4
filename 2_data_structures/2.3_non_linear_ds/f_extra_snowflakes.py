# Unique Snowflakes

# RUNTIME: 0.26 s (FASTER)
#
# Reasoning
#
# We want the largest continuous sequence of unique elements.
# For each element, we require a way to lookup in the current sequence of unique elements 
# if we already have the current element. For this we need a set or a hash table.
# Then we delete this element and the previous ones from the current sequence of elements 
# to maintain its continuity and the uniqueness of its elements.
# Delete elements is easy in a deque (it's suitable for removing from the begining), 
# but for delete elements in a set (or hash table) we need to know its keys. 
# So we can store the keys in a deque to then delete the elements from the set or hash table.
# The deque and the set (or hash table) must to be synchronized.
# A hash table let to increase a little the speed compared to a set
# if we calculate how many elements we need to delete (in my code is called stop).

import sys
from collections import deque
input = sys.stdin.readline

num_cases = int(input())
for _ in range(num_cases):
    num_sf = int(input())
    package = deque()
    curr_unique = {}
    max_streak = 0
    for i in range(num_sf):
        curr_sf = int(input())
        if curr_sf not in curr_unique:
            curr_unique[curr_sf] = i
            package.append(curr_sf)
        else:
            max_streak = max(max_streak, len(package))
            stop = len(package) - (i - curr_unique[curr_sf]) + 1 # tricky
            for _ in range(stop):
                sf = package.popleft()
                del curr_unique[sf]
            
            curr_unique[curr_sf] = i
            package.append(curr_sf)
        max_streak = max(max_streak, len(package))
    print(max_streak)

# RUNTIME: 0.38 s (SLOW)
#
# num_cases = int(input())
# for _ in range(num_cases):
#     curr_unique = {}
#     max_streak = 0
#     n = int(input()) # number o snowflakes
#     snowflakes = [int(input()) for _ in range(n)]
#     i = 0
#     while i < n:
#         sf = snowflakes[i]
#         if sf in curr_unique:
#             max_streak = max(max_streak, len(curr_unique))
#             i = curr_unique[sf]+1
#             curr_unique = {}
#         else:
#             curr_unique[sf] = i
#             i += 1
#     max_streak = max(max_streak, len(curr_unique))
#     print(max_streak)