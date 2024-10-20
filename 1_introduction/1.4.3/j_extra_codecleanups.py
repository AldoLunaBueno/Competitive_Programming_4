n = int(input())
dirty_days = [int(x) for x in input().split()]

dirty_track = []
cleanup_phases = 0

for i in range(len(dirty_days)):
    curr_day = dirty_days[i]
    dirtiness = sum(curr_day - day for day in dirty_track)

    if dirtiness < 20:
        dirty_track.append(curr_day)
    else:
        dirty_track.clear() # cleanup phase happened in certain day, but it doesn't matter
        cleanup_phases += 1
        dirty_track.append(curr_day)
    
    if i == len(dirty_days) - 1:
        cleanup_phases += 1
        
print(cleanup_phases)



        

