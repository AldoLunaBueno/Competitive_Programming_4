import sys
input = sys.stdin.readline

# Reasoning
#
# At the begining the head can start from all spots.
# Iteratively for each interval, mark the spots that can be reached 
# when traverse this interval from each reachable spot,
# and update the reachable spots.

num_freqs = int(input())
for _ in range(num_freqs):
    traversal_time, num_intervals = map(int, input().split())
    reachable_spots = [1]*(traversal_time+1) # spots from where step to the next interval
    for _ in range(num_intervals):
        to_spot = [0]*(traversal_time+1)
        t1, t2 = map(int, input().split())
        interval = t2-t1
        for i in range(traversal_time+1):
            if reachable_spots[i] == 0: # this spot could not be reached
                continue
            if i >= interval:
                to_spot[i-interval] = 1
            if i <= traversal_time - interval:
                to_spot[i+interval] = 1
        reachable_spots = to_spot
    if sum(to_spot) == 0:
        print('impossible')
        exit(0)
print('possible')