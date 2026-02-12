matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            one_row, one_col = i, j

moves = abs(one_row - 2) + abs(one_col - 2)

print(moves)
