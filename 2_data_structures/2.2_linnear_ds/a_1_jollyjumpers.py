# Jolly Jumpers

# Instead of using a boolean array to keep track of the differences
# from 1 to n-1 just for ask if it is there, 
# I used a set to store these differences.

while True:
    try:
        n, *arr = [*map(int, input().split())]
    except EOFError:
        break
    jolly_values = set()
    not_jolly = False
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        if (diff in jolly_values) or not (0 < diff < len(arr)):
            not_jolly = True
            break
        jolly_values.add(diff)
        
    if not_jolly:
        print("Not jolly")
    else:
        print("Jolly")
