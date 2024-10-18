# FizzBuzz - Kattis

def replacing(x: int, y: int, n: int):
    x_eval = n % x == 0
    y_eval = n % y == 0

    if not x_eval and not y_eval:
        return n
    
    if not x_eval:
        return "Buzz"
    elif not y_eval:
        return "Fizz"
    else:
        return "FizzBuzz"

x, y, n = [int(x) for x in input().split(" ")]

for i in range(1, n+1):
    print(replacing(x, y, i))