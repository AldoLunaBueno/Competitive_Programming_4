# All Just A Dream - Kattis

# Reasoning
#
# Combo: Stack + Hash Table
# Three operations are needed to solve this problem:
# (1) Add events one by one into a collection
# (2) Lookup the event and its position (index by order of insertion in the collection)
# (3) Delete the last k events (LIFO)
# A stack of events can satisfy 1 and 3, but not 2 (it can, but it's too slow).
# A hash table of event-index pairs can satisfy 1 and 2, but not 3.
# So we use together these two data structures to satisfy all operations.

from sys import stdin
inputs = stdin.read().splitlines()
events = []
events_table = {}
for line in inputs[1:]:
    op, *args = line.split()
    if op == "E":
        events_table[args[0]] = len(events)
        events.append(args[0])
    elif op == "D":
        r = int(args[0])
        for _ in range(r):
            e = events.pop()
            del events_table[e]
    elif op == "S":
        _, *questions = args
        min_event = float("Inf")
        max_non_event = -1
        is_correct = True
        is_impossible = False
        n = len(events)
        for q in questions:
            if q[0] != "!":
                try:
                    i_non_event = n - events_table[q[1:]]
                    max_non_event = max(max_non_event, i_non_event)
                    is_correct = False
                except:
                    continue
            else:
                try:
                    i_event = n - events_table[q]
                    min_event = min(min_event, i_event)                    
                except:
                    is_impossible = True
                    break
        if is_impossible:
            print("Plot Error")
        elif is_correct:
            print("Yes")
        else:
            if min_event > max_non_event:
                print(f"{max_non_event} Just A Dream")
            else:
                print("Plot Error")

# Naive version: TLE
# from sys import stdin
# inputs = stdin.read().splitlines()
# events = []
# for line in inputs[1:]:
#     op, *args = line.split()
#     if op == "E":
#         events.append(args[0])
#     elif op == "D":
#         r = int(args[0])
#         del events[-r:]        
#     elif op == "S":
#         _, *questions = args
#         min_event = float("Inf")
#         max_non_event = -1
#         is_correct = True
#         is_impossible = False
#         n = len(events)
#         for q in questions:
#             if q[0] == "!":
#                 try:
#                     i_non_event = n - events.index(q[1:])
#                     max_non_event = max(max_non_event, i_non_event)
#                     is_correct = False
#                 except:
#                     continue
#             else:
#                 try:
#                     i_event = n - events.index(q)
#                     min_event = min(min_event, i_event)                    
#                 except:
#                     is_impossible = True
#                     break
#         if is_impossible:
#             print("Plot Error")
#         elif is_correct:
#             print("Yes")
#         else:
#             if min_event > max_non_event:
#                 print(f"{max_non_event} Just A Dream")
#             else:
#                 print("Plot Error")