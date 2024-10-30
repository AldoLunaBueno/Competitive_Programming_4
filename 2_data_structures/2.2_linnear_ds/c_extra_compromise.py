# Best Compromise

# Reasoning:
#
# Suppose the belief in the i-th issue is "yes" for most people.
# Say the i-th agreed outcome by H function is "no" 
# (this is supposed to minimize the count of beliefs contrary to the outcome).
# Then for each person the i-th belief been "yes" counts for the H function.
# But if the i-th agreed outcome were "yes", the count were less than before (-> <-).
# So the i-th agreed outcome must be the most common i-th belief to minimize H.

num_cases = int(input())
for _ in range(num_cases):
    n, m = map(int, input().split())

    count_ones = [0]*m
    for _ in range(n):
        ones = [i for i, x in enumerate(input()) if int(x) == 1]
        for i in ones:
            count_ones[i] += 1
    half = n // 2
    agreed_list = [("1" if count > half else "0") for count in count_ones]
    outcome = "".join(agreed_list)
    print(outcome)
