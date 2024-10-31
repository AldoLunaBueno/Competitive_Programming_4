# Ups and Downs of Investing - Kattis

# Reasoning

# Just keep counting prices until its increasing or decreasing behavior 
# (according to the previous price) changes.
# Record always the current and previous count to verify peaks or valleys.
# This verification is done after each change in behavior and after the last price.

# A big bug comes from not reading carefully the input instructions:
# "Following this line will be one or MORE LINES containing a total of s stock prices."

def solve():
    num_prices, peak_len, valley_len = map(int, input().split())
    prices = []
    while True:
        try:
            prices.extend([*map(int, input().split())])
        except EOFError:
            break

    count = 0
    prev_count = 0
    peaks = 0
    valleys = 0

    if len(prices) == 1:
        print("0 0")
        return

    rising = prices[1] > prices[0]
    for i in range(1, num_prices):
        if (rising and prices[i] > prices[i-1]) or (not rising and prices[i] < prices[i-1]):
            count += 1
            continue
        # direction change detected
        if rising and (prev_count + 1 >= valley_len and count + 1 >= valley_len):
            valleys += 1
        elif not rising and (prev_count + 1 >= peak_len and count + 1 >= peak_len):
            peaks += 1

        prev_count = count
        count = 1
        rising = not rising

    if rising and (prev_count + 1 >= valley_len and count + 1 >= valley_len):
        valleys += 1
    elif not rising and (prev_count + 1 >= peak_len and count + 1 >= peak_len):
        peaks += 1

    print(peaks, valleys)

solve()