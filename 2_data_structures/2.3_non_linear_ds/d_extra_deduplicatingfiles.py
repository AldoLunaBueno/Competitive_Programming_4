from collections import defaultdict
from typing import Dict

# Reasoning
#
# If two different files (strings here) have the same hash key, they collide.
# But two copies of the same file don't collide, despite having the same hash key.
#
# We organize the file count in a nested dictionary.
# First group by hash, and then group by file.
# So in the outer dictionary each hash key founded is assigned to a inner dictionary
# where each file is assigned to its count.
#
# The total collisions are the sum of the collisions for each hash.
# For the collisions in one hash, multiply the count values assinged for each file
# taking two by two the files.

def calculate_colissions(hashes: Dict[int, Dict[str, int]]):
    num_collisions = 0
    for file_count in hashes.values():
        counts = list(file_count.values())
        # taking two by two the files
        for i in range(len(counts)-1):
            for j in range(i+1, len(counts)):
                num_collisions += counts[i] * counts[j]
    return num_collisions

while True:
    num_files = int(input())
    if num_files == 0:
        break
    files = set()
    file_count = lambda: defaultdict(int)
    hashes = defaultdict(file_count)
    for i in range(num_files):
        file = input()
        hash = 0 # it doesn't alterate the result
        for c in file:
            hash ^= ord(c)
        hashes[hash][file] += 1
        files.add(file)
    print(f"{len(files)} {calculate_colissions(hashes)}")

        