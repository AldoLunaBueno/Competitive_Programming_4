# Unique Snowflakes

# RUNTIME: 0.26 s (FASTER)
#
# Reasoning
#
# 

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