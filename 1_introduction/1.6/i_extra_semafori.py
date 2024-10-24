def get_time_left(curr_time, red_time, green_time):
    time_left = 0
    cycle = red_time + green_time
    mod_time = curr_time % cycle
    if mod_time < red_time:
        time_left = red_time - mod_time
    return time_left


num_lights, road_length = map(int, input().split())

# get data and calculate answer in one go!
curr_time = 0
last_dist = 0
for _ in range(num_lights):
    distance, red_time, green_time = map(int, input().split())
    curr_time += distance - last_dist # velocity = 1 distance unit per time unit
    curr_time += get_time_left(curr_time, red_time, green_time) # if green, zero
    last_dist = distance
curr_time += road_length - last_dist
print(curr_time)
