from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y, direct, val = q.popleft()
        nx = x + dx[direct]
        ny = y + dy[direct]
        if direct == 3 and nx == start_x and ny == start_y:
            graph[nx][ny] = val
            return
        elif start_x <= nx < start_x + len_r  and start_y <= ny < start_y + len_c :
            cur = graph[nx][ny]
            graph[nx][ny] = val
            q.append((nx, ny, direct, cur))
        else:
            q.append((x, y, direct+1, val))


n, m, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

while r:
    cnt = min(n, m) // 2
    len_r = n
    len_c = m
    for i in range(cnt):
        q = deque()
        q.append((i, i, 0, graph[i][i]))
        bfs(i, i)
        len_r -= 2
        len_c -= 2
    r -= 1
for g in graph:
    print(*g)