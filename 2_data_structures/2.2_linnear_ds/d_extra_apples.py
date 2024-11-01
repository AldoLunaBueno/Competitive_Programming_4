# Falling Apples

# Reasoning
#
# Don't simulate.
# Use an auxiliary matrix to record at each position 
# the number of apples above if the current position
# is an obstacle or the ground.
# Then go backwards filling one by one the counted apples

APPLE = "a"
OBSTACLE = "#"
EMPTY = "."

num_rows, num_columns = map(int, input().split())

row_count = [0] * num_columns
global_count = [[0] * num_columns for _ in range(num_rows)]

for i in range(num_rows):
    for j, c in enumerate(input()):        
        if c == APPLE:
            row_count[j] += 1
        elif c == OBSTACLE:
            if row_count[j] > 0:
                global_count[i-1][j] = row_count[j] # record the count of apples above
            global_count[i][j] = -1 # record the position of a obstacle
            row_count[j] = 0 # reset the count
        
        if i == num_rows-1 and c != OBSTACLE:
            global_count[i][j] = row_count[j]

board = [[None] * num_columns for _ in range(num_rows)]

for i in range(num_rows-1, -1, -1):
    for j in range(num_columns):
        if global_count[i][j] == -1:
            board[i][j] = OBSTACLE
        elif global_count[i][j] == 0:
            board[i][j] = EMPTY
        elif global_count[i][j] == 1:
            board[i][j] = APPLE
        elif global_count[i][j] > 1:
            board[i][j] = APPLE
            global_count[i-1][j] = global_count[i][j]-1

for row in board:
    print("".join(row))
