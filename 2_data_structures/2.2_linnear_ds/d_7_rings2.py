# Rings - Kattis

# Reasoning
#
# First fill a matrix transforming empty squares into 0's 
# and tree squares into 1's.
# Rings are record one by one in iterations.
# At the k-th iteration (being the first k=2)
# do one of two things for each cell (except margin squares)
# If the square is k-1, replace with k if all neighbours (up, down, left, right) are k-1
# Otherwise, pass.
# The iteration ends when there are no more squares to replace.

TREE = "T"
EMPTY = "."

# get data
num_rows, num_cols = map(int, input().split())
matrix = [[0] * num_cols for _ in range(num_rows)]
for i in range(num_rows):
    for j, c in enumerate(input()):
        if c == EMPTY:
            continue
        matrix[i][j] = 1

# iterate search of rings
max_iterations = min(num_rows, num_cols)
for k in range(2, max_iterations):
    is_finish = True
    for i in range(1, num_rows-1):
        for j in range(1, num_cols-1):
            if matrix[i][j] < k-1:
                continue
            value = min(matrix[i-1][j], matrix[i+1][j], matrix[i][j-1], matrix[i][j+1])
            if value == k-1:
                matrix[i][j] = k
            is_finish = False
    if is_finish:
        break

# right justify
num_dots = 2 if k<10 else 3
for i in range(num_rows):
    for j in range(num_cols):
        square = str(matrix[i][j]) if matrix[i][j] > 0 else ""
        print(square.rjust(num_dots, EMPTY), end="")
    print()

# The code golfing way:
# T="T";E=".";g,p=range,print;rs,cs=map(int,input().split());m=[[0]*cs for _ in g(rs)]
# for i in g(rs):
#  for j,c in enumerate(input()):
#   if not c==E:m[i][j]=1
# mi=min(rs,cs)
# for k in g(2,mi):
#  fi=True
#  for i in g(1,rs-1):
#   for j in g(1,cs-1):
#    if m[i][j]<k-1:continue
#    v=min(m[i-1][j],m[i+1][j],m[i][j-1],m[i][j+1])
#    if v==k-1:m[i][j]=k
#    fi=False
#  if fi:break
# d=2 if k<10 else 3
# for i in g(rs):
#  for j in g(cs):
#   s=str(m[i][j])if m[i][j]>0 else"";p(s.rjust(d,"."),end="")
#  p()