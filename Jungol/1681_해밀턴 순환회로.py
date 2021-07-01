import sys
input = sys.stdin.readline

def dfs(x, y, cnt, cost):
    global ans
    if cost > ans:
        return
    if cnt == n-1:
        if board[y][0] != 0:
            if cost + board[y][0] < ans:
                ans = cost + board[y][0]
        return

    for i in range(1, n):
        if not visited[i] and board[y][i] != 0:
            visited[i] = True
            dfs(y, i, cnt + 1, cost + board[y][i])
            visited[i] = False

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
ans = sys.maxsize
visited = [False] * n
visited[0] = True
for i in range(1, n):
    if not visited[i] and board[0][i] != 0:
        visited[i] = True
        dfs(0, i, 1, board[0][i])
        visited[i] = False

print(ans)
