# Amalgamated Artichokes - Kattis

from math import sin, cos

p, a, b, c, d, n = [int(x) for x in input().split(" ")]

price = lambda k: p * (sin(a*k+b) + cos(c*k+d) + 2)

max_decline = 0
price_decline = 0
i = 1
price_i = price(i)
while i < n:    
    j = i + 1
    while j <= n:
        price_j = price(j)
        if price_i < price_j:
            i = j
            price_i = price_j
            break
        price_decline = price_i - price_j
        max_decline = price_decline if price_decline > max_decline else max_decline
        j += 1
    if j == n+1:
        break

print(max_decline)


