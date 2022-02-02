import sys
input = sys.stdin.readline

def check(x, y):

    row, col, itv = set(), set(), set()
    r_x, r_y, c_x, c_y, i_x, i_y = 0, 0, 0, 0, 0, 0

    # 가로 검색
    for i in range(9):
        if board[x][i] == 0:
            r_x, r_y = x, i
        row.add(board[x][i])
    # 세로 검색
    for i in range(9):
        if board[i][y] == 0:
            c_x, c_y = i, y
        col.add(board[i][y])

    # 굵은선
    for i in range(x - x%3, x - x%3 + 3):
        for j in range(y - y%3, y - y%3 + 3):
            if board[i][j] == 0:
                i_x, i_y = i, j
            itv.add(board[i][j])


    row = set(range(10)) - row
    col = set(range(10)) - col
    itv = set(range(10)) - itv

    if len(row) == 1:
        visited[r_x][r_y] = True
        board[r_x][r_y] = row.pop()
    elif len(col) == 1:
        visited[c_x][c_y] = True
        board[c_x][c_y] = col.pop()
    elif len(itv) == 1:
        visited[i_x][i_y] = True
        board[i_x][i_y] = itv.pop()


board = []
for i in range(9):
    board.append(list(map(int, input().split())))

visited = [[True] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            visited[i][j] = False

while True:
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                check(i, j)

    if all(visited):
        break

for i in range(9):
    print(*board[i])