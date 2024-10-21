from_degree = int(input())
to_degree = int(input())
change = to_degree - from_degree
if -180 < change <= 180:
    print(change)
elif change <= -180:
    print(360 + change)
elif change > 180:
    print(change - 360)
