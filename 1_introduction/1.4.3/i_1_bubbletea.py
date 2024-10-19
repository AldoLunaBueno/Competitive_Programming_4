# Delicious Bubble Tea - Kattis

def split_input():
    return input().strip().split()

n = int(input())
tea_prices = [int(x) for x in split_input()]
m = int(input())
topping_prices = [None] + [int(x) for x in split_input()]
allowed_toppings = [[int(x) for x in split_input()][1:] for _ in range(n)]
x_total_money = int(input())

min_cup_price = float("Inf")

for i in range(n):
    tea = tea_prices[i]
    topping = min(topping_prices[j] for j in allowed_toppings[i]) # not so easy to figure out
    cup = tea + topping
    min_cup_price = cup if cup < min_cup_price else min_cup_price

max_people = x_total_money // min_cup_price
if max_people == 0:
    print(0) # This was the tricky part
else:
    print(max_people - 1)

