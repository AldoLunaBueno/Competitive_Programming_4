# Credit Card Payment - Kattis

def solve(r: float, b: float, m: float):
    """
    Parameters:
    r: monthly interest rate
    b: outstanding balance (debt)
    m: monthly payment
    """
    r /= 100
    if b == 0:
        print(0)
        return
    for count in range(1200):
        interest = b * r
        interest = round(interest*100) / 100 # tricky round: integer / 100
        b += interest
        b = round(b * 100) / 100 # tricky round
        b -= m
        if b <= 0.0001:
            print(count+1)
            return
    print("impossible")
    
n = int(input())
for _ in range(n):
    r, b, m = [float(x) for x in input().split()]
    solve(r, b, m)