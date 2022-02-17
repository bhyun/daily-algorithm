import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for x in range(n):
    for y in range(n):
        dx = [graph[x][y], 0]
        dy = [0, graph[x][y]]

        if graph[x][y] == 0:
            break

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                dp[nx][ny] += dp[x][y]

print(dp[n-1][n-1])