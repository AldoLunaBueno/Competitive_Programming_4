# Juggling Patterns - Kattis

# Reasoning
# Priority queue is not needed.

from sys import stdin

def solve(pattern_str):
    pattern = [*map(int, pattern_str)]
    num_balls = sum(pattern) / len(pattern)
    if num_balls % 1 != 0: # not an integer!
        return f"{pattern_str}: invalid # of balls"
    
    simul = set()
    simul_size = 2 * len(pattern) + 1
    for i in range(simul_size):
        d = pattern[i % len(pattern)]
        if i+d in simul:
            return f"{pattern_str}: invalid pattern"
        else:
            simul.add(i+d)
    return f"{pattern_str}: valid with {int(num_balls)} balls"

for pattern in stdin:
    print(solve(pattern.strip()))

#The golfing way (3th place!)
# import sys;v,b="valid","balls"
# def s(y):
#  p=[*map(int,y)];l=len(p);n=sum(p)/l
#  if n%1!=0:return f"{y}: in{v} # of {b}"
#  s=set();ss=l*2+1
#  for i in range(ss):
#   d=p[i%l]
#   if i+d in s:return f"{y}: in{v} pattern"
#   else:s.add(i+d)
#  return f"{y}: {v} with {int(n)} {b}"
# for p in sys.stdin:print(s(p.strip()))