from collections import deque

def bfs(q):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                graph[nx][ny] = -1

r, c, n = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == ".":
            graph[i][j] = -1 # 폭탄 설치 x
        else:
            graph[i][j] = 1 # 폭탄 설치 후 1초 시간 지남

sec = 1 # 시작 시간: 1초
q = deque()

if n != 1:
    while True:
        for i in range(r):
            for j in range(c):
                graph[i][j] += 1
                if graph[i][j] == 3:
                    graph[i][j] = -1
                    q.append((i, j))
        if q:
            bfs(q)
        sec += 1
        if sec == n:
            break

for i in range(r):
    for j in range(c):
        if graph[i][j] != -1:
            print('O', end= "")
        else:
            print(".", end="")
    print()


