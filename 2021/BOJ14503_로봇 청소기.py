import sys
input = sys.stdin.readline

def dfs(x, y, d):

    global answer

    if board[x][y] == 0:
        answer += 1
        board[x][y] = 2

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    flag = False

    for i in range(4):
        nd = (d+3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0:
                flag = True
                dfs(nx, ny, nd)
                return
            d = nd

    if not flag:
        nd = (d + 2) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1:
                return
            dfs(nx, ny, d)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
answer = 0
for _ in range(n):
    board.append(list(map(int, input().split())))
dfs(r, c, d)
print(answer)


