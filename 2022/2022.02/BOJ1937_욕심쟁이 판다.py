import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    origin = dp[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dp[x][y] = max(dp[x][y], origin + dfs(nx, ny))
            else:
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    return dp[x][y]

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [[1] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            answer = max(answer, dfs(i, j))
print(answer)
