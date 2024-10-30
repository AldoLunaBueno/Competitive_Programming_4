# Rock Band

# Reasoning:
#
# Group the songs of all the members up to the k preference.
# Is guranteed that there are at least k unique songs in this group.
# If there are exactly k unique songs, the answer is this set.
# Otherswise, we keep moving to the next column of preferences k+1.


def solve():
    num_members, num_songs = map(int, input().split())
    songs = [[*map(int, input().split())] for _ in range(num_members)]
    unique = set()

    for k in range(num_songs):
        col = [row[k] for row in songs]
        unique.update(col)
        if k+1 == len(unique):
            break
    print(k+1)
    print(*sorted(list(unique)))

solve()