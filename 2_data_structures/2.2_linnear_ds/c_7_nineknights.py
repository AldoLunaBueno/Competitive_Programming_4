# Nine Knights

# For each knight, record the positions under its attack.
# If the position of some knight is in the record
# or the knights are less than nine, then the solution is invalid.
# Otherwise, the solution is valid.

BOARD_SIZE = 5
NUM_KNIGHTS = 9

def get_under_attack(x, y):
    """
    Return all the positions under the attack of a knight at (x,y), 
    included invalid positions outside the board
    """
    return [(x+2,y+1), (x+2,y-1), (x-2, y+1), (x-2, y-1),
            (x+1,y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]

def solve():
    count = 0
    under_attack = set()
    for y in range(BOARD_SIZE):
        x_values = [i for i, c, in enumerate(input()) if c == "k"]
        for x in x_values:
            if (x, y) in under_attack:
                return "invalid"
            under_attack.update(get_under_attack(x, y))
            count += 1

    return "valid" if count == NUM_KNIGHTS else "invalid"

print(solve())
