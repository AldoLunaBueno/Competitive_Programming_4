num_pokenoms, k = map(int, input().split())

stats = [(i, [*map(int, input().split())]) for i in range(num_pokenoms)]

selected = set()
max_attack = sorted(stats, key = lambda arr: arr[1][0], reverse=True)
max_attack = [i for i, stat in max_attack[:k]]
selected.update(max_attack)
max_defense = sorted(stats, key = lambda arr: arr[1][1], reverse=True)
max_defense = [i for i, stat in max_defense[:k]]
selected.update(max_defense)
max_health = sorted(stats, key = lambda arr: arr[1][2], reverse=True)
max_health = [i for i, stat in max_health[:k]]
selected.update(max_health)
print(len(selected))
    