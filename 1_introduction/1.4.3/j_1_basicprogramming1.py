n, t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()] # len(a) >= 3

match t:
    case 1:
        print(7)
    case 2:
        if a[0] > a[1]:
            print("Bigger")
        elif a[0] == a[1]:
            print("Equal")
        else:
            print("Smaller")
    case 3:
        sub_a = sorted(a[0:3])
        print(sub_a[1])
    case 4:
        print(sum(a))
    case 5:
        a = [i for i in a if i % 2 == 0]
        print(sum(a))
    case 6:
        a = [i % 26 for i in a]
        ord_a = ord("a")
        a = [chr(i + ord_a) for i in a]
        print("".join(a))
    case 7:
        i = a[0]
        visited_indexes = set([0])
        while True:
            if i >= n:
                print("out")
                break
            elif i < n-1:
                i = a[i]
                if i in visited_indexes:
                    print("Cyclic")
                    break
                else:
                    visited_indexes.add(i)
            elif i == n-1:
                print("Done")
                break
            
            