# 2048 - Kattis

BOARD_SIZE = 4
SYMMETRY = 4
board = [[int(x) for x in input().split()] for i in range(BOARD_SIZE)]
move = int(input()) # 0, 1, 2, 3

def get_new_line(line):
    line = [cell for cell in line if cell != 0]
    new_line = line
    if len(line) == 2 and line[0] == line[1]:
        new_line = [2 * line[0]]
    elif len(line) == 3:
        a, b, c = line
        if a == b:
            new_line = [2*a, c]
        elif b == c:
            new_line = [a, 2*b]        
    elif len(line) == 4:
        a, b, c, d = line
        if a == b and c == d:
            new_line = [2*a, 2*c]
        elif a == b:
            new_line = [2*a, c, d] 
        elif b == c:
            new_line = [a, 2*b, d]
        elif c == d:
            new_line = [a, b, 2*c]
    new_line = new_line + [0 for _ in range(BOARD_SIZE - len(new_line))]
    return new_line
    
def rotate(matrix):
    new_matrix = [[None]*BOARD_SIZE for _ in range(BOARD_SIZE)]
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            new_matrix[i][j] = matrix[BOARD_SIZE-1-j][i]
    return new_matrix

for i in range(SYMMETRY - move):
    board = rotate(board)

for i in range(BOARD_SIZE):
    board[i] = get_new_line(board[i])

for i in range(move):
    board = rotate(board)

# print the board
for line in board:
    print(*line)