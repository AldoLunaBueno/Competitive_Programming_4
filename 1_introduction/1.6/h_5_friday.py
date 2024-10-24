# Friday the 13th

# modular arithmetic
# the key is start from the first day of each month
# then you need to find what day of the week is 
# after 12 days (13th day of the month)

num_cases = int(input())
FRIDAY = 5 # begining from sunday at 0
for _ in range(num_cases):
    year_days, num_month = map(int, input().split())
    days_of_months = map(int, input().split())
    month_first_day = 0
    count_friday_13th = 0
    for month_days in days_of_months:
        if month_days >= 13:            
            day_13 = month_first_day + 12
            day_13 %= 7
            if day_13 == FRIDAY:
                count_friday_13th += 1
        month_first_day += month_days
    print(count_friday_13th)