from sys import stdin

a_won = "Player 1 wins."
b_won = "Player 2 wins."
tie = "Tie."

def solve(a1, a2, b1, b2):
    max_a = a1 == 1 and a2 == 2 or a1 == 2 and a2 == 1
    max_b = b1 == 1 and b2 == 2 or b1 == 2 and b2 == 1
    if max_a and max_b:
        return tie
    elif max_a:
        return a_won
    elif max_b:
        return b_won
    elif a1 == a2 or b1 == b2:
        if a1 != a2:
            return b_won
        elif b1 != b2:
            return a_won
        # a1 == a2 and b1 == b2
        if a1 > b1:
            return a_won
        elif a1 < b1:
            return b_won
        elif a1 == b2:
            return tie

    # a1 != a2 and b1 != b2
    if a1 < a2:
        a1, a2 = a2, a1
    if b1 < b2:
        b1, b2 = b2, b1

    aa = a1 * 10 + a2
    bb = b1 * 10 + b2

    if aa > bb:
        return a_won
    elif aa < bb:
        return b_won
    elif aa == bb:
        return tie

while True:
    a1, a2, b1, b2 = [int(x) for x in stdin.readline().strip().split(" ")]
    if a1 == 0:
        break
    result = solve(a1, a2, b1, b2)
    print(result)