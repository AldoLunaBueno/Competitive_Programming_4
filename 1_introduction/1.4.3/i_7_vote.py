N = int(input())
for _ in range(N):
    n = int(input())
    total_votes = 0
    max_votes = -1
    no_winner = True
    for i in range(1, n+1):
        votes = int(input())
        total_votes += votes
        if max_votes < votes:
            max_index = i
            max_votes = votes
            no_winner = False
        elif max_votes == votes:
            no_winner = True
    if no_winner:
        print("no winner")
    else:
        if max_votes > total_votes / 2:
            print(f"majority winner {max_index}")
        else:
            print(f"minority winner {max_index}")