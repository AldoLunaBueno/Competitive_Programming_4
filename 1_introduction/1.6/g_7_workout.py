from typing import Tuple

NUM_MACHINES = 10
NUM_SETS = 3

# get data

jim_times = [int(x) for x in input().strip().split()]
jim_use_times = jim_times[::2]
jim_recov_times = jim_times[1::2]

time_matrix = [[int(x) for x in input().strip().split()] for _ in range(NUM_MACHINES)]
use_times, recov_times, start_times = [*zip(*time_matrix)] # transpose
start_times = list(start_times)

# algorithm

def state_n_time_left(curr_t: int, use_t: int, recov_t: int, start_t: int) -> Tuple[bool, int]:
    is_using = False

    # be careful when curr_time < start_time
    if curr_t < start_t:
        return is_using, -1

    time_left = 0
    cycle = use_t + recov_t
    remaining = (curr_t - start_t) % (cycle)
    if remaining < use_t:
        is_using = True
        time_left = use_t - remaining
    else:
        time_left = cycle - remaining
    return is_using, time_left

curr_time = 0
for _ in range(NUM_SETS):
    for i in range(NUM_MACHINES):
        is_using, time_left = state_n_time_left(curr_time, use_times[i], recov_times[i], start_times[i])
        if is_using:
            curr_time += time_left + jim_use_times[i]
            start_times[i] = curr_time # gym bro j begins
            curr_time += jim_recov_times[i]
        else:
            if time_left == -1: # curr_time < start_time
                if curr_time + jim_use_times[i] > start_times[i]:
                    start_times[i] = curr_time + jim_use_times[i]
                curr_time += jim_use_times[i] + jim_recov_times[i]
            elif jim_use_times[i] > time_left:
                curr_time +=  jim_use_times[i] + jim_recov_times[i]
                offset = jim_use_times[i] - time_left
                start_times[i] += offset
            else:
                curr_time += jim_use_times[i] + jim_recov_times[i]

curr_time -= jim_recov_times[-1]
print(curr_time)