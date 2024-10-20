m, l = [int(x) for x in input().split()]
M, L =  [int(x) for x in input().split()]
tm, tl =  [int(x) for x in input().split()]

# two options
def solve():
    if first_m():
        print("possible")
    elif first_l():
        print("possible")
    else:
        print("impossible")

def first_m():
    time = 0
    pos = 0
    is_timeout = False
    time += abs(m-pos)
    pos = m
    is_timeout = time > tm or time > tl
    time += abs(M-pos)
    pos = M
    is_timeout = time > tm or time > tl
    # second l
    time += abs(l-pos)
    pos = l
    is_timeout = time > tl
    time += abs(L-pos)
    pos = L
    is_timeout = time > tl
    return not is_timeout

def first_l():
    time = 0
    pos = 0
    is_timeout = False
    time += abs(l-pos)
    pos = l
    is_timeout = time > tm or time > tl
    time += abs(L-pos)
    pos = L
    is_timeout = time > tm or time > tl

    # second m
    time += abs(m-pos)
    pos = m
    is_timeout = time > tm
    time += abs(M-pos)
    pos = M
    is_timeout = time > tm
    return not is_timeout

solve()