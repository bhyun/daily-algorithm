from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = True

q = deque()
q.append((0, 0, 0, 1))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
flag = False
while q:
    x, y, cnt, path = q.popleft()

    if x == n-1 and y == m-1:
        flag = True
        print(path)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == "0":
                if not visited[nx][ny][0] and cnt == 0:
                    visited[nx][ny][0] = True
                    q.append((nx, ny, cnt, path + 1))
                elif not visited[nx][ny][1] and cnt == 1:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, cnt, path + 1))

            elif graph[nx][ny] == "1":
                if not visited[nx][ny][1] and cnt == 0:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, cnt + 1, path + 1))

if not flag:
    print(-1)