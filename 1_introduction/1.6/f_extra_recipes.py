# the code golfing insane way (226 characters)
# https://open.kattis.com/problems/recipes/statistics (top 2 :D)
i,f,p,g=input,float,print,range
for j in g(int(i())):r,y,d=map(int,i().split());p(f"Recipe # {j+1}");t,w,e=zip(*[i().split()for _ in"1"*r]);e=[*map(f,e)];[p(f"{t[k]} {f(w[e.index(100)])*e[k]*d/y/100}")for k in g(r)];p("-"*40)

# 570 characters, but readable
# num_cases = int(input())
# for j in range(1, num_cases+1):
#     r, p, d = [int(x) for x in input().split()]
#     print(f"Recipe # {j}")
#     factor = d / p
#     data = [input().split() for _ in range(r)]
#     names, weights, percentages = [*zip(*data)]
#     percentages = [float(x) for x in percentages]
#     main_i = percentages.index(100.0)
#     main_weight = float(weights[main_i])
#     for j in range(r):
#         desired_weight = main_weight * percentages[j] * factor / 100
#         print(f"{names[j]} {desired_weight:.1f}")
#     print("----------------------------------------")