# ACM Contest Scoring - Kattis

from typing import List

ord_a = ord("A")
num_problems = ord("Z") - ord_a + 1
problems: List[List] = [None] * num_problems
log_entry = ""

while True:
    log_entry = input().strip()
    if log_entry == "-1":
        break
    time, letter, verdict = log_entry.strip().split()
    time = int(time)
    pos = ord(letter) - ord_a

    if problems[pos] == None:
        problems[pos] = [0, 0]
        
    if verdict == "wrong":
        problems[pos][1] += 1
    elif verdict == "right":
        problems[pos][0] = time

count_right = 0
acc_points = 0
penalty_points = 20
for prob in problems:
    if prob == None or prob[0] == 0:
        continue
    count_right += 1
    time = prob[0]
    penalty = prob[1] * penalty_points
    acc_points += time + penalty

print(count_right, acc_points)

