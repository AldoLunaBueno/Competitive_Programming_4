# Ferry Loading III

# 3 hours bug due to not reading properly this:
# "in the same order as the input"

num_cases = int(input())

for i_case in range(num_cases):
    n, time_to_cross, m = map(int, input().split())
    left, right = [], []
    for i in range(m):
        t, pos = input().split()
        t = int(t)
        if pos[0] == "l":
            left.append((t, i))
        else:
            right.append((t, i))
    left = left[::-1]
    right = right[::-1]
    curr_time = 0
    unload_times = [0]*m
    while left or right:
        if not left:
            curr_time = max(curr_time, right[-1][0])
        elif curr_time < left[-1][0]: # cars have not arrived yet
            if right and right[-1][0] < left[-1][0]: # go to the right?
                    curr_time = max(curr_time, right[-1][0])
            else:
                curr_time = left[-1][0]
                continue
        else:
            count = 0
            unload_time = curr_time + time_to_cross
            while left and curr_time >= left[-1][0] and count < n:
                t, i = left.pop()
                unload_times[i] = unload_time
                count += 1
        left, right = right, left
        curr_time += time_to_cross
    print(*unload_times, sep="\n")
    if i_case == num_cases-1:
        continue
    print()
