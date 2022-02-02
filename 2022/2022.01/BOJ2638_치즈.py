import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def checkOutAir(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                visited[nx][ny] = True
                graph[nx][ny] = 2
                checkOutAir(nx, ny)

def isEmptyCheese():
    candidates = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 2:
                            cnt += 1
                if cnt >= 2:
                    graph[i][j] = 0
                    candidates.append((i, j))
    return len(candidates) == 0


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
while True:
    visited = [[False] * m for _ in range(n)]
    checkOutAir(0, 0)
    if isEmptyCheese():
        break
    answer += 1
print(answer)
