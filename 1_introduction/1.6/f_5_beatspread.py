# Beat the Spread! - Kattis

num_cases = int(input())
for i in range(num_cases):
    s, d = map(int, input().split())
    if s < d:
        print("impossible")
    elif (s+d) % 2 == 1 or (s-d) % 2 == 1: # tricky part
         # (s+d)/2 = x needs to be an integer, so s+d needs to be even
         print("impossible")
    else:        
        x = (s+d)//2
        y = (s-d)//2
        print(x, y)