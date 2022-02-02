import sys
from collections import deque

input = sys.stdin.readline

def spread():
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                q.append((i, j, graph[i][j]))

    while q:
        x, y, origin = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                graph[nx][ny] += (origin // 5)
                cnt += 1
        graph[x][y] -= ((origin // 5) * cnt)


def find():
    cleaner = []
    for i in range(r):
        if graph[i][0] == -1:
            cleaner.append(i)
    return cleaner


def clean(x, dir):
    # 시계
    if dir == 0:
        for i in range(x+1, r-1):
            graph[i][0] = graph[i+1][0]
        for i in range(c-1):
            graph[r-1][i] = graph[r-1][i+1]
        for i in range(r-1, x-1, -1):
            graph[i][c-1] = graph[i-1][c-1]
        for i in range(c-1, 1, -1):
            graph[x][i] = graph[x][i-1]
        graph[x][1] = 0
    # 반시계
    else:
        tmp = graph[0][c-1]
        for i in range(x):
            graph[i][c-1] = graph[i+1][c-1]
        for i in range(c-1, 1, -1):
            graph[x][i] = graph[x][i-1]
        graph[x][1] = 0
        for i in range(x-1, 0, -1):
            graph[i][0] = graph[i-1][0]
        for i in range(c-2):
            graph[0][i] = graph[0][i+1]
        graph[0][c-2] = tmp

def summary():
    summary = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1:
                summary += graph[i][j]
    return summary


r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))
for _ in range(t):
    spread()
    first, second = find()
    clean(first, 1)
    clean(second, 0)
print(summary())

