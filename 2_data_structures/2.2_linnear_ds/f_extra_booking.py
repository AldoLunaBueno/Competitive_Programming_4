# Booking

# Reasoning
#
# The rooms required are the maximum count of overlapping time intervals
# of booking plus cleaning.
# The overlapping interval counting problem (time, distance or anything)
# can be solved by flatten the intervals to its start and end points.
# Just attach an in/out flag: 1 for a start point and -1 for an end point, 
# and sort by the point measure.
# Additionaly, stably sort previously by this in/out flag if the intervals
# aren't given sorted by the start point to avoid overcounting.
# Finally, iterate over the flatten list accumulating the in/out values.
# This accumulated value is exactly the number of overlapping intervals
# at each moment, until the next point.
#
# Related problem: Parking

from datetime import datetime, timedelta

num_cases = int(input())
date_format = "%Y-%m-%d %H:%M"

for _ in range(num_cases):
    # data preparation
    num_bookings, cleaning = map(int, input().split())
    cleaning = timedelta(minutes=cleaning)
    bookings = []
    for _ in range(num_bookings):
        _, date_1, time_1, date_2, time_2 = input().split()
        arrival = datetime.strptime(date_1 + " " + time_1, date_format)
        departure = datetime.strptime(date_2 + " " + time_2, date_format)
        ready = departure + cleaning
        bookings.extend([(arrival, 1), (ready, -1)])
    bookings.sort(key = lambda arr: arr[1])
    bookings.sort(key = lambda arr: arr[0])
    
    # counting rooms
    count = 0
    rooms_required = 0
    for _, in_out in bookings:
        count += in_out
        if count > rooms_required:
            rooms_required = count
    print(rooms_required)