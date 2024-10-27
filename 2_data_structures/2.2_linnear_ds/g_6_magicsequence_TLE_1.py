# Magic Sequence

# Time Limit Exceeded
# Runtime: > 2.00 s
# Test cases: 7/13

num_cases = int(input())
for _ in range(num_cases):
    n = int(input())
    a, b, c = map(int, input().split())
    x, y = map(int, input().split())

    s = [a]
    for i in range(1, n):
        s_i = (s[i-1] * b + a) % c
        s.append(s_i)
    r = sorted(s)
    
    # hash process
    v = 0
    for i in range(n):
        v = (v * x + r[i]) % y
    
    print(v)