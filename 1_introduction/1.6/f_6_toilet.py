# Toilet Seat - Kattis

initial, *preferences = input()

# policy 1: leave the seat up

seat = initial
num_adjustments = 0
for p in preferences:
    if seat != p:
        seat = p
        num_adjustments += 1
    if seat != "U":
        seat = "U"
        num_adjustments += 1
print(num_adjustments)

# policy 2: leave the seat down

seat = initial
num_adjustments = 0
for p in preferences:
    if seat != p:
        seat = p
        num_adjustments += 1
    if seat != "D":
        seat = "D"
        num_adjustments += 1
print(num_adjustments)

# policy 3: leave the seat up as you like to find it
seat = initial
num_adjustments = 0
for p in preferences:
    if seat != p:
        seat = p
        num_adjustments += 1
print(num_adjustments) 
