import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)


n = int(input())
graph = []
minheight, maxheight = 101, 0

for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

answer = 0
for h in range(101):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h:
                visited[i][j] = True

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1
    answer = max(answer, cnt)

print(answer)