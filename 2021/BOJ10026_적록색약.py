import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y, col):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:

            if board[nx][ny] == col:
                visited[nx][ny] = True
                dfs(nx, ny, col)

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))

visited = [[False]*n for _ in range(n)]

# 적록색약 x
answer = []
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, board[i][j])
            cnt += 1
answer.append(cnt)

# green -> red
for i in range(n):
    for j in range(n):
        if board[i][j] == "G":
            board[i][j] = "R"

visited = [[False]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, board[i][j])
            cnt += 1
answer.append(cnt)

print(*answer)