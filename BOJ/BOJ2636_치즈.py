import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
hour = 0

while True:
    visited = [[False] * m for _ in range(n)]
    q = deque()

    q.append((0, 0))
    visited[0][0] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if graph[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = True
                    graph[nx][ny] = 0

    if cnt == 0: # 남아있는 치즈 없음
        print(hour)
        print(answer)
        break
    else:
        answer = cnt
        hour += 1

