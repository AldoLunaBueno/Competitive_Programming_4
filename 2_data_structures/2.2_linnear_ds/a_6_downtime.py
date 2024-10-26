# Disastrous Downtime

# An interesting problem about string manipulation.
# The key is to operate the numbers in a human way
# by dealing with the numbers in its string representation,
# because these are monumentally large numbers! (10**10**6 order)
# There are 4 cases:
# ....****0000 = n
# m =
#            1 <- case 1
#          100 <- case 2
#       100000 <- case 3
#   1000000000 <- case 4

n = input()
m = input()

k = len(m)-1 # number of zeros in m

# case 1:
if k == 0:
    print(n)
else:
    num_trailing_zeros = None
    for i in range(1, len(n)+1):
        if n[len(n)-i] != "0":
            num_trailing_zeros = i-1
            break
    d = len(n) - k # number of whole part digits of quotient
    z0 = len(n) - num_trailing_zeros # index of first trailing zero in number n
    if k <= num_trailing_zeros: # case 2
        quotient = n[:d]
    elif k < len(n): # case 3
        w = n[:d] # whole part
        d = n[d:z0] # decimal part
        quotient = w + "." + d
    else:
        quotient = "0." + "0"*(-d) + n[:z0]
    print(quotient)