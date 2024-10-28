# Astro

# Interesting problem solved by modular math

# Reasoning:
# star 1 flash times: a, a+c, a + c(2), ..., a + c(k)
# star 2 flash times: b, b+d, b + d(2), ..., b + d(h)
# Is there k,h for a+ck=b+dh?
# ¿a+ck = b (mod d)?
# Find k (old solution: test for every k in {0, 1, ..., d-1})
# If there is a k, calculate the date and time based on m = a+ck (minutes)

from math import gcd

WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
TODAY = 6 # Saturday
M = 24*60 # minutes in a day

def main():
    times = [[int(x) for x in input().split(":")] for _ in range(4)]
    a, b, c, d = [t[0]*60 + t[1] for t in times]
    if a < b:
        a, b = b, a
        c, d = d, c
    
    m = same_minute(a, b, c, d)
    if m == -1:
        print("Never")
        return
    d = (TODAY + (m // M)) % 7
    m = m % M
    h = m // 60
    m = m % 60
    print(WEEKDAYS[d])
    print(f"{h:02d}:{m:02d}")

# previous functional solution
#
# def same_minute(a, b, c, d):
#     m = -1
#     for k in range(d):
#         if (a+c*k - b) % d == 0:
#             m = a + c*k
#             break
#     return m

# this solution has no advantage over the previous one
def same_minute(a, b, c, d):
    k = solve_linear_congruence(c, b-a, d) # c  k  = b-a (d)
    if k == -1:
        return -1
    return a + c*k

def solve_linear_congruence(a, b, m):
    """
    Returns the first solution of the linear congruence a x ≡ b (mod m)
    If there is no solution, returns -1
    """
    g = gcd(a, m)
    if b % g != 0:
        return -1
    else:
        a, b, m = a//g, b//g, m//g
        a_inv = pow(a, -1, m)
        return b * a_inv % m

main()
