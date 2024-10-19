# Batter Up - Kattis

_ = input()
battings = [int(x) for x in input().strip().split() if x != "-1"]

mean = sum(battings) / len(battings)
print(mean)
