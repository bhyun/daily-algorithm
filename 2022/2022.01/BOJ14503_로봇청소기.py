def changeDirection(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2

def dfs(x, y, d):
    global answer

    answer += 1
    graph[x][y] = 2

    cnt = 0
    while True:
        d = changeDirection(d)
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            dfs(nx, ny, d)
        else:
            cnt += 1
            if cnt == 4:
                # 후
                x -= dx[d]
                y -= dy[d]
                if 0 <= x < n and 0 <= y < m:
                    if graph[x][y] == 1:
                        break
                    elif graph[x][y] == 2:
                        cnt = 0
                else:
                    break

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


answer = 0
dfs(x, y, d)
print(answer)