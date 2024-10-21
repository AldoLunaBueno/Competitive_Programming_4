from typing import List

def calories(one_food: List):
    """
    Parameters:
    one_food: fat a b c alchohol (list of 5 components)
        - each component consists of an integer and a certain unit
        - units: g C %
        - conversion from g to C depends of the component:
            - fat: 1g -> 9C
            - a, b, c: 1g -> 4C
            - alcohol: 1g -> 7C
        - the % unit indicates the percentage of food total calories
    Returns fat calories and total calories of the food
    """
    calories = [0]*5
    percentages = [0]*5
    for i, component in enumerate(one_food):
        if component[-1] == "%":
            percentages[i] = int(component[:-1])
        elif component[-1] == "g":
            c = int(component[:-1])
            if i == 0:
                c = 9*c
            elif i <= 3:
                c = 4*c
            elif i == 4:
                c = 7*c
            calories[i] = c
        elif component[-1] == "C":
            calories[i] = int(component[:-1])
    
    explicit_calories = sum(calories)
    calories_percentage = sum(percentages) # always < 100
    total_cal = 100 * explicit_calories / (100 - calories_percentage)
    if calories[0] == 0:
        calories[0] = total_cal * percentages[0] / 100
    fat_cal = calories[0]
    return fat_cal, total_cal

while True:
    one_food = input()
    if one_food == "-":
        break
    acc_fat, acc_total = calories(one_food.split())
    while True:
        one_food = input()
        if one_food == "-":
            fat_percent = round(acc_fat * 100 / acc_total)
            print(f"{fat_percent}%")
            break
        fat, total = calories(one_food.split())
        acc_fat += fat
        acc_total += total
        
