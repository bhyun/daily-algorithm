import sys
sys.setrecursionlimit(10000)
from itertools import combinations
import copy
input = sys.stdin.readline


def dfs(g, x, y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if g[nx][ny] == 0:
                visited[nx][ny] = True
                g[nx][ny] = 2
                dfs(g, nx, ny)

def calculate(g):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 빈칸 위치 구하기
blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append([i, j])
cases = list(combinations(blank, 3))
maxcnt = -sys.maxsize
for case in cases:
    g = copy.deepcopy(graph)
    visited = [[False] * m for _ in range(n)]
    # 벽 세우기
    for c in case:
        x, y = c
        g[x][y] = 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and g[i][j] == 2:
                visited[i][j] = True
                dfs(g, i, j)

    cnt = calculate(g)
    if cnt > maxcnt:
        maxcnt = cnt


print(maxcnt)



