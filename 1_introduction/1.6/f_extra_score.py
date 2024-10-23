MIN_32 = 60*32

num_baskets = int(input())
leading_time = {"H": 0, "A": 0}
acc_points = {"H": 0, "A": 0}
curr_leading = None
last_leading_team = None
last_leading_time = 0
for i in range(num_baskets):
    team, points, time = input().split()
    m, s = map(int, time.split(":"))
    time = 60*m + s
    acc_points[team] += int(points)
    
    if acc_points["H"]==acc_points["A"]:
        curr_leading = None  
    else:
        curr_leading = "H" if acc_points["H"] > acc_points["A"] else "A"

    if last_leading_team == curr_leading:
        pass
    elif last_leading_team != None and curr_leading != None: # leading team switches
        leading_time[last_leading_team] += time - last_leading_time
        last_leading_time = time
    elif last_leading_team != None:
        leading_time[last_leading_team] += time - last_leading_time
    elif curr_leading != None:
        last_leading_time = time

    last_leading_team = curr_leading
    
    if i == num_baskets - 1 and time < MIN_32:
        if last_leading_team == None:
            pass
        else:
            leading_time[last_leading_team] += MIN_32 - last_leading_time

def time_formater(time: int):
    m = time // 60
    s = time % 60
    return f"{m}:{s:02d}"

winner_team = "H" if acc_points["H"] > acc_points["A"] else "A"
print(winner_team, end="")
for time in leading_time.values():
    print(f" {time_formater(time)}", end="")