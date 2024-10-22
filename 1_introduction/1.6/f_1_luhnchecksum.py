num_cases = int(input())
for _ in range(num_cases):
    n = input()
    acc = 0
    for i in range(len(n)):
        d = int(n[i])
        if (len(n)-i-1) % 2 == 1:
            d = 2 * d
            if d >= 10:
                u = d % 10
                d = 1 + u
        acc += d
        
    if acc % 10 == 0:
        print("PASS")
    else:
        print("FAIL")