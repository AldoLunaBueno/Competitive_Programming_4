# Basic Programming 2

from sys import stdin

n, t = map(int, stdin.readline().split())
arr = [*map(int, stdin.readline().split())]

def main():
    match t:
        case 1: # x + y = 7777 -> y = 7777 - x ("Two Sum" problem)
            complement = set([7777 - x for x in arr])
            for x in arr:
                if x in complement:
                    print("Yes")
                    return
            print("No")        
        case 2:
            ans = ("Unique" if len(arr) == len(set(arr)) 
                   else "Contains duplicate")
            print(ans)
        case 3:
            count_dict = {}
            for a in arr:
                if a in count_dict:
                    count_dict[a] += 1
                else:
                    count_dict[a] = 1
            a_max, count = max(count_dict.items(), key = lambda item: item[1])
            print(a_max if count > n//2 else -1)
        case 4: # median
            arr.sort()
            center = len(arr)//2
            if len(arr) % 2 == 1:
                print(arr[center])
            else:
                print(arr[center-1], arr[center])
        case 5:
            arr.sort()
            print(*[x for x in arr if 100 <= x < 1000])

main()