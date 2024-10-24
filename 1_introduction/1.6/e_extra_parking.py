# Parking

# this is an intersting problem about counting 
# the number of overlaping intervals for each point

# the code golfing way
# p=[0]+[*map(int,input().split())];i=sorted([e for(a,d)in[[*map(int,input().split())]for _ in"1"*3]for e in[(1,a),(-1,d)]],key=lambda a:a[1]);a,c,l=0,0,0
# for s,t in i:
#  a+=c*(t-l)*p[c];l=t;c+=s
# print(a)

NUM_TRUCKS = 3 # this can be generalized to n trucks!
price_per_min = [0] + [*map(int, input().split())] # descending with number of trucks
intervals_2d = [[*map(int, input().split())] for _ in range(NUM_TRUCKS)]
intervals_1d = [] # flatten version of intervals_2d
for (a,d) in intervals_2d:
    intervals_1d.extend([(1,a),(-1,d)]) # I don't need to distinguish between trucks
intervals_1d.sort(key = lambda a: a[1])

acc_price, last_time = 0, 0
count = 0 # number of trucks at each time
for in_out, time in intervals_1d:
    acc_price += count * (time - last_time) * price_per_min[count]
    last_time = time
    count += in_out

print(acc_price)
