# Inverted Deck
#
# This was exceptionally difficult for me
#
# Reasoning:
#
# The card values can be decomposed in three decks: 
# S1, S2 and S3, where S2 is the supposed inverted deck.
# If the collection was in non-decreasing order 
# before and now S2 is inverted,
# then S1 and S3 are still in non-decreasing order 
# and S2 is now in non-increasing order.
# We traverse S1, S2 and S3 in one go, 
# and we find end indexes of S2, r and l.
# Things can happen along the way: dumb or impossible case
# Dumb case is when all the collection is non-decreasing
# Impossible case is more difficult.


from typing import List
from sys import stdin

def solve(n, arr: List):
    if n == 1:
        print(1, 1)
        return
    
    # n >= 2

    # S1: non-decreasing
    is_decreasing = False
    l = 0
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            l = i+1
        elif arr[i] > arr[i+1]:
            is_decreasing = True
            break

    if not is_decreasing:
        print(1, 1)
        return

    # S3: non-decreasing
    r = n-1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            r = i
        elif arr[i] > arr[i+1]:
            break
    
    # S2: non-increasing
    for i in range(l, r):
        if arr[i] < arr[i+1]:
            print("impossible")
            return
    
    if (l > 0 and arr[l-1] > arr[r]) or (r < n-1 and arr[l] > arr[r+1]):
        print("impossible")
        return
    
    print(l+1, r+1)

n = int(input())
arr = [*map(int, stdin.readline().split())]

solve(n, arr)