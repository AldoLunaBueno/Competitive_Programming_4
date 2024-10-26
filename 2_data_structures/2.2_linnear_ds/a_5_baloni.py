# Balloni - Kattis

n = int(input())
heights = [*map(int, input().split())]

# Here we iterate over the list of balloon heights. 
# The clever idea is to mantain all the time a number of balloons 
# equal to the number of arrows that we need to throw to pop 
# all the balloons visited up to that point.
# These balloons are the last to be popped by an arrow.
# We do it by dicounting a baloon previously counted if its height 
# is one unit more than the current balloon's height
# (because the discounted balloon and the current balloon
# are popped by the same arrow).

count_balloons = {heights[0]: 1}
for i in range(1, n):
    regresion_height = heights[i]+1 # height of the arrow if it had poped a balloon previously
    if regresion_height in count_balloons: # a ballon actually was poped at the regresion height
        count_balloons[regresion_height] -= 1
        if count_balloons[regresion_height] == 0:
            count_balloons.pop(regresion_height) # we discount any poped balloon, except for the last ones
    if heights[i] not in count_balloons:
        count_balloons[heights[i]] = 0
    count_balloons[heights[i]] += 1 # we have a new balloon to count until were poped
    
print(sum(count_balloons.values()))