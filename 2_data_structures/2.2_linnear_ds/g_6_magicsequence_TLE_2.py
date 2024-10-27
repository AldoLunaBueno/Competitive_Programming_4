# Magic Sequence

# radix solution

from typing import List

import itertools

def radix_sort(unsorted):
    "Fast implementation of radix sort for any size num."
    maximum, minimum = max(unsorted), min(unsorted)

    max_bits = maximum.bit_length()
    highest_byte = max_bits // 8 if max_bits % 8 == 0 else (max_bits // 8) + 1

#    min_bits = minimum.bit_length()
#    lowest_byte = min_bits // 8 if min_bits % 8 == 0 else (min_bits // 8) + 1

    sorted_list = unsorted
#    xrange changed to range, lowest_byte deleted from the arguments
    for offset in range(highest_byte):
        sorted_list = radix_sort_offset(sorted_list, offset)

    return sorted_list

def radix_sort_offset(unsorted, offset):
    "Helper function for radix sort, sorts each offset."
    byte_check = (0xFF << offset*8)

#    xrange changed to range
    buckets = [[] for _ in range(256)]

    for num in unsorted:
        byte_at_offset = (num & byte_check) >> offset*8
        buckets[byte_at_offset].append(num)

    return list(itertools.chain.from_iterable(buckets))

num_cases = int(input())
for _ in range(num_cases):
    n = int(input())
    a, b, c = map(int, input().split())
    x, y = map(int, input().split())

    s = [a]
    for i in range(1, n):
        s_i = (s[i-1] * b + a) % c
        s.append(s_i)
    r = radix_sort(s)
    
    # hash process
    v = 0
    for i in range(n):
        v = (v * x + r[i]) % y
    
    print(v)