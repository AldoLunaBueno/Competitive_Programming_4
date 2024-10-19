# Hanging Out on the Terrace - Kattis

limit, num_events = [int(x) for x in input().split()]
total_people = 0
count_not_allowed = 0
for _ in range(num_events):
    event, num_group = input().split()
    num_group = int(num_group)

    if event == "leave":
        total_people -= num_group
        continue

    if total_people + num_group > limit:
        count_not_allowed += 1
    else:
        total_people += num_group

print(count_not_allowed)
