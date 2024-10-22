# Bungee Jumping
from math import sqrt
DIE = "Killed by the impact."
HANGING = "Stuck in the air."
SURVIVES = "James Bond survives."
g = 9.81
while True:
    k, l, s, m = [float(x) for x in input().strip().split()]
    if k == l == s == m == 0:
        break
    if s < l:
        v = sqrt(2*g*s)
        print(DIE) if v > 10 else print(SURVIVES)            
    else:
        v_square = 2*g*s - k * (s-l)**2 / m
        if v_square < 0:
            print(HANGING)
        else:
            print(DIE) if sqrt(v_square) > 10 else print(SURVIVES)