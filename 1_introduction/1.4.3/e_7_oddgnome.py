n = int(input())

for _ in range(n):
    gnomes = [int(x) for x in input().split(" ")]
    for i in range(2, len(gnomes)-1):
        if gnomes[i] != gnomes[i-1] + 1:
            print(i)
            break