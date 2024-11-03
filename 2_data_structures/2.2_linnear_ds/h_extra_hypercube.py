# Hamiltonian Hypercube - Kattis

# Reasoning
#
# Calculate the position of a and b in the n-bit Grey Code
# by iteration bit by bit from left to right (1 to n)
# Note that in n-bit Grey Code the first half begins with zeros,
# and the second half begins with ones, but in reversed version
# the opposite happens.
# Iteratively, 
# at the bit k we accumulate in the position half of the way 
# of the subsequence (n-k)-bit Grey Code (length of 2**(n-k))
# only on these scenarios:
# (1) If we count an even number of ones and then we find a one, 
# because it means that the subsequence is ordered and
# position advance to the second half.
# (2) If we count an odd number of ones and then we find a zero,
# because it means that the subsequence is reversed and
# position advance to the second half.
# The position can be easily use to calculate 
# the number of vertices between any two.

ZERO = "0"
ONE = "1"
n, a, b = input().split()
n = int(n)

def position(n: int, bit_str: str):
    even_ones = True # previous bit
    position = 0
    for i, b in enumerate(bit_str, 1):
        if b == ONE:
            if even_ones:
                position += 2**(n-i)
            even_ones = not even_ones
        elif not even_ones and b == ZERO:
            position += 2**(n-i)

    return position

print(position(n, b) - position(n, a) -1)