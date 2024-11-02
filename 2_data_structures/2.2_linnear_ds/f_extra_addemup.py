# Add 'Em Up!

# Reasoning
#
# For each number in its string form, calculate its upside down version
# and store both the number and the turned number (converted to int),
# each one attached with the same index,
# except for these 2 cases:
# (1) the number has digits that can't be turned
# (2) the turned number is equal to the number
# In these 2 cases store only the number attached with a unique index.
#
# Sort the list of tuples by first element for binary search.
# Then make a copy for calculate the complement of the list
# for the given sum.
# This is the "Two Sum" problem now, pairing equal numbers of both lists,
# except for this case:
# Say we found a list number equal to a complement number.
# If its indexes are also equal, then this pair can't be used
# because it comes from the same card, and we need to look
# for some immediate adyacent number (because it's sorted!)
#
# Time complexity: O(n*log(n))


from sys import stdin


turn = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": None,
    "4": None,
    "5": "5",
    "6": "9",
    "7": None,
    "8": "8",
    "9": "6"
}

def turn_card(card: str):
    turned = []
    for d in card[::-1]:
        td = turn[d]
        if td is None:
            return None
        turned.append(td)
    if turned == list(card):
        return None
    return "".join(turned)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2
        if arr[mid][0] < x:
            low = mid + 1
        elif arr[mid][0] > x:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    # data preparation
    n, desired_sum = map(int, input().split())
    arr = stdin.readline().split()
    indexed_arr = []
    for id, card in enumerate(arr):
        number = int(card)
        indexed_arr.append((number, id))
        turned = turn_card(card)
        if turned is not None:
            indexed_arr.append((int(turned), id))
    
    # complement and sorting
    complement = [(desired_sum - x[0], x[1]) for x in indexed_arr]
    complement.sort(key = lambda a: a[0])

    # binary search and finding a valid pair
    for number, id in indexed_arr:
        i_compl = binary_search(complement, number)
        if i_compl == -1:
            continue
        id_compl = complement[i_compl][1]
        if id == id_compl:
            if 0 < i_compl < n-1:
                if (number == complement[i_compl+1][0] 
                    or number == complement[i_compl-1][0]): # adyacents
                    return "YES"
        else:
            return "YES"
    
    return "NO"
    
print(main())