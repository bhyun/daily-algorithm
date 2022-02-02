import sys
input = sys.stdin.readline

def dfs(x, y):
    result_row, result_col = 0, 0
    # 가로
    row = 1
    for i in range(1, n):
        if boards[x][i] != boards[x][i-1]:
            row = 1
        else:
            row += 1
        if row > result_row:
            result_row = row

    # 세로
    col = 1
    for i in range(1, n):
        if boards[i][y] != boards[i-1][y]:
            col = 1
        else:
            col += 1
        if col > result_col:
            result_col = col

    return max(result_col, result_row)


n = int(input())
boards = []
for _ in range(n):
    boards.append(list(input()))

answer = 0
# (i, j) & (i, j+1) swap
for i in range(n):
    for j in range(n-1):
        # swap
        boards[i][j], boards[i][j+1] = boards[i][j+1], boards[i][j]
        answer = max(answer, dfs(i, j), dfs(i, j+1))
        boards[i][j], boards[i][j + 1] = boards[i][j + 1], boards[i][j]

# (i, j) & (i+1, j) swap
for i in range(n-1):
    for j in range(n):
        # swap
        boards[i][j], boards[i+1][j] = boards[i+1][j], boards[i][j]
        answer = max(answer, dfs(i, j), dfs(i+1, j))
        boards[i][j], boards[i+1][j] = boards[i+1][j], boards[i][j]

print(answer)