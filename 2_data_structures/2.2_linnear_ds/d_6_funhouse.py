# Fun House - Kattis

# Reasoning
#
# Each house is interpreted rotating the string representation 
# 90 degrees counterclockwise
# x and y defines position.
# axis and sign defines direction.
# - axis can be horizontal (True) of vertical (False)
# - sign can be positive (True) or negative (False)
# This definition of direction makes it 
# easy to change it when a mirror appears 
# by fliping the axis or the axis and the sign 
# depending on the mirror type and previous direction.

from typing import List, Tuple

WALL = "x"
ENTRANCE = "*"
EXIT = "&"
MIRROR_BCK = "\\"
MIRROR_DIV = "/"
SPACE = "."


def find_entrance(house: List[str]) -> Tuple[int]:
    for x, line in enumerate(house):
        y = line.find(ENTRANCE)
        if y != -1:
            return y, x

def initial_direction(x: int, y: int, width: int, length: int) -> Tuple[bool]:
    if x == 0:
        return True, True
    elif y == 0:
        return False, True
    elif x == width-1:
        return True, False
    elif y == length-1:
        return False, False

def move(x, y, axis, sign) -> List[int]:
    step = 1 if sign else -1
    if axis: # horizontal
        x += step
    else: # vertical
        y += step
    return x, y

house_i = 1
while True:
    w, l = map(int, input().split())
    if w == l == 0:
        break
    house: List[str] = []
    for _ in range(l):
        house.append(input())
    
    y, x = find_entrance(house)
    axis, sign = initial_direction(x, y, l, w) # rotate 90 ccw
    while house[x][y] != WALL:
        if house[x][y] == SPACE:
            pass
        elif house[x][y] == MIRROR_DIV:
            axis, sign = not axis, not sign
        elif house[x][y] == MIRROR_BCK:
            axis = not axis
        x, y = move(x, y, axis, sign)
    
    # Insert the exit
    house[x] = house[x][:y] + EXIT + house[x][y+1:]

    # Print the house with exit
    print(f"HOUSE {house_i}")
    for line in house:
        print(line)
    house_i += 1
    
    
        

