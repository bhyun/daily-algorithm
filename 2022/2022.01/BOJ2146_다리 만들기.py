import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

def identify(x, y, number):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            graph[nx][ny] = number
            identify(nx, ny, number)

def isOK(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    candidates = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                candidates.append((nx, ny))
    return candidates

def move(x, y, island):
    global answer

    q = deque()
    q.append((x, y, 1))

    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    while q:
        x, y, distance = q.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny, distance + 1))
                elif graph[nx][ny] != island:
                    answer = min(answer, distance)
                    return


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

number = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = number
            identify(i, j, number)
            number += 1

answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            candidates = isOK(i, j)
            for x, y in candidates:
                move(x, y, graph[i][j])

print(answer)
