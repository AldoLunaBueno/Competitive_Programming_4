# Bits Equalizer - Kattis

from typing import List

def equalize(seq: List, res: List):
    size = len(seq)
    seq_1, res_1 = 0, 0
    s0r1, s1r0 = 0, 0
    questions = 0
    for i in range(size):
        # is solvable?
        if seq[i] == "1":
            seq_1 += 1
        if res[i] == "1":
            res_1 += 1

        # necessary moves
        if seq[i] == "?": # question
            questions += 1
        # heavy strategy
        elif seq[i] == "0" and res[i] == "1":
            s0r1 += 1
        elif seq[i] == "1" and res[i] == "0":
            s1r0 += 1

    if res_1 < seq_1:
        # impossible
        return -1
    
    ans = questions # necessary moves
    # add max(s1r0, s0r1) to ans
    # Why? Follow the strategy:
    if s1r0 >= s0r1:
        # compensate the excess of ones (s1r0 - s0r1) 
        # changing some questions to zeros 
        # (this was already counted, so adds 0), 
        # and then swap all the ones counted by s1r0
        # (so adds s1r0)
        ans += s1r0
    elif s1r0 < s0r1:
        # compensate the excess of zeros (s0r1 - s1r0) 
        # changing "s0r1 - s1r0" zeros (counted by s0r1) to ones, 
        # and then swap the remaining zeros
        # (so adds s0r1 - s1r0 + s1r0 = s0r1)
        ans += s0r1
    return ans

n = int(input())
for i in range(1, n+1):
    line_1 = list(input().strip())
    line_2 = list(input().strip())
    result = equalize(line_1, line_2)
    print(f"Case {i}: {result}")
